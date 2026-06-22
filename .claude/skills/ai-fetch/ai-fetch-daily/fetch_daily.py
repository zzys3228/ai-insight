"""
AI Fetch Daily - Main Entry Point

Orchestrates fetching from all AI news sources.
"""

import sys
import os
import json
import time
import argparse
import importlib
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# Add parent directory to path for imports
SKILLS_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(SKILLS_DIR))
from _shared.config import STORAGE_BASE, URL_INDEX_FILE, FAILED_URLS_FILE
from _shared.utils import (
    read_json, write_json, get_file_timestamp,
    extract_domain, slugify, get_url_hash
)


def import_fetcher(module_name: str, class_name: str):
    """Dynamically import a fetcher class from a hyphenated module name"""
    # Convert hyphens to underscores for Python import
    module_path = SKILLS_DIR / module_name.replace('_', '-') / f"fetch_{module_name.split('_')[-1]}.py"
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, class_name)


class FetchDaily:
    """Main orchestrator for daily fetching"""

    def __init__(self, sources_file: str = None):
        # Default to project root ai-news-sources.md
        if sources_file is None:
            sources_file = SKILLS_DIR.parent.parent.parent / "ai-news-sources.md"
        else:
            sources_file = Path(sources_file)
        self.sources_file = sources_file
        self.url_index = read_json(URL_INDEX_FILE)
        self.failed_urls = read_json(FAILED_URLS_FILE)

    def get_stats(self) -> Dict:
        """Get fetch statistics"""
        total = len(self.url_index)
        translated = sum(1 for v in self.url_index.values() if v.get('translated'))
        failed = len(self.failed_urls)

        return {
            'total_urls': total,
            'translated': translated,
            'failed': failed,
            'last_fetch': max([v.get('fetched_at', '') for v in self.url_index.values()], default='')
        }

    def list_urls(self, category: str = None):
        """List all URLs from sources file"""
        # Parse markdown table
        with open(self.sources_file, 'r', encoding='utf-8') as f:
            content = f.read()

        urls = []
        current_section = ''

        for line in content.split('\n'):
            # Track section
            if line.startswith('## '):
                current_section = line.replace('## ', '').strip()
            elif line.startswith('### '):
                current_section = line.replace('### ', '').strip()

            # Extract URLs from table
            if 'http' in line:
                parts = line.split('|')
                for part in parts:
                    if 'http' in part:
                        url = part.strip()
                        if url.startswith('http'):
                            urls.append({
                                'url': url,
                                'section': current_section
                            })

        if category:
            cat_lower = category.lower()
            # Filter by section name OR by URL domain
            urls = [u for u in urls if
                    cat_lower in u['section'].lower() or
                    (cat_lower == 'github' and 'github.com' in u['url'].lower())]

        return urls

    def mark_fetched(self, url: str, path: str, metadata: Dict = None):
        """Mark URL as fetched"""
        url_hash = get_url_hash(url)
        self.url_index[url_hash] = {
            'url': url,
            'path': path,
            'fetched_at': get_file_timestamp(),
            'metadata': metadata or {}
        }
        write_json(URL_INDEX_FILE, self.url_index)

    def mark_failed(self, url: str, error: str):
        """Mark URL as failed"""
        url_hash = get_url_hash(url)
        self.failed_urls[url_hash] = {
            'url': url,
            'error': error,
            'last_try': get_file_timestamp()
        }
        write_json(FAILED_URLS_FILE, self.failed_urls)

    def should_fetch(self, url: str, force: bool = False) -> bool:
        """Check if URL should be fetched"""
        if force:
            return True

        url_hash = get_url_hash(url)
        if url_hash not in self.url_index:
            return True

        # Check if fetched today
        last_fetch = self.url_index.get(url_hash, {}).get('fetched_at', '')
        if not last_fetch:
            return True

        # Simple daily check
        today = datetime.now().strftime('%Y-%m-%d')
        if not last_fetch.startswith(today):
            return True

        return False

    def fetch_github(self, urls: List = None):
        """Fetch GitHub repos"""
        GitHubFetcher = import_fetcher('ai_fetch_github', 'GitHubFetcher')

        if not urls:
            urls = self.list_urls('GitHub')

        fetcher = GitHubFetcher()
        count = 0

        for item in urls:
            url = item['url']
            if 'github.com' not in url:
                continue

            if not self.should_fetch(url):
                print(f"Skipping (already fetched): {url}")
                continue

            print(f"Fetching GitHub: {url}")
            try:
                from _shared.utils import parse_github_url
                owner, repo = parse_github_url(url)

                results = fetcher.fetch_repo(owner, repo)
                md = fetcher.format_as_markdown(results, owner, repo)

                # Save
                output_dir = Path(STORAGE_BASE) / 'github' / f"{owner}_{repo}"
                output_dir.mkdir(parents=True, exist_ok=True)
                output_file = output_dir / 'README.md'
                output_file.write_text(md, encoding='utf-8')

                self.mark_fetched(url, str(output_file))
                count += 1
                print(f"  -> Saved to {output_file}")

            except Exception as e:
                print(f"  -> Error: {e}")
                self.mark_failed(url, str(e))

        return count

    def fetch_academic(self, urls: List = None):
        """Fetch academic papers"""
        AcademicFetcher = import_fetcher('ai_fetch_academic', 'AcademicFetcher')

        if not urls:
            urls = self.list_urls('Academic')

        fetcher = AcademicFetcher()
        count = 0

        for item in urls:
            url = item['url']
            if 'arxiv.org' not in url and 'paperswithcode' not in url:
                continue

            if not self.should_fetch(url):
                print(f"Skipping: {url}")
                continue

            print(f"Fetching academic: {url}")
            try:
                from _shared.utils import parse_arxiv_id

                paper_id = parse_arxiv_id(url)
                if paper_id:
                    result = fetcher.fetch_paper(paper_id)
                    md = fetcher.format_as_markdown(result)

                    # Save
                    category = 'cs_CL'  # default
                    output_dir = Path(STORAGE_BASE) / 'academic' / 'arxiv' / category
                    output_dir.mkdir(parents=True, exist_ok=True)
                    output_file = output_dir / f"{paper_id}.md"
                    output_file.write_text(md, encoding='utf-8')

                    self.mark_fetched(url, str(output_file))
                    count += 1
                    print(f"  -> Saved to {output_file}")

            except Exception as e:
                print(f"  -> Error: {e}")
                self.mark_failed(url, str(e))

        return count

    def fetch_company(self, urls: List = None):
        """Fetch company blogs"""
        CompanyFetcher = import_fetcher('ai_fetch_company', 'CompanyFetcher')

        if not urls:
            urls = self.list_urls('Company')

        fetcher = CompanyFetcher()
        count = 0

        for item in urls:
            url = item['url']
            section = item.get('section', '')

            if not self.should_fetch(url):
                print(f"Skipping: {url}")
                continue

            print(f"Fetching company: {url}")
            try:
                # Extract company name from domain
                company = extract_domain(url).replace('.com', '').replace('.cn', '')

                article = fetcher.fetch_article(url, company)
                md = fetcher.format_as_markdown(article)

                # Save
                slug = slugify(article['title'], max_length=50)
                output_dir = Path(STORAGE_BASE) / 'company' / company / 'blogs'
                output_dir.mkdir(parents=True, exist_ok=True)
                output_file = output_dir / f"{slug}.md"
                output_file.write_text(md, encoding='utf-8')

                self.mark_fetched(url, str(output_file))
                count += 1
                print(f"  -> Saved to {output_file}")

            except Exception as e:
                print(f"  -> Error: {e}")
                self.mark_failed(url, str(e))

        return count

    def fetch_media(self, urls: List = None):
        """Fetch newsletters and podcasts"""
        NewsletterFetcher = import_fetcher('ai_fetch_media', 'NewsletterFetcher')
        PodcastFetcher = import_fetcher('ai_fetch_media', 'PodcastFetcher')

        if not urls:
            urls = self.list_urls('Media')

        newsletter_fetcher = NewsletterFetcher()
        podcast_fetcher = PodcastFetcher()
        count = 0

        for item in urls:
            url = item['url']
            section = item.get('section', '').lower()

            if not self.should_fetch(url):
                print(f"Skipping: {url}")
                continue

            print(f"Fetching media: {url}")
            try:
                if 'substack' in url or 'newsletter' in section:
                    publisher = extract_domain(url).replace('.com', '').replace('.substack', '')
                    article = newsletter_fetcher.fetch_article(url, publisher)
                    md = newsletter_fetcher.format_as_markdown(article)
                    slug = slugify(article['title'], max_length=50)
                    output_dir = Path(STORAGE_BASE) / 'media' / 'newsletter' / publisher

                elif 'podcast' in section or 'lexfridman' in url or 'dwarkesh' in url:
                    podcast_name = url.split('/')[2].replace('.com', '') if len(url.split('/')) > 2 else 'unknown'
                    episode = podcast_fetcher.fetch_episode(url, podcast_name)
                    md = podcast_fetcher.format_as_markdown(episode)
                    slug = slugify(episode['title'], max_length=50)
                    output_dir = Path(STORAGE_BASE) / 'media' / 'podcast' / podcast_name

                else:
                    continue

                output_dir.mkdir(parents=True, exist_ok=True)
                output_file = output_dir / f"{slug}.md"
                output_file.write_text(md, encoding='utf-8')

                self.mark_fetched(url, str(output_file))
                count += 1
                print(f"  -> Saved to {output_file}")

            except Exception as e:
                print(f"  -> Error: {e}")
                self.mark_failed(url, str(e))

        return count


