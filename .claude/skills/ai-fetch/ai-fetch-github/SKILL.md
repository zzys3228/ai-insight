# AI Fetch GitHub Skill

## Description
Fetch GitHub repository information including README, releases, and repository metadata. Covers Company open-source projects and OpenSource community projects.

## Usage
```
/ai-fetch-github           # Fetch all GitHub repos
/ai-fetch-github --list   # List all configured GitHub repos
/ai-fetch-github --repo owner/repo  # Fetch specific repo
/ai-fetch-github --force # Force re-fetch even if cached
```

## Supported Repos
| Type | Examples | Content |
|------|----------|---------|
| Company Open Source | NVIDIA/TensorRT-LLM, pytorch/pytorch | Releases + README |
| Community Frameworks | vllm-project/vllm, ollama/ollama | Releases + README |
| Independent Models | THUDM/ChatGLM, deepseek-ai/DeepSeek-V3 | Releases + README |

## Output
Files saved to: `ai-content-fetched/github/{owner}_{repo}/`
- README.md - Repository README (translated to Chinese)
- releases.md - Recent releases (last 6 months)
- repo_info.md - Repository metadata

## Technical
- Uses GitHub API (60 req/hr without token)
- Rate limiting: 1.5s between requests
- Falls back to web scraping if API fails
