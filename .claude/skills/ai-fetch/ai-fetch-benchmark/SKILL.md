# AI Fetch Benchmark Skill

## Description
Fetch AI benchmark rankings and evaluation results. Covers LMSYS Arena, OpenCompass, SWE-bench, and other AI benchmarks.

## Usage
```
/ai-fetch-benchmark              # Fetch all benchmarks
/ai-fetch-benchmark --arena    # Fetch LMSYS Arena
/ai-fetch-benchmark --swebench # Fetch SWE-bench
```

## Supported Benchmarks
| Benchmark | URL | Content |
|-----------|-----|---------|
| LMSYS Arena | arena.ai | Chatbot ELO rankings |
| OpenCompass | opencompass.org.cn | Chinese model benchmarks |
| SWE-bench | swebench.com | Code repair benchmarks |
| LiveCodeBench | livecodebench.github.io | Real-time code评测 |
| Artificial Analysis | artificialanalysis.ai | Independent rankings |
| HF Open LLM | huggingface.co/spaces/open-llm-leaderboard | Open source LLM rankings |

## Output
Files saved to: `ai-content-fetched/benchmark/{name}/{date}.md`
- Full ranking tables
- Model scores and metrics
- Historical data when available

## Technical
- Table parsing from HTML
- JSON/API for some benchmarks
- Regular updates tracked by date
