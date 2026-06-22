# AI Fetch Person Skill

## Description
Fetch AI researcher and influencer content including blog posts, articles, and social media. Covers Sam Altman, Yann LeCun, Andrej Karpathy, and other AI personalities.

## Usage
```
/ai-fetch-person              # Fetch all person content
/ai-fetch-person --karpathy # Fetch specific person
```

## Supported People
| Person | URL | Content |
|--------|-----|---------|
| Andrej Karpathy | karpathy.ai | Blog posts, education |
| Lilian Weng | lilianweng.github.io | Deep technical posts |
| Simon Willison | simonwillison.net | Model reviews |
| Chip Huyen | huyenchip.com | ML systems |
| Yann LeCun | x.com/ylecun | Twitter/X posts |
| Sam Altman | x.com/sama | Twitter/X posts |

## Output
Files saved to: `ai-content-fetched/person/{name}/{article_slug}.md`
- Index file for person overview
- Each blog post as separate markdown file
- Translated to Chinese

## Technical
- Blog scraping for personal websites
- Nitter mirrors for Twitter/X (no API needed)
- Proxy for restricted sites
