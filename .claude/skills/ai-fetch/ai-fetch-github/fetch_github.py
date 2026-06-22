"""
GitHub Repository Fetcher

Fetches GitHub repository information including README, releases, and metadata.
"""

import sys
import os
import base64
import time
import requests
from pathlib import Path
from datetime import datetime, timedelta

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from _shared.config import should_use_proxy, REQUEST_TIMEOUT, STORAGE_BASE
from _shared.translate import Translator
from _shared.utils import (
    parse_github_url,
    format_markdown_frontmatter,
    slugify,
    get_file_timestamp,
    extract_domain,
)


class GitHubFetcher:
    """Fetcher for GitHub repositories"""

    def __init__(self, use_proxy: bool = False):
        self.api_base = "https://api.github.com"
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Claude-Code-AI-Fetcher'
        }
        self.translator = Translator()
        self.last_request = 0
        self.delay = 10.0  # Rate limit: 60 req/hr without token, use 10s to be safe
        self.use_proxy = use_proxy

    def _rate_limit_wait(self):
        """Wait to respect rate limits"""
        elapsed = time.time() - self.last_request
        if elapsed < self.delay:
            time.sleep(self.delay - elapsed)
        self.last_request = time.time()

    def fetch_repo(self, owner: str, repo: str) -> dict:
        """
        Fetch complete repository information.

        Args:
            owner: Repository owner
            repo: Repository name

        Returns:
            Dictionary with repo info, README, and releases
        """
        results = {}

        # 1. Repository info
        self._rate_limit_wait()
        results['info'] = self._fetch_repo_info(owner, repo)

        # 2. Latest release
        self._rate_limit_wait()
        results['latest_release'] = self._fetch_latest_release(owner, repo)

        # 3. Recent releases (last 6 months)
        self._rate_limit_wait()
        results['releases'] = self._fetch_recent_releases(owner, repo)

        # 4. README
        self._rate_limit_wait()
        results['readme'] = self._fetch_readme(owner, repo)

        return results

    def _fetch_repo_info(self, owner: str, repo: str) -> dict:
        """Fetch repository metadata"""
        url = f"{self.api_base}/repos/{owner}/{repo}"
        response = self._get(url)

        if response.status_code == 200:
            data = response.json()
            return {
                'full_name': data.get('full_name'),
                'description': data.get('description'),
                'stars': data.get('stargazers_count'),
                'forks': data.get('forks_count'),
                'language': data.get('language'),
                'topics': data.get('topics', []),
                'homepage': data.get('homepage'),
                'pushed_at': data.get('pushed_at'),
                'created_at': data.get('created_at'),
                'url': data.get('html_url'),
            }
        else:
            raise Exception(f"Failed to fetch repo info: {response.status_code}")

    def _fetch_latest_release(self, owner: str, repo: str) -> dict:
        """Fetch latest release"""
        url = f"{self.api_base}/repos/{owner}/{repo}/releases/latest"
        response = self._get(url)

        if response.status_code == 200:
            data = response.json()
            return {
                'tag': data.get('tag_name'),
                'name': data.get('name'),
                'body': data.get('body'),
                'published_at': data.get('published_at'),
                'url': data.get('html_url'),
            }
        elif response.status_code == 404:
            return None  # No releases
        else:
            raise Exception(f"Failed to fetch latest release: {response.status_code}")

    def _fetch_recent_releases(self, owner: str, repo: str, months: int = 6) -> list:
        """Fetch releases from last N months"""
        url = f"{self.api_base}/repos/{owner}/{repo}/releases"
        response = self._get(url)

        if response.status_code != 200:
            return []

        data = response.json()
        cutoff_date = datetime.now() - timedelta(days=months * 30)

        releases = []
        for release in data:
            published_at = datetime.strptime(
                release.get('published_at', '2000-01-01'),
                '%Y-%m-%dT%H:%M:%SZ'
            )
            if published_at >= cutoff_date:
                releases.append({
                    'tag': release.get('tag_name'),
                    'name': release.get('name'),
                    'body': release.get('body'),
                    'published_at': release.get('published_at'),
                    'url': release.get('html_url'),
                })

        return releases

    def _fetch_readme(self, owner: str, repo: str) -> dict:
        """Fetch repository README"""
        url = f"{self.api_base}/repos/{owner}/{repo}/readme"
        response = self._get(url)

        if response.status_code == 200:
            data = response.json()
            content = base64.b64decode(data['content']).decode('utf-8')

            # Detect encoding from content
            encoding = data.get('encoding', 'base64')
            if encoding == 'base64':
                pass  # Already decoded

            return {
                'content': content,
                'encoding': encoding,
                'sha': data.get('sha'),
                'url': data.get('html_url'),
            }
        else:
            raise Exception(f"Failed to fetch README: {response.status_code}")

    def _get(self, url: str, retry_count: int = 3) -> requests.Response:
        """Make GET request with proxy support and retry on 403"""
        proxies = {}
        if self.use_proxy or should_use_proxy(url):
            proxies = {
                'http': 'http://127.0.0.1:26001',
                'https': 'http://127.0.0.1:26001'
            }

        for attempt in range(retry_count):
            response = requests.get(
                url,
                headers=self.headers,
                proxies=proxies,
                timeout=REQUEST_TIMEOUT
            )

            if response.status_code == 403:
                # Rate limited - wait longer and retry
                wait_time = (attempt + 1) * 30  # 30s, 60s, 90s
                print(f"  Rate limited (403), waiting {wait_time}s...")
                time.sleep(wait_time)
                continue
            return response

        return response  # Return last response even if failed

    def format_as_markdown(self, results: dict, owner: str, repo: str) -> str:
        """
        Format repository information as markdown.

        Args:
            results: Results from fetch_repo
            owner: Repository owner
            repo: Repository name

        Returns:
            Formatted markdown string
        """
        info = results.get('info', {})
        readme = results.get('readme', {})
        releases = results.get('releases', [])
        latest = results.get('latest_release')

        # Translate README
        readme_content = readme.get('content', '')
        if readme_content:
            readme_translated = self.translator.translate(readme_content)
        else:
            readme_translated = ''

        # Build markdown
        md = format_markdown_frontmatter(
            title=repo,
            source='github.com',
            url=f"https://github.com/{owner}/{repo}",
            date=datetime.now().strftime('%Y-%m-%d'),
            category='github',
            translated=True,
            fetched_at=get_file_timestamp()
        )

        # Repository header
        md += f"# {owner}/{repo}\n\n"
        md += f"**Stars**: {info.get('stars', 0):,} | "
        md += f"**Forks**: {info.get('forks', 0):,} | "
        md += f"**语言**: {info.get('language', 'N/A')}\n\n"

        if info.get('description'):
            md += f"**描述**: {info.get('description')}\n\n"

        if info.get('topics'):
            topics = ', '.join(info.get('topics', []))
            md += f"**Topics**: {topics}\n\n"

        md += "---\n\n"

        # README section
        md += "## 项目介绍\n\n"
        md += readme_translated if readme_translated else "[README内容]\n"
        md += "\n\n---\n\n"

        # Releases section
        if releases:
            md += "## 发布记录（近半年）\n\n"

            for release in releases:
                tag = release.get('tag', '')
                name = release.get('name', '')
                published = release.get('published_at', '')[:10]
                body = release.get('body', '')

                if body:
                    body_translated = self.translator.translate(body)
                else:
                    body_translated = ''

                md += f"【{tag}】{published}\n\n"
                if name and name != tag:
                    md += f"**{name}**\n\n"
                if body_translated:
                    md += f"{body_translated}\n"
                md += "\n---\n\n"

        # Footer
        md += f"*原文请访问 [GitHub仓库](https://github.com/{owner}/{repo})*\n"

        return md


