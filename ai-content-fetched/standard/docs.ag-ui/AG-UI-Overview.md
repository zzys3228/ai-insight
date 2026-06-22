---
title: AG-UI Overview
source: docs.ag-ui.com
url: https://docs.ag-ui.com
date: 2026-06-22
category: standard/docs.ag-ui
translated: true
fetched_at: 2026-06-22T18:26:49.229152
---
# AG-UI Overview

**来源**: docs.ag-ui.com | **日期**: 2026-06-22

---


On this page

The Agent–User Interaction (AG-UI) Protocol
Agentic Protocols
Building blocks (today & upcoming)
Why Agentic Apps need AG-UI
The requirements of user‑facing agents
AG-UI in Action
Supported Integrations
Direct to LLM
Agent Framework - Partnerships
Agent Framework - 1st Party
Agent Framework - Community
Agent Interaction Protocols
Infrastructure / Deployment
Specification (standard)
SDKs
Clients
Quick Start
Explore AG-UI
Resources
Contributing
Support and Feedback

The requirements of user‑facing agents

Direct to LLM
Agent Framework - Partnerships
Agent Framework - 1st Party
Agent Framework - Community
Agent Interaction Protocols
Infrastructure / Deployment
Specification (standard)
SDKs
Clients

​
Agentic Protocols

Layer
Protocol / Example
Purpose
Agent ↔ User Interaction
AG-UI
(Agent–User Interaction Protocol)
The open, event-based standard that connects agents to user-facing applications — enabling real-time, multimodal, interactive experiences.
Agent ↔ Tools & Data
MCP
(Model Context Protocol)
Open standard (originated by Anthropic) that lets agents securely connect to external systems — tools, workflows, and data sources.
Agent ↔ Agent
A2A
(Agent to Agent)
Open standard (originated by Google) which defines how agents coordinate and share work across distributed agentic systems.

​
Building blocks (today & upcoming)

​
Why Agentic Apps need AG-UI

​
The requirements of user‑facing agents

Agents are
long‑running
and
stream
intermediate work—often across multi‑turn sessions.
Agents are
nondeterministic
and can
control application UI nondeterministically
.
Agents simultanously mix
structured + unstructured IO
(e.g. text & voice, alongside tool calls and state updates).
Agents need user-interactive
composition
: e.g. they may call sub‑agents, often recursively.
And more…

​
AG-UI in Action

​
Supported Integrations

​
Direct to LLM

Framework
Status
AG-UI Resources
Direct to LLM
Supported
Docs

​
Agent Framework - Partnerships

Framework
Status
AG-UI Resources
LangGraph
Supported
Docs
,
Demos
CrewAI
Supported
Docs
,
Demos

​
Agent Framework - 1st Party

Framework
Status
AG-UI Resources
Microsoft Agent Framework
Supported
Docs
,
Demos
Google ADK
Supported
Docs
,
Demos
AWS Strands Agents
Supported
Docs
,
Demos
AWS Bedrock AgentCore
Supported
Docs
Mastra
Supported
Docs
,
Demos
Pydantic AI
Supported
Docs
,
Demos
Agno
Supported
Docs
,
Demos
LlamaIndex
Supported
Docs
,
Demos
AG2
Supported
Docs
Demos
AWS Bedrock Agents
In Progress
–

​
Agent Framework - Community

Framework
Status
AG-UI Resources
OpenAI Agent SDK
In Progress
–
Cloudflare Agents
In Progress
–

​
Agent Interaction Protocols

Protocol
Status
AG-UI Resources
Integrations
A2A Middleware
Supported
Docs
Partnership

​
Infrastructure / Deployment

Platform
Status
AG-UI Resources
Integrations
Amazon Bedrock AgentCore
Supported
Docs
1st Party

​
Specification (standard)

Framework
Status
AG-UI Resources
Oracle Agent Spec
Supported
Docs
,
Demos

​
SDKs

SDK
Status
AG-UI Resources
Integrations
Kotlin
Supported
Getting Started
Community
Golang
Supported
Getting Started
Community
Dart
Supported
Getting Started
Community
Java
Supported
Getting Started
Community
Rust
Supported
Getting Started
Community
.NET
In Progress
PR
Community
Nim
In Progress
PR
Community
Flowise
In Progress
GitHub Source
Community
Langflow
In Progress
GitHub Source
Community

​
Clients

Client
Status
AG-UI Resources
Integrations
CopilotKit
Supported
Getting Started
1st Party
Terminal + Agent
Supported
Getting Started
Community
React Native
Help Wanted
GitHub Source
Community

​
Quick Start

Build agentic applications

Build new AG-UI integrations

Build AG-UI compatible clients

​
Explore AG-UI

Core architecture

Events

​
Resources

Developing with Cursor

Troubleshooting AG-UI

​
Contributing

​
Support and Feedback

For bug reports and feature requests related to the AG-UI specification, SDKs,
or documentation (open source), please
create a GitHub issue
For discussions or Q&A about AG-UI, please join the
Discord community

Was this page helpful?


*原文请访问 [docs.ag-ui.com](https://docs.ag-ui.com)*