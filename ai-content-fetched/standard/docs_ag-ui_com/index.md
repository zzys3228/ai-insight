---
title: ​The Agent–User Interaction (AG-UI) Protocol
source: docs.ag-ui.com
url: https://docs.ag-ui.com
category: standard
---
# ​The Agent–User Interaction (AG-UI) Protocol

# Agent–User Interaction (AG-UI) 协议

AG-UI 是一个**开放的**、**轻量级的**、**基于事件的**协议，用于标准化 AI 代理如何连接到面向用户的应用程序。

AG-UI 被设计为面向用户的应用程序与任何代理后端之间的通用双向连接。它专为简单性和灵活性而设计，标准化了代理状态、UI 意图和用户交互如何在您的模型/代理运行时与面向用户的前端应用程序之间流动——使应用程序开发者能够快速交付可靠的、可调试的、用户友好的代理功能，同时专注于应用程序需求，避免复杂的临时连接。

---

## 代理协议

**对 "A2UI" 和 "AG-UI" 感到困惑？** 这是可以理解的！尽管命名相似，但它们完全不同，且可以很好地协同工作。A2UI 是一种[生成式 UI 规范](./concepts/generative-ui-specs)——允许代理交付 UI 组件，而 AG-UI 是代理↔用户交互协议——将代理前端连接到任何代理后端。[了解更多](https://copilotkit.ai/ag-ui-and-a2ui)

AG-UI 是三个主流开放[代理协议](./agentic-protocols)之一。

| **层级** | **协议/示例** | **目的** |
| --- | --- | --- |
| **代理 ↔ 用户交互** | **AG-UI (Agent–User Interaction Protocol)** | 开放的、基于事件的连接代理与面向用户应用程序的标准——实现实时、多模态、交互式体验。 |
| **代理 ↔ 工具与数据** | **MCP (Model Context Protocol)** | 开放标准（由 Anthropic 提出），允许代理安全地连接到外部系统——工具、工作流和数据源。 |
| **代理 ↔ 代理** | **A2A (Agent to Agent)** | 开放标准（由 Google 提出），定义了代理如何在分布式代理系统中协调和共享工作。 |

---

## 构建模块（当前与即将推出）

**流式聊天**

用于响应式多轮会话的实时令牌和事件流，支持取消和恢复。

**多模态**

类型化附件和实时媒体（文件、图像、音频、转录文本）；支持语音、预览、注释和溯源。

**生成式 UI，静态**

在应用程序控制下将模型输出渲染为稳定的、类型化的组件。

**生成式 UI，声明式**

用于受限 UI 组件的小型声明式语言...

*原文: https://docs.ag-ui.com*