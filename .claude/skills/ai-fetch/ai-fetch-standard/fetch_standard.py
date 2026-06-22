"""
Standard/Protocol Documentation Fetcher

Fetches AI protocol specifications and standards documentation.
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


class StandardFetcher:
    """Fetcher for protocol specifications"""

    def __init__(self, use_proxy: bool = False):
        self.translator = Translator()
        self.use_proxy = use_proxy

    def _get(self, url: str, **kwargs) -> requests.Response:
        proxies = {}
        if self.use_proxy or should_use_proxy(url):
            proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
        return requests.get(url, proxies=proxies, timeout=REQUEST_TIMEOUT, **kwargs)

    def fetch_doc(self, url: str, protocol: str) -> dict:
        """Fetch documentation page"""
        response = self._get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch: {response.status_code}")

        return self._parse_doc(response.text, url, protocol)

    def _parse_doc(self, html: str, url: str, protocol: str) -> dict:
        """Parse documentation page"""
        soup = BeautifulSoup(html, 'html.parser')

        # Title
        title = ''
        title_tag = soup.find('h1') or soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Main content
        content = ''
        main_tag = soup.find('main') or soup.find('article') or soup.find(class_=['content', 'documentation', 'spec'])
        if main_tag:
            # Preserve code blocks
            for pre in main_tag.find_all('pre'):
                content += '\n```\n' + pre.get_text() + '\n```\n'
            # Get rest of text
            for elem in main_tag.find_all(['p', 'h2', 'h3', 'h4', 'ul', 'ol', 'table']):
                text = elem.get_text(separator='\n', strip=True)
                if text:
                    content += '\n' + text + '\n'

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
            'title': title,
            'title_zh': title_zh,
            'url': url,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'protocol': protocol,
            'content': content_zh,
            'source': extract_domain(url),
        }

    def discover_pages(self, base_url: str) -> list:
        """Discover documentation pages"""
        response = self._get(base_url)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith('/') or href.startswith(base_url):
                if href.startswith('/'):
                    from urllib.parse import urljoin
                    href = urljoin(base_url, href)
                if any(ext in href for ext in ['.html', '/docs/', '/spec/', '/guide/']):
                    if href not in links:
                        links.append(href)

        return links[:20]  # Limit to 20 pages

    def format_as_markdown(self, doc: dict) -> str:
        """Format as markdown"""
        md = format_markdown_frontmatter(
            title=doc['title_zh'],
            source=doc['source'],
            url=doc['url'],
            date=doc['date'],
            category=f"standard/{doc['protocol']}",
            translated=True,
            fetched_at=get_file_timestamp(),
        )

        md += f"# {doc['title_zh']}\n\n"
        md += f"**来源**: {doc['source']} | **日期**: {doc['date']}\n\n"
        md += "---\n\n"

        if doc.get('content'):
            md += doc['content']
            md += "\n\n"

        md += f"*原文请访问 [{doc['source']}]({doc['url']})*"
        return md


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch protocol documentation')
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--protocol', type=str, required=True)
    parser.add_argument('--discover', action='store_true', help='Discover doc pages')

    args = parser.parse_args()
    fetcher = StandardFetcher()

    if args.discover:
        print(f"Discovering pages from {args.url}...")
        pages = fetcher.discover_pages(args.url)
        print(f"Found {len(pages)} pages:")
        for i, page in enumerate(pages[:10]):
            print(f"  {i+1}. {page}")

    else:
        print(f"Fetching doc: {args.url}...")
        try:
            doc = fetcher.fetch_doc(args.url, args.protocol)
            md = fetcher.format_as_markdown(doc)

            slug = slugify(doc['title'], max_length=50)
            output_dir = Path(STORAGE_BASE) / 'standard' / args.protocol
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{slug}.md"
            output_file.write_text(md, encoding='utf-8')
            print(f"Saved to {output_file}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
