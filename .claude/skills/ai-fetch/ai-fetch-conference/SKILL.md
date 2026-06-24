# AI Fetch Conference Skill

## Description
抓取大会议程、议题描述和完整文字稿(transcript)。支持传统网站和现代SPA应用(如Google I/O)。**内置中文翻译**。

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   ConferenceFetcher                      │
├─────────────────────────────────────────────────────────┤
│  Extractors           │  Transcript Sources             │
│  ─────────────       │  ─────────────────            │
│  GoogleIOExtractor   │  BlogArticleSource (优先)     │
│  GenericExtractor    │  PageTranscriptSource          │
│  [可扩展]            │  YouTubeCaptionSource         │
├─────────────────────────────────────────────────────────┤
│  Translator (MiniMax API) - 自动翻译为中文              │
└─────────────────────────────────────────────────────────┘
```

## Features
- **Session 列表**: 提取所有 session 标题、描述、时间、演讲者、分类
- **完整文字稿**: 从 blog/页面/YouTube 获取完整 transcript
- **中文翻译**: 使用 MiniMax API 自动翻译标题、描述、文字稿
- **Playwright 支持**: SPA 页面 JavaScript 渲染
- **通用可扩展**: 支持添加新的 extractor 和 transcript source

## Usage

### 基本用法
```bash
# 抓取 session 列表 (默认翻译为中文)
python fetch_conference.py --url <url> --name <name> --year <year>

# 使用 Playwright (SPA 网站)
python fetch_conference.py --url https://io.google --name google-io --year 2026 --playwright

# 获取完整文字稿 (transcripts)
python fetch_conference.py --url https://io.google --name google-io --year 2026 --playwright --transcripts --max-transcripts 50

# 跳过翻译
python fetch_conference.py --url <url> --name <name> --year <year> --no-translate
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
| `--playlist-transcripts` | 获取 YouTube 播放列表文字稿 |
| `--no-translate` | 跳过翻译(保留英文原文) |

## 输出文件结构

```
conference/{name}/{year}/
├── index.md              # 大会整体议程
├── sessions/            # 每个议题一个md
│   ├── 01-xxx.md
│   ├── 02-xxx.md
│   └── ...
└── transcripts/         # 原始字幕文件
    ├── xxx.txt
    └── ...
```

## index.md 格式要求

### 必须包含的内容

1. **大会基础信息**
   - 举办地点
   - 举办日期
   - 时区说明（PT太平洋时间+北京时间换算）
   - 核心主题

2. **分时段议程表**（按时间顺序）
   - Day1 主会场 Keynote（含时间、主讲人、核心主题、细分议题内容）
   - Day1 下午并行分会场
   - Day2 深度技术分会场

3. **关键发布落地时间线**
   - 产品/技术名称
   - 发布状态
   - 上线时间

4. **全部议题索引**
   - 表格形式：编号、议题链接、日期、时间、分类、演讲者

5. **主要议题完整文字稿索引**

### index.md 模板

```markdown
# {大会名称} {年份} 完整分时段议程总表

## 大会基础信息

- **举办地点**: xxx
- **举办日期**: xxxx-xx-xx (Day1)、xxxx-xx-xx (Day2)
- **时区**: PT 太平洋时间；北京时间 = PT+15 小时
- **核心主题**: xxx

---

## 一、Day1 主会场 Keynote

| 场次 | PT时间 | 北京时间 | 主讲人 | 细分议题内容 |
| --- | --- | --- | --- | --- |
| xxx | 10:00–11:00 | 01:00–02:00 | 主讲人名 | 1. xxx<br>2. xxx<br>3. xxx |

---

## 二、Day1 下午并行分会场

| 分会场 | PT时间 | 主讲 | 核心议题 |
| --- | --- | --- | --- |
| xxx | 15:30–16:15 | 负责人 | 核心议题描述 |

---

## 三、Day2 深度技术分会场

| 场次主题 | PT时间 | 主讲人 | 详细内容 |
| --- | --- | --- | --- |
| xxx | 10:00–10:45 | 主讲人 | 详细内容描述 |

---

## 四、关键发布落地时间线

| 产品/技术 | 发布状态 | 上线时间 |
| --- | --- | --- |
| xxx | 正式GA/内测/预览 | 2026年x月 |

---

## 五、全部XX个议题索引

详见 `sessions/` 目录

| # | 议题 | 日期 | 时间 | 分类 | 演讲者 |
|---| --- | --- | --- | --- | --- |
| 1 | [议题名称](sessions/01-xxx.md) | xx-xx | xx:xx | 分类 | 演讲者 |

---

## 六、主要议题完整文字稿

XX个议题已获取完整字幕（YouTube自动字幕）

| 议题 | 文字稿 |
| --- | --- |
| [议题名](sessions/01-xxx.md) | xxK字符 |
```

