"""
Configuration module for AI Content Fetch
"""

# Proxy configuration
PROXY = "http://127.0.0.1:26001"

# Domestic domains that should be accessed directly (no proxy)
CN_DOMAINS = [
    '.cn',
    'aliyun.com', 'baidu.com', 'tencent.com', 'tencent.com',
    'volcengine.com', 'huaweicloud.com', 'jd.com', 'bytedance.com',
    'xiaomi.com', 'meituan.com', 'weibo.com', 'zhihu.com',
    'bilibili.com', 'taobao.com', 'qq.com', 'sina.com',
    '163.com', 'alipay.com', 'taobao.com', 'jd.com',
    'alibaba.com', '1688.com', 'dingtalk.com', 'xianyu.com',
    'autohome.com.cn', 'lizhi.fm', 'itheima.com',
    'qunar.com', 'mogujie.com', 'vip.com', 'meituan.com',
    'dianping.com', 'ele.me', ' damai.cn', 'taopiaopiao.com',
    # MiniMax related - 直连不需代理
    'minimaxi.com', 'minimax.io', 'minimaxi.cn',
    'kxai.com', 'ailab.com',
]

# Storage paths
STORAGE_BASE = "ai-content-fetched"
STORAGE_STRUCTURE = {
    'github': 'github/{owner}_{repo}/',
    'company': 'company/{company}/blogs/',
    'academic': 'academic/{source}/{category}/',
    'newsletter': 'media/newsletter/{publisher}/',
    'podcast': 'media/podcast/{name}/',
    'benchmark': 'benchmark/{name}/',
    'robot': 'robot/{company}/',
    'standard': 'standard/{protocol}/',
    'person': 'person/{name}/',
    'conference': 'conference/{name}/{year}/',
    'industry': 'industry/{type}/',
}

# MiniMax API configuration
MINIMAX_API_KEY = "REDACTED_API_KEY"
MINIMAX_API_URL = "https://api.minimaxi.com/anthropic/v1/messages"
MINIMAX_MODEL = "MiniMax-M2.7"
MINIMAX_MAX_TOKENS = 4096

# Browser headers
BROWSER_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
}

# Request settings
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3
RETRY_DELAY = 5

# Concurrency settings
MAX_CONCURRENT = 5
REQUEST_DELAY = 1.0  # seconds between requests

# File settings
URL_INDEX_FILE = f"{STORAGE_BASE}/_url_index.json"
FAILED_URLS_FILE = f"{STORAGE_BASE}/_failed_urls.json"
METADATA_FILE = f"{STORAGE_BASE}/_metadata.json"


def should_use_proxy(url: str) -> bool:
    """
    Determine if proxy should be used for the given URL.

    Args:
        url: URL to check

    Returns:
        True if proxy should be used, False for direct access
    """
    url_lower = url.lower()

    # Check if it's a domestic domain
    for domain in CN_DOMAINS:
        if domain in url_lower:
            return False

    # Default to proxy for overseas domains
    return True


def get_storage_path(category: str, **kwargs) -> str:
    """
    Generate storage path for a given category.

    Args:
        category: Content category (github, company, academic, etc.)
        **kwargs: Category-specific parameters

    Returns:
        Storage path relative to STORAGE_BASE
    """
    if category not in STORAGE_STRUCTURE:
        return f"{category}/"

    template = STORAGE_STRUCTURE[category]

    try:
        return template.format(**kwargs)
    except KeyError:
        return f"{category}/"
