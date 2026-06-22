# AI Fetch Conference Skill

## Description
Fetch conference agenda, speaker information, and presentation content. Covers WAIC, NeurIPS, CVPR, and other AI conferences.

## Usage
```
/ai-fetch-conference              # Fetch all conferences
/ai-fetch-conference --waic    # Fetch WAIC
/ai-fetch-conference --neurips # Fetch NeurIPS
```

## Supported Conferences
| Conference | URL | Content |
|-----------|-----|---------|
| WAIC | worldaic.com.cn | World AI Conference |
| NeurIPS | nips.cc | ML conference |
| ICML | icml.cc | ML conference |
| CVPR | cvpr.thecvf.com | Computer vision |
| ICLR | iclr.cc | Deep learning |

## Output
Files saved to: `ai-content-fetched/conference/{name}/{year}/{slug}.md`
- Conference overview
- Agenda by day/track
- Speaker information
- Presentation content (when available)

## Technical
1. **Phase 1**: Scrape official website for agenda/summaries
2. **Phase 2**: Download videos when released, transcribe with Whisper
3. **Phase 3**: Search speaker articles and news reports
4. **Phase 4**: Cross-reference multiple sources
