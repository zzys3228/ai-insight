# AI Fetch Conference Skill

## Description
Fetches conference agenda, session descriptions, and full transcripts. Supports both traditional websites and modern SPA (Single Page Applications) like Google I/O.

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   ConferenceFetcher                      │
├─────────────────────────────────────────────────────────┤
│  Extractors           │  Transcript Sources             │
│  ─────────────        │  ─────────────────            │
│  GoogleIOExtractor    │  BlogArticleSource (优先)     │
│  GenericExtractor     │  PageTranscriptSource          │
│  [可扩展]             │  YouTubeTranscriptSource       │
└─────────────────────────────────────────────────────────┘
```

## Features
- **Session 列表**: 提取所有 session 标题和描述
- **完整文字稿**: 从 blog/页面/YouTube 获取完整 transcript
- **Playwright 支持**: SPA 页面 JavaScript 渲染
- **通用可扩展**: 支持添加新的 extractor 和 transcript source

## Usage

### 基本用法
```bash
# 抓取 session 列表
python fetch_conference.py --url <url> --name <name> --year <year>

# 使用 Playwright (SPA 网站)
python fetch_conference.py --url https://io.google --name google-io --year 2026 --playwright

# 获取完整文字稿 (transcripts)
python fetch_conference.py --url https://io.google --name google-io --year 2026 --playwright --transcripts --max-transcripts 5
```

### 参数说明
| 参数 | 说明 |
|------|------|
| `--url` | 大会 URL |
| `--name` | 大会名称 |
| `--year` | 年份 (默认当前年) |
| `--playwright` | 使用浏览器渲染 SPA |
| `--wait` | Playwright 等待秒数 |
| `--transcripts` | 获取完整文字稿 |
| `--max-transcripts` | 最大文字稿数量 |
| `--no-translate` | 跳过翻译 |

## Transcript 来源 (优先级顺序)

1. **Blog Article**: 从官方博客获取完整文章 (keynote)
2. **Page Transcript**: 从 session 页面提取嵌入文字稿
3. **YouTube Caption**: 从 YouTube 字幕获取

## 添加新的 Transcript Source

```python
from fetch_conference import TranscriptSource, ConferenceFetcher

class MyTranscriptSource(TranscriptSource):
    def fetch(self, session_url: str, session_id: str) -> Optional[str]:
        # 实现获取文字稿的逻辑
        return transcript

fetcher = ConferenceFetcher()
fetcher.transcript_sources.append(MyTranscriptSource())
```

## 添加新的 Conference Extractor

```python
from fetch_conference import ConferenceExtractor, Session

class MyConferenceExtractor(ConferenceExtractor):
    def extract_sessions(self, html: str, url: str) -> List[Session]:
        sessions = []
        # 解析 HTML 提取 sessions
        return sessions

fetcher = ConferenceFetcher()
fetcher.set_extractor(MyConferenceExtractor())
```

## 支持的大会

| 大会 | URL | 类型 | Transcript |
|------|-----|------|-----------|
| Google I/O | io.google | SPA | ✅ blog.google |
| NVIDIA GTC | nvidia.com/gtc | Traditional | ⏳ 待实现 |
| NeurIPS | nips.cc | Traditional | ⏳ 待实现 |

## 输出格式

```markdown
---
title: google-io
source: io.google
category: conference/google-io/2026
---

# google-io 2026

## Sessions (83个)

### 1. Google keynote
描述摘要...

---

#### 完整文字稿

I/O 2026: Welcome to the agentic Gemini era...

Editor's note: Below is an edited transcript...

It's been an extraordinary year...
```