def main():
    parser = argparse.ArgumentParser(description='AI Content Fetch Daily')
    parser.add_argument('--stats', action='store_true', help='Show fetch statistics')
    parser.add_argument('--list', action='store_true', help='List all URLs')
    parser.add_argument('--failed', action='store_true', help='Show failed URLs')
    parser.add_argument('--full', action='store_true', help='Force full fetch')
    parser.add_argument('--github', action='store_true', help='Fetch GitHub only')
    parser.add_argument('--academic', action='store_true', help='Fetch academic only')
    parser.add_argument('--company', action='store_true', help='Fetch company only')
    parser.add_argument('--media', action='store_true', help='Fetch media only')

    args = parser.parse_args()

    fetcher = FetchDaily()

    if args.stats:
        stats = fetcher.get_stats()
        print("=== Fetch Statistics ===")
        print(f"Total URLs: {stats['total_urls']}")
        print(f"Translated: {stats['translated']}")
        print(f"Failed: {stats['failed']}")
        print(f"Last fetch: {stats['last_fetch']}")

    elif args.list:
        urls = fetcher.list_urls()
        print(f"=== All URLs ({len(urls)}) ===")
        for i, item in enumerate(urls[:50]):
            print(f"{i+1}. [{item['section']}] {item['url']}")
        if len(urls) > 50:
            print(f"... and {len(urls) - 50} more")

    elif args.failed:
        print("=== Failed URLs ===")
        for url_hash, data in fetcher.failed_urls.items():
            print(f"- {data['url']}: {data.get('error', 'Unknown')}")

    else:
        print("=== AI Content Fetch Daily ===")
        print(f"Mode: {'Full' if args.full else 'Incremental'}")
        print()

        total = 0

        if args.github or not any([args.github, args.academic, args.company, args.media]):
            print("Fetching GitHub...")
            total += fetcher.fetch_github()

        if args.academic or not any([args.github, args.academic, args.company, args.media]):
            print("Fetching Academic...")
            total += fetcher.fetch_academic()

        if args.company or not any([args.github, args.academic, args.company, args.media]):
            print("Fetching Company...")
            total += fetcher.fetch_company()

        if args.media or not any([args.github, args.academic, args.company, args.media]):
            print("Fetching Media...")
            total += fetcher.fetch_media()

        print()
        print(f"Done! Fetched {total} items.")


if __name__ == '__main__':
    main()
