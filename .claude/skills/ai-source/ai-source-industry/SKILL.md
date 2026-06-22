---
name: ai-source-industry
description: 检查行业洞察信息源（VC/智库/政策/AI安全机构），只做源发现不做内容追踪。追踪a16z/Stanford HAI/Gartner等机构的行业报告、政策法规、AI安全评估。Use when user mentions /ai-source-industry, or asks to check AI industry reports, VC insights, policy sources, AI investment trends.
---

> **状态**：✅ 已更新（2026-06-21）

# AI Source Industry Skill

## Quick Start

- `/ai-source-industry` — 全量检查，输出建议新增/更新的行业信息源

## URL规则 ⚠️ 重要

### URL类型规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | 机构官网 | hai.stanford.edu | Stanford HAI |
| ✅次选 | 报告页面 | a16z.com/ai | VC报告页 |
| ✅可选 | 政策主页 | cac.gov.cn | 政策官网 |

### URL验证要点 ⚠️ 必须

```
❌ 错误：直接使用跳转前的URL
- mattturck.com → 307跳转到/mad-landscape

✅ 正确：用 curl -L 检查最终跳转URL
- mattturck.com → mattturck.com/mad-landscape
```

**验证命令：**
```bash
curl -sI --max-time 10 -L {URL}  # 跟随跳转
```

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（第八章及以后无编号）
```

### 输出模板

```markdown
## 八、行业洞察报告

### 8.1 VC/风投机构

| 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|------|-----|---------|------|------|------|
| a16z AI | https://a16z.com/ai | AI投资趋势 | ✅ | - | - |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ⚠️403 | 需代理 |
| ⚠️412 | 需特殊headers |

## Workflows

### 阶段一：URL有效性检查
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段二：分类检索
按6类分别检索

### 阶段三：筛选规则核验
按分类筛选规则验证

### 阶段四：结构化输出
```
## Industry 源检查结果

### 建议新增源
| 名称 | URL | 分类 | 验证依据 |

### 移除建议
| 名称 | 原因 |
|------|------|
| XXX | 已停更/合并 |
```

## 分类体系（6类）

| 分类 | 定义 | 代表 |
|------|------|------|
| VC/风投机构 | 发布AI赛道投融资、创业趋势报告 | a16z、Sequoia，红杉中国 |
| 中立智库 | 高校/第三方独立研究机构，输出AI年度全景 | Stanford HAI、State of AI Report、Epoch AI |
| 专业咨询公司 | 面向企业的AI落地、市场规模报告 | McKinsey AI、Gartner AI |
| 政策监管机构 | 出台AI法规、治理框架、行业标准 | EU AI Office、中国网信办 |
| AI安全专项机构 | 专注模型风险、对齐、安全评估 | METR、Apollo Research、UK AISI |
| 企业研究院 | 大厂内部研究部门，输出技术产业观察 | 腾讯研究院、阿里达摩院、华为2012实验室 |

## 分类边界

- Company管产品发布：官方产品发布页归 ai-source-company
- Industry管研究报告：研究院产出的报告归这里
- 学术论文/顶会 → Academic skill
- Agent协议/标准 → Standard skill

## 筛选标准

| 标准 | 要求 |
|------|------|
| 内容垂直 | 核心内容围绕AI产业/投资/政策/安全 |
| 更新时效 | 近6个月有持续更新/发布报告 |
| 行业认可 | 被业内VC/研究员/创始人高频引用 |
| 权威门槛 | 一级机构，不收录自媒体/小机构 |

## 发现方法：如何发现新的行业信息源

**❌ 错误做法**：只维护现有机构列表

**✅ 正确做法**：定期扫描以下渠道

```
# 方法一：VC机构追踪（年度AI报告必看）
- a16z AI → a16z.com/ai （a16z AI年度报告）
- Sequoia AI → sequoiacap.com/ai
- 红杉中国AI → hongshanzihua.com
- Bloomberg Beta → bloombergbeta.com
- NFX → nfx.com

# 方法二：智库年度报告
- Stanford HAI → hai.stanford.edu （AI Index年度报告）
- State of AI Report → stateof.ai
- Epoch AI → epoch.ai （算力scaling laws）
- McKinsey AI → mckinsey.com/ai
- Gartner AI → gartner.com/ai

# 方法三：国内政策追踪
- 网信办 → cac.gov.cn （AI监管政策）
- 信通院 → caict.ac.cn （AI白皮书/产业报告）
- 发改委 → ndrc.gov.cn （AI产业政策）
- 工信部 → miit.gov.cn （AI发展规划）

# 方法四：GitHub Awesome列表
- awesome-ai-infra → AI基础设施全景
- awesome-llm-long-context-modeling → 大模型上下文
- awesome-ai-investors → AI投资人列表

# 方法五：学术转产业
- arXiv → cs.CY (Computation and Society)
- Papers With Code Industry → 找商业化案例
```

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
