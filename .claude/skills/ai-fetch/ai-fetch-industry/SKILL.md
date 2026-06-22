---
name: ai-fetch-industry
description: 抓取AI行业报告、VC智库、政策报告。覆盖a16z/YCombinator/Gartner/McKinsey等机构的研究报告、 landscape图、年度AI报告等。Use when user mentions /ai-fetch-industry, or asks to fetch VC blogs, research reports, AI landscape, policy documents.
---

# Industry 行业报告抓取 Skill

## Quick Start
- `/ai-fetch-industry` — 抓取所有行业报告源

## 分类
| 分类 | URL数 | 抓取方式 |
|------|-------|---------|
| 8.1 AI VC/投资机构 | ~30 | 博客/报告页 |
| 8.2 智库/政策 | ~20 | 官网/报告页 |
| 8.3 咨询机构 | ~15 | 官网/报告页 |
| 8.4 学术机构 | ~5 | 官网 |

## 抓取内容
- 博客文章/报告摘要
- Landscape图
- 年度AI报告
- 政策文档

## 存储路径
`ai-content-fetched/industry/{type}/{org}/`
