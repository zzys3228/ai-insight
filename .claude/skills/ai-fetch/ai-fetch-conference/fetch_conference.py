"""
Conference Fetcher V2 - Generic with Transcript Support

Fetches conference content including:
- Session list with descriptions
- Full transcripts (from page, YouTube, or external sources)
- Speaker information
- Video links

Architecture:
- Generic extractors for traditional sites
- Site-specific extractors for special handling
- YouTube transcript fetching
- Web search for external transcripts
"""

import sys
import os
import re
import time
import json
import html as html_module
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Callable, Optional
from bs4 import BeautifulSoup
import requests

sys.path.insert(0, str(Path(__file__).parent.parent))
from _shared.config import should_use_proxy, REQUEST_TIMEOUT, STORAGE_BASE
from _shared.translate import Translator
from _shared.utils import format_markdown_frontmatter, get_file_timestamp, extract_domain

# Optional Playwright
try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False


# ============================================================================
# Transcript Sources (in priority order)
# ============================================================================

class TranscriptSource:
    """Base class for transcript sources"""
    def fetch(self, session_url: str, session_id: str) -> Optional[str]:
        """Fetch transcript. Return None if not available."""
        raise NotImplementedError


class PageTranscriptSource(TranscriptSource):
    """Try to get transcript from session page HTML"""
    def fetch(self, session_url: str, session_id: str) -> Optional[str]:
        # Check if transcript is embedded in page
        try:
            proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
            resp = requests.get(session_url, proxies=proxies, timeout=30)
            if resp.status_code != 200:
                return None

            unescaped = html_module.unescape(resp.text)

            # Pattern for embedded transcript
            patterns = [
                r'"transcript":"([^"]{100,})"',
                r'"full_transcript":"([^"]{100,})"',
                r'"content":"([^"]{500,})"',
            ]

            for pattern in patterns:
                match = re.search(pattern, unescaped)
                if match:
                    return match.group(1).replace('\\n', '\n').replace('\\"', '"')

            return None
        except:
            return None


