# AI Fetch Academic Skill

## Description
Fetch academic papers from arXiv, HuggingFace Papers, and other academic sources. Downloads PDF, parses content, and translates to Chinese.

## Usage
```
/ai-fetch-academic          # Fetch recent papers
/ai-fetch-academic --arxiv # Fetch from arXiv
/ai-fetch-academic --hf    # Fetch from HuggingFace Papers
/ai-fetch-academic --paper_id 2606.20527  # Fetch specific paper
```

## Supported Sources
| Source | URL Pattern | Content |
|--------|-------------|---------|
| arXiv | arxiv.org/abs/* | Paper PDF + Abstract |
| HuggingFace | huggingface.co/papers | Paper listings |
| Papers With Code | paperswithcode.com | Paper + Code |

## Output
Files saved to: `ai-content-fetched/academic/{source}/{category}/{paper_id}.md`
- PDF downloaded and parsed
- Full paper content translated to Chinese
- Frontmatter with paper metadata

## Technical
1. Parse paper_id from URL
2. Download PDF: `https://arxiv.org/pdf/{paper_id}.pdf`
3. Parse with PyMuPDF
4. Translate with MiniMax API
5. Save as markdown
