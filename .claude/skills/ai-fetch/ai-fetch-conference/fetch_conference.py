"""
Conference Fetcher

Fetches conference agenda, speaker info, and presentation content.
Multi-source strategy: official website -> video -> speaker articles -> news reports.

Architecture:
- Generic extractors work for most conference sites
- Site-specific extractors can be registered for special handling (e.g., Google I/O SPA)
"""

import sys
import os
import re
import time
import json
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Callable, Optional
from bs4 import BeautifulSoup
import requests

sys.path.insert(0, str(Path(__file__).parent.parent))
from _shared.config import should_use_proxy, REQUEST_TIMEOUT, STORAGE_BASE
from _shared.translate import Translator
from _shared.utils import (
    format_markdown_frontmatter,
    slugify,
    get_file_timestamp,
    extract_domain,
)


# ============================================================================
# Extractor Registry - Allows site-specific extractors
# ============================================================================

class ExtractorRegistry:
    """Registry for content extractors with priority ordering"""

    def __init__(self):
        self._extractors: List[tuple[int, str, Callable]] = []

    def register(self, priority: int, name: str, extractor: Callable):
        """Register an extractor with priority (higher = tried first)"""
        self._extractors.append((priority, name, extractor))
        self._extractors.sort(key=lambda x: -x[0])  # Sort by priority descending

    def extract(self, html: str, soup: BeautifulSoup, url: str) -> Optional[str]:
        """Try each extractor in priority order until one returns content"""
        for priority, name, extractor in self._extractors:
            try:
                result = extractor(html, soup, url)
                if result and len(result.strip()) > 100:
                    print(f"    [Extractor '{name}' matched, got {len(result)} chars]")
                    return result
            except Exception as e:
                print(f"    [Extractor '{name}' failed: {e}]")
        return None


# Global registry instance
_extractor_registry = ExtractorRegistry()


def register_extractor(priority: int, name: str):
    """Decorator to register an extractor function"""
    def decorator(func: Callable):
        _extractor_registry.register(priority, name, func)
        return func
    return decorator


# ============================================================================
# Generic Extractors (work for most sites)
# ============================================================================

@register_extractor(priority=10, name="generic_html")
def generic_html_extractor(html: str, soup: BeautifulSoup, url: str) -> Optional[str]:
    """Generic HTML content extraction for traditional websites"""
    content = ''

    # Try main/article tags
    for tag in ['main', 'article', 'div[class*="content"]', 'div[class*="main"]', 'div[id*="content"]']:
        main_tag = soup.select_one(tag)
        if main_tag:
            for remove in main_tag.find_all(['script', 'style', 'nav', 'footer', 'header', 'aside']):
                remove.decompose()
            content = main_tag.get_text(separator='\n\n', strip=True)
            if len(content) > 200:
                break

    if not content or len(content) < 100:
        body = soup.find('body')
        if body:
            for tag in body.find_all(['script', 'style', 'noscript', 'iframe', 'svg']):
                tag.decompose()
            content = body.get_text(separator='\n\n', strip=True)

    return content[:10000] if content else None


@register_extractor(priority=20, name="meta_tags")
def meta_tags_extractor(html: str, soup: BeautifulSoup, url: str) -> Optional[str]:
    """Extract meta tags as fallback content"""
    parts = []

    for selector, attr in [
        ('meta[name="description"]', 'content'),
        ('meta[property="og:title"]', 'content'),
        ('meta[property="og:description"]', 'content'),
    ]:
        tag = soup.select_one(selector)
        if tag and tag.get(attr):
            parts.append(f"{tag.get(attr)}")

    return '\n\n'.join(parts) if parts else None


# ============================================================================
# Google I/O Specific Extractor
# ============================================================================

@register_extractor(priority=100, name="google_io_spa")
def google_io_spa_extractor(html: str, soup: BeautifulSoup, url: str) -> Optional[str]:
    """Specialized extractor for Google I/O SPA pages"""
    if 'io.google' not in url:
        return None

    parts = []

    # 1. Extract sessions from embedded JSON
    sessions_data = extract_google_io_sessions(html)
    if sessions_data:
        parts.append(sessions_data)

    # 2. Extract navigation structure
    nav_text = extract_nav_structure(soup)
    if nav_text and len(nav_text) > 50:
        parts.append(f"\n### 导航结构\n{nav_text}")

    return '\n\n'.join(parts) if parts else None


