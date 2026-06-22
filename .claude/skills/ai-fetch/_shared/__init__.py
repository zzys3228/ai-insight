"""
AI Content Fetch - Shared Modules

This package contains shared utilities and configuration
used by all fetch skills.
"""

from .config import (
    should_use_proxy,
    get_storage_path,
    PROXY,
    CN_DOMAINS,
    STORAGE_BASE,
    MINIMAX_API_KEY,
    MINIMAX_API_URL,
    MINIMAX_MODEL,
    MINIMAX_MAX_TOKENS,
    BROWSER_HEADERS,
    REQUEST_TIMEOUT,
    MAX_RETRIES,
    MAX_CONCURRENT,
    REQUEST_DELAY,
)

from .translate import Translator, get_translator
from .utils import (
    get_url_hash,
    slugify,
    extract_domain,
    extract_filename_from_url,
    get_file_timestamp,
    read_json,
    write_json,
    format_markdown_frontmatter,
    parse_github_url,
    parse_arxiv_id,
    get_arxiv_pdf_url,
    clean_html_tags,
    truncate_text,
)
from .task_queue import TaskQueue, SyncTaskQueue, TaskResult

__all__ = [
    # config
    'should_use_proxy',
    'get_storage_path',
    'PROXY',
    'CN_DOMAINS',
    'STORAGE_BASE',
    'MINIMAX_API_KEY',
    'MINIMAX_API_URL',
    'MINIMAX_MODEL',
    'MINIMAX_MAX_TOKENS',
    'BROWSER_HEADERS',
    'REQUEST_TIMEOUT',
    'MAX_RETRIES',
    'MAX_CONCURRENT',
    'REQUEST_DELAY',
    # translate
    'Translator',
    'get_translator',
    # utils
    'get_url_hash',
    'slugify',
    'extract_domain',
    'extract_filename_from_url',
    'get_file_timestamp',
    'read_json',
    'write_json',
    'format_markdown_frontmatter',
    'parse_github_url',
    'parse_arxiv_id',
    'get_arxiv_pdf_url',
    'clean_html_tags',
    'truncate_text',
    # task_queue
    'TaskQueue',
    'SyncTaskQueue',
    'TaskResult',
]
