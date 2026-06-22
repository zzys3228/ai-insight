# AI Fetch Conference Skill

## Description
Fetches conference agenda, speaker information, and presentation content. Supports both traditional websites and modern SPA (Single Page Applications) like Google I/O.

## Architecture
- **Generic extractors**: Work for most conference sites (HTML parsing, meta tags)
- **Site-specific extractors**: Registered for special handling (e.g., Google I/O SPA)
- **Extractor registry**: Allows adding custom extractors per-conference

## Usage
```bash
# Basic fetch
python fetch_conference.py --url <url> --name <name> --year <year>

# With subpage discovery (recommended for SPA sites)
python fetch_conference.py --url <url> --name <name> --year <year> --subpages --max-subpages 5

# Via ai-fetch-daily
python fetch_daily.py --conference
```

## CLI Arguments
| Argument | Description |
|----------|-------------|
| `--url` | Conference URL (required) |
| `--name` | Conference name (required) |
| `--year` | Conference year (optional, defaults to current year) |
| `--subpages` | Discover and fetch sub-pages (keynotes, sessions) |
| `--max-subpages` | Max sub-pages to fetch (default: 10) |
| `--discover` | Only discover agenda links without fetching |

## Supported Conferences
| Conference | URL | Type | Features |
|-----------|-----|------|----------|
| WAIC | worldaic.com.cn | Traditional | Full HTML extraction |
| Google I/O | io.google | SPA | Sessions JSON, keynotes, topics |
| NVIDIA GTC | nvidia.com/gtc | Traditional | Full HTML extraction |
| NeurIPS | nips.cc | Traditional | Full HTML extraction |
| ICML | icml.cc | Traditional | Full HTML extraction |

## Output
Files saved to: `ai-content-fetched/conference/{name}/{year}/index.md`

Content includes:
- Conference overview and title
- Agenda/sessions with descriptions
- Speaker information (when available)
- Topic categories
- Navigation structure (for SPA sites)

## Adding Site-Specific Extractors
Extend `ConferenceFetcher` with custom extractors:

```python
fetcher = ConferenceFetcher(use_proxy=True)
fetcher.add_extractor(priority=100, name="my_conference", extractor=my_extractor)
conf = fetcher.fetch_with_subpages(url, name, year)
```

Extractor function signature:
```python
def my_extractor(html: str, soup: BeautifulSoup, url: str) -> Optional[str]:
    # Return extracted content or None if not applicable
    if 'my-conference.com' not in url:
        return None
    # Extract and return content
    return extracted_content
```

## Technical Details
1. **Phase 1**: Extract content using registered extractors (priority-ordered)
2. **Phase 2**: Discover sub-pages (keynotes, sessions, speakers)
3. **Phase 3**: Fetch discovered sub-pages
4. **Phase 4**: Translate content (if enabled in config)