def extract_google_io_sessions(html: str) -> Optional[str]:
    """Extract session data from Google I/O page"""
    parts = []

    # Pattern 1: Find sessions from data-analytic-event-params attributes
    # Format: {"sessionName": "Google keynote", "sessionId": "google-keynote-1", ...}
    session_pattern = r'data-analytic-event-params=\'{"sessionName":\s*"([^"]+)",\s*"sessionId":\s*"([^"]+)",\s*"sessionCode":\s*"([^"]+)"'
    matches = re.findall(session_pattern, html)
    if matches:
        sessions = []
        for name, session_id, code in matches:
            sessions.append({
                'name': name,
                'uid': session_id,
                'code': code,
                'content_type': 'Session',
            })
        if sessions:
            parts.append(format_google_io_sessions(sessions))
            print(f"    [Found {len(sessions)} sessions from analytics]")

    # Pattern 2: Look for iodata.vars with PA_KEYNOTE_IDS for keynote info
    iodata_match = re.search(r'window\.iodata\.vars\s*=\s*(\{[^;]+\})', html)
    if iodata_match:
        try:
            iodata = json.loads(iodata_match.group(1))
            keynote_ids = iodata.get('PA_KEYNOTE_IDS', [])
            if keynote_ids:
                parts.append(f"\n### 主题演讲数量\n共 {len(keynote_ids)} 个 PA Keynote")
        except json.JSONDecodeError:
            pass

    # Pattern 3: Extract topic IDs from the page
    topic_pattern = r'\{"id":(\d+),"name":"([^"]+)"\}'
    topic_matches = re.findall(topic_pattern, html)
    if topic_matches:
        topics = [{'id': int(id), 'name': name} for id, name in topic_matches]
        unique_topics = {t['id']: t for t in topics}.values()
        parts.append(f"\n### 主题分类 ({len(unique_topics)}个)\n")
        for t in list(unique_topics)[:20]:
            parts.append(f"- {t['name']}")

    return '\n\n'.join(parts) if parts else None


def format_google_io_sessions(sessions: list) -> str:
    """Format Google I/O sessions as markdown"""
    parts = [f"\n## 会议Sessions (共 {len(sessions)} 个)\n"]

    for s in sessions[:30]:
        name = s.get('name', 'Unknown')
        uid = s.get('uid', '')
        code = s.get('code', '')
        ctype = s.get('content_type', 'Session')

        parts.append(f"- **{name}**")
        if uid:
            parts.append(f"  - ID: {uid}")
        if code:
            parts.append(f"  - Code: {code}")

    if len(sessions) > 30:
        parts.append(f"\n  ... 还有 {len(sessions) - 30} 个sessions")

    return '\n'.join(parts)


def extract_nav_structure(soup: BeautifulSoup) -> str:
    """Extract navigation structure"""
    parts = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        if '/2026/' in href and href not in parts:
            text = link.get_text(strip=True)
            if text and len(text) > 1 and len(text) < 50:
                parts.append(f"- {text}: /2026/{href.split('/2026/')[-1]}")
    return '\n'.join(parts[:20])


# ============================================================================
# Conference Fetcher Class
# ============================================================================

