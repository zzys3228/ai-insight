"""
Conference Fetcher

Fetches conference agenda, speaker info, and presentation content.
Multi-source strategy: official website -> video -> speaker articles -> news reports.
"""

import sys
import os
import re
import time
import requests
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent.parent))
from _shared.config import should_use_proxy, REQUEST_TIMEOUT, STORAGE_BASE
from _shared.translate import Translator
from _shared.utils import (
    format_markdown_frontmatter,
    slugify,
    get_file_timestamp,
    extract_domain,
)


class ConferenceFetcher:
    """Fetcher for conference content"""

    def __init__(self, use_proxy: bool = False):
        self.translator = Translator()
        self.use_proxy = use_proxy

    def _get(self, url: str, **kwargs) -> requests.Response:
        proxies = {}
        if self.use_proxy or should_use_proxy(url):
            proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
        return requests.get(url, proxies=proxies, timeout=REQUEST_TIMEOUT, **kwargs)

    def fetch_conference(self, url: str, name: str, year: str = None) -> dict:
        """Fetch conference overview"""
        if year is None:
            year = datetime.now().strftime('%Y')

        response = self._get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch: {response.status_code}")

        return self._parse_conference(response.text, url, name, year)

    def _parse_conference(self, html: str, url: str, name: str, year: str) -> dict:
        """Parse conference page"""
        soup = BeautifulSoup(html, 'html.parser')

        # Title
        title = ''
        title_tag = soup.find('h1') or soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Main content
        content = ''
        main_tag = soup.find('main') or soup.find('article') or soup.find(class_=['content', 'main'])
        if main_tag:
            for tag in main_tag.find_all(['script', 'style', 'nav']):
                tag.decompose()
            content = main_tag.get_text(separator='\n\n', strip=True)

        if not content:
            body = soup.find('body')
            if body:
                for tag in body.find_all(['script', 'style', 'nav', 'footer', 'header']):
                    tag.decompose()
                content = body.get_text(separator='\n\n', strip=True)

        # Translate
        title_zh = self.translator.translate(title)
        content_zh = self.translator.translate(content) if content else ''

        return {
            'name': name,
            'title': title,
            'title_zh': title_zh,
            'url': url,
            'year': year,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'content': content_zh,
            'source': extract_domain(url),
        }

    def discover_agenda(self, agenda_url: str) -> list:
        """Discover agenda/session links"""
        response = self._get(agenda_url)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for link in soup.find_all('a', href=True):
            href = link['href']
            if any(skip in href for skip in ['#', 'login', 'register']):
                continue
            if '/session/' in href or '/speaker/' in href or '/agenda/' in href or '/program/' in href:
                if href.startswith('http'):
                    links.append(href)
                else:
                    from urllib.parse import urljoin
                    links.append(urljoin(agenda_url, href))

        return list(set(links))[:30]

    def format_as_markdown(self, conf: dict) -> str:
        """Format as markdown"""
        md = format_markdown_frontmatter(
            title=conf['title_zh'],
            source=conf['source'],
            url=conf['url'],
            date=conf['date'],
            category=f"conference/{conf['name']}/{conf['year']}",
            translated=True,
            fetched_at=get_file_timestamp(),
            content_sources=[
                {"type": "official_website", "url": conf['url'], "status": "completed"},
                {"type": "video_transcript", "status": "pending"},
                {"type": "speaker_article", "status": "pending"},
                {"type": "news_report", "status": "pending"},
            ]
        )

        md += f"# {conf['title_zh']}\n\n"
        md += f"**来源**: {conf['source']} | **年份**: {conf['year']} | **日期**: {conf['date']}\n\n"
        md += "---\n\n"

        if conf.get('content'):
            md += conf['content']
            md += "\n\n"

        md += "---\n\n## 内容来源\n\n"
        md += "- [ ] 官网摘要 ✅ 已完成\n"
        md += "- [ ] 官方视频转写 ⏳ 待完成\n"
        md += "- [ ] 演讲者文章 ⏳ 待完成\n"
        md += "- [ ] 新闻媒体报道 ⏳ 待完成\n\n"

        md += f"*原文请访问 [{conf['source']}]({conf['url']})*"
        return md


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch conference')
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--year', type=str, help='Conference year')
    parser.add_argument('--discover', action='store_true', help='Discover agenda pages')

    args = parser.parse_args()
    fetcher = ConferenceFetcher()

    if args.discover:
        print(f"Discovering agenda from {args.url}...")
        pages = fetcher.discover_agenda(args.url)
        print(f"Found {len(pages)} pages:")
        for i, page in enumerate(pages[:10]):
            print(f"  {i+1}. {page}")

    else:
        print(f"Fetching conference: {args.url}...")
        try:
            conf = fetcher.fetch_conference(args.url, args.name, args.year)
            md = fetcher.format_as_markdown(conf)

            output_dir = Path(STORAGE_BASE) / 'conference' / args.name / (args.year or datetime.now().strftime('%Y'))
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / 'index.md'
            output_file.write_text(md, encoding='utf-8')
            print(f"Saved to {output_file}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
