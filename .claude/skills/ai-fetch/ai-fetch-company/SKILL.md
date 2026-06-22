# AI Fetch Company Skill

## Description
Fetch company blog posts, product pages, and developer documentation. Covers NVIDIA, Google, Microsoft, OpenAI, Anthropic, Alibaba, Baidu, Tencent, ByteDance and other AI companies.

## Usage
```
/ai-fetch-company           # Fetch all company blogs
/ai-fetch-company --nvidia # Fetch specific company
/ai-fetch-company --list   # List configured companies
```

## Supported Companies
| Company | URL Pattern | Content |
|---------|------------|---------|
| NVIDIA | blogs.nvidia.com | Blog posts |
| OpenAI | openai.com/blog | Blog posts (needs proxy) |
| Anthropic | anthropic.com/news | News and research |
| Google | blog.google, deepmind.google | AI Blog posts |
| Microsoft | azure.microsoft.com/blog | Azure AI Blog |
| Alibaba | qwenlm.github.io, yq.aliyun.com | Qwen blogs |
| Baidu | yiyan.baidu.com, research.baidu.com | ERNIE, research |
| Tencent | cloud.tencent.com | Hunyuan, cloud AI |
| ByteDance | volcengine.com, seed.bytedance.com | Doubao, Seed |

## Output
Files saved to: `ai-content-fetched/company/{company}/blogs/{article_slug}.md`
- Complete blog post content
- Translated to Chinese
- Original links preserved

## Technical
- HTML scraping with BeautifulSoup
- JS rendering with Playwright for dynamic pages
- Translation via MiniMax API
