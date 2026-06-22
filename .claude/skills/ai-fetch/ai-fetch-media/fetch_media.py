"""
Media Fetcher

Fetches newsletters, podcasts, and tech media content.
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
)


class NewsletterFetcher:
    """Fetcher for AI newsletters (Substack, etc.)"""

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

    def fetch_article(self, url: str, publisher: str) -> dict:
        """Fetch a single newsletter article"""
        response = self._get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch: {response.status_code}")

        return self._parse_article(response.text, url, publisher)

    def _parse_article(self, html: str, url: str, publisher: str) -> dict:
        """Parse newsletter article HTML"""
        soup = BeautifulSoup(html, 'html.parser')

        # Title
        title = ''
        title_tag = soup.find('h1') or soup.find(class_=['post-title', 'article-title'])
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Date
        date = ''
        date_tag = soup.find('time') or soup.find(class_=['post-date', 'published'])
        if date_tag:
            date = date_tag.get('datetime', '') or date_tag.get_text(strip=True)
            date = date[:10] if len(date) > 10 else date

        # Content
        content = ''
        article_tag = soup.find('article') or soup.find(class_=['post-content', 'article-content', 'substack'])
        if article_tag:
            content = article_tag.get_text(separator='\n\n', strip=True)

        if not content:
            body = soup.find('body')
            if body:
                for tag in body.find_all(['script', 'style', 'nav']):
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
            'publisher': publisher,
            'content': content_zh,
            'source': extract_domain(url),
        }

    def format_as_markdown(self, article: dict) -> str:
        """Format as markdown"""
        md = format_markdown_frontmatter(
            title=article['title_zh'],
            source=article['source'],
            url=article['url'],
            date=article['date'],
            category=f"media/newsletter/{article['publisher']}",
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


class PodcastFetcher:
    """Fetcher for AI podcasts"""

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

    def fetch_episode(self, url: str, podcast_name: str) -> dict:
        """Fetch podcast episode info and shownotes"""
        response = self._get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch: {response.status_code}")

        return self._parse_episode(response.text, url, podcast_name)

    def _parse_episode(self, html: str, url: str, podcast_name: str) -> dict:
        """Parse podcast episode page"""
        soup = BeautifulSoup(html, 'html.parser')

        # Title
        title = ''
        title_tag = soup.find('h1') or soup.find(class_=['episode-title', 'podcast-title'])
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Audio URL
        audio_url = ''
        audio_tag = soup.find('audio')
        if audio_tag:
            audio_url = audio_tag.get('src', '')

        # Date
        date = ''
        date_tag = soup.find('time') or soup.find(class_=['episode-date', 'published'])
        if date_tag:
            date = date_tag.get('datetime', '') or date_tag.get_text(strip=True)
            date = date[:10] if len(date) > 10 else date

        # Description/Shownotes
        description = ''
        desc_tag = soup.find(class_=['episode-description', 'shownotes', 'transcript'])
        if desc_tag:
            description = desc_tag.get_text(separator='\n\n', strip=True)

        if not description:
            # Try meta description
            meta_desc = soup.find('meta', attrs={'name': 'description'})
            if meta_desc:
                description = meta_desc.get('content', '')

        # Translate
        title_zh = self.translator.translate(title)
        desc_zh = self.translator.translate(description) if description else ''

        return {
            'title': title,
            'title_zh': title_zh,
            'url': url,
            'audio_url': audio_url,
            'date': date or datetime.now().strftime('%Y-%m-%d'),
            'podcast_name': podcast_name,
            'description': desc_zh,
            'source': extract_domain(url),
        }

    def format_as_markdown(self, episode: dict) -> str:
        """Format as markdown"""
        md = format_markdown_frontmatter(
            title=episode['title_zh'],
            source=episode['source'],
            url=episode['url'],
            date=episode['date'],
            category=f"media/podcast/{episode['podcast_name']}",
            translated=True,
            fetched_at=get_file_timestamp(),
            audio_url=episode.get('audio_url', ''),
        )

        md += f"# {episode['title_zh']}\n\n"
        md += f"**来源**: {episode['source']} | **日期**: {episode['date']}\n\n"

        if episode.get('audio_url'):
            md += f"**音频**: [{episode['audio_url']}]({episode['audio_url']})\n\n"

        md += "---\n\n"

        md += "## 音频信息\n\n"
        md += f"- **音频URL**: {episode.get('audio_url', 'N/A')}\n"
        md += f"- **发布日期**: {episode['date']}\n\n"

        if episode.get('description'):
            md += "---\n\n## Shownotes / 内容\n\n"
            md += episode['description']
            md += "\n\n"

        md += "---\n\n"
        md += "注：完整Transcript需下载音频后使用Whisper转写\n\n"

        md += f"*原文请访问 [{episode['source']}]({episode['url']})*"

        return md


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Fetch media content')
    parser.add_argument('--type', choices=['newsletter', 'podcast'], required=True)
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--name', type=str, required=True, help='Publisher or podcast name')

    args = parser.parse_args()

    if args.type == 'newsletter':
        fetcher = NewsletterFetcher()
        print(f"Fetching newsletter: {args.url}...")
        try:
            article = fetcher.fetch_article(args.url, args.name)
            md = fetcher.format_as_markdown(article)

            slug = slugify(article['title'], max_length=50)
            output_dir = Path(STORAGE_BASE) / 'media' / 'newsletter' / args.name
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{slug}.md"
            output_file.write_text(md, encoding='utf-8')

            print(f"Saved to {output_file}")
        except Exception as e:
            print(f"Error: {e}")

    else:
        fetcher = PodcastFetcher()
        print(f"Fetching podcast: {args.url}...")
        try:
            episode = fetcher.fetch_episode(args.url, args.name)
            md = fetcher.format_as_markdown(episode)

            slug = slugify(episode['title'], max_length=50)
            output_dir = Path(STORAGE_BASE) / 'media' / 'podcast' / args.name
            output_dir.mkdir(parents=True, exist_ok=True)
            output_file = output_dir / f"{slug}.md"
            output_file.write_text(md, encoding='utf-8')

            print(f"Saved to {output_file}")
            if episode.get('audio_url'):
                print(f"Audio URL: {episode['audio_url']}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == '__main__':
    main()
