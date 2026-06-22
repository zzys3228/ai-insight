---
name: ai-source-company
description: 检查AI大公司四维信息源的源列表，只做源发现不做内容追踪。追踪NVIDIA/Google/OpenAI等大公司产品线、官方博客、年度大会、开源项目（整合到各公司章节）。Use when user mentions /ai-source-company, or asks to check AI company products, news sources, open source projects.
---

> **状态**：✅ 已更新（2026-06-22）按维度重构

# AI Source Company Skill

## Quick Start

- `/ai-source-company` — 全量检查，输出建议新增/更新的公司产品源
- `/ai-source-company --all` — 检查所有头部AI公司三维信息
- `/ai-source-company --check` — 只做URL有效性检查

## URL规则 ⚠️ 重要

### 公司/产品URL规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | 产品页/官方文档 | platform.openai.com/docs | API文档 |
| ✅首选 | 官方博客 | blogs.nvidia.com | 官方博客 |
| ✅可选 | 年度大会 | io.google | 大会主页 |
| ❌避免 | 公司首页 | nvidia.com | 应指向具体产品 |

### 云厂商首页产品区（必须fetch）

| 云厂商 | 首页产品区URL |
|--------|--------------|
| 华为云 | huaweicloud.com → AI产品区 |
| 腾讯云 | cloud.tencent.com → AI产品区 |
| 阿里云 | aliyun.com → AI产品区 |
| 火山引擎 | volcengine.com → AI产品区 |
| 百度云 | cloud.baidu.com → AI产品区 |
| AWS | aws.amazon.com/machine-learning |
| Google Cloud | cloud.google.com/products/machine-learning |
| Azure | azure.microsoft.com/services/ai-services |

### 人物URL规则（如涉及CEO）

| 优先级 | URL类型 | 示例 |
|--------|---------|------|
| ✅首选 | 个人X/Twitter | x.com/sama |
| ✅可选 | 公司官方X | x.com/deepseek_ai（无个人账号时） |
| ❌避免 | 公司首页 | deepseek.com |

## 输出格式 ⚠️ 重要

### 编号规则

```
✅ 正确：第一章独立编号1-N（如1. NVIDIA, 2. AMD...）
❌ 错误：全局连续编号
```

### 输出模板

```markdown
## 一、AI头部公司

### 1.1 算力&底层硬件

| # | 三级 | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|------|-----|---------|------|------|------|
| 1 | NVIDIA | NVIDIA 官网 | https://www.nvidia.com | AI芯片龙头 | ✅ | - | - |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ✅302→ | 跳转后可达 |
| ⚠️403 | 需代理 |

## Workflows ⚠️ 必须执行

### 阶段一：fetch所有大模型原生公司产品页

**❌ 错误做法**：只检查已知的产品列表

**✅ 正确做法**：fetch每个公司的产品页，提取全部产品

```
# 每个大模型原生公司必须执行：
1. fetch {公司官网}/products 或 /product
2. 提取：列出所有AI产品名称
3. 对比现有列表
4. 缺失的添加
```

### 必须fetch的公司（不分国内外）

| 公司 | 产品页URL | 已知遗漏 |
|------|----------|---------|
| Anthropic | anthropic.com/products | Claude Cowork, Claude Design |
| OpenAI | openai.com/products | （待fetch） |
| DeepSeek | deepseek.com/products | （待fetch） |
| Mistral | mistral.ai/products | （待fetch） |
| xAI | x.ai/products | （待fetch） |
| Cohere | cohere.com/products | （待fetch） |
| Google DeepMind | deepmind.google/products | （待fetch） |
| NVIDIA | nvidia.com/products | TensorRT-LLM GitHub |

### 阶段二：检查大厂开源项目

**❌ 错误做法**：只检查产品，不检查开源

**✅ 正确做法**：每个大厂都要检查其GitHub org

```
# 每个大厂必须执行：
1. fetch github.com/{公司名}
2. 找AI相关仓库（ML/LLM/AI关键词）
3. 检查Star增长
4. 缺失的添加
```

**必查大厂GitHub Org**：
- NVIDIA → github.com/NVIDIA
- Microsoft → github.com/microsoft
- Google → github.com/google、github.com/google-research
- Meta → github.com/facebook、github.com/meta-llama
- HuggingFace → github.com/huggingface
- OpenAI → github.com/openai
- DeepSeek → github.com/deepseek-ai
- Qwen → github.com/QwenLM

### 阶段三：URL有效性检查
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段四：筛选规则核验
按筛选标准验证

### 阶段五：结构化输出
```
## [公司名]

### 产品线
| # | 产品 | URL | 追踪信源 | 状态 |
|---|---|---|---------|------|
| 1 | 产品名 | URL | 开发者文档 | ✅ |

