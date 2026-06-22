---
title: **Translation:**

AITP：智能体交互与事务协议

---

**Notes:**

- **Agent** → 智能体 (commonly used in AI context; alternatively 代理 in more general computing contexts)
- **Interaction** → 交互
- **&** → 与
- **Transaction** → 事务 (in computing/software context, refers to operations/transactions; use 交易 if referring to commercial/financial transactions)
- **Protocol** → 协议
source: aitp.dev
url: https://aitp.dev
date: 2026-06-22
category: standard/aitp.dev
translated: true
fetched_at: 2026-06-22T19:12:08.172733
---
# **Translation:**

AITP：智能体交互与事务协议

---

**Notes:**

- **Agent** → 智能体 (commonly used in AI context; alternatively 代理 in more general computing contexts)
- **Interaction** → 交互
- **&** → 与
- **Transaction** → 事务 (in computing/software context, refers to operations/transactions; use 交易 if referring to commercial/financial transactions)
- **Protocol** → 协议

**来源**: aitp.dev | **日期**: 2026-06-22

---

# 翻译

## 概述

版本：0.1.0

状态：草稿

AITP 是一个正在制定中的规范，我们欢迎评论、反馈和贡献！

我们同时在编写此规范、将 AITP 支持集成到 NEAR AI Hub 中，并构建与 AITP 兼容的智能体——以便在 v1.0 之前根据实际使用情况调整协议设计。

## 引言

AITP 使智能体能够在跨越信任边界的同时进行安全通信，并提供可扩展的结构化交互机制。

试想这样的场景：
您让 AI 助手预订一张飞往迈阿密的机票。您的助手无需手动浏览航空公司网站，而是可以通过标准化协议直接与航空公司的预订智能体通信。您的助手和航空公司智能体交换有关航班选项、乘客详情和支付信息的结构化数据——无论您选择哪家航空公司，都使用相同的协议。

### AITP 的核心优势

**通用通信**：任何兼容 AITP 的智能体都可以相互交互，不受构建者限制
**结构化数据交换**：除文本外，智能体还可以共享 UI 元素、表单和支付请求
**跨越信任边界**：代表不同实体的智能体之间可进行安全交互
**可扩展能力**：通过能力系统可添加新的交互类型

我们设想一个未来：大多数在线交互将由代表个人、企业和政府机构的 AI 智能体执行，彼此之间以及与用户进行通信。这些智能体将结合当前在线服务的规模和成本优势，同时具备人类交互的灵活性和个性化特点。正如 HTTP 和 HTML 使任何网页浏览器都能访问任何网站一样，AITP 为智能体对智能体以及用户对智能体的通信提供了统一标准，无论这些智能体运行在何处或如何构建。

要深入了解 AITP 旨在解决的问题以及我们对智能体交互未来的愿景，请参阅愿景页面。

## 协议概述

AITP 由两部分组成：

1. 用于在聊天线程中与智能体通信的核心协议，灵感来源于 OpenAI Assistant/Threads API 并与之高度兼容。了解更多：
   - 为何使用线程？
   - 线程传输层
   - 线程规范

2. 一组通过聊天线程传输的可扩展能力集，用于表明智能体客户端（即用户界面或其他智能体）支持有用的标准化功能，如多模态输入、生成式 UI、支付和/或人工确认见证。了解更多：
   - 什么是能力？
   - 能力交换
   - 能力列表

这些组件协同工作：智能体通过线程进行通信，线程使用传输层传输，当特定操作需要时通过能力交换结构化数据。

## AITP 与其他方案对比

| 协议类型 | 目的 | 使用场景 | 与 AITP 的关系 |
|---------|------|---------|---------------|
| 多智能体编排框架<br>（CrewAI、Autogen、LangGraph） | 协调同一所有者的智能体 | 内部智能体工作流 | 互补——可用于内部编排，同时使用 AITP 进行外部通信 |
| 服务元数据协议<br>（MCP、Bitte、llms.txt） | 帮助智能体使用现有 API | 访问传统服务 | 互补——服务智能体可在内部使用 MCP，同时对外提供 AITP 接口 |
| 浏览器使用智能体<br>（ChatGPT Operator、Proxy、Rabbit LAM） | 导航现有网站 | 桥接到当前网络 | 过渡性——在 AITP 采用率增长之前有用 |

虽然这些框架和 AITP 都涉及智能体通信，但 AITP 专门解决跨信任边界的交互问题，例如用户的智能体与企业智能体之间的通信。

关于这一主题的更多内容，请参阅愿景页面。

## 如何参与？

**加入我们的 Telegram 社区**：
https://t.me/nearaialpha

**构建更多智能体**：兼容 AITP 的智能体越多，每个智能体就越有用。在 NEAR AI Hub 上构建的智能体支持所有 AITP 功能。

**为更多 AI 智能体框架和客户端构建 AITP 支持**：我们希望每个 AI 智能体框架、托管提供商和聊天 UI 都支持 AITP。

**为协议做出贡献**：在 AITP 代码库上提交 issue、pull request 或讨论。

如果您使用 AI 开发辅助工具，最新的规范已打包为 aitp-repomix.txt，非常适合添加到 AI 的上下文中，让它了解如何使用 AITP。

## 术语表

| 术语 | 定义 |
|------|------|
| 智能体（Agent） | 使用 AI 模拟类人推理以实现特定目标的软件实体 |
| 能力（Capability） | 特定交互类型的标准化消息格式 |
| 线程（Thread） | 两个或多个智能体和/或人类之间的对话 |
| 传输层（Transport） | 在智能体之间传输自然语言或 AITP 消息的机制 |
| 个人助理（Personal Assistant） | 代表用户并代其与服务智能体交互的智能体 |
| 服务智能体（Service Agent） | 代表企业、服务或组织的智能体 |
| 发现智能体（Discovery Agent） | 帮助查找和连接合适服务智能体的智能体 |
| 信任边界（Trust Boundary） | 具有不同安全域或所有者的系统或智能体之间的分隔 |
| 直通模式（Passthrough） | 智能体将 AITP 消息转发到其他已连接的智能体或用户的模式 |

---

**目录**
- 引言
- 协议概述
- AITP 与其他方案对比
- 如何参与？
- 术语表

*原文请访问 [aitp.dev](https://aitp.dev)*