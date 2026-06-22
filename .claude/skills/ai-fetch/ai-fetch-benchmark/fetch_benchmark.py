"""
Benchmark Fetcher

Fetches AI benchmark rankings and evaluation results.
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


class BenchmarkFetcher:
    """Fetcher for AI benchmarks"""

    def __init__(self, use_proxy: bool = False):
        self.translator = Translator()
        self.use_proxy = use_proxy

    def _get(self, url: str, **kwargs) -> requests.Response:
        proxies = {}
        if self.use_proxy or should_use_proxy(url):
            proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
        return requests.get(url, proxies=proxies, timeout=REQUEST_TIMEOUT, **kwargs)

    def fetch_benchmark(self, url: str, name: str) -> dict:
        """Fetch benchmark data from URL"""
        response = self._get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch: {response.status_code}")

        return self._parse_benchmark(response.text, url, name)

    def _parse_benchmark(self, html: str, url: str, name: str) -> dict:
        """Parse benchmark page"""
        soup = BeautifulSoup(html, 'html.parser')

        # Try to find tables
        tables = soup.find_all('table')
        table_data = []
        for table in tables:
            rows = []
            for row in table.find_all('tr'):
                cells = [cell.get_text(strip=True) for cell in row.find_all(['th', 'td'])]
                if cells:
                    rows.append(cells)
            if rows:
                table_data.append(rows)

        # Find title
        title = soup.find('h1')
        if not title:
            title = soup.find('title')
        title_text = title.get_text(strip=True) if title else name

        # Find description
        description = ''
        desc_elem = soup.find(['p', 'div'], class_=lambda x: x and 'description' in x.lower() if x else False)
        if desc_elem:
            description = desc_elem.get_text(strip=True)

        # Translate
        title_zh = self.translator.translate(title_text)
        desc_zh = self.translator.translate(description) if description else ''

        return {
            'name': name,
            'title': title_text,
            'title_zh': title_zh,
            'url': url,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'description': desc_zh,
            'tables': table_data,
            'source': extract_domain(url),
        }

    def format_as_markdown(self, data: dict) -> str:
        """Format benchmark as markdown"""
        md = format_markdown_frontmatter(
            title=data['title_zh'],
            source=data['source'],
            url=data['url'],
            date=data['date'],
            category=f"benchmark/{data['name']}",
            translated=True,
            fetched_at=get_file_timestamp(),
        )

        md += f"# {data['title_zh']}\n\n"
        md += f"**来源**: {data['source']} | **日期**: {data['date']}\n\n"
        md += "---\n\n"

        if data.get('description'):
            md += f"{data['description']}\n\n---\n\n"

        # Format tables
        for i, table in enumerate(data.get('tables', [])):
            md += f"### 表格 {i+1}\n\n"
            for row in table:
                md += '| ' + ' | '.join(row) + ' |\n'
            md += "\n"

        md += f"*原文请访问 [{data['source']}]({data['url']})*"
        return md


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch benchmark')
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--name', type=str, required=True)
    args = parser.parse_args()

    fetcher = BenchmarkFetcher()
    print(f"Fetching benchmark from {args.url}...")

    try:
        data = fetcher.fetch_benchmark(args.url, args.name)
        md = fetcher.format_as_markdown(data)

        output_dir = Path(STORAGE_BASE) / 'benchmark' / args.name
        output_dir.mkdir(parents=True, exist_ok=True)
        output_file = output_dir / f"{datetime.now().strftime('%Y-%m-%d')}.md"
        output_file.write_text(md, encoding='utf-8')
        print(f"Saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == '__main__':
    main()