### 官方博客
| # | 博客 | URL | RSS | 状态 |
|---|---|---|-----|------|
| 1 | 公司博客 | URL | RSS | ✅ |

### 开源项目
| # | 项目 | GitHub | Stars | 状态 |
|---|---|-------|-------|------|
| 1 | TensorRT-LLM | NVIDIA/TensorRT-LLM | 15k+ | ✅ |
```

## 追踪维度（4维）

| 维度 | 内容 | 信源 |
|------|------|------|
| 产品线 | AI产品/服务/平台 | 产品页/API文档/Changelog |
| 官方博客 | 公司官方发布的博客/RSS | 博客RSS |
| 年度大会 | 公司年度技术大会 | 大会主页/演讲回放 |
| 开源项目 | 大厂官方开源的AI项目 | GitHub仓库 |

## 大厂开源项目追踪清单

**已整合到各公司章节**：大厂开源项目不再单独列出，而是整合到对应公司的章节中：

| 公司 | 开源项目 | 归属章节 |
|------|----------|---------|
| NVIDIA | TensorRT-LLM GitHub, cuDNN GitHub, CUDA GitHub | 1.1 算力&底层硬件 |
| Microsoft | AutoGen, DeepSpeed, Semantic Kernel, Playwright | 1.3 综合科技-海外 |
| Google | TensorFlow, BERT, JAX/Flax, Gemma | 1.3 综合科技-海外 |
| Meta | PyTorch, Llama | 1.3 综合科技-海外 |
| HuggingFace | Transformers, Diffusers, TGI | 1.3 综合科技-海外 |
| OpenAI | Whisper, CLIP | 1.2 大模型原生企业 |
| DeepSeek | DeepSeek-V3 | 1.2 大模型原生企业 |
| Qwen | Qwen系列 | 1.4 阿里云产品 |
| 智谱 | ChatGLM | 三、开源社区项目 |

## 大厂开源发现方法

```
# 每个大厂必查开源项目
- GitHub → {公司名} → 找AI相关仓库
- 搜索 site:github.com/{org} AI/ML/LLM
- 关注Star增长快的新仓库

