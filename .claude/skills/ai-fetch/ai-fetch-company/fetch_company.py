"""
Company Blog Fetcher

Fetches company blog posts and articles.
"""

import sys
import os
import re
import time
import requests
from pathlib import Path
from datetime import datetime
from bs4 import BeautifulSoup

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from _shared.config import should_use_proxy, REQUEST_TIMEOUT, STORAGE_BASE
from _shared.translate import Translator
from _shared.utils import (
    format_markdown_frontmatter,
    slugify,
    get_file_timestamp,
    extract_domain,
    extract_filename_from_url,
)


class CompanyFetcher:
    """Fetcher for company blogs and news"""

    def __init__(self, use_proxy: bool = False):
        self.translator = Translator()
        self.use_proxy = use_proxy

    def _get(self, url: str, **kwargs) -> requests.Response:
        """Make GET request with proxy support"""
        proxies = {}
        if self.use_proxy or should_use_proxy(url):
            proxies = {
                'http': 'http://127.0.0.1:26001',
                'https': 'http://127.0.0.1:26001'
            }

        return requests.get(url, proxies=proxies, timeout=REQUEST_TIMEOUT, **kwargs)

    def fetch_article(self, url: str, company: str) -> dict:
        """
        Fetch a single article.

        Args:
            url: Article URL
            company: Company name (for storage path)

        Returns:
            Dictionary with article content
        """
        # Skip GitHub URLs - they should be handled by GitHub fetcher
        if 'github.com' in url:
            raise Exception("GitHub URLs should be handled by GitHub fetcher")

        response = self._get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch article: {response.status_code}")

        return self._parse_article(response.text, url, company)

    def _parse_article(self, html: str, url: str, company: str) -> dict:
        """Parse article HTML to extract content with proper cleaning"""
        soup = BeautifulSoup(html, 'html.parser')

        # Remove unwanted elements first
        for tag in soup.find_all(['script', 'style', 'nav', 'footer', 'header',
                                   'noscript', 'iframe', 'svg', 'form']):
            tag.decompose()

        # Also remove common nav/footer/sidebar classes
        for elem in soup.find_all(class_=['nav', 'navbar', 'sidebar', 'cookie', 'consent',
                                            'cookie-banner', 'popup', 'modal', 'footer', 'header']):
            elem.decompose()

        # Extract title
        title = ''
        title_tag = soup.find('h1') or soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Extract date
        date = ''
        date_tag = soup.find('time') or soup.find(class_=['date', 'published', 'timestamp', 'meta-date'])
        if date_tag:
            date = date_tag.get('datetime', '') or date_tag.get_text(strip=True)
            date = date[:10] if len(date) > 10 else date

        # Extract author
        author = ''
        author_tag = soup.find(class_=['author', 'byline', 'post-author'])
        if author_tag:
            author = author_tag.get_text(strip=True)

        # Extract main content - try multiple selectors
        content = ''
        article_tag = (soup.find('article') or
                       soup.find(class_=['post-content', 'article-content', 'entry-content', 'content']) or
                       soup.find('main'))
        if article_tag:
            # Extract paragraphs, avoiding short snippets (likely nav/menu items)
            paragraphs = []
            for p in article_tag.find_all(['p', 'h2', 'h3', 'h4', 'li']):
                text = p.get_text(strip=True)
                # Only include substantial text (not short nav items)
                if len(text) > 30:
                    paragraphs.append(text)
            content = '\n\n'.join(paragraphs)

        # Fallback to body if no content found
        if not content or len(content) < 100:
            body = soup.find('body')
            if body:
                paragraphs = []
                for p in body.find_all(['p', 'h2', 'h3', 'h4']):
                    text = p.get_text(strip=True)
                    if len(text) > 30:
                        paragraphs.append(text)
                content = '\n\n'.join(paragraphs)

        # Translate
        title_zh = self.translator.translate(title)
        content_zh = self.translator.translate(content) if content and len(content) > 50 else ''

        return {
            'title': title,
            'title_zh': title_zh,
            'url': url,
            'date': date or datetime.now().strftime('%Y-%m-%d'),
            'author': author,
            'company': company,
            'content': content_zh,
            'source': extract_domain(url),
        }

    def format_as_markdown(self, article: dict) -> str:
        """Format article as markdown"""
        md = format_markdown_frontmatter(
            title=article['title_zh'],
            source=article['source'],
            url=article['url'],
            date=article['date'],
            category=f"company/{article['company']}/blogs",
            translated=True,
            fetched_at=get_file_timestamp(),
            author=article.get('author', ''),
        )

        md += f"# {article['title_zh']}\n\n"
        md += f"**来源**: {article['source']}"

        if article.get('author'):
            md += f" | **作者**: {article['author']}"
        if article.get('date'):
            md += f" | **日期**: {article['date']}"

        md += "\n\n---\n\n"

        if article.get('content'):
            md += article['content']
            md += "\n\n"

        md += f"*原文请访问 [{article['source']}]({article['url']})*"

        return md

    def discover_articles(self, blog_url: str) -> list:
        """
        Discover article links from a blog listing page.

        Args:
            blog_url: Blog homepage or listing URL

        Returns:
            List of article URLs
        """
        response = self._get(blog_url)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []

        # Find article links
        for link in soup.find_all('a', href=True):
            href = link['href']

            # Skip navigation and non-article links
            if any(skip in href for skip in ['/category/', '/tag/', '/author/', '#', 'login', 'subscribe']):
                continue

            # Article URL patterns
            if '/blog/' in href or '/post/' in href or '/news/' in href or '/article/' in href:
                if href.startswith('http'):
                    articles.append(href)
                else:
                    from urllib.parse import urljoin
                    articles.append(urljoin(blog_url, href))

        # Deduplicate
        return list(set(articles))


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Fetch company blog posts')
    parser.add_argument('--url', type=str, required=True, help='Article URL')
    parser.add_argument('--company', type=str, required=True, help='Company name')
    parser.add_argument('--discover', action='store_true', help='Discover articles from blog URL')

    args = parser.parse_args()
    fetcher = CompanyFetcher()

    if args.discover:
        print(f"Discovering articles from {args.url}...")
        articles = fetcher.discover_articles(args.url)
        print(f"Found {len(articles)} articles:")
        for i, url in enumerate(articles[:10]):
            print(f"  {i+1}. {url}")
        if len(articles) > 10:
            print(f"  ... and {len(articles) - 10} more")

    else:
        print(f"Fetching article from {args.url}...")
        try:
            article = fetcher.fetch_article(args.url, args.company)
            md = fetcher.format_as_markdown(article)

            # Save
            slug = slugify(article['title'], max_length=50)
            output_dir = Path(STORAGE_BASE) / 'company' / args.company / 'blogs'
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{slug}.md"
            output_file.write_text(md, encoding='utf-8')

            print(f"Saved to {output_file}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
