---
title: Simon Willison’s Weblog
source: simonwillison.net
url: https://simonwillison.net
category: person
---
# Simon Willison’s Weblog

# Simon Willison 的博客

=======================

关于 [沙箱隔离 48](/tags/sandboxing/) [生成式 AI 1,838](/tags/generative-ai/) [大语言模型定价 77](/tags/llm-pricing/) [Claude 284](/tags/claude/) [MicroPython 9](/tags/micropython/) [...](/tags/)

**赞助商：** 微软 — Agent 项目在演示与生产之间停滞不前。微软的 MVP 清单可弥合这一差距。[立即试用](https://fandf.co/3POWawQ)

[文章](/entries/) [链接](/blogmarks/) [语录](/quotations/) [笔记](/notes/) [指南](/guides/) [其他](/elsewhere/)
-----------------------------------------------------------------------------------------------------------------------------

### 2026 年 6 月 21 日

### [sqlite-utils 4.0rc1 新增迁移和嵌套事务](/2026/Jun/21/sqlite-utils-40rc1/)

[sqlite-utils](https://sqlite-utils.datasette.io/en/latest/) 是一个结合了 Python 库和 CLI 工具的综合解决方案，用于处理 SQLite 数据库。它在 Python 默认的 [sqlite3 包](https://docs.python.org/3/library/sqlite3.html) 之上提供了大量高级操作，包括对[复杂表转换](https://sqlite-utils.datasette.io/en/latest/cli.html#transforming-tables)的支持、从 [JSON 数据自动创建表](https://sqlite-utils.datasette.io/en/latest/cli.html#inserting-json-data)以及更多功能。

[... [975 字](/2026/Jun/21/sqlite-utils-40rc1/)]

[晚上 11:35](/2026/Jun/21/sqlite-utils-40rc1/ "《sqlite-utils 4.0rc1 新增迁移和嵌套事务》的永久链接") / [迁移](/tags/migrations/)、[项目](/tags/projects/)、[SQLite](/tags/sqlite/)、[sqlite-utils](/tags/sqlite-utils/)、[带注释的发布说明](/tags/annotated-release-notes/)

[发布](/elsewhere/release/)
[sqlite-utils 4.0rc1](https://github.com/simonw/sqlite-utils/releases/tag/4.0rc1)

详见 [sqlite-utils 4.0rc1 新增迁移和嵌套事务](https://simonwillison.net/2026/Jun/21/sqlite-utils-40rc1/)。

[2026 年 6 月 21 日，晚上 11:30](/2026/Jun/21/sqlite-utils/) · [sqlite-utils](/tags/sqlite-utils/)

**[面向 AI Agent 的临时 Cloudflare 账户](https://blog.cloudflare.com/temporary-accounts/)**
（来源：[Hacker News](https://news.ycombinator.com/item?id=48608394)）

公告称这是"面向 AI Agent 的"，但（如同近期的常见情况一样）AI 的噱头其实并非必需，这对其他人来说也是一个有趣的功能。

简要说明：现在你可以创建一个 Cloudflare Workers 项目并运行它，甚至无需创建 Cloudflare 账户：

```
npx wrangler deploy --temporary
```

Cloudflare 会将应用部署到一个新的临时项目中，该项目将保持在线 60 分钟。

我[使用 GPT-5.5 xhigh](https://gist.github.com/simonw/264bd6b8a39fc34c91c9c867454c64b9) 在 Codex Desktop 中[构建了这个测试应用](https://github.com/simonw/cloudflare-redirect-resolver)，提供了一个用于跟踪 HTTP 重定向并返回最终目标的工具。临时部署按预期工作。

运行部署后会输出：

*原文: https://simonwillison.net*