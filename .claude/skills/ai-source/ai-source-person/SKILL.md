---
name: ai-source-person
description: 检查AI关键人物的源列表，只做源发现不做内容追踪。追踪Sam Altman/Yann LeCun/Hinton等AI CEO、首席科学家、高校学者，投资人、技术博主。Use when user mentions /ai-source-person, or asks to check AI influencers, key people, thought leaders, AI researchers.
---

> **状态**：✅ 已更新（2026-06-21）

# AI Source Person Skill

## Quick Start

- `/ai-source-person` — 全量检查，输出建议新增/更新的人物源

## URL规则 ⚠️ 重要

### 人物URL优先级

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | 个人X/Twitter | x.com/sama | OpenAI CEO |
| ✅次选 | 个人博客/网站 | karpathy.ai | AI教育先驱 |
| ✅可选 | 公开访谈/演讲 | Lex Fridman Podcast | 无个人账号时 |
| ❌避免 | 公司官方X | x.com/deepseek_ai | ❌不是个人账号 |
| ❌避免 | 公司首页 | deepseek.com | 无意义 |
| ❌避免 | 院系主页 | ai.stanford.edu | 应指向个人或创业公司 |
| ❌避免 | 微博 | weibo.com/xxx | 需登录不可用 |

### CEO/创始人URL规则 ⚠️ 重要

```
❌ 错误示例：
- 梁文锋 (DeepSeek) → https://x.com/deepseek_ai （这是公司账号！）
- 张宏江 → https://www.minimaxi.com/news （这是公司新闻页！）

✅ 正确示例：
- 梁文锋 (DeepSeek) → 无个人账号，删除
- 张宏江 → 无个人账号，删除
- 杨植麟 → 无个人账号，删除
- 李开复 → weibo.com/u/1195230310（但微博需登录，删除更佳）
- 黄仁勋 → https://blogs.nvidia.com （CEO署名文章）
```

### 国内创始人社交媒体现状

**有公开社交媒体的（极少）：**
- 李开复 → weibo.com/u/1195230310（但需登录，删除更佳）
- 刘庆峰 → weibo.com/liuqingfeng（但需登录，删除更佳）
- 王小川 → weibo.com/wangxiaochuan（但需登录，删除更佳）

**无公开社交媒体的（大多数）：**
- 梁文锋 (DeepSeek) - 极度低调
- 张宏江 (MiniMax) - 低调
- 杨植麟 (月之暗面) - 低调
- 唐杰 (智谱AI) - 低调
- 姜大昕 (阶跃星辰) - 低调

**建议**：国内创始人如无X/个人博客/可访问的微博，一律删除，不要放"未知活跃平台"
| 字节豆包 | 张楠 | 抖音CEO |  |
| 腾讯 | 姚期智 | 首席科学家 |  |
| 腾讯云 | 邱跃鹏(待确认) | 云负责人 |  |
| 阿里云 | 周靖人 | CTO |  |
| 百度 | 王海峰 | CTO |  |
| 华为 | 张平安 | 海思总裁 |  |

### 公司/产品URL规则

| 优先级 | URL类型 | 示例 |
|--------|---------|------|
| ✅首选 | 产品页/官方文档 | platform.openai.com/docs |
| ✅次选 | 官方博客 | blogs.nvidia.com |
| ❌避免 | 公司首页 | 应指向具体产品页 |

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（第五章无编号）
```

### 输出模板

```markdown
## 五、AI关键人物

### 5.1 知名AI企业CEO

| 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|------|-----|---------|------|------|------|
| Sam Altman | https://x.com/sama | OpenAI CEO风向标 | ✅ | - | - |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ✅302→ | 跳转后可达 |
| ⚠️403 | 需代理 |

## Workflows

### 阶段一：fetch公司官网人物页

**❌ 错误做法**：只搜索已知人物

**✅ 正确做法**：fetch每个AI公司的"About"或"Leadership"页，找核心人物

```
# 每个AI公司必须执行：
1. fetch {公司官网}/about 或 /leadership
2. 提取：CEO、CTO、首席科学家
3. 找个人社交媒体
4. 对比现有列表
```

### 阶段二：按分类检索人物

