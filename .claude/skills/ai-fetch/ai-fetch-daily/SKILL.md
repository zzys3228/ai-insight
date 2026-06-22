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
