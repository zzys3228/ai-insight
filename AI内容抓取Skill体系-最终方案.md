# AI内容抓取Skill体系 - 最终方案

> 创建时间：2026-06-22
> 状态：待修正

---

## 一、已确认的格式标准（10个分类）

| # | 分类 | 存储路径 | 内容要求 | 示例 |
|---|------|----------|---------|------|
| 1 | **GitHub** | `github/{repo}/` | README翻译 + 近半年Releases | `github/vllm-project_vllm/README.md` |
| 2 | **Company** | `company/{公司}/blogs/` | 完整博客文章翻译 | `company/nvidia/blogs/france-advances-xxxxx.md` |
| 3 | **Academic** | `academic/{来源}/{分类}/{paper_id}.md` | 每篇论文单独md，PDF下载→解析→翻译 | `academic/arxiv/cs_cl/2606.20527.md` |
| 4 | **Newsletter** | `media/newsletter/{publisher}/` | 完整文章翻译 | `media/newsletter/import_ai/alignment-is-not-on.md` |
| 5 | **Podcast** | `media/podcast/{name}/` | 音频→Whisper转写→翻译Transcript | `media/podcast/lex_fridman/don-lincoln-physics.md` |
| 6 | **Benchmark** | `benchmark/{name}/` | 完整评测数据（表格形式） | `benchmark/opencompass/2026-06-22.md` |
| 7 | **Robot** | `robot/{公司}/{新闻标题}.md` | 每条新闻单独md，完整文章内容 | `robot/figure/helix-02-full-body.md` |
| 8 | **Standard** | `standard/{protocol}/` | 完整协议规范文档 | `standard/mcp/introduction.md` |
| 9 | **Person** | `person/{name}/{文章标题}.md` | 每篇博客单独md，完整文章内容 | `person/karpathy/rnn-effectiveness.md` |
| 10 | **Conference** | `conference/{name}/{year}/` | 完整议程+演讲内容（多源策略） | `conference/waic/2026/day1-mainforum.md` |

---

## 二、核心技术流程

### 1. PDF论文抓取（Academic）

```
arXiv列表页 → 解析paper_id → 下载PDF → PyMuPDF解析 → 分段翻译 → 保存md
```

**示例**：paper_id = 2606.20527
- PDF URL: `https://arxiv.org/pdf/2606.20527.pdf`
- 存储路径: `academic/arxiv/cs_cl/2606.20527.md`

**技术要点**：
- PDF解析用 PyMuPDF
- 大论文分段处理（每段约2000字符）
- max_tokens≥4096 避免截断

### 2. 播客转写（Podcast）

```
播客页面 → 获取音频URL → 下载音频 → Whisper转写 → 翻译Transcript → 保存md
```

**技术要点**：
- 使用 `openai-whisper` 或 `faster-whisper`
- 音频文件可能100MB+，下载需要时间
- 部分播客有RSS订阅源

### 3. Conference多源策略

**第一阶段：官网基础信息抓取**
- 抓取大会官网，获取议程页面
- 解析议程安排（时间、演讲者、题目）
- 抓取演讲摘要

**第二阶段：完整内容获取**

1. **官方视频发布后下载转写**
   - 监控官方视频平台（B站、YouTube等）
   - 下载视频 → Whisper转写 → 翻译

2. **搜索演讲者后续发布的文章/PPT**
   - 搜索演讲者个人博客、社媒
   - 抓取演讲者后续分享的详细内容

3. **多源报道交叉验证**
   - 搜索媒体报道（36kr、机器之心、量子位等）
   - 交叉验证演讲内容
   - 补充遗漏的关键信息

### 4. 社交媒体（Person）

- **Twitter/X**：使用nitter镜像站（如 nitter.net、nitter.privacydev.net）或代理
- **微博**：代理访问
- **知乎**：代理访问
- 失败记录到 `_failed_urls.json`

---

## 三、Frontmatter统一格式

```markdown
---
title: [标题，中文]
source: [域名]
url: [原文URL]
date: [发布日期]
category: [分类路径]
translated: true
fetched_at: [抓取时间戳]
---

# 内容标题

---

## 正文内容

---

*原文请访问 [URL]*
```

### 特定类型额外字段

| 类型 | 额外字段 | 说明 |
|------|----------|------|
| Academic | `paper_id`, `authors`, `pdf_url` | 论文ID、作者列表、PDF链接 |
| Podcast | `audio_url` | 音频URL |
| Conference | `content_sources` | 内容来源列表和状态 |

### Conference content_sources 示例

```yaml
content_sources:
  - type: official_website
    url: https://worldaic.com.cn/waic2026
    status: completed
  - type: video_transcript
    url: https://...
    status: pending
  - type: speaker_article
    url: https://...
    status: pending
  - type: news_report
    sources: [36kr, jiqizhixin]
    status: pending
```

---

## 四、代理策略

- **国内域名**：直连
  - `.cn`, `aliyun.com`, `baidu.com`, `tencent.com`, `volcengine.com`, `huaweicloud.com` 等
- **海外域名**：代理（`127.0.0.1:26001`）
- **403站点**：走代理访问

### 国内域名直连清单

