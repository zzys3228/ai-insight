---
title: a2wf.github.io
source: a2wf.github.io
url: https://a2wf.github.io/spec
category: standard
---
# a2wf.github.io

# Agent-to-Web 框架 (A2WF)

Agent-to-Web 框架 (A2WF) 定义了 `siteai.json`，这是一种机器可读的政策文件，网站运营商通过发布它来声明 AI 代理在网站上允许执行、限制执行或禁止执行的操作。`robots.txt` [[ROBOTS-TXT]] 规定了哪些内容可以被*爬取*，`siteai.json` 则规定了代理可以*做什么*：提交表单、完成交易、预约或提取数据。

本规范定义了 `siteai.json` 的文件位置、语法、语义和合规要求，以及支持《欧盟 AI 法案》（特别是第 14、26 和 50 条）下透明度和人类监督义务的字段。

本文档是由 [A2WF 社区组](https://www.w3.org/community/a2wf/) 开发的**正在进行中的工作**。欢迎在 [GitHub 上的 A2WF 规范仓库](https://github.com/a2wf/spec) 提出评论、问题和 Pull 请求。

社区组于 2026 年 3 月 29 日正式启动。这是规范的首个基于 ReSpec 的修订版，其技术内容与仓库中的 [specification-v1.0.md](https://github.com/a2wf/spec/blob/main/spec/specification-v1.0.md) 相同，并根据 [W3C 社区组规范要求](https://www.w3.org/community/reports/reqs/) 进行了重新组织。

## 引言

AI 代理现在以远超传统爬取的方式与网站进行交互。代理填写表单、完成结账、预约、比较价格并代表用户操作账户。现有 Web 标准仅涉及相关问题：

- `robots.txt` [[ROBOTS-TXT]] 规定哪些 URL 可以被爬取，采用二元允许/拒绝模式。它不涉及操作行为。
- IETF AIPREF 表达了对训练和内容重用的偏好。它不管理交互行为。
- Cookie 同意横幅管理人类对客户端追踪，而非自主代理执行的操作。

A2WF 填补了这一空白。网站运营商将 `siteai.json` 文档放置在已知位置，并以结构化形式声明 AI 代理在网站上操作的条件。

### 问题陈述

AI 代理越来越多地与网站进行交互——浏览产品、比较价格、预约、填写表单、提取数据。网站运营商面临一个关键缺口：目前没有标准能让网站运营商以机器可读的方式声明：

- 代理**允许**做什么（读取目录、搜索、比较价格）。
- 代理**禁止**做什么（批量抓取、发布虚假评论、完成未授权的交易）。
- 什么需要**人工验证**（结账、预约、联系表单）。
- 代理必须如何**标识自身**（名称、运营商、目的）。
- 适用哪些**法律条款**（服务条款、管辖权、监管合规）。
- 强制执行哪些**速率限制**（按操作、按分钟、按小时）。

当前的代理端标准（MCP [[MCP]]、A2A [[A2A]]、企业 IAM）从代理运营方的角度管理代理——A2WF 则是从*网站运营商*的角度来管理代理。

*原文: https://a2wf.github.io/spec*