---
title: AG-UI 概述
source: docs.ag-ui.com
url: https://docs.ag-ui.com
date: 2026-06-22
category: standard/docs.ag-ui
translated: true
fetched_at: 2026-06-22T17:52:28.820358
---
# AG-UI 概述

**来源**: docs.ag-ui.com | **日期**: 2026-06-22

---

# 翻译

在本页

Agent-User 交互 (AG-UI) 协议
Agentic 协议
构建模块（当前和即将推出）
为什么 Agentic 应用需要 AG-UI
用户界面代理的需求
AG-UI 实践
支持的集成
直连 LLM
Agent 框架 - 合作伙伴
Agent 框架 - 第一方
Agent 框架 - 社区
Agent 交互协议
基础设施 / 部署
规范（标准）
SDK
客户端
快速开始
探索 AG-UI
资源
贡献
支持和反馈

用户界面代理的需求

直连 LLM
Agent 框架 - 合作伙伴
Agent 框架 - 第一方
Agent 框架 - 社区
Agent 交互协议
基础设施 / 部署
规范（标准）
SDK
客户端

Agentic 协议

层级
协议 / 示例
目的
Agent ↔ 用户交互
AG-UI
（Agent-User 交互协议）
开放的、基于事件的连接标准，将 Agent 与用户界面应用相连——实现实时、多模态、交互式体验。
Agent ↔ 工具和数据
MCP
（模型上下文协议）
开放标准（由 Anthropic 发起），让 Agent 能够安全地连接到外部系统——工具、工作流和数据源。
Agent ↔ Agent
A2A
（Agent 到 Agent）
开放标准（由 Google 发起），定义了 Agent 在分布式 Agentic 系统中协调和共享工作的方式。

构建模块（当前和即将推出）

为什么 Agentic 应用需要 AG-UI

用户界面代理的需求

Agent 是
长期运行的
并且
流式传输中间结果——通常跨越多轮会话。
Agent 是
非确定性的
可以
非确定性控制应用界面
。
Agent 同时混合
结构化和非结构化输入输出
（例如：文本和语音，以及工具调用和状态更新）。
Agent 需要用户交互式
组合
：例如，它们可能调用子 Agent，通常是递归的。
以及更多……

AG-UI 实践

支持的集成

直连 LLM

框架
状态
AG-UI 资源
直连 LLM
支持中
文档

Agent 框架 - 合作伙伴

框架
状态
AG-UI 资源
LangGraph
支持中
文档
、演示
CrewAI
支持中
文档
、演示

Agent 框架 - 第一方

框架
状态
AG-UI 资源
Microsoft Agent Framework
支持中
文档
、演示
Google ADK
支持中
文档
、演示
AWS Strands Agents
支持中
文档
、演示
AWS Bedrock AgentCore
支持中
文档
Mastra
支持中
文档
、演示
Pydantic AI
支持中
文档
、演示
Agno
支持中
文档
、演示
LlamaIndex
支持中
文档
、演示
AG2
支持中
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
支持中
文档
合作伙伴

基础设施 / 部署

平台
状态
AG-UI 资源
集成
Amazon Bedrock AgentCore
支持中
文档
第一方

规范（标准）

框架
状态
AG-UI 资源
Oracle Agent 规范
支持中
文档
、演示

SDK

SDK
状态
AG-UI 资源
集成
Kotlin
支持中
入门指南
社区
Golang
支持中
入门指南
社区
Dart
支持中
入门指南
社区
Java
支持中
入门指南
社区
Rust
支持中
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
支持中
入门指南
第一方
终端 + Agent
支持中
入门指南
社区
React Native
需要帮助
GitHub 源码
社区

快速开始

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

支持和反馈

对于与 AG-UI 规范、SDK 或文档（开源）相关的错误报告和功能请求，请
创建 GitHub issue
对于关于 AG-UI 的讨论或问答，请加入
Discord 社区

本页对您有帮助吗？

*原文请访问 [docs.ag-ui.com](https://docs.ag-ui.com)*