## sessions/{编号}-{uid}.md 格式要求

每个议题文件必须包含：

```markdown
---
title: {原标题}
title_zh: {中文标题}
category: conference/{name}/{year}/sessions
date: {日期 YYYY-MM-DD}
time: {时间 HH:MM - HH:MM PT}
track: {分类}
type: {类型：技术演讲/工作坊/编程实验室/主题演讲}
level: {等级：Beginner/Intermediate}
speakers: {演讲者列表}
video: {YouTube链接}
---

# {中文标题}

## 📋 摘要

**📅 日期**: {日期} | **🕐 时间**: {时间 PT} | **📂 分类**: {分类} | **🎯 类型**: {类型} | **📊 等级**: {等级}

**👤 演讲者**: {演讲者}

{中文描述摘要}

---

## 📝 详细原文

### {原标题}

{英文原描述}

---

## 📝 完整文字稿

{YouTube字幕内容}
```

## Session 数据结构

Session 对象必须包含以下字段：

| 字段 | 说明 | 示例 |
|------|------|------|
| `id` | 会话ID | "1" |
| `uid` | URL友好ID | "google-keynote-1" |
| `title` | 原标题 | "Google keynote" |
| `title_zh` | 中文标题 | "Google 主题演讲" |
| `short_description` | 短描述 | "" |
| `long_description` | 长描述 | "Discover how we're..." |
| `description_zh` | 中文描述 | "了解我们如何..." |
| `session_date` | 日期 | "2026-05-19" |
| `start_time` | 开始时间 | "10:00:00" |
| `end_time` | 结束时间 | "11:45:00" |
| `track` | 分类 | "AI/机器学习" |
| `content_type` | 类型 | "Google主题演讲" |
| `level` | 等级 | "Beginner" |
| `speakers` | 演讲者列表 | ["sundar", "demis"] |
| `video_url` | YouTube链接 | "https://..." |
| `transcript` | 完整字幕 | "Kind: captions..." |

## Transcript 获取

### 来源优先级
1. **Blog Article**: 从官方博客获取完整文章 (keynote)
2. **Page Transcript**: 从 session 页面提取嵌入文字稿
3. **YouTube Caption**: 从 YouTube 字幕获取 (使用 yt-dlp)

### YouTube 字幕获取
```bash
# 使用 yt-dlp 获取自动字幕
yt-dlp --write-auto-subs --sub-langs en --skip-download -o caption https://www.youtube.com/watch?v=xxx
```

### 字幕清理
YouTube 自动字幕可能有重复，需要清理：
- 去除重复句子
- 限制每条字幕长度

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
        # 必须提取: id, uid, title, date, time, track, type, level, speakers, video_url
        return sessions

fetcher = ConferenceFetcher()
fetcher.set_extractor(MyConferenceExtractor())
```

## 支持的大会

| 大会 | URL | 类型 | 格式 |
|------|-----|------|------|
| Google I/O | io.google | SPA | ✅ 参考本skill完整实现 |
| NVIDIA GTC | nvidia.com/gtc | Traditional | ⏳ 待实现 |
| NeurIPS | nips.cc | Traditional | ⏳ 待实现 |

## Troubleshooting & Tips

### YouTube Cookie 配置

获取 YouTube 字幕需要认证 cookie（某些视频需要登录）：

**cookies.txt 格式要求**：
```
# Netscape HTTP Cookie File
.youtube.com	TRUE	/	FALSE	0	COOKIE_NAME	COOKIE_VALUE
```

**关键注意事项**：
1. 必须添加 `# Netscape HTTP Cookie File` 头行（yt-dlp 要求）
2. 域名格式为 `.youtube.com`（单点，非 `..youtube.com`）
3. 从浏览器导出时可使用 "Get cookies.txt" 扩展

**Playwright 自动获取 cookie**（可选）：
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://www.youtube.com')
    # 手动登录后
    context.cookies()  # 获取 cookies
```

### MiniMax API 翻译

**API 配置**（config.py）：
```python
MINIMAX_API_URL = "https://api.minimaxi.com/anthropic/v1/messages"
MINIMAX_MODEL = "MiniMax-M2.7"
MINIMAX_API_KEY = "your-api-key"
```

**API 调用方式**：
- Header: `Authorization: Bearer {api_key}`
- Content-Type: `application/json`
- 格式兼容 Anthropic API 格式

**翻译分块**：
- 单次最大 1500 字符
- 长文本自动分块翻译
- 分块间隔 0.2 秒（避免 rate limit）

### 文件格式检查

**正确的 frontmatter 格式**：
```yaml
---
title: Original Title
title_zh: 中文标题
category: conference/google-io/2026/sessions
date: 2026-05-19
time: 10:00 - 11:45 PT
track: AI/机器学习
type: 技术演讲
level: Beginner
speakers: speaker1, speaker2
video: https://www.youtube.com/watch?v=xxx
---
```

**常见错误**：
1. ❌ 翻译输出泄露到 frontmatter（检查是否有多余文本）
2. ❌ 缺少 `title_zh` 字段
3. ❌ `---` 分隔符不完整

### 内容总结生成

每个 session 文件应包含 AI 生成的结构化总结：

**总结结构建议**：
1. 核心主题概述
2. 关键要点（带数据/数字）
3. 技术细节摘要
4. 发布时间/状态信息

**示例**：
```markdown
## 📝 内容总结

**《演讲主题》核心要点**

一、整体背景
- 数据：xxx增长xxx%

二、技术发布
- 产品A：xxx功能
- 产品B：xxx时间上线

三、落地案例
- 案例A：xxx应用场景
```

### 常见问题解决

| 问题 | 解决方案 |
|------|----------|
| YouTube 字幕获取失败 | 检查 cookies.txt 格式、添加 Netscape 头行 |
| 翻译 API 报错 | 检查 API key 是否有效、确认 endpoint 正确 |
| 字幕内容截断 | 检查 fetch_conference.py 是否有 truncation limit |
| Frontmatter 损坏 | 重新生成文件，确保翻译输出不入侵 frontmatter |

## 翻译说明

- 标题、描述、文字稿自动翻译为中文
- 使用 `--no-translate` 保留英文原文
- 翻译调用 MiniMax API (MiniMax-M2 模型)
- 文字稿超过 1500 字符自动分块翻译
- 翻译prompt: "翻译成中文，只返回翻译结果，不要解释"

## 质量检查标准（大会特定）

### sessions/*.md 质量要求

| 检查项 | 要求 | 当前问题 |
|--------|------|---------|
| Frontmatter | 必含 source/url/translated/fetched_at | ⚠️ 缺少 source/translated/fetched_at |
| 摘要重复 | 只保留一个概述章节 | ⚠️ "摘要"+"详细原文"重复 |
| 文字稿处理 | 提炼为结构化要点，不保留原始转录 | ⚠️ 原始转录稿过长未整理 |
| 英文原文 | 不保留完整英文 | ⚠️ 末尾保留完整英文字幕 |
| 表格化 | 关键发布/技术参数用表格 | ⚠️ 缺少表格化呈现 |
| 原文链接 | 文末必须有原文链接 | ⚠️ 缺少原文链接 |

### transcripts 目录要求

| 文件类型 | 处理方式 |
|---------|---------|
| .vtt 原始字幕 | ⚠️ 质量差，建议删除或单独存储 |
| .txt 转录文本 | ⚠️ 需清洗重复后才能使用 |

**字幕清洗要求**：
- 去除时间戳和重复句子
- 合并为连贯文本
- 翻译后再保存到 sessions/*.md

### 内容总结质量要求

#### 关键信息类型

阅读完整文字稿时，提取以下通用类型：

| 信息类型 | 说明 |
|---------|------|
| 产品发布/技术更新 | 新产品、新功能、版本更新 |
| 数据/数字 | 具体数值、增长比例、规模 |
| 核心观点/洞察 | 关键结论、方法论、趋势判断 |
| 时间线 | 发布时间、上线日期、路线图 |
| 案例/演示 | 重要应用案例或演示 |

#### 结构模板

```markdown
## 📝 内容总结

**核心要点**

1. **[主题]**：[关键内容]

**关键发布**（如有产品发布）

| 项目 | 说明 | 时间 |
|------|------|------|
| xxx | xxx | xxx |
```

#### 检查清单

- 是否提取所有产品发布/技术更新？
- 是否包含具体数据和数字？
- 是否标注时间线？
- 是否提及重要案例？
- 是否逐段检查无遗漏？

### 高质量输出示例

```markdown
---
title: 定义代理式人工智能时代
source: io.google.com
url: https://io.google/2026/sessions/defining-agentic-era
date: 2026-05-20
category: conference/google-io/2026/sessions
translated: true
fetched_at: 2026-06-22T10:00:00
---

# 定义代理式人工智能时代

**来源**: Google I/O 2026 | **日期**: 2026-05-20

---

## 演讲概述

Gemini 3.5 系列发布，开启智能体时代...

---

## 核心要点

### 1. 模型能力飞跃
- Gemini 3.5 Flash 强化编程与智能体工作流
- 处理长周期任务能力大幅提升

### 2. 全栈AI协同
- 第八代TPU专为训练/推理场景优化
- 模型-框架-产品共生关系

---

## 关键发布

| 产品 | 说明 | 上线时间 |
|------|------|---------|
| Gemini 3.5 Flash | 前沿智能+快速响应 | 当日开放 |
| Gemini Spark | 24/7个人AI代理 | 下周Beta |

---

## 演讲嘉宾

| 嘉宾 | 职位 | 分享内容 |
|------|------|---------|
| Josh | Gemini运营负责人 | Spark应用场景 |
| Koray | DeepMind CTO | 模型架构演进 |

---

*原文请访问 [Google I/O](https://io.google/2026/sessions/defining-agentic-era)*
```

---

## Google I/O 特殊说明

Google I/O 网站是 SPA (Single Page Application)，数据嵌入在 HTML 的 JavaScript 中：

```python
# 提取 sessions JSON
pattern = r'sessions="(\[.*?\])"'
match = re.search(pattern, unescaped_html, re.DOTALL)
sessions = json.loads(match.group(1))
```

Session JSON 结构：
```json
{
  "id": 1,
  "uid": "google-keynote-1",
  "content_type": "Google Keynote",
  "level": "Beginner",
  "start_time": "10:00:00",
  "end_time": "11:45:00",
  "topics": [{"id": 1, "name": "AI/Machine Learning"}],
  "speaker": [{"id": 1, "ldap": "sundar"}],
  "session_date": "2026-05-19",
  "youtube_vod_id": "abc123",
  "event_title": "Google keynote",
  "event_short_description": "",
  "event_long_description": "Discover how..."
}
```
