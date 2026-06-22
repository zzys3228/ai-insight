---
name: ai-source-benchmark
description: 检查评测榜单的AI源列表，只做源发现不做内容追踪。追踪LMSYS Arena/SWE-bench/GAIA等模型评测、Agent评测、代码评测榜单。Use when user mentions /ai-source-benchmark, or asks to check AI benchmarks, leaderboards, evaluation sources, model rankings.
---

> **状态**：✅ 已更新（2026-06-21）

# AI Source Benchmark Skill

## Quick Start

- `/ai-source-benchmark` — 全量检查，输出建议新增/更新的榜单源

## URL规则 ⚠️ 重要

### URL类型规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | 榜单主页 | arena.ai | LMSYS官方 |
| ✅首选 | 官方文档 | modelcontextprotocol.io/docs | 协议规范 |
| ✅次选 | GitHub | github.com/THUDM/AgentBench | 代码/评测集 |
| ✅次选 | arXiv | arxiv.org/abs/xxx | 论文描述 |

### URL验证要点 ⚠️ 必须

```
❌ 错误：直接使用跳转前的URL
- agentarena.ai → 405错误

✅ 正确：用 curl -L 检查最终跳转URL
- agentarena.ai → designarena.ai
```

**验证命令：**
```bash
curl -sI --max-time 10 {URL}
curl -sI --max-time 10 -L {URL}  # 跟随跳转
```

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（第六章及以后无编号）
```

### 输出模板

```markdown
## 六、权威评测榜单

### 6.1 通用大模型综合榜单

| 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|------|-----|---------|------|------|------|
| LMSYS Chatbot Arena | https://arena.ai | 人类盲评对战榜 | ✅302→ | 是 | daily |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ✅302→ | 跳转后可达 |
| ⚠️403 | 需代理 |
| ⚠️404 | 不存在 |

## Workflows

### 阶段一：URL有效性检查
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段二：分类检索
按3类分别检索模型榜单/Agent榜单/代码榜单

### 阶段三：筛选规则核验
四重核验：维护主体/评测方案/付费机制/行业引用

### 阶段四：结构化输出
```
## Benchmark 源检查结果

### URL更新
| 榜单 | 原URL | 新URL |

### 建议新增源
| 榜单 | URL | 分类 | 核心用途 |

### 移除建议
| 榜单 | 原因 |
|------|------|
| XXX | 停更/付费提分 |
```

## 分类体系（3类）

| 分类 | 定义 | 示例 |
|------|------|------|
| 模型评测榜单 | 通用大模型综合能力排名 | LMSYS Arena、HF Open LLM、OpenCompass |
| Agent评测榜单 | 智能体任务执行/协作能力评测 | GAIA、AgentBench、OSWorld |
| 代码评测榜单 | 编程能力评测榜单 | SWE-bench、LiveCodeBench |

## 分类边界

- 论文榜单归 Academic（HF Papers、Papers With Code）
- 算力/芯片榜单归 Company
- 产业报告归 Industry

## 筛选标准

| 标准 | 要求 |
|------|------|
| 维护主体 | 高校/中立开源联盟/标准化组织 |
| 评测方案 | 完整数据集、测试用例、复现代码开源 |
| 付费机制 | 禁止厂商付费提分 |
| 行业引用 | OpenAI/华为等官方技术文档引用 |

## 注意事项

| 问题 | 说明 |
|------|------|
| LMSYS Arena | 已从 lmarena.ai 迁移至 arena.ai |
| URL变更 | 及时检查重定向，保持最新URL |

## 发现方法：如何发现新的评测榜单

**❌ 错误做法**：只维护已知榜单

**✅ 正确做法**：定期扫描以下渠道

```
# 方法一：权威榜单聚合
- LMSYS Chatbot Arena → arena.ai （最权威人类对战）
- HuggingFace Open LLM Leaderboard → huggingface.co/spaces/open-llm-leaderboard
- OpenCompass → opencompass.org.cn （国内权威）
- Scale AI Leaderboard → scale.com/leaderboard

# 方法二：GitHub搜索新榜单
- site:github.com benchmark LLM evaluation
- site:github.com SWE-bench agent evaluation
- site:github.com GAIA benchmark

# 方法三：论文发现新榜单
- arXiv搜索 "benchmark" "leaderboard" "evaluation"
- 顶会论文中的评测方法 → 找公开榜单
- Papers With Code → 找SOTA对比中的新榜单

# 方法四：Agent评测发现
- GAIA → gaia-benchmark.github.io
- AgentBench → github.com/THUDM/AgentBench
- OSWorld → os-world.github.io
- WebArena → web-arena.benchmark.com
- MiniWob++ → miniwob.florian.github.io

# 方法五：代码评测发现
- SWE-bench → github.com/princeton-nlp/SWE-bench
- LiveCodeBench → livecodebench.github.io
- HumanEval → github.com/openai/human-eval
- BigCodeBench → huggingface.co/datasets/bigcode/bigcodebench

# 方法六：行业引用追踪
- 关注OpenAI/Anthropic/DeepSeek技术报告中的评测榜单
- 关注arXiv新论文引用次数高的榜单
```

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
