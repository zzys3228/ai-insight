---
title: AG-UI 概述
source: docs.ag-ui.com
url: https://docs.ag-ui.com
date: 2026-06-22
category: standard/docs.ag-ui
translated: true
fetched_at: 2026-06-22T20:17:24.523636
---
# AG-UI 概述

**来源**: docs.ag-ui.com | **日期**: 2026-06-22

---

在此页面上

Agent–用户交互（AG-UI）协议
Agentic 协议
构建块（当前和即将推出）
为什么 Agentic 应用需要 AG-UI
对面向用户的代理的要求
AG-UI 实际应用
支持的集成
直连 LLM
Agent 框架 - 合作
Agent 框架 - 第一方
Agent 框架 - 社区
Agent 交互协议
基础设施/部署
规范（标准）
SDK
客户端
快速入门
探索 AG-UI
资源
贡献
支持与反馈

对面向用户的代理的要求

直连 LLM
Agent 框架 - 合作
Agent 框架 - 第一方
Agent 框架 - 社区
Agent 交互协议
基础设施/部署
规范（标准）
SDK
客户端

Agentic 协议

层级
协议/示例
用途
Agent ↔ 用户交互
AG-UI
（Agent–用户交互协议）
开放的、基于事件的标准，将代理连接到面向用户的应用——实现实时、多模态、交互式体验。
Agent ↔ 工具与数据
MCP
（模型上下文协议）
开放标准（由 Anthropic 发起），让代理安全地连接到外部系统——工具、工作流和数据源。
Agent ↔ Agent
A2A
（Agent 间协议）
开放标准（由 Google 发起），定义代理如何在分布式 Agentic 系统中协调和共享工作。

构建块（当前和即将推出）

为什么 Agentic 应用需要 AG-UI

对面向用户的代理的要求

代理是
长期运行
的，并且
流式输出中间工作结果——通常跨越多轮会话。
代理是
非确定性的
，并且可以
非确定性控制应用 UI
。
代理同时混合
结构化 + 非结构化 IO
（例如文本和语音，以及工具调用和状态更新）。
代理需要用户交互式
组合
能力：例如，它们可能调用子代理，通常是递归的。
还有更多……

AG-UI 实际应用

支持的集成

直连 LLM

框架
状态
AG-UI 资源
直连 LLM
支持
文档

Agent 框架 - 合作

框架
状态
AG-UI 资源
LangGraph
支持
文档
、演示
CrewAI
支持
文档
、演示

Agent 框架 - 第一方

框架
状态
AG-UI 资源
Microsoft Agent Framework
支持
文档
、演示
Google ADK
支持
文档
、演示
AWS Strands Agents
支持
文档
、演示
AWS Bedrock AgentCore
支持
文档
Mastra
支持
文档
、演示
Pydantic AI
支持
文档
、演示
Agno
支持
文档
、演示
LlamaIndex
支持
文档
、演示
AG2
支持
文档
演示
AWS Bedrock Agents
进行中
–

Agent 框架 - 社区

框架
状态
AG-UI 资源
OpenAI Agent SDK
进行中
–
Cloudflare Agents
进行中
–

Agent 交互协议

协议
状态
AG-UI 资源
集成
A2A 中间件
支持
文档
合作

基础设施/部署

平台
状态
AG-UI 资源
集成
Amazon Bedrock AgentCore
支持
文档
第一方

规范（标准）

框架
状态
AG-UI 资源
Oracle Agent Spec
支持
文档
、演示

SDK

SDK
状态
AG-UI 资源
集成
Kotlin
支持
入门指南
社区
Golang
支持
入门指南
社区
Dart
支持
入门指南
社区
Java
支持
入门指南
社区
Rust
支持
入门指南
社区
.NET
进行中
PR
社区
Nim
进行中
PR
社区
Flowise
进行中
GitHub 源码
社区
Langflow
进行中
GitHub 源码
社区

客户端

客户端
状态
AG-UI 资源
集成
CopilotKit
支持
入门指南
第一方
Terminal + Agent
支持
入门指南
社区
React Native
需要帮助
GitHub 源码
社区

快速入门

构建 Agentic 应用

构建新的 AG-UI 集成

构建 AG-UI 兼容客户端

探索 AG-UI

核心架构

事件

资源

使用 Cursor 开发

AG-UI 故障排除

贡献

支持与反馈

对于与 AG-UI 规范、SDK 或文档（开源）相关的错误报告和功能请求，请
创建 GitHub issue
对于关于 AG-UI 的讨论或问答，请加入
Discord 社区

这个页面有帮助吗？

*原文请访问 [docs.ag-ui.com](https://docs.ag-ui.com)*