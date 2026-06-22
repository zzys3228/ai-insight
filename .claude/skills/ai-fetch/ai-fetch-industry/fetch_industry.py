"""
Industry Fetcher - AI行业报告、VC智库、政策报告抓取
"""

import re
import time
import requests
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional
from bs4 import BeautifulSoup
from markdownify import markdownify

# Import shared utilities
import sys
SKILLS_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(SKILLS_DIR))
from _shared.config import PROXY, CN_DOMAINS, should_use_proxy
from _shared.translate import get_translator


class IndustryFetcher:
    """抓取AI行业报告和VC智库内容"""

    def __init__(self):
        self.session = requests.Session()
        self.translator = get_translator()
        self.BROWSER_HEADERS = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

    def _get_session(self, url: str) -> requests.Session:
        """获取配置好的Session"""
        session = requests.Session()
        session.headers.update(self.BROWSER_HEADERS)
        if should_use_proxy(url):
            session.proxies = {'http': PROXY, 'https': PROXY}
        return session

    def fetch(self, url: str, name: str = None) -> Dict:
        """抓取行业报告页面"""
        if not name:
            name = url.split('//')[1].split('/')[0] if '//' in url else url

        session = self._get_session(url)
        try:
            resp = session.get(url, timeout=30)
            resp.raise_for_status()
        except Exception as e:
            return {'error': str(e), 'url': url}

        # Parse content
        soup = BeautifulSoup(resp.text, 'html.parser')

        # Remove scripts and styles
        for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
            tag.decompose()

        # Get main content
        main = soup.find('main') or soup.find('article') or soup.find('div', class_=re.compile(r'content|main|article')) or soup.body

        content = ''
        if main:
            content = markdownify(str(main), heading_style="atx")

        # Get title
        title = soup.find('h1')
        title = title.get_text(strip=True) if title else name

        # Get description
        desc = soup.find('meta', attrs={'name': 'description'})
        description = desc.get('content', '') if desc else ''

        return {
            'url': url,
            'name': name,
            'title': title,
            'description': description,
            'content': content,
            'fetched_at': datetime.now().isoformat()
        }

    def format_as_markdown(self, data: Dict, category: str = 'industry') -> str:
        """格式化为Markdown"""
        if 'error' in data:
            return f"---\nerror: {data['error']}\nurl: {data['url']}\n---\n\n# Error Fetching {data['url']}\n\n{data['error']}"

        # Translate title
        title = self.translator.translate(data.get('title', ''))
        description = self.translator.translate(data.get('description', ''))

        md = f"""---
title: {title}
source: {data.get('url', '').split('/')[2] if '://' in data.get('url', '') else 'unknown'}
url: {data['url']}
category: {category}
fetched_at: {data['fetched_at']}
translated: true
---

# {title}

**来源**: {data.get('url', '').split('/')[2]} | **抓取时间**: {data['fetched_at'][:10]}

"""

        if description:
            md += f"**摘要**: {description}\n\n"

        if data.get('content'):
            content = data['content'][:5000]  # Limit content length
            if len(data['content']) > 5000:
                content += f"\n\n... (内容截断，原始长度 {len(data['content'])} 字符)"
            translated_content = self.translator.translate(content)
            md += f"---\n\n{translated_content}\n"

        md += f"\n\n*原文请访问 [{data['url']}]({data['url']})*"

        return md


def fetch_industry_urls(urls: List[Dict]) -> int:
    """批量抓取行业URL"""
    fetcher = IndustryFetcher()
    count = 0

    for item in urls:
        url = item['url']
        section = item.get('section', 'industry')

        try:
            data = fetcher.fetch(url)
            md = fetcher.format_as_markdown(data, category=f'industry/{section}')

            # Save
            from _shared.config import STORAGE_BASE
            domain = url.split('/')[2].replace('.', '_')
            output_dir = Path(STORAGE_BASE) / 'industry' / domain
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / 'index.md'
            output_file.write_text(md, encoding='utf-8')

            print(f"  Saved: {output_file}")
            count += 1

        except Exception as e:
            print(f"  Error: {url} - {e}")

        time.sleep(1)  # Rate limit

    return count