class YouTubeCaptionSource(TranscriptSource):
    """Fetch transcript from YouTube using yt-dlp"""
    def fetch(self, session_url: str, session_id: str) -> Optional[str]:
        # First find YouTube URL from session page
        youtube_url = self._find_youtube_url(session_url)
        if not youtube_url:
            return None

        video_id = self._extract_video_id(youtube_url)
        if not video_id:
            return None

        return self._get_captions_via_ytdlp(video_id)

    def _find_youtube_url(self, session_url: str) -> Optional[str]:
        try:
            proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
            resp = requests.get(session_url, proxies=proxies, timeout=30)
            if resp.status_code != 200:
                return None

            # Find YouTube links
            yt_pattern = r'https?://(?:www\.)?youtube\.com/[^\s"\'<>]+'
            matches = re.findall(yt_pattern, resp.text)
            for match in matches:
                if 'playlist' not in match and ('watch' in match or '/shorts/' in match):
                    return match.split('?')[0]  # Remove params
            return None
        except:
            return None

    def _extract_video_id(self, url: str) -> Optional[str]:
        patterns = [
            r'youtube\.com/watch\?v=([^&\s]+)',
            r'youtu\.be/([^&\s]+)',
            r'youtube\.com/shorts/([^&\s]+)',
        ]
        for pattern in patterns:
            match = re.search(pattern, url)
            if match:
                return match.group(1)
        return None

    def _get_captions_via_ytdlp(self, video_id: str) -> Optional[str]:
        """Get captions using yt-dlp"""
        import subprocess
        import tempfile
        import os

        # Cookies file path (if exists)
        cookies_file = Path(__file__).parent / "cookies.txt"

        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                output_file = os.path.join(tmpdir, 'caption')

                cmd = ['python', '-m', 'yt_dlp', '--write-auto-subs', '--sub-langs', 'en', '--skip-download', '--convert-subs', 'srt']

                # Add cookies if available
                if cookies_file.exists():
                    cmd.extend(['--cookies', str(cookies_file)])

                cmd.extend(['-o', output_file, f'https://www.youtube.com/watch?v={video_id}'])

                result = subprocess.run(cmd, capture_output=True, timeout=120, env={**os.environ, 'PYTHONIOENCODING': 'utf-8'})

                srt_file = output_file + '.en.srt'
                if os.path.exists(srt_file):
                    with open(srt_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    text = self._parse_srt(content)
                    if len(text) > 100:
                        return text

                vtt_file = output_file + '.en.vtt'
                if os.path.exists(vtt_file):
                    with open(vtt_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    text = self._parse_vtt(content)
                    if len(text) > 100:
                        return text

        except Exception as e:
            print(f"    yt-dlp error: {e}")

        return None

    def _parse_srt(self, content: str) -> str:
        """Parse SRT subtitle to plain text"""
        lines = content.strip().split('\n')
        text_parts = []

        for line in lines:
            line = line.strip()
            # Skip timestamps and numbers
            if '-->' in line or line.isdigit():
                continue
            # Clean HTML tags
            line = re.sub(r'<[^>]+>', '', line)
            # Skip empty lines
            if line:
                text_parts.append(line)

        return ' '.join(text_parts)

    def _parse_vtt(self, content: str) -> str:
        """Parse VTT subtitle to plain text"""
        lines = content.strip().split('\n')
        text_parts = []

        for line in lines:
            line = line.strip()
            # Skip timestamps and WEBVTT header
            if '-->' in line or line.startswith('WEBVTT') or line.startswith('NOTE'):
                continue
            # Clean HTML tags
            line = re.sub(r'<[^>]+>', '', line)
            # Skip empty lines
            if line:
                text_parts.append(line)

        return ' '.join(text_parts)


class BlogArticleSource(TranscriptSource):
    """Fetch full articles from blog.google (published keynotes)"""
    BLOG_URLS = {
        'google-io-2026-ceo': 'https://blog.google/innovation-and-ai/sundar-pichai-io-2026/',
        'google-io-2026-developer': 'https://blog.google/technology/developers/google-i-o-2026-developer-keynote/',
    }

    def fetch(self, session_url: str, session_id: str) -> Optional[str]:
        # Map session to blog article
        session_lower = session_id.lower()

        for key, url in self.BLOG_URLS.items():
            if key.replace('-', '') in session_lower.replace('-', '').replace('_', ''):
                return self._fetch_blog_article(url)

        # Try to find matching blog URL
        if 'keynote' in session_lower or 'keynote-1' in session_url:
            return self._fetch_blog_article(self.BLOG_URLS['google-io-2026-ceo'])

        return None

    def _fetch_blog_article(self, url: str) -> Optional[str]:
        try:
            proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
            resp = requests.get(url, proxies=proxies, timeout=30)
            if resp.status_code != 200:
                return None

            soup = BeautifulSoup(resp.text, 'html.parser')

            # Get article content
            article = soup.find('article') or soup.find('main') or soup.find('div', class_=lambda x: x and 'article' in x if x else False)

            if article:
                # Remove script, style, nav, footer, share buttons
                for tag in article.find_all(['script', 'style', 'nav', 'footer', 'aside']):
                    tag.decompose()
                for tag in article.find_all(class_=lambda x: x and any(y in str(x) for y in ['share', 'social', 'icon'])):
                    tag.decompose()

                text = article.get_text(separator='\n\n', strip=True)
                # Clean up share buttons and social links
                text = re.sub(r'\n+(Share|x\.com|Facebook|LinkedIn|Mail|Copy link)\n+', '\n', text)
                text = re.sub(r'\n{3,}', '\n\n', text)
                if len(text) > 500:
                    return text.strip()

            return None
        except:
            return None


# ============================================================================
# Conference Session
# ============================================================================

class Session:
    def __init__(self):
        self.id = ""
        self.uid = ""
        self.title = ""           # 原标题
        self.title_zh = ""        # 中文标题
        self.short_description = ""
        self.description = ""     # 原描述
        self.description_zh = ""  # 中文描述
        self.url = ""
        self.video_url = ""
        self.speakers = []       # 原始speaker对象列表
        self.speaker_names = []  # speaker ldap列表
        self.start_time = ""
        self.end_time = ""
        self.session_date = ""
        self.track = ""          # 分类
        self.track_zh = ""        # 中文分类
        self.content_type = ""   # 类型：技术演讲/工作坊/编程实验室/主题演讲
        self.level = ""          # 等级：Beginner/Intermediate
        self.transcript = None   # 完整字幕
        self.transcript_source = ""


# ============================================================================
# Generic Conference Extractor
# ============================================================================

class ConferenceExtractor:
    """Base class for conference extractors"""

    def extract_sessions(self, html: str, url: str) -> List[Session]:
        """Extract sessions from conference page HTML"""
        raise NotImplementedError

    def get_session_url(self, session: Session, base_url: str) -> str:
        """Get full URL for session page"""
        raise NotImplementedError


class GoogleIOExtractor(ConferenceExtractor):
    """Extractor for Google I/O conferences"""

    def extract_sessions(self, html: str, url: str) -> List[Session]:
        import json
        unescaped = html_module.unescape(html)
        sessions = []

        # Find sessions JSON array in the HTML
        # Pattern: sessions="[{...}]"
        pattern = r'sessions="(\[.*?\])"'
        match = re.search(pattern, unescaped, re.DOTALL)

        if not match:
            return sessions

        try:
            data = json.loads(match.group(1))
        except json.JSONDecodeError:
            return sessions

        for item in data:
            s = Session()

            # Basic fields
            s.id = str(item.get('id', ''))
            s.uid = item.get('uid', '')
            s.title = self._clean(item.get('event_title', ''))
            s.short_description = self._clean(item.get('event_short_description', ''))
            s.description = self._clean(item.get('event_long_description', '')) or s.short_description

            # Time fields
            s.start_time = item.get('start_time') or ''
            s.end_time = item.get('end_time') or ''
            s.session_date = item.get('session_date') or ''

            # Content type, level
            s.content_type = item.get('content_type', '')
            s.level = item.get('level', '')

            # Track (topic)
            topics = item.get('topics', [])
            if topics and isinstance(topics, list):
                s.track = topics[0].get('name', '') if topics else ''

            # Speakers
            speakers = item.get('speaker', [])
            if speakers and isinstance(speakers, list):
                s.speaker_names = [sp.get('ldap', '') for sp in speakers if sp.get('ldap')]

            # Video URL from youtube_vod_id
            youtube_id = item.get('youtube_vod_id')
            if youtube_id:
                s.video_url = f"https://www.youtube.com/watch?v={youtube_id}"

            # URL
            dest_url = item.get('destination_url', '')
            if dest_url:
                s.url = dest_url
            elif s.uid:
                s.url = f"https://io.google/2026/explore/{s.uid}"
            else:
                s.url = f"https://io.google/2026/explore/{self._to_id(s.title)}"

            if s.title:
                sessions.append(s)

        return sessions

    def get_session_url(self, session: Session, base_url: str) -> str:
        return session.url

    def _clean(self, text: str) -> str:
        if not text:
            return ""
        text = text.replace('\\u2019', "'").replace('\\u201c', '"').replace('\\u201d', '"')
        text = text.replace('\\n', ' ').replace('\\r', '').replace('\\', '')
        return text.strip()

    def _to_id(self, title: str) -> str:
        # Convert title to URL-friendly ID
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9\s-]', '', slug)
        slug = re.sub(r'[\s]+', '-', slug)
        return slug[:50]


# ============================================================================
# Conference Fetcher
# ============================================================================

class ConferenceFetcher:
    def __init__(self, use_proxy: bool = True):
        self.translator = Translator()
        self.use_proxy = use_proxy
        self.extractor: Optional[ConferenceExtractor] = None
        self.transcript_sources: List[TranscriptSource] = [
            BlogArticleSource(),
            YouTubeCaptionSource(),  # Uses yt-dlp for YouTube captions
            PageTranscriptSource(),
        ]

    def set_extractor(self, extractor: ConferenceExtractor):
        self.extractor = extractor

    def _get(self, url: str) -> requests.Response:
        proxies = {}
        if self.use_proxy:
            proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
        return requests.get(url, proxies=proxies, timeout=REQUEST_TIMEOUT)

    def fetch_conference(self, url: str, name: str, year: str = None,
                        fetch_transcripts: bool = True,
                        max_transcripts: int = 5) -> dict:
        """Fetch conference with sessions and optional transcripts"""
        if year is None:
            year = datetime.now().strftime('%Y')

        # Fetch main page
        if PLAYWRIGHT_AVAILABLE:
            html = self._fetch_with_playwright(url)
        else:
            resp = self._get(url)
            html = resp.text

        if not html:
            raise Exception("Failed to fetch page")

        # Extract sessions
        if self.extractor:
            sessions = self.extractor.extract_sessions(html, url)
        else:
            sessions = self._generic_extract_sessions(html, url)

        # Fetch transcripts - prioritize keynotes, then first N sessions
        if fetch_transcripts and sessions:
            # First try to find keynotes
            keynotes = [s for s in sessions if 'keynote' in s.title.lower()]
            transcript_count = 0

            # Fetch transcripts for keynotes (blog)
            for session in keynotes[:3]:
                transcript = self._fetch_transcript_by_title(session.title, session.url)
                if transcript:
                    session.transcript = transcript
                    session.transcript_source = "blog"
                    print(f"  Blog transcript: {session.title[:50]}")
                    transcript_count += 1
                time.sleep(0.5)

            # Then fetch YouTube captions for all remaining sessions
            print(f"  Fetching YouTube captions for {len(sessions)} sessions...")
            for session in sessions:
                if session.transcript:
                    continue  # Already has transcript
                # Try YouTube caption
                transcript = self._try_youtube_caption(session.url)
                if transcript:
                    session.transcript = transcript
                    session.transcript_source = "youtube"
                    print(f"  YouTube caption: {session.title[:50]}")
                    transcript_count += 1
                time.sleep(1)  # Rate limit

            print(f"  Total transcripts: {transcript_count}")

        return {
            'name': name,
            'url': url,
            'year': year,
            'date': datetime.now().strftime('%Y-%m-%d'),
            'sessions': sessions,
            'source': extract_domain(url),
        }

    def _fetch_with_playwright(self, url: str, wait: int = 15) -> str:
        if not PLAYWRIGHT_AVAILABLE:
            return ""

        html = ""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, args=['--no-sandbox'])
            context = browser.new_context(
                proxy={"server": "http://127.0.0.1:26001"},
                ignore_https_errors=True
            )
            page = context.new_page()
            try:
                page.goto(url, wait_until='domcontentloaded', timeout=30000)
                time.sleep(wait)
                html = page.content()
            except Exception as e:
                print(f"Playwright error: {e}")
            finally:
                browser.close()
        return html

    def _generic_extract_sessions(self, html: str, url: str) -> List[Session]:
        """Generic session extraction"""
        sessions = []
        unescaped = html_module.unescape(html)

    def _try_youtube_caption(self, session_url: str) -> Optional[str]:
        """Try to get YouTube caption for a session"""
        yt_source = YouTubeCaptionSource()
        return yt_source.fetch(session_url, "")

    def search_youtube_for_session(self, session_title: str) -> Optional[Dict]:
        """Search YouTube for a video matching the session title"""
        import subprocess

        try:
            # Search YouTube
            search_query = f"Google I/O 2026 {session_title}"
            cmd = ['python', '-m', 'yt_dlp', '--flat-playlist', '--print', '%(title)s|%(id)s',
                   f'ytsearch1:{search_query}']

            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

            if result.stdout.strip():
                line = result.stdout.strip().split('\n')[0]
                if '|' in line:
                    parts = line.split('|', 1)
                    return {'title': parts[0], 'id': parts[1]}

        except Exception as e:
            print(f"    Search error: {e}")

        return None

    def get_youtube_playlist_transcripts(self, playlist_url: str = "https://www.youtube.com/playlist?list=PLOU2XLYxmsILVF9qmspC4i4R0t3o64HSx",
                                        sessions: List = None) -> Dict[str, str]:
        """Get transcripts for all videos in YouTube playlist and search for session videos"""
        import subprocess

        transcripts = {}

        # First get playlist videos
        try:
            cmd = ['python', '-m', 'yt_dlp', '--flat-playlist', '--print', '%(title)s|%(id)s', playlist_url]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

            videos = []
            for line in result.stdout.strip().split('\n'):
                if '|' in line:
                    parts = line.split('|', 1)
                    if len(parts) == 2:
                        videos.append({'title': parts[0], 'id': parts[1]})

            print(f"  Found {len(videos)} videos in playlist")

            # Get transcript for each video
            yt_source = YouTubeCaptionSource()
            for video in videos:
                print(f"    Getting caption: {video['title'][:50]}...")
                transcript = yt_source._get_captions_via_ytdlp(video['id'])
                if transcript:
                    transcripts[video['title']] = transcript
                time.sleep(1)

        except Exception as e:
            print(f"  Playlist transcript error: {e}")

        # Then search for additional session videos
        if sessions:
            print(f"  Searching for {len(sessions)} session videos...")
            yt_source = YouTubeCaptionSource()
            found_count = 0

            for session in sessions:
                # Search YouTube
                result = self.search_youtube_for_session(session.title)
                if result:
                    video_id = result['id']
                    video_title = result['title']
                    print(f"    Found: {video_title[:50]}...")
                    transcript = yt_source._get_captions_via_ytdlp(video_id)
                    if transcript:
                        transcripts[video_title] = transcript
                        found_count += 1
                time.sleep(2)  # Rate limit

            print(f"  Found {found_count} additional session transcripts via search")

        return transcripts

        # Try Google I/O pattern first
        if 'io.google' in url:
            extractor = GoogleIOExtractor()
            sessions = extractor.extract_sessions(html, url)

        return sessions

    def _fetch_transcript(self, session: Session) -> Optional[str]:
        """Try each transcript source in order"""
        for source in self.transcript_sources:
            try:
                transcript = source.fetch(session.url, session.id)
                if transcript and len(transcript) > 100:
                    return transcript
            except Exception as e:
                print(f"  Transcript source {source.__class__.__name__} failed: {e}")
        return None

    def _fetch_transcript_by_title(self, title: str, url: str) -> Optional[str]:
        """Fetch transcript based on session title"""
        title_lower = title.lower()

        # Map titles to blog articles
        blog_mapping = {
            'ceo': 'https://blog.google/innovation-and-ai/sundar-pichai-io-2026/',
            'developer': 'https://blog.google/technology/developers/google-i-o-2026-developer-keynote/',
        }

        # Match by keywords
        if 'keynote' in title_lower and 'developer' not in title_lower:
            url = blog_mapping.get('ceo')
        elif 'developer' in title_lower and 'keynote' in title_lower:
            url = blog_mapping.get('developer')
        else:
            return None

        if url:
            try:
                proxies = {'http': 'http://127.0.0.1:26001', 'https': 'http://127.0.0.1:26001'}
                resp = requests.get(url, proxies=proxies, timeout=30)
                if resp.status_code == 200:
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    article = soup.find('article') or soup.find('main')
                    if article:
                        for tag in article.find_all(['script', 'style', 'nav', 'footer', 'aside']):
                            tag.decompose()
                        text = article.get_text(separator='\n\n', strip=True)
                        text = re.sub(r'\n+(Share|x\.com|Facebook|LinkedIn|Mail|Copy link)\n+', '\n', text)
                        text = re.sub(r'\n{3,}', '\n\n', text)
                        if len(text) > 500:
                            return text.strip()
            except:
                pass

        return None

    def format_as_markdown(self, conf: dict, translate: bool = True) -> str:
        """Format conference as markdown with optional translation"""
        md = format_markdown_frontmatter(
            title=conf['name'],
            source=conf['source'],
            url=conf['url'],
            date=conf['date'],
            category=f"conference/{conf['name']}/{conf['year']}",
            translated=translate,
            fetched_at=get_file_timestamp(),
        )

        # Translate name and source if needed
        conf_name = conf['name']
        conf_source = conf['source']
        if translate and self.translator:
            conf_name = self.translator.translate(conf['name']) or conf['name']
            conf_source = self.translator.translate(conf['source']) or conf['source']

        md += f"# {conf_name} {conf['year']}\n\n"
        md += f"**来源**: {conf_source} | **日期**: {conf['date']}\n\n"
        md += "---\n\n"

        # Sessions
        sessions = conf.get('sessions', [])
        md += f"## Sessions ({len(sessions)}个)\n\n"

        for i, session in enumerate(sessions, 1):
            # Translate title
            title = session.title
            if translate and self.translator:
                title = self.translator.translate(session.title) or session.title

            md += f"### {i}. {title}\n\n"

            # Session metadata
            meta_parts = []

            # Time and date
            if session.session_date:
                date_str = session.session_date
                if translate:
                    # Convert date format
                    date_str = self.translator.translate(date_str) or date_str
                meta_parts.append(f"📅 {date_str}")

            if session.start_time:
                # Format time (10:00:00 -> 10:00)
                start = session.start_time[:5] if session.start_time else ""
                end = session.end_time[:5] if session.end_time else ""
                if start and end:
                    time_str = f"{start} - {end}"
                elif start:
                    time_str = start
                else:
                    time_str = ""
                if time_str:
                    meta_parts.append(f"🕐 {time_str} PT")

            # Track
            if session.track:
                track = session.track
                if translate:
                    track = self.translator.translate(track) or track
                meta_parts.append(f"📂 {track}")

            # Content type
            if session.content_type:
                ct = session.content_type
                if translate:
                    ct = self.translator.translate(ct) or ct
                meta_parts.append(f"🎯 {ct}")

            # Level
            if session.level:
                meta_parts.append(f"📊 {session.level}")

            if meta_parts:
                md += " | ".join(meta_parts) + "\n\n"

            # Speakers (ldap)
            if session.speaker_names:
                md += f"👤 **演讲者**: {', '.join(session.speaker_names)}\n\n"

            # Description
            if session.description:
                desc = session.description
                if translate and self.translator:
                    desc = self.translator.translate(desc) or desc
                md += f"{desc}\n\n"

            # Transcript
            if session.transcript:
                md += "---\n\n"
                md += f"#### 完整文字稿\n\n"

                # Translate transcript if needed
                transcript = session.transcript
                if translate and self.translator:
                    transcript = self.translator.translate(transcript) or transcript

                md += transcript  # 保留完整字幕，不截断
                md += "\n\n"

            md += "---\n\n"

        # Add playlist transcripts
        playlist_transcripts = conf.get('playlist_transcripts', {})
        if playlist_transcripts:
            md += f"\n\n## YouTube 视频文字稿 ({len(playlist_transcripts)}个)\n\n"
            for title, transcript in playlist_transcripts.items():
                # Translate YouTube title
                display_title = title
                if translate and self.translator:
                    display_title = self.translator.translate(title) or title

                md += f"### {display_title}\n\n"

                # Translate transcript if needed
                if translate and self.translator:
                    transcript = self.translator.translate(transcript) or transcript

                md += transcript  # 保留完整字幕，不截断
                md += "\n\n---\n\n"

        return md