# 示例：
- NVIDIA → github.com/NVIDIA → 找TensorRT、cuDNN等
- Microsoft → github.com/microsoft → 找AI、Copilot相关
- Google → github.com/google → 找TensorFlow、BERT、Flax
```

## 大公司清单

**只追踪大公司**：海外≥100亿美金 / 国内≥500亿RMB

| 分类 | 公司 |
|------|------|
| 算力底层 | NVIDIA |
| 大模型原生 | OpenAI, Anthropic, DeepSeek, Mistral, xAI, Cohere |
| 综合科技-海外 | Google Cloud, AWS, Azure |
| 综合科技-国内 | 阿里云, 百度, 腾讯, 字节, 华为 |

## 分类边界

- 机器人公司 → Robot skill
- 学术/研究院 → Academic skill
- 中小型AI创业公司 → 不追踪（除非达到大公司门槛）

## 追踪范围扩展：AI应用产品公司

**❌ 当前问题**：只追踪大厂，遗漏新兴AI应用产品公司

**✅ 应追踪的AI应用产品公司**（达到以下任一条件）：

| 条件 | 说明 | 示例 |
|------|------|------|
| 融资≥1亿美元 | 头部AI创业公司 | Cursor, Devin |
| MAU≥100万 | C端AI产品 |  |
| GitHub Star≥10k | 开源但流行的AI工具 |  |
| 营收快速增长 | 商业化验证 |  |

**AI Coding类产品发现方法**：

```
1. Product Hunt AI分类 → 找当日/本周热门
2. FutureTools / There's An AI For That → AI工具目录
3. GitHub Trending AI → 找Star增长快的AI项目
4. Y Combinator AI Startup → 看最新批次的AI公司
5. a16z AI Top 100 → 权威榜单
```

**必检AI Coding产品清单**（归属1.10节）：

| 产品 | 公司 | 官网 |
|------|------|------|
| Cursor | Anysphere | cursor.com |
| Dify | langgenius | dify.ai |
| Claude Code | Anthropic | docs.anthropic.com/en/docs/claude-code |
| GitHub Copilot | GitHub/Microsoft | github.blog/category/engineering |
| Devin | Cognition | cognition.ai/blog |
| Codeium | Exafunction | codeium.com/blog |
| Continue | Continue.dev | blog.continue.dev |

## 按维度发现方法 ⚠️ 核心

**❌ 错误做法**：按公司找产品（遗漏博客/开源维度）

**✅ 正确做法**：按维度扫描，每个大公司都要检查四个维度

---

### 维度一：产品线发现

**通用URL模式**（每个大公司都检查）：
```
{公司官网}/products
{公司官网}/product
{公司官网}/platform
platform.{公司官网}
/products
```

**通用发现渠道**：
| 渠道 | URL | 说明 |
|------|-----|------|
| 云厂商首页产品区 | 见下方云厂商表格 | 必须fetch提取AI产品 |
| 融资榜单 | Crunchbase AI Funding, a16z AI Top 100 | 发现新大公司 |
| Product Hunt AI | producthunt.com/topics/artificial-intelligence | 热门AI产品 |

**云厂商AI产品区（必须fetch）**：
| 云厂商 | 首页产品区URL |
|--------|--------------|
| 华为云 | huaweicloud.com → AI产品区 |
| 腾讯云 | cloud.tencent.com → AI产品区 |
| 阿里云 | aliyun.com → AI产品区 |
| 火山引擎 | volcengine.com → AI产品区 |
| 百度云 | cloud.baidu.com → AI产品区 |
| AWS | aws.amazon.com/machine-learning |
| Google Cloud | cloud.google.com/products/machine-learning |
| Azure | azure.microsoft.com/services/ai-services |

---

### 维度二：官方博客发现

**通用URL模式**（每个大公司都检查）：
```
{公司官网}/blog
{公司官网}/news
{公司官网}/research
{公司官网}/engineering
{公司官网}/posts
blog.{公司官网}
news.{公司官网}
```

**通用发现方法**：
| 方法 | 说明 |
|------|------|
| fetch {公司}/blog | 提取所有博客栏目 |
| fetch {公司}/news | 提取所有新闻栏目 |
| 搜索 blog.{公司域名} | 找独立博客域名 |
| 检查RSS | 博客页底部找RSS订阅链接 |

---

### 维度三：开源项目发现

**通用URL模式**：
```
github.com/{公司名}
github.com/{公司名}-ai
github.com/{公司名}lab
```

**通用发现方法**：
| 方法 | 说明 |
|------|------|
| fetch github.com/{org} | 提取AI相关仓库 |
| 搜索 site:github.com/{org} AI/ML/LLM | 找AI相关仓库 |
| 关注Star增长 | 检查仓库热度变化 |

**必查GitHub Org模式**：
```
github.com/{公司名小写}
github.com/{公司名}ai
github.com/{公司名}-ai
github.com/{公司名}_ai
```

---

### 维度四：年度大会发现

**通用URL模式**：
```
{公司官网}/events
{公司官网}/conference
{公司官网}/ summit
io.{公司官网}
```

**通用发现方法**：
| 方法 | 说明 |
|------|------|
| fetch {公司}/events | 找年度技术大会 |
| 搜索 "{公司} AI Day" "{公司} Summit" | 找大会名称 |
| 关注大会主页 | 找演讲回放/PPT下载 |

---

### 发现新大公司

**融资榜单**：
| 渠道 | URL |
|------|-----|
| Crunchbase | crunchbase.com/category/artificial-intelligence |
| a16z | a16z.com/ai |
| CB Insights | cbinsights.com/research/ai-startup-funding |

**YC最新批次**：
| 渠道 | URL |
|------|-----|
| YC Directory | ycombinator.com/companies |
| YC Batch | ycombinator.com/colleges |

**行业报告**：
| 渠道 | 说明 |
|------|------|
| a16z AI Report | 年度AI格局 |
| CB Insights AI 100 | 创新公司榜单 |

## 快速检查清单

**每个大公司都要按维度检查**：

```
□ 产品线 → fetch {公司}/products → 提取全部AI产品
□ 官方博客 → fetch {公司}/blog 和 {公司}/news → 找博客栏目
□ 开源项目 → fetch github.com/{org} → 找AI相关仓库
□ 年度大会 → fetch {公司}/events → 找技术大会
□ RSS订阅 → 检查博客页底部 → 找RSS链接
```

**云厂商快速检查**：
```
□ fetch华为云首页 → 提取AI产品区
□ fetch腾讯云首页 → 提取AI产品区
□ fetch阿里云首页 → 提取AI产品区
□ fetch火山引擎首页 → 提取AI产品区
□ fetch百度云首页 → 提取AI产品区
```

## 筛选标准

| 标准 | 要求 |
|------|------|
| 规模 | 大公司（见清单），不追踪中小AI公司 |
| 活跃度 | 近2年有更新 |
| 可追踪 | 有公开文档/博客/大会议程 |

## 常见错误警示

```
❌ 错误：fetch单个产品页 → 遗漏其他产品
❌ 错误：用公司首页作为人物URL
❌ 错误：使用全局连续编号

✅ 正确：fetch云厂商首页产品区 → 提取全部AI产品
✅ 正确：人物用个人X/博客，或公司官方X（当无个人账号时）
✅ 正确：第一章独立编号
```

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
