"""
Utility functions for AI Content Fetch
"""

import re
import hashlib
import json
from pathlib import Path
from datetime import datetime
from typing import Optional, Tuple
from urllib.parse import urlparse, quote


def get_url_hash(url: str) -> str:
    """
    Generate a short hash for URL to use as filename.

    Args:
        url: URL to hash

    Returns:
        12-character hash
    """
    return hashlib.md5(url.encode()).hexdigest()[:12]


def slugify(text: str, max_length: int = 50) -> str:
    """
    Convert text to a URL-safe slug.

    Args:
        text: Text to slugify
        max_length: Maximum length of slug

    Returns:
        URL-safe slug
    """
    # Remove special characters, keep Chinese and alphanumeric
    slug = re.sub(r'[^\w\s-]', '', text)
    # Replace spaces with hyphens
    slug = re.sub(r'[\s]+', '-', slug)
    # Remove consecutive hyphens
    slug = re.sub(r'-+', '-', slug)
    # Truncate
    slug = slug[:max_length].strip('-')
    return slug


def extract_domain(url: str) -> str:
    """
    Extract domain from URL.

    Args:
        url: URL to extract from

    Returns:
        Domain name
    """
    parsed = urlparse(url)
    domain = parsed.netloc
    # Remove www. prefix
    if domain.startswith('www.'):
        domain = domain[4:]
    return domain


def extract_filename_from_url(url: str) -> str:
    """
    Extract a filename-safe string from URL path.

    Args:
        url: URL to extract from

    Returns:
        Filename-safe string
    """
    parsed = urlparse(url)
    path = parsed.path.strip('/')

    if not path:
        return slugify(parsed.netloc)

    # Get last part of path
    parts = path.split('/')
    filename = parts[-1]

    # Remove extension
    if '.' in filename:
        filename = filename.rsplit('.', 1)[0]

    if not filename:
        filename = parts[-2] if len(parts) > 1 else slugify(parsed.netloc)

    return slugify(filename, max_length=60)


def get_file_timestamp() -> str:
    """
    Get current timestamp for file metadata.

    Returns:
        ISO format timestamp
    """
    return datetime.now().isoformat()


def read_json(filepath: str) -> dict:
    """
    Read JSON file.

    Args:
        filepath: Path to JSON file

    Returns:
        Dictionary or empty dict if file doesn't exist
    """
    path = Path(filepath)
    if not path.exists():
        return {}

    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}


def write_json(filepath: str, data: dict):
    """
    Write dictionary to JSON file.

    Args:
        filepath: Path to JSON file
        data: Dictionary to write
    """
    path = Path(filepath)
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def format_markdown_frontmatter(
    title: str,
    source: str,
    url: str,
    date: str,
    category: str,
    translated: bool = True,
    fetched_at: Optional[str] = None,
    **kwargs
) -> str:
    """
    Format markdown file with frontmatter.

    Args:
        title: Page title
        source: Source domain
        url: Original URL
        date: Publication date
        category: Content category
        translated: Whether content is translated
        fetched_at: Fetch timestamp
        **kwargs: Additional frontmatter fields

    Returns:
        Formatted markdown string
    """
    if fetched_at is None:
        fetched_at = get_file_timestamp()

    frontmatter = f"""---
title: {title}
source: {source}
url: {url}
date: {date}
category: {category}
translated: {'true' if translated else 'false'}
fetched_at: {fetched_at}
"""
    # Add additional fields
    for key, value in kwargs.items():
        if value is not None:
            frontmatter += f"{key}: {value}\n"

    frontmatter += "---\n"

    return frontmatter


def parse_github_url(url: str) -> Tuple[str, str]:
    """
    Parse GitHub URL to extract owner and repo.

    Args:
        url: GitHub URL

    Returns:
        Tuple of (owner, repo)
    """
    # Handle various GitHub URL formats
    patterns = [
        r'github\.com[/:]([^/]+)/([^/.]+)',
        r'github\.com[/:]([^/]+)/([^/]+)/tree/[^/]+/([^/]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            groups = match.groups()
            if len(groups) == 2:
                return groups
            elif len(groups) == 3:
                return (groups[0], groups[2])

    raise ValueError(f"Invalid GitHub URL: {url}")


def parse_arxiv_id(url: str) -> Optional[str]:
    """
    Extract arXiv paper ID from URL.

    Args:
        url: arXiv URL

    Returns:
        arXiv paper ID or None
    """
    # Patterns for arXiv URLs
    patterns = [
        r'arxiv\.org/abs/([0-9]+\.[0-9]+)',
        r'arxiv\.org/pdf/([0-9]+\.[0-9]+)',
        r'arxiv\.org/abs/([0-9]+\.[0-9]+v[0-9]+)',
    ]

    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)

    return None


def get_arxiv_pdf_url(paper_id: str) -> str:
    """
    Get PDF URL from arXiv paper ID.

    Args:
        paper_id: arXiv paper ID

    Returns:
        PDF URL
    """
    return f"https://arxiv.org/pdf/{paper_id}.pdf"


def clean_html_tags(html: str) -> str:
    """
    Remove HTML tags from text.

    Args:
        html: HTML string

    Returns:
        Plain text
    """
    # Remove script and style elements
    html = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r'<style[^>]*>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
    # Remove HTML tags
    html = re.sub(r'<[^>]+>', '', html)
    # Decode HTML entities
    html = html.replace('&nbsp;', ' ')
    html = html.replace('&amp;', '&')
    html = html.replace('&lt;', '<')
    html = html.replace('&gt;', '>')
    html = html.replace('&quot;', '"')
    html = html.replace('&#39;', "'")
    # Normalize whitespace
    html = re.sub(r'\s+', ' ', html).strip()

    return html


def truncate_text(text: str, max_length: int = 2000, suffix: str = '...') -> str:
    """
    Truncate text to maximum length.

    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated

    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text

    return text[:max_length - len(suffix)].rstrip() + suffix
