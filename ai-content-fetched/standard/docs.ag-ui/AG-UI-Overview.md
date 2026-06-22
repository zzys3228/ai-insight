---
title: **AG-UI 概述**
source: docs.ag-ui.com
url: https://docs.ag-ui.com
date: 2026-06-22
category: standard/docs.ag-ui
translated: true
fetched_at: 2026-06-22T17:37:00.913283
---
# **AG-UI 概述**

**来源**: docs.ag-ui.com | **日期**: 2026-06-22

---

# 页面内容

## 标题

**Agent–User Interaction (AG-UI) Protocol**

**Agentic Protocols**

**Building blocks (today & upcoming)**

**Why Agentic Apps need AG-UI**

**The requirements of user‑facing agents**

**AG-UI in Action**

**Supported Integrations**

**Direct to LLM**

**Agent Framework - Partnerships**

**Agent Framework - 1st Party**

**Agent Framework - Community**

**Agent Interaction Protocols**

**Infrastructure / Deployment**

**Specification (standard)**

**SDKs**

**Clients**

**Quick Start**

**Explore AG-UI**

**Resources**

**Contributing**

**Support and Feedback**

---

## Agentic Protocols

| 层级 | 协议 / 示例 | 目的 |
|------|-------------|------|
| Agent ↔ User Interaction | **AG-UI** (Agent–User Interaction Protocol) | 一个开放的、基于事件的标准，用于将 Agent 连接到用户面向的应用程序——实现实时、多模态、交互式体验。 |
| Agent ↔ Tools & Data | **MCP** (Model Context Protocol) | 开放标准（由 Anthropic 发起），允许 Agent 安全地连接到外部系统——工具、工作流和数据源。 |
| Agent ↔ Agent | **A2A** (Agent to Agent) | 开放标准（由 Google 发起），定义了 Agent 如何在分布式 Agent 系统中协调和共享工作。 |

---

## Building blocks (today & upcoming)

## Why Agentic Apps need AG-UI

## The requirements of user‑facing agents

Agent 的特点：
- **长期运行**：并**流式传输中间结果**——通常跨越多轮会话。
- **非确定性**：能够**非确定性控制应用程序 UI**。
- Agent 同时混合**结构化 + 非结构化 IO**（例如文本和语音，以及工具调用和状态更新）。
- Agent 需要用户交互式**组合**：例如，它们可能调用子 Agent，通常是递归的。
- 还有更多……

---

## AG-UI in Action

## Supported Integrations

### Direct to LLM

| Framework | Status | AG-UI Resources |
|-----------|--------|------------------|
| Direct to LLM | Supported | Docs |

### Agent Framework - Partnerships

| Framework | Status | AG-UI Resources |
|-----------|--------|------------------|
| LangGraph | Supported | Docs, Demos |
| CrewAI | Supported | Docs, Demos |

### Agent Framework - 1st Party

| Framework | Status | AG-UI Resources |
|-----------|--------|------------------|
| Microsoft Agent Framework | Supported | Docs, Demos |
| Google ADK | Supported | Docs, Demos |
| AWS Strands Agents | Supported | Docs, Demos |
| AWS Bedrock AgentCore | Supported | Docs |
| Mastra | Supported | Docs, Demos |
| Pydantic AI | Supported | Docs, Demos |
| Agno | Supported | Docs, Demos |
| LlamaIndex | Supported | Docs, Demos |
| AG2 | Supported | Docs, Demos |
| AWS Bedrock Agents | In Progress | – |

### Agent Framework - Community

| Framework | Status | AG-UI Resources |
|-----------|--------|------------------|
| OpenAI Agent SDK | In Progress | – |
| Cloudflare Agents | In Progress | – |

### Agent Interaction Protocols

| Protocol | Status | AG-UI Resources | Integrations |
|----------|--------|-----------------|--------------|
| A2A Middleware | Supported | Docs | Partnership |

### Infrastructure / Deployment

| Platform | Status | AG-UI Resources | Integrations |
|----------|--------|-----------------|--------------|
| Amazon Bedrock AgentCore | Supported | Docs | 1st Party |

### Specification (standard)

| Framework | Status | AG-UI Resources |
|-----------|--------|------------------|
| Oracle Agent Spec | Supported | Docs, Demos |

### SDKs

| SDK | Status | AG-UI Resources | Integrations |
|-----|--------|-----------------|--------------|
| Kotlin | Supported | Getting Started | Community |
| Golang | Supported | Getting Started | Community |
| Dart | Supported | Getting Started | Community |
| Java | Supported | Getting Started | Community |
| Rust | Supported | Getting Started | Community |
| .NET | In Progress | PR | Community |
| Nim | In Progress | PR | Community |
| Flowise | In Progress | GitHub Source | Community |
| Langflow | In Progress | GitHub Source | Community |

### Clients

| Client | Status | AG-UI Resources | Integrations |
|--------|--------|-----------------|--------------|
| CopilotKit | Supported | Getting Started | 1st Party |
| Terminal + Agent | Supported | Getting Started | Community |
| React Native | Help Wanted | GitHub Source | Community |

---

## Quick Start

- Build agentic applications
- Build new AG-UI integrations
- Build AG-UI compatible clients

---

## Explore AG-UI

- Core architecture
- Events

---

## Resources

- Developing with Cursor
- Troubleshooting AG-UI

---

## Contributing

## Support and Feedback

对于与 AG-UI 规范、SDK 或文档（开源）相关的错误报告和功能请求，请提交 GitHub Issue。

对于关于 AG-UI 的讨论或问答，请加入 Discord 社区。

---

Was this page helpful?
*此页面对您有帮助吗？*

*原文请访问 [docs.ag-ui.com](https://docs.ag-ui.com)*