---
name: ai-source-media
description: 检查媒体/播客/Newsletter的AI源列表，只做源发现不做内容追踪。追踪Import AI/The Batch/Lex Fridman等Newsletter、播客，科技媒体。Use when user mentions /ai-source-media, or asks to check AI newsletters, podcasts, media sources, AI news outlets.
---

> **状态**：✅ 已更新（2026-06-21）

# AI Source Media Skill

## Quick Start

- `/ai-source-media` — 全量检查，输出建议新增/更新的媒体源

## URL规则 ⚠️ 重要

### URL类型规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | Newsletter订阅页 | importai.substack.com | 官方订阅页 |
| ✅首选 | 播客官网 | lexfridman.com | 官方主页 |
| ✅首选 | 框架博客 | blog.langchain.dev | 官方博客 |
| ✅首选 | 媒体AI专栏 | techcrunch.com/category/artificial-intelligence | AI专属板块 |
| ✅次选 | RSS源 | export.arxiv.org/rss/cs.CL | 学术RSS |

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（第二章及以后无编号）
```

### 输出模板

```markdown
## 九、媒体快讯

### 9.1 Newsletter

| 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|------|-----|---------|------|------|------|
| Import AI | https://importai.substack.com | Jack Clark政策/技术 | ✅ | 是 | daily |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ✅302→ | 跳转后可达 |
| ⚠️403 | 需代理 |
| ⚠️429 | 反爬限制 |

## Workflows

### 阶段一：URL有效性检查
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段二：分类检索
按5类分别检索Newsletter/播客/社区/媒体/博客

### 阶段三：筛选规则核验
按分类筛选规则验证

### 阶段四：结构化输出
```
## Media 源检查结果

### 建议新增源
| 名称 | URL | 分类 | 更新频率 | 验证依据 |

### 移除建议
| 名称 | 原因 |
|------|------|
| XXX | 停更/质量下降 |
```

## 分类体系（6类）

| 分类 | 定义 | 示例 |
|------|------|------|
| Newsletter订阅专栏 | 邮件订阅制AI深度周报 | Import AI、The Batch、Ben's Bites |
| 播客音频栏目 | 音频为主含配套视频的AI访谈 | Lex Fridman、Dwarkesh、No Priors |
| 框架/工具博客 | AI框架官方技术博客 | LangChain博客、vLLM博客 |
| AI社区讨论 | Reddit/HackerNews等社区 | r/LocalLLaMA、HackerNews |
| 海外科技媒体 | 综合科技网站AI专属板块 | TechCrunch AI、VentureBeat AI |
| 国内AI垂直媒体 | 本土聚焦大模型、机器人的产业媒体 | 机器之心、量子位、智东西 |

## 必检框架/工具博客

| 框架 | 官方博客URL |
|------|------------|
| LangChain | blog.langchain.dev |
| vLLM | vllm.ai |
| PyTorch | pytorch.org/blog |

## 分类边界

- 个人技术博客 → Person skill
- 公司官方博客 → Company skill
- 开发者社区 → OpenSource skill

## 中文AI播客发现渠道 ⚠️ 必须

```
# 方法一：小宇宙AI播客分类
- 小宇宙 → 搜索"AI"/"大模型"/"算力"
- 小宇宙 → 科技/商业分类下的AI相关播客

# 方法二：微信公众号发现
- 搜索"AI播客" "大模型访谈" "算力圆桌" "Agent"
- 关注晚点、机器之心、量子位等媒体播客频道

# 方法三：RSS聚合搜索
- podnews.net/search?q=AI+Chinese

# 方法四：嘉宾发现法
- Lex Fridman → 找中文嘉宾（如有）→ 找该嘉宾的主播播客
- 晚点聊 LateTalk → 嘉宾名单发现新播客
```

### 中文AI播客筛选标准
| 标准 | 要求 |
|------|------|
| 主持人 | 科技媒体/投资机构/独立KOL |
| 嘉宾 | AI创始人/首席科学家/投资人 |
| 频率 | 月更≥2期 |
| 深度 | 单集60分钟以上 |

**发现后**：添加到 ai-news-sources.md 第九章 9.2 播客音频栏目

## 已收录中文AI播客RSS

| 播客 | RSS | 备注 |
|------|-----|------|
| 晚点聊 LateTalk | https://feeds.fireside.fm/latetalk/rss | 晚点团队·双周更新 |

## 筛选标准

| 分类 | 标准 |
|------|------|
| Newsletter | 稳定周更，70%+内容聚焦AI，业内高频引用 |
| 播客 | 月更新≥2期，嘉宾为AI学者/创始人/投资人 |
| 框架博客 | 框架核心迭代、行业落地案例 |
| 海外媒体 | 独立AI专栏，原创深度报道 |
| 国内媒体 | 每日产出AI原创，自有专职采编 |

## 发现方法：如何发现新的AI媒体源

**❌ 错误做法**：只维护现有媒体列表

**✅ 正确做法**：定期扫描以下渠道

```
# 方法一：Newsletter发现
- Substack AI目录 → substack.com/topics/artificial-intelligence
- Beehiiv AI目录 → beehiiv.com
- 搜索 "best AI newsletter" "AI weekly digest"
- 播客RSS聚合 → podnews.net/search?q=AI

# 方法二：播客发现
- Apple Podcasts AI分类 → 搜索"AI"筛选
- Spotify AI Podcast → 搜索"artificial intelligence"
- 小宇宙AI播客 → 国内AI播客聚合
- Lex Fridman → 嘉宾名单发现新人物播客
- Dwarkesh Patel → 嘉宾发现
- No Priors → 嘉宾发现

# 方法三：科技媒体AI专栏
- TechCrunch AI → techcrunch.com/category/artificial-intelligence
- VentureBeat AI → venturebeat.com/category/ai
- The Verge AI → theverge.com/ai-artificial-intelligence
- Wired AI → wired.com/tag/artificial-intelligence
- MIT Technology Review AI → technologyreview.com/topic/artificial-intelligence

# 方法四：国内AI媒体
- 机器之心 → jiqizhixin.com
- 量子位 → qbitai.com
- 智东西 → zhidx.com
- 极客公园 → geekpark.net
- 36氪AI → 36kr.com/tag/人工智能

# 方法五：框架/工具博客追踪
- LangChain博客 → blog.langchain.dev
- vLLM博客 → vllm.ai
- HuggingFace博客 → huggingface.co/blog
- PyTorch博客 → pytorch.org/blog
- GitHub模型博客 → models.github.com

# 方法六：社区发现
- Hacker News → news.ycombinator.com （AI讨论）
- Reddit r/LocalLLaMA → reddit.com/r/LocalLLaMA
- Reddit r/MachineLearning → reddit.com/r/MachineLearning
- Twitter/X AI列表 → 搜索"AI newsletter"
```

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