| 分类 | 搜索关键词 |
|------|---------|
| AI企业CEO | AI startup CEO 2024, founder deepseek openai |
| 首席科学家 | AI chief scientist, research director |
| 高校学者 | AI professor Stanford, ML researcher |
| 投资人 | AI VC partner, investor foundation |
| 技术博主 | AI blog author, ML newsletter writer |

### 阶段三：确定人物渠道

按URL规则选择正确的渠道类型

### 阶段四：结构化输出
```
## Person 人物检查结果

### 建议新增人物
| 人物 | 公司/机构 | 分类 | 渠道 | URL | 推荐理由 |
|------|----------|------|------|-----|---------|

### ⚠️ URL问题
| 人物 | 当前URL | 问题 | 建议 |
|------|---------|------|------|
| XXX | 公司首页 | 无意义 | 改为个人X/博客 |

### 移除建议
| 人物 | 原因 |
|------|------|
| XXX | 长期无产出/已离职 |
```

## 分类体系（8类）

| 分类 | 定义 | 示例 |
|------|------|------|
| 知名AI企业CEO | 大模型/算力/机器人企业创始人 | Sam Altman、梁文锋、黄仁勋 |
| 企业首席科学家 | 商业AI公司技术总负责人 | Yann LeCun、Demis Hassabis |
| 高校学术学者 | 大学全职教授、实验室负责人 | Geoffrey Hinton、吴恩达、何恺明 |
| AI专业投资人 | 专注大模型/Agent赛道的VC/天使 | Sarah Guo、Marc Andreessen |
| 技术博主 | 长期输出个人博客/专栏 | Andrej Karpathy、Lilian Weng |
| 开源社区领袖 | 主流LLM/推理/Agent项目核心维护人 | ggerganov、vLLM团队 |
| AI安全专家 | AI安全/对齐/治理领域核心研究者 | Ilya Sutskever |
| 独立研究者 | 纯自由职业AI科研创作者 | 待补充 |

## 分类边界

- 高校Lab归 Academic（Stanford SAIL等）
- 播客/Newsletter归 Media（Lex Fridman等）
- 公司研究院归 Company（Meta FAIR等）
- 一人多身份以主业归入单一分类

## 筛选标准

| 标准 | 要求 |
|------|------|
| 产出门槛 | CEO：公司估值头部；科学家：近3年顶会一作；影响者：持续1年以上稳定输出 |
| 行业共识 | 被论文/发布会/权威媒体多次引用 |
| 身份归类 | 一人多身份只归一个分类 |

## 发现方法：如何发现新的AI关键人物

**❌ 错误做法**：只维护现有人物列表

**✅ 正确做法**：定期扫描以下渠道

```
# 方法一：公司About/Leadership页（每次必查）
- 每个AI公司 → {官网}/about 或 /leadership
- 提取：CEO、CTO、首席科学家、VP of AI
- 对应找个人X/博客

# 方法二：顶会论文作者发现
- arXiv每日新论文 → 第一作者/通讯作者
- NeurIPS/ICML/ICLR → 最佳论文作者
- Google Scholar AI High Citers → 高引作者
- Papers With Code → 高引用模型作者

# 方法三：播客/访谈发现
- Lex Fridman → 嘉宾名单（每期都是AI关键人物）
- Dwarkesh Patel → 嘉宾名单
- No Priors → 嘉宾名单
- a16z Podcast → AI嘉宾
- 中国：42章经、硅谷101嘉宾

# 方法四：GitHub Star发现
- trending仓库 → 找核心维护者
- Star>10k的AI项目 → 找创始人/核心开发者
- 个人GitHub主页 → 找博客/社交链接

# 方法五：媒体引用发现
- TechCrunch/VentureBeat文章 → 引用的人物
- 36氪/机器之心文章 → 引用的人物
- 搜索 "[人物名] AI founder" 或 "[人物名] CEO"

# 方法六：VC投资发现
- a16z portfolio → 找AI创始人
- Sequoia China portfolio → 找AI创始人
- YC最新批次 → AI公司创始人
- 搜索 "AI startup founder interview"

# 方法七：国内AI人物发现
- 百度"AI人物"专题
- 量子位/机器之心"专访"栏目
- 智东西"深度"栏目
- 搜索 "[公司名] 创始人 AI"
```

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
