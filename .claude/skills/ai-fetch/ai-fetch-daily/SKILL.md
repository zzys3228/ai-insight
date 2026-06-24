# AI Fetch Daily - 主入口Skill

## Description
主入口调度skill，用于抓取所有AI信息源内容。支持分类调度、增量更新、失败重试。

## Usage
```
/ai-fetch-daily              # 增量抓取所有源
/ai-fetch-daily --full     # 全量抓取（覆盖所有）
/ai-fetch-daily --stats    # 查看抓取统计
/ai-fetch-daily --list     # 列出所有待抓取URL
/ai-fetch-daily --failed   # 查看失败记录

# 分类抓取
/ai-fetch-daily --github   # 仅GitHub
/ai-fetch-daily --academic # 仅学术论文
/ai-fetch-daily --company  # 仅公司博客
/ai-fetch-daily --media   # 仅媒体快讯
```

## 抓取顺序（按优先级）
1. **P0: GitHub** - GitHub仓库（限流严格，先跑）
2. **P0: Company** - 公司博客（最多URL）
3. **P1: Academic** - 学术论文
4. **P1: Media** - Newsletter/播客
5. **P1: Person** - 人物动态
6. **P1: Benchmark** - 评测榜单
7. **P1: Robot** - 机器人动态
8. **P1: Standard** - 协议文档
9. **P2: Conference** - 大会信息
10. **P2: Industry** - 行业报告

## 增量更新策略
- 对比内容变化（hash或diff）
- 只更新变化的部分
- 没变化就跳过

## 配置
读取 `ai-news-sources.md` 获取URL列表

## 质量标准
所有抓取内容必须符合以下标准：
- **翻译质量**：英文全文翻译为中文，无混杂英文导航
- **内容清洗**：移除页脚、导航菜单、Cookie提示等无关内容
- **格式规范**：Frontmatter完整，包含title/url/date/category/translated
- **编码正确**：无mojibake（乱码），使用UTF-8

## 质量检查标准

所有抓取内容必须符合以下质量标准：

### 一、Frontmatter 格式

```yaml
---
title: [标题，中文翻译]
source: [域名]
url: [原文URL]
date: [发布日期 YYYY-MM-DD]
category: [分类路径]
translated: true/false
fetched_at: [抓取时间戳]
---
```

**必填字段**：title, source, url, date, category, translated, fetched_at
**禁止字段**：冗余字段如 track/type/level（大会类除外）

### 二、正文结构

```markdown
# [中文标题]

**来源**: [域名] | **日期**: [日期]

---

## [章节名称]

[正文内容]

---

*原文请访问 [链接文字](URL)*
```

**要求**：
- 标题与frontmatter一致
- 来源信息简洁一行
- 各章节用 `---` 分隔
- 末尾必须有原文链接

### 三、内容要求

| 要求 | 说明 |
|------|------|
| 翻译完整 | 英文全文翻译为中文，技术术语可保留英文 |
| 无重复 | 摘要/概述只写一次，不重复 |
| 表格化数据 | 规格、议程、发布列表用表格呈现 |
| 结构化要点 | 用标题+列表提炼核心内容 |
| 内容清洗 | 移除网站导航、Cookie提示、页脚等无关内容 |
| 编码正确 | UTF-8编码，无乱码(mojibake) |

### 四、禁止项

| 禁止 | 原因 |
|------|------|
| 原始字幕/转录稿 | 可读性差，重复文本（需清洗后再保存） |
| 完整英文原文 | 冗余，不保留（除非 translated=false） |
| 网站导航/菜单 | 无关内容 |
| Cookie/Footer | 无关内容 |

### 五、分类特定要求

| 分类 | 特定要求 |
|------|---------|
| Company博客 | 概述 → 正文 → 相关资源 |
| GitHub | 项目信息 → README翻译 → 发布记录表格 |
| Academic | 摘要 → 引言 → 方法 → 结果 → 结论 |
| Conference | 概述 → 内容总结 → 完整文字稿 → 原文链接 |
| Benchmark | 平台简介 → 评测结果表格 → 相关资源 |

### 六、内容总结要求

#### 关键信息类型

阅读完整内容时，提取以下通用类型的关键信息：

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

2. **[主题]**：[关键内容]

...

**关键发布/数据**（如有）

| 项目 | 说明 | 时间 |
|------|------|------|
| xxx | xxx | xxx |
```

#### 检查清单

- 是否提取了所有产品发布/技术更新？
- 是否包含具体数据和数字？
- 是否标注时间线？
- 是否提及重要案例？
- 是否逐段检查确认无遗漏？

---

## 翻译模块
- 使用MiniMax API via curl subprocess（避免Windows编码问题）
- 跳过短内容（<10字符）
- 中文内容保留原文
- max_tokens >= 500避免截断