def main():
    """Main entry point"""
    import argparse

    parser = argparse.ArgumentParser(description='Fetch GitHub repositories')
    parser.add_argument('--repo', type=str, help='Specific repo (owner/repo format)')
    parser.add_argument('--list', action='store_true', help='List configured repos')
    parser.add_argument('--force', action='store_true', help='Force re-fetch')

    args = parser.parse_args()

    fetcher = GitHubFetcher()

    if args.list:
        print("Configured GitHub repos would be listed here")
        print("Source from: ai-news-sources.md")
        return

    if args.repo:
        # Fetch specific repo
        try:
            owner, repo = args.repo.split('/')
            print(f"Fetching {owner}/{repo}...")

            results = fetcher.fetch_repo(owner, repo)
            md = fetcher.format_as_markdown(results, owner, repo)

            # Save to file
            output_dir = Path(STORAGE_BASE) / 'github' / f"{owner}_{repo}"
            output_dir.mkdir(parents=True, exist_ok=True)

            output_file = output_dir / 'README.md'
            output_file.write_text(md, encoding='utf-8')

            print(f"Saved to {output_file}")

        except Exception as e:
            print(f"Error: {e}")

    else:
        print("Fetching all GitHub repos...")
        print("Use --repo owner/repo to fetch specific repo")
        print("Use --list to list configured repos")


if __name__ == '__main__':
    main()
