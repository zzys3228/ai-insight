"""
Person Blog/Content Fetcher

Fetches AI researcher and influencer content.
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


class PersonFetcher:
    """Fetcher for personal blogs and content"""

    def __init__(self, use_proxy: bool = False):
        self.translator = Translator()
        self.use_proxy = use_proxy

    def _get(self, url: str, **kwargs) -> requests.Response:
        proxies = {}
        if self.use_proxy or should_use_proxy(url):
            proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
        return requests.get(url, proxies=proxies, timeout=REQUEST_TIMEOUT, **kwargs)

    def fetch_article(self, url: str, person: str) -> dict:
        """Fetch a single article"""
        response = self._get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch: {response.status_code}")

        return self._parse_article(response.text, url, person)

    def _parse_article(self, html: str, url: str, person: str) -> dict:
        """Parse article page"""
        soup = BeautifulSoup(html, 'html.parser')

        # Title
        title = ''
        title_tag = soup.find('h1') or soup.find('h2') or soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Date
        date = ''
        date_tag = soup.find('time') or soup.find(class_=['date', 'published', 'post-date'])
        if date_tag:
            date = date_tag.get('datetime', '') or date_tag.get_text(strip=True)
            date = date[:10] if len(date) > 10 else date

        # Content
        content = ''
        article_tag = soup.find('article') or soup.find(class_=['post-content', 'article-content', 'entry-content'])
        if article_tag:
            content = article_tag.get_text(separator='\n\n', strip=True)

        if not content:
            main_tag = soup.find('main') or soup.find(class_=['content', 'main'])
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
            'title': title,
            'title_zh': title_zh,
            'url': url,
            'date': date or datetime.now().strftime('%Y-%m-%d'),
            'person': person,
            'content': content_zh,
            'source': extract_domain(url),
        }

    def discover_articles(self, blog_url: str) -> list:
        """Discover article links from blog"""
        response = self._get(blog_url)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        for link in soup.find_all('a', href=True):
            href = link['href']
            if any(skip in href for skip in ['/category/', '/tag/', '#', 'login', 'subscribe', '/about']):
                continue
            if href.endswith('.html') or '/blog/' in href or '/post/' in href or href.endswith('/'):
                if href.startswith('http'):
                    links.append(href)
                else:
                    from urllib.parse import urljoin
                    links.append(urljoin(blog_url, href))

        return list(set(links))[:20]

    def format_as_markdown(self, article: dict) -> str:
        """Format as markdown"""
        md = format_markdown_frontmatter(
            title=article['title_zh'],
            source=article['source'],
            url=article['url'],
            date=article['date'],
            category=f"person/{article['person']}",
            translated=True,
            fetched_at=get_file_timestamp(),
        )

        md += f"# {article['title_zh']}\n\n"
        md += f"**来源**: {article['source']} | **日期**: {article['date']}\n\n"
        md += "---\n\n"

        if article.get('content'):
            md += article['content']
            md += "\n\n"

        md += f"*原文请访问 [{article['source']}]({article['url']})*"
        return md


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch person content')
    parser.add_argument('--url', type=str, help='Article URL')
    parser.add_argument('--person', type=str, required=True, help='Person name')
    parser.add_argument('--discover', action='store_true', help='Discover articles from blog')

    args = parser.parse_args()
    fetcher = PersonFetcher()

    if args.discover and args.url:
        print(f"Discovering articles from {args.url}...")
        links = fetcher.discover_articles(args.url)
        print(f"Found {len(links)} articles:")
        for i, link in enumerate(links[:10]):
            print(f"  {i+1}. {link}")

    elif args.url:
        print(f"Fetching article: {args.url}...")
        try:
            article = fetcher.fetch_article(args.url, args.person)
            md = fetcher.format_as_markdown(article)

            slug = slugify(article['title'], max_length=50)
            output_dir = Path(STORAGE_BASE) / 'person' / args.person
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{slug}.md"
            output_file.write_text(md, encoding='utf-8')
            print(f"Saved to {output_file}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
