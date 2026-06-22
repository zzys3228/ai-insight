# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

AI趋势洞察系统 - 追踪AI公司动态、学术论文、机器人进展、会议信息等各类信息源。核心文件是 `ai-news-sources.md`（单一真实来源）。

## Core Files

| 文件 | 说明 |
|------|------|
| `ai-news-sources.md` | 所有AI信息源的SSOT（Single Source of Truth） |
| `.claude/skills/ai-source-*/` | 源发现技能（11个） |
| `.claude/skills/ai-fetch-*/` | 内容抓取技能（10个） |
| `ai-content-fetched/` | 抓取后的内容存储目录 |

## AI Source Skills (ai-source-*)

使用 `/ai-source-{category}` 调用：

| Skill | 用途 |
|-------|------|
| `/ai-source-company` | AI大公司四维信息源 |
| `/ai-source-academic` | 学术论文/顶会 |
| `/ai-source-media` | Newsletter/播客/媒体 |
| `/ai-source-robot` | 机器人/具身智能 |
| `/ai-source-person` | AI人物动态 |
| `/ai-source-benchmark` | 评测榜单 |
| `/ai-source-opensource` | 开源社区 |
| `/ai-source-conference` | 大会信息 |
| `/ai-source-industry` | VC/智库/政策报告 |
| `/ai-source-standard` | Agent协议/标准 |

## ai-news-sources.md 格式规则

### 编号规则
- 第一章独立编号1-N
- 第二章及以后无编号
- ❌ 禁止全局连续编号

### URL类型规则
- 公司/产品：产品页 > 官方博客 > 公司首页
- 人物：个人X/Twitter > 个人博客 > 公司官方X
- 白皮书：必须是PDF格式

### 状态标记
| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ✅302→ | 跳转后可达（更新为最终URL） |
| ⚠️403 | 需代理 |
| ⚠️404 | 不存在 |

## URL验证命令

```bash
# 直连测试
curl -sI --max-time 10 {URL}

# 代理测试
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}

# 跟随跳转检查
curl -sI --max-time 10 -L {URL}
```

## 公司追踪四维

每个大公司按以下维度检查：

| 维度 | 信源 |
|------|------|
| 产品线 | 产品页/API文档/Changelog |
| 官方博客 | 公司博客RSS |
| 年度大会 | 大会主页/演讲回放 |
| 开源项目 | GitHub仓库 |

## 大公司门槛

- 海外：估值≥100亿美金
- 国内：估值≥500亿RMB

## 分类边界

- 机器人公司 → ai-source-robot
- 学术/研究院 → ai-source-academic
- 中小型AI创业公司 → 不追踪（除非达到大公司门槛）

## 内容抓取流程

```
/ai-fetch-daily              # 增量抓取所有源
/ai-fetch-daily --full       # 全量抓取
/ai-fetch-daily --{category} # 按分类抓取
```

抓取顺序：GitHub > Company > Academic > Media > Person > Benchmark > Robot > Standard > Conference > Industry
