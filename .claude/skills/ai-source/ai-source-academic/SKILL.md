---
name: ai-source-academic
description: 检查学术来源（预印本/顶会/期刊/研究机构），只做源发现不做内容追踪。追踪arXiv/ NeurIPS/ Stanford HAI等学术平台和高校AI实验室。Use when user mentions /ai-source-academic, or asks to check AI papers, conferences, academic sources, research publications.
---

> **状态**：✅ 已更新（2026-06-21）

# AI Source Academic Skill

## Quick Start

- `/ai-source-academic` — 全量检查，输出建议新增/更新的学术源

## URL规则 ⚠️ 重要

### URL类型规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | RSS源 | export.arxiv.org/rss/cs.CL | arXiv RSS |
| ✅首选 | 官方主页 | nips.cc | 会议主页 |
| ✅次选 | 机构主页 | hai.stanford.edu | Stanford HAI |
| ✅次选 | GitHub | github.com/THUDM/ChatGLM | 模型仓库 |

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（第四章及以后无编号）
```

### 输出模板

```markdown
## 四、学术前沿论文

### 4.1 预印本平台

| 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|------|-----|---------|------|------|------|
| arXiv cs.CL | https://export.arxiv.org/rss/cs.CL | NLP每日新论文 | ✅ | - | - |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ✅302→ | 跳转后可达 |
| ⚠️403 | 需代理 |

## Workflows

### 阶段一：URL有效性检查
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段二：分类检索
按5类分别检索预印本/期刊/顶会/高校/机构

### 阶段三：筛选规则核验
按分类筛选规则验证

### 阶段四：结构化输出
```
## Academic 源检查结果

### 建议新增源
| 名称 | URL | 分类 | 核心用途 | 验证依据 |

### 移除建议
| 名称 | 原因 |
|------|------|
| XXX | 停更/合并 |
```

## 分类体系（5类）

| 分类 | 定义 | 示例 |
|------|------|------|
| 预印本平台 | 论文预印本归档/编辑推荐 | arXiv、HF Papers、Papers With Code |
| 学术期刊 | 同行评审的学术期刊 | Nature AI、Science AI、JMLR |
| 学术会议 | AI/ML/CV/NLP领域顶级会议 | NeurIPS、ICML、ICLR、CVPR |
| 高校研究 | 大学AI实验室/研究组博客 | Stanford SAIL、Berkeley BAIR、CMU ML |
| 独立研究机构 | 非公司非高校的独立AI研究机构 | AI2、Mila、Vector Institute、BAAI |

## 分类边界

- 评测榜单归 Benchmark skill
- 公司研究院归 Company skill
- arXiv 包含在内

## 筛选标准

| 标准 | 要求 |
|------|------|
| 内容垂直 | 核心围绕AI/ML/CV/NLP学术研究 |
| 更新时效 | 近6个月有学术产出 |
| 学术认可 | 被顶会/期刊收录或引用 |
| 机构权威 | 高校/知名研究机构 |

## 发现方法：如何发现新的学术源

**❌ 错误做法**：只维护现有顶会列表

**✅ 正确做法**：定期扫描以下渠道

```
# 方法一：顶会追踪
- NeurIPS → nips.cc （每年12月）
- ICML → icml.cc （每年7月）
- ICLR → iclr.cc （每年5月）
- CVPR/ECCV → cvpr.cc / eccv.cc
- AAAI/IJCAI → aaai.org / ijcai.org
- ACL/EMNLP/NAACL → aclanthology.org

# 方法二：预印本平台RSS订阅
- arXiv cs.CL → export.arxiv.org/rss/cs.CL （NLP）
- arXiv cs.LG → export.arxiv.org/rss/cs.LG （机器学习）
- arXiv cs.AI → export.arxiv.org/rss/cs.AI （AI）
- arXiv cs.CV → export.arxiv.org/rss/cs.CV （计算机视觉）
- arXiv cs.RO → export.arxiv.org/rss/cs.RO （机器人）

# 方法三：论文聚合平台
- Papers With Code → paperswithcode.com （论文+代码）
- HuggingFace Papers → huggingface.co/papers
- Semantic Scholar → semanticscholar.org
- Connected Papers → connectedpapers.dev

# 方法四：高校AI实验室发现
- 追踪Stanford HAI、Berkeley BAIR、CMU ML最新博客
- 搜 "site:ai.stanford.edu blog"
- 搜 "site:bair.berkeley.edu blog"

# 方法五：研究机构发现
- AI2 (Allen Institute) → allenai.org
- Mila Quebec → mila.quebec
- Vector Institute → vectorinstitute.ai
- 北京智源人工智能研究院 → baai.org.cn
```

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
