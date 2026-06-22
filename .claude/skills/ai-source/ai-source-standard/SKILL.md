---
name: ai-source-standard
description: 检查Agent协议与AI标准类型的源列表，只做源发现不做内容追踪。追踪MCP/A2A/ISO 42001等协议标准组织，行业事实协议、实验/新兴协议。Use when user mentions /ai-source-standard, or asks to check AI protocols, standards, MCP, A2A, agent communication.
---

> **状态**：✅ 已更新（2026-06-21）

# AI Source Standard Skill

## Quick Start

- `/ai-source-standard` — 全量检查，输出建议新增/更新的协议与标准源

## URL规则 ⚠️ 重要

### URL类型规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | 协议官网 | modelcontextprotocol.io | MCP官方 |
| ✅次选 | 规范文档 | docs.anthropic.com | Anthropic文档 |
| ✅可选 | GitHub规范 | github.com/modelcontextprotocol/spec | 协议规范仓库 |
| ✅可选 | IETF草案 | datatracker.ietf.org/doc/draft-xxx | IETF RFC草案 |

### URL验证要点 ⚠️ 必须

```
❌ 错误：URL结尾缺少斜杠导致404
- w3.org/groups/wg/agents → 404
- opentelemetry.io/docs/specs/semconv/gen-ai → 301

✅ 正确：W3C/标准化组织页面必须加斜杠
- w3.org/groups/wg/agents/
- opentelemetry.io/docs/specs/semconv/gen-ai/
```

**验证命令：**
```bash
curl -sI --max-time 10 {URL}/  # 测试加斜杠版本
```

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（第七章无编号）
```

### 输出模板

```markdown
## 七、协议与标准

### 7.1 标准治理组织

| 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|------|-----|---------|------|------|------|
| AAIF | https://agentic.ai | MCP/A2A/AGENTS.md托管方 | ✅ | 否 | daily |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ⚠️403 | 需代理 |

## Workflows

### 阶段一：划定检索范围
8个维度：LLM推理/Agent工具调用/Agent间通信/人机交互/安全合规/可观测/价值交换/Agent发现

### 阶段零（可选）：URL有效性验证
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段二：多渠道分层检索
标准化组织/头部AI厂商/社区Awesome/学术机构

### 阶段三：筛选与清洗
区分正式标准/行业协议/实验协议

### 阶段四：结构化输出
```
## Standard 协议检查结果

### 建议新增协议
| 协议 | URL | 分类 | 核心用途 | 验证依据 |

### 移除建议（已废弃）
| 协议 | 原因 |
|------|------|
| XXX | 规范已废弃/合并 |
```

## 分类体系（6类）

| 分类 | 定义 | 示例 |
|------|------|------|
| 协议制定组织 | 制定/托管协议标准的组织 | AAIF、W3C、IETF、ISO/IEC |
| 正式标准 | ISO/IEC、W3C已发布推荐标准 | ISO/IEC 42001、W3C DID |
| 行业事实协议 | 大厂开源+全生态兼容+广泛落地 | MCP、A2A、OpenAI API |
| 实验/新兴协议 | IETF draft、0.x版本规范、未稳定 | WebMCP、ANP、CHAP |
| AI安全与对齐机构 | AI安全研究机构、政府安全办公室 | METR、CAIS、UK AISI、US AISI |
| AI政策与法规 | AI监管政策、法规、国际条约 | EU AI Act、网信办、信通院 |

## 分类边界

- Standard管协议本身：MCP、A2A、OWASP Top10
- Industry管机构报告：OWASP年度报告、NIST AI RMF报告
- IETF draft ≠ 正式标准
- 框架/工具 ≠ 协议（Goose是agent框架，不是协议）
- AI安全机构：只管安全研究机构/政府办公室，不管公司内部安全团队（归Company）

## AI安全机构发现方法

**❌ 当前问题**：遗漏安全机构

**✅ 发现渠道**：

```
# 方法一：政府AI安全机构
- UK AISI (AI Safety Institute) → aisi.gov.uk
- US AISI → nist.gov/aisi
- 中国AI安全 → 需关注两会/信通院动态

# 方法二：独立安全研究机构
- METR → metr.org （前沿模型危险能力评估）
- Apollo Research → apolloresearch.ai （欺骗性评估）
- CAIS → cais.ai （旧金山AI安全中心）

# 方法三：安全研究非营利
- Redwood Research → redwoodresearch.com
- Conjecture → conjecture.dev
- EleutherAI → eleuther.ai （开源LLM研究）
- FAR AI → far.ai
- Machine Intelligence Research → intelligence.org
- Ought → ought.org

# 方法四：行业引用追踪
- Anthropic Alignment → alignment.anthropic.com
- OpenAI Safety → openai.com/safety
- Google DeepMind Safety → deepmind.google/safety
```

## AI政策与法规发现方法

**❌ 当前问题**：遗漏政策动态

**✅ 发现渠道**：

```
# 国际政策
- EU AI Act → artificialintelligenceact.eu
- ISO/IEC SC42 → iso.org/committee/6794475
- IEEE AI Standards → standards.ieee.org/beyond-standards/ai
- NIST AI → nist.gov/artificial-intelligence
- ITU AI → itu.int/en/ITU-T/ai

# 国内政策
- 网信办 → cac.gov.cn （国内AI监管源头）
- 信通院 → caict.ac.cn （工信部白皮书、政策落地）
- 全国人大AI立法 → npc.gov.cn
- 发改委AI政策 → ndrc.gov.cn

# 专利追踪
- WIPO AI Patents → wipo.int/tech_trends/en/artificial_intelligence
- Google Patents → patents.google.com （AI专利检索）
- CNIPA → cnipa.gov.cn （中国专利局）
```

## 发现方法：如何持续发现新协议/标准/机构

**❌ 错误做法**：只维护现有清单

**✅ 正确做法**：定期扫描以下渠道

```
# 方法一：协议规范仓库Watch
- github.com/modelcontextprotocol/spec → 关注Release
- github.com/agentprotocol → A2A协议
- github.com/agentics-org → AGENTS.md标准

# 方法二：Awesome列表追踪
- awesome-mcp-servers → MCP生态新服务器
- awesome-ai-agent → Agent协议汇总
- awesome-mlops → MLOps标准

# 方法三：行业会议发现
- AI Safety Summit → 年度安全会议
- International AI Safety Symposium
- OECD AI Policy Observatory

# 方法四：学术追踪
- arXiv cs.AI / cs.CY → AI安全和伦理论文
- Papers With Code AI Safety → 论文+实现
```

## 分类边界

- Standard管协议本身：MCP、A2A、OWASP Top10
- Industry管机构报告：OWASP年度报告、NIST AI RMF报告
- IETF draft ≠ 正式标准
- 框架/工具 ≠ 协议（Goose是agent框架，不是协议）

## 筛选标准

| 类型 | 标准 |
|------|------|
| 国际正式标准 | ISO/IEC、W3C推荐标准、IETF正式RFC |
| 行业事实协议 | 大厂开源+全生态兼容+广泛落地 |
| 实验/新兴 | IETF draft、arXiv论文、0.x版本 |

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