# ============================================================================
# Main
# ============================================================================

def main():
    import argparse
    parser = argparse.ArgumentParser(description='Fetch conference with transcripts')
    parser.add_argument('--url', required=True, help='Conference URL')
    parser.add_argument('--name', required=True, help='Conference name')
    parser.add_argument('--year', default=None, help='Year')
    parser.add_argument('--playwright', action='store_true', help='Use Playwright')
    parser.add_argument('--wait', type=int, default=15, help='Wait seconds')
    parser.add_argument('--transcripts', action='store_true', default=True, help='Fetch transcripts')
    parser.add_argument('--max-transcripts', type=int, default=5, help='Max transcripts')
    parser.add_argument('--playlist-transcripts', action='store_true', default=True, help='Fetch YouTube playlist transcripts')
    parser.add_argument('--no-translate', action='store_true', help='Skip translation')

    args = parser.parse_args()

    fetcher = ConferenceFetcher(use_proxy=True)

    # Set extractor based on URL
    if 'io.google' in args.url:
        fetcher.set_extractor(GoogleIOExtractor())

    print(f"Fetching {args.url}...")
    conf = fetcher.fetch_conference(
        args.url,
        args.name,
        args.year,
        fetch_transcripts=args.transcripts,
        max_transcripts=args.max_transcripts
    )

    print(f"Found {len(conf['sessions'])} sessions")

    # Count session transcripts
    session_transcripts = sum(1 for s in conf['sessions'] if s.transcript)
    print(f"Session transcripts: {session_transcripts}")

    # Fetch YouTube playlist transcripts and search for important sessions only
    if args.playlist_transcripts:
        print("Fetching YouTube playlist transcripts...")
        # Only search for top sessions (first 10 important ones, excluding keynotes)
        top_sessions = conf['sessions'][:20]
        important_sessions = [s for s in top_sessions if 'keynote' not in s.title.lower()][:10]
        conf['playlist_transcripts'] = fetcher.get_youtube_playlist_transcripts(sessions=important_sessions)

    # Format
    md = fetcher.format_as_markdown(conf, translate=not args.no_translate)

    # Save
    output_dir = Path(STORAGE_BASE) / 'conference' / args.name / (args.year or datetime.now().strftime('%Y'))
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / 'index.md'
    output_file.write_text(md, encoding='utf-8')
    print(f"Saved to {output_file}")


if __name__ == '__main__':
    main()