class ConferenceFetcher:
    """Fetcher for conference content"""

    def __init__(self, use_proxy: bool = True):
        """use_proxy defaults to True for overseas conferences"""
        self.translator = Translator()
        self.use_proxy = use_proxy
        self._custom_extractors: List[tuple[int, str, Callable]] = []

    def add_extractor(self, priority: int, name: str, extractor: Callable):
        """Add a custom extractor for this fetcher instance"""
        self._custom_extractors.append((priority, name, extractor))
        self._custom_extractors.sort(key=lambda x: -x[0])

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
        """Parse conference page using registered extractors"""
        soup = BeautifulSoup(html, 'html.parser')

        # Title
        title = ''
        title_tag = soup.find('h1') or soup.find('title')
        if title_tag:
            title = title_tag.get_text(strip=True)

        # Try custom extractors first, then global registry
        content = None

        # Try custom extractors (site-specific ones added to this instance)
        for priority, ext_name, extractor in self._custom_extractors:
            try:
                content = extractor(html, soup, url)
                if content and len(content.strip()) > 100:
                    print(f"  [Custom extractor '{ext_name}' matched]")
                    break
            except Exception as e:
                print(f"  [Custom extractor '{ext_name}' failed: {e}]")

        # Try global registry
        if not content or len(content.strip()) < 100:
            content = _extractor_registry.extract(html, soup, url)

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

    def discover_subpages(self, url: str, max_pages: int = 20) -> list:
        """Discover sub-pages from conference site"""
        try:
            response = self._get(url)
            if response.status_code != 200:
                return []
        except Exception:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        base_url = url.rstrip('/')
        if '/2026/' in base_url:
            base_url = base_url.split('/2026/')[0] + '/2026'
        elif '/2025/' in base_url:
            base_url = base_url.split('/2025/')[0] + '/2025'

        links = []
        seen = set()

        for link in soup.find_all('a', href=True):
            href = link['href']
            if not href:
                continue

            if any(skip in href for skip in ['#', 'javascript', 'mailto:', 'tel:']):
                continue

            if href.startswith('/'):
                full_url = base_url + href
            elif href.startswith('http') and base_url not in href:
                continue
            else:
                full_url = href

            if any(ext in full_url for ext in ['.css', '.js', '.png', '.jpg', '.svg', '.ico', '.webp', '.woff']):
                continue

            if full_url not in seen:
                seen.add(full_url)
                links.append({'url': full_url, 'title': link.get_text(strip=True) or ''})

        return links[:max_pages]

    def fetch_with_subpages(self, url: str, name: str, year: str = None, max_subpages: int = 10) -> dict:
        """Fetch conference with discovered sub-pages"""
        if year is None:
            year = datetime.now().strftime('%Y')

        print(f"Fetching main page: {url}")
        conf = self.fetch_conference(url, name, year)
        all_content = [conf.get('content', '')]

        subpages = self.discover_subpages(url, max_pages=max_subpages)
        print(f"Discovered {len(subpages)} sub-pages")

        for i, page in enumerate(subpages[:max_subpages]):
            if page['url'] == url:
                continue
            print(f"  Fetching [{i+1}/{min(len(subpages), max_subpages)}]: {page['url']}")
            try:
                sub_conf = self.fetch_conference(page['url'], name, year)
                if sub_conf.get('content') and len(sub_conf['content']) > 100:
                    all_content.append(f"\n\n## {sub_conf.get('title', page['title'])}\n\n{sub_conf['content']}")
            except Exception as e:
                print(f"    Error: {e}")
            time.sleep(0.5)

        conf['content'] = '\n\n'.join(filter(None, all_content))
        return conf

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


# ============================================================================
# Main Entry Point
# ============================================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch conference')
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--name', type=str, required=True)
    parser.add_argument('--year', type=str, help='Conference year')
    parser.add_argument('--discover', action='store_true', help='Discover agenda pages')
    parser.add_argument('--subpages', action='store_true', help='Fetch sub-pages (keynotes, sessions)')
    parser.add_argument('--max-subpages', type=int, default=10, help='Max sub-pages to fetch')

    args = parser.parse_args()
    fetcher = ConferenceFetcher(use_proxy=True)

    if args.discover:
        print(f"Discovering agenda from {args.url}...")
        pages = fetcher.discover_agenda(args.url)
        print(f"Found {len(pages)} pages:")
        for i, page in enumerate(pages[:10]):
            print(f"  {i+1}. {page}")

    else:
        print(f"Fetching conference: {args.url}...")
        try:
            if args.subpages:
                conf = fetcher.fetch_with_subpages(args.url, args.name, args.year, args.max_subpages)
            else:
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