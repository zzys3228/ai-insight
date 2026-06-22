# AI Fetch Media Skill

## Description
Fetch AI newsletters, podcasts, and tech media content. Covers Import AI, The Batch, Lex Fridman, Dwarkesh, and other AI media sources.

## Usage
```
/ai-fetch-media              # Fetch all media content
/ai-fetch-media --newsletter # Fetch newsletters only
/ai-fetch-media --podcast  # Fetch podcasts only
```

## Supported Sources

### Newsletter
| Source | URL | Content |
|--------|-----|---------|
| Import AI | importai.substack.com | AI news and analysis |
| The Batch | deeplearning.ai/the-batch | Andrew Ng weekly |
| Ben's Bites | bensbites.co | AI product updates |
| TLDR AI | tldr.tech/ai | AI daily news |

### Podcast
| Source | URL | Content |
|--------|-----|---------|
| Lex Fridman | lexfridman.com | AI interviews |
| Dwarkesh | dwarkesh.com | AI deep dives |
| Latent Space | latent.space | AI engineering |
| No Priors | nopriors.com | AI investing |

## Output
- Newsletter: `ai-content-fetched/media/newsletter/{publisher}/{slug}.md`
- Podcast: `ai-content-fetched/media/podcast/{name}/{slug}.md`
  - Full transcript translated to Chinese
  - Audio downloaded separately

## Technical
- Newsletter: HTML scraping + RSS
- Podcast: RSS + audio download + Whisper transcription
