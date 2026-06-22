---
title: **AG-UI 概述**
source: docs.ag-ui.com
url: https://docs.ag-ui.com
date: 2026-06-22
category: standard/docs.ag-ui
translated: true
fetched_at: 2026-06-22T18:57:26.519696
---
# **AG-UI 概述**

**来源**: docs.ag-ui.com | **日期**: 2026-06-22

---

# Agent‑User Interaction (AG‑UI) 协议

## 目录

导航链接：

- Agentic 协议
- 构建模块（当前与即将推出）
- 为什么 Agentic 应用需要 AG-UI
- 用户界面代理的要求
- AG-UI 实际应用
- 支持的集成
- 直连 LLM
- Agent 框架 - 合作伙伴
- Agent 框架 - 第一方
- Agent 框架 - 社区
- Agent 交互协议
- 基础设施 / 部署
- 规范（标准）
- SDK
- 客户端
- 快速开始
- 探索 AG-UI
- 资源
- 贡献指南
- 支持与反馈

---

## Agentic 协议

| 层级 | 协议 / 示例 | 用途 |
|------|------------|------|
| Agent ↔ 用户交互 | **AG-UI**<br>(Agent‑User Interaction Protocol) | 开放的、基于事件的标准，将代理连接到用户面向的应用程序——实现实时、多模态、交互式体验。 |
| Agent ↔ 工具 & 数据 | **MCP**<br>(Model Context Protocol) | 开放标准（由 Anthropic 提出），允许代理安全地连接到外部系统——包括工具、工作流和数据源。 |
| Agent ↔ Agent | **A2A**<br>(Agent to Agent) | 开放标准（由 Google 提出），定义代理如何在分布式代理系统中协调和共享工作。 |

---

## 构建模块（当前与即将推出）

[图示区域]

---

## 为什么 Agentic 应用需要 AG-UI

### 用户界面代理的要求

代理具有以下特点：

- **长期运行**，并且**流式传输中间结果**——通常跨越多轮会话。
- **不确定性**，可以**非确定性地控制应用程序 UI**。
- 同时混合**结构化 + 非结构化输入/输出**（例如文本和语音，以及工具调用和状态更新）。
- 需要用户交互式**组合**：例如，它们可能调用子代理，通常是递归调用。
- 以及更多……

---

## AG-UI 实际应用

[图示区域]

---

## 支持的集成

### 直连 LLM

| 框架 | 状态 | AG-UI 资源 |
|------|------|------------|
| Direct to LLM | 支持 | 文档 |

### Agent 框架 - 合作伙伴

| 框架 | 状态 | AG-UI 资源 |
|------|------|------------|
| LangGraph | 支持 | 文档、Demo |
| CrewAI | 支持 | 文档、Demo |

### Agent 框架 - 第一方

| 框架 | 状态 | AG-UI 资源 |
|------|------|------------|
| Microsoft Agent Framework | 支持 | 文档、Demo |
| Google ADK | 支持 | 文档、Demo |
| AWS Strands Agents | 支持 | 文档、Demo |
| AWS Bedrock AgentCore | 支持 | 文档 |
| Mastra | 支持 | 文档、Demo |
| Pydantic AI | 支持 | 文档、Demo |
| Agno | 支持 | 文档、Demo |
| LlamaIndex | 支持 | 文档、Demo |
| AG2 | 支持 | 文档、Demo |
| AWS Bedrock Agents | 进行中 | – |

### Agent 框架 - 社区

| 框架 | 状态 | AG-UI 资源 |
|------|------|------------|
| OpenAI Agent SDK | 进行中 | – |
| Cloudflare Agents | 进行中 | – |

### Agent 交互协议

| 协议 | 状态 | AG-UI 资源 | 集成 |
|------|------|------------|------|
| A2A Middleware | 支持 | 文档 | 合作伙伴 |

### 基础设施 / 部署

| 平台 | 状态 | AG-UI 资源 | 集成 |
|------|------|------------|------|
| Amazon Bedrock AgentCore | 支持 | 文档 | 第一方 |

### 规范（标准）

| 框架 | 状态 | AG-UI 资源 |
|------|------|------------|
| Oracle Agent Spec | 支持 | 文档、Demo |

### SDK

| SDK | 状态 | AG-UI 资源 | 集成 |
|------|------|------------|------|
| Kotlin | 支持 | 入门指南 | 社区 |
| Golang | 支持 | 入门指南 | 社区 |
| Dart | 支持 | 入门指南 | 社区 |
| Java | 支持 | 入门指南 | 社区 |
| Rust | 支持 | 入门指南 | 社区 |
| .NET | 进行中 | PR | 社区 |
| Nim | 进行中 | PR | 社区 |
| Flowise | 进行中 | GitHub 源码 | 社区 |
| Langflow | 进行中 | GitHub 源码 | 社区 |

### 客户端

| 客户端 | 状态 | AG-UI 资源 | 集成 |
|--------|------|------------|------|
| CopilotKit | 支持 | 入门指南 | 第一方 |
| Terminal + Agent | 支持 | 入门指南 | 社区 |
| React Native | 需要帮助 | GitHub 源码 | 社区 |

---

## 快速开始

- 构建 Agentic 应用程序
- 构建新的 AG-UI 集成
- 构建 AG-UI 兼容客户端

---

## 探索 AG-UI

- 核心架构
- 事件

---

## 资源

- 使用 Cursor 开发
- AG-UI 故障排除

---

## 贡献指南

---

## 支持与反馈

如需报告与 AG-UI 规范、SDK 或文档（开源）相关的错误报告和功能请求，请创建 GitHub Issue。

如需讨论或关于 AG-UI 的问答，请加入 Discord 社区。

---

**这个页面对您有帮助吗？**

*原文请访问 [docs.ag-ui.com](https://docs.ag-ui.com)*