```
.cn, aliyun.com, baidu.com, tencent.com, volcengine.com,
huaweicloud.com, jd.com, bytedance.com, xiaomi.com,
meituan.com, weibo.com, zhihu.com, bilibili.com,
taobao.com, qq.com, sina.com, 163.com, sina.com
```

---

## 五、翻译策略

- **英文内容**：翻译为中文
- **中文内容**：也翻译（统一流程）
- **代码/公式**：原样保留不翻译
- **API**：MiniMax API
  - endpoint: `https://api.minimaxi.com/v1/text/chatcompletion_v2`
  - model: `MiniMax-M2.7`
  - max_tokens: ≥4096（避免截断）

### API调用示例

```python
import requests

response = requests.post(
    "https://api.minimaxi.com/v1/text/chatcompletion_v2",
    headers={
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    },
    json={
        "model": "MiniMax-M2.7",
        "messages": [
            {"role": "user", "content": f"Translate to Chinese, keep technical terms accurate:\n\n{text}"}
        ],
        "max_tokens": 4096
    }
)
content = response.json()['choices'][0]['message']['content']
```

---

## 六、增量更新策略

- 对比内容变化（hash或diff）
- 只更新变化的部分
- 没变化就跳过
- 支持手动触发

---

## 七、存储结构

```
ai-content-fetched/
├── github/
│   └── {owner}_{repo}/
│       ├── README.md
│       └── releases.md
├── company/
│   └── {公司}/
│       └── blogs/
│           └── {文章slug}.md
├── academic/
│   └── {来源}/
│       └── {分类}/
│           └── {paper_id}.md
├── media/
│   ├── newsletter/
│   │   └── {publisher}/
│   │       └── {article_slug}.md
│   ├── podcast/
│   │   └── {podcast_name}/
│   │       └── {episode_slug}.md
│   └── ...
├── benchmark/
│   └── {benchmark_name}/
│       └── {date}.md
├── robot/
│   └── {公司}/
│       └── {news_slug}.md
├── standard/
│   └── {protocol}/
│       └── {doc_slug}.md
├── person/
│   └── {name}/
│       ├── index.md          (个人简介)
│       └── {article_slug}.md  (博客文章)
├── conference/
│   └── {conference_name}/
│       └── {year}/
│           └── {forum_slug}.md
├── _url_index.json          # URL索引
├── _failed_urls.json        # 失败URL记录
├── _metadata.json          # 抓取状态
└── _samples/               # 格式样本（已完成）
    ├── 1_github.md
    ├── 2_company.md
    ├── 3_academic.md
    ├── 4_newsletter.md
    ├── 5_podcast.md
    ├── 6_benchmark.md
    ├── 7_robot.md
    ├── 8_standard.md
    ├── 9_person.md
    └── 10_conference.md
```

---

## 八、技术栈

| 功能 | 工具 | 说明 |
|------|------|------|
| HTTP抓取 | requests | 普通网页 |
| JS渲染 | Playwright | 动态页面 |
| PDF解析 | PyMuPDF (fitz) | 论文PDF提取 |
| 音频转写 | whisper / faster-whisper | 播客转文字 |
| HTML转Markdown | markdownify, BeautifulSoup | 内容提取 |
| 翻译 | MiniMax API | 云端翻译 |

---

## 九、源信息文件

- **位置**：`ai-news-sources.md`
- **状态**：已验证
- **URL数量**：460+
- **分类**：10个主要分类

### 分类统计

| 分类 | URL数 | 优先级 |
|------|-------|--------|
| Company | ~250 | P0 |
| GitHub/OpenSource | ~130 | P0 |
| Academic | ~60 | P1 |
| Benchmark | ~35 | P1 |
| Person | ~35 | P1 |
| Robot | ~30 | P1 |
| Standard | ~30 | P1 |
| Media | ~50 | P1 |
| Conference | ~15 | P2 |
| Industry | ~25 | P2 |

---

## 十、实现优先级

### Phase 1: 核心基础设施
- [ ] 创建目录结构
- [ ] 创建 requirements.txt
- [ ] 创建共享模块（config, translate, utils, task_queue）

### Phase 2: 高优先级Skill
- [ ] ai-fetch-github
- [ ] ai-fetch-company
- [ ] ai-fetch-academic（PDF抓取+翻译）

### Phase 3: 中优先级Skill
- [ ] ai-fetch-media（Newsletter + Podcast）
- [ ] ai-fetch-benchmark
- [ ] ai-fetch-robot
- [ ] ai-fetch-standard
- [ ] ai-fetch-person

### Phase 4: 低优先级
- [ ] ai-fetch-conference
- [ ] ai-fetch-industry
- [ ] ai-fetch-daily（调度入口）
- [ ] ai-fetch-validate（URL验证）

---

## 十一、注意事项

1. **plan mode限制**：当前处于plan mode，无法实际执行
2. **样本验证**：所有格式样本已保存在 `_samples/` 目录
3. **待修正**：方案可能需要根据实际情况调整

---

## 更新记录

| 日期 | 更新内容 |
|------|---------|
| 2026-06-22 | 初始方案，包含10个分类格式确认 |
