---
title: 模型上下文协议 (MCP) 技术规范
source: modelcontextprotocol.io
url: https://modelcontextprotocol.io/introduction
date: 2026-06-22
category: standard/mcp
translated: true
fetched_at: 2026-06-22T09:30:17.608035
---

# 模型上下文协议 (MCP) 技术规范

**来源**: Model Context Protocol | **日期**: 2026-06-22

---

## 简介

MCP（Model Context Protocol，模型上下文协议）是一个开放源码协议标准，旨在实现 AI 应用与外部数据源、工具和服务之间的无缝连接。作为 AI 应用的"USB-C 接口"，MCP 提供了标准化方式，让 AI 系统能够安全、受控地访问外部资源。

---

## 核心架构

### 协议设计原则

MCP 基于以下核心设计原则：

1. **开放性**：协议规范完全开放，任何人都可以实现
2. **安全性**：强调本地优先，所有数据保留在本地环境
3. **可扩展性**：模块化设计，支持自定义工具和数据源
4. **标准化**：统一接口，简化 AI 应用与外部系统的集成

### 架构组件

MCP 协议包含三个核心组件：

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   主机应用   │ ←→  │   MCP协议   │ ←→  │  本地服务器  │
│ (AI应用)    │     │  (通信层)   │     │ (数据源/工具) │
└─────────────┘     └─────────────┘     └─────────────┘
```

**主机应用 (Host)**：
- AI 应用的运行容器（如 Claude Desktop）
- 管理连接和权限
- 处理用户交互

**MCP 协议层**：
- 标准化通信格式
- JSON-RPC 消息传递
- 请求/响应管理

**本地服务器 (Server)**：
- 提供数据访问能力
- 定义可用工具
- 运行在用户本地环境

---

## 协议消息格式

### JSON-RPC 2.0

MCP 使用 JSON-RPC 2.0 作为消息格式：

**请求消息**：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {}
}
```

**响应消息**：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "filesystem_read",
        "description": "读取本地文件",
        "inputSchema": {
          "type": "object",
          "properties": {
            "path": {"type": "string"}
          }
        }
      }
    ]
  }
}
```

**错误消息**：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32600,
    "message": "Invalid Request"
  }
}
```

---

## 核心能力

### 1. 资源访问 (Resources)

资源是 AI 应用可以读取的外部数据：

**资源定义**：
```typescript
interface Resource {
  uri: string;           // 资源标识符
  name: string;          // 资源名称
  mimeType?: string;    // MIME类型
  description?: string; // 资源描述
}
```

**资源类型**：
- 文件系统文件
- 数据库记录
- API 响应
- 环境变量
- 配置信息

**操作示例**：
```json
// 列出资源
{"method": "resources/list"}

// 读取资源
{"method": "resources/read", "params": {"uri": "file:///path/to/file"}}

// 订阅资源更新
{"method": "resources/subscribe", "params": {"uri": "file:///path/to/file"}}
```

### 2. 工具调用 (Tools)

工具是 AI 应用可以执行的外部函数：

**工具定义**：
```typescript
interface Tool {
  name: string;         // 工具名称
  description: string;  // 工具描述
  inputSchema: object;  // 输入参数模式
}
```

**执行流程**：
1. AI 应用识别需要执行的操作
2. 调用 MCP `tools/call` 方法
3. 本地服务器执行实际操作
4. 返回执行结果

**示例工具**：
```json
{
  "name": "database_query",
  "description": "执行SQL查询",
  "inputSchema": {
    "type": "object",
    "properties": {
      "sql": {
        "type": "string",
        "description": "SQL查询语句"
      }
    },
    "required": ["sql"]
  }
}
```

### 3. 提示词模板 (Prompts)

提示词模板是可复用的提示词定义：

**模板定义**：
```typescript
interface Prompt {
  name: string;           // 模板名称
  description?: string;    // 模板描述
  arguments?: Argument[]; // 参数定义
  template: string;        // 提示词模板
}
```

**使用示例**：
```json
{
  "name": "code_review",
  "description": "代码审查模板",
  "arguments": [
    {"name": "language", "required": true},
    {"name": "code", "required": true}
  ],
  "template": "请审查以下{{language}}代码：\n{{code}}"
}
```

---

## 安全模型

### 本地优先原则

MCP 强调数据本地化：

1. **数据不离开本地**：所有数据访问通过本地服务器
2. **用户控制**：用户明确授权每个数据源
3. **最小权限**：仅请求必要的数据访问权限

### 权限管理

**连接权限**：
- 用户需明确批准每个 MCP 服务器连接
- 可以随时撤销权限
- 权限粒度可配置

**数据权限**：
- 按资源类型设置访问权限
- 工具调用需要明确授权
- 敏感操作需要二次确认

---

## 传输层

### 标准传输

MCP 支持多种传输机制：

**1. 标准输入输出 (stdio)**
```json
{
  "transport": "stdio",
  "command": "npx",
  "args": ["-y", "@modelcontextprotocol/server-filesystem"]
}
```

**2. HTTP+SSE (Server-Sent Events)**
```json
{
  "transport": "http",
  "url": "http://localhost:8080/mcp",
  "headers": {
    "Authorization": "Bearer token"
  }
}
```

### 消息分帧

**JSON-RPC 消息编码**：
- 使用 UTF-8 编码
- 消息之间使用换行符分隔
- 支持批处理多条消息

---

## 实现示例

### Python 服务器实现

```python
from mcp.server import Server
from mcp.types import Tool, Resource

app = Server("example-server")

@app.list_tools()
async def list_tools() -> list[Tool]:
    return [
        Tool(
            name="get_weather",
            description="获取指定城市的天气",
            inputSchema={
                "type": "object",
                "properties": {
                    "city": {"type": "string"}
                }
            }
        )
    ]

@app.call_tool()
async def call_tool(name: str, arguments: dict) -> str:
    if name == "get_weather":
        city = arguments["city"]
        return f"{city}的天气是晴天，25°C"
    raise ValueError(f"Unknown tool: {name}")
```

### JavaScript 客户端实现

```javascript
import { Client } from "@modelcontextprotocol/sdk";

const client = new Client({
  name: "example-client",
  version: "1.0.0"
});

await client.connect({
  transport: "stdio",
  command: "npx",
  args: ["-y", "@modelcontextprotocol/server-filesystem"]
});

const tools = await client.listTools();
console.log("Available tools:", tools);

const result = await client.callTool({
  name: "read_file",
  arguments: { path: "/example.txt" }
});
```

---

## 生态系统

### 官方服务器

MCP 提供官方维护的服务器实现：

| 服务器 | 功能 | 安装命令 |
|--------|------|---------|
| filesystem | 本地文件访问 | `npx -y @modelcontextprotocol/server-filesystem` |
| github | GitHub API集成 | `npx -y @modelcontextprotocol/server-github` |
| slack | Slack消息发送 | `npx -y @modelcontextprotocol/server-slack` |
| postgres | PostgreSQL查询 | `npx -y @modelcontextprotocol/server-postgres` |

### 社区贡献

大量社区维护的服务器实现：
- AWS, GCP, Azure 云服务集成
- 数据库连接（MySQL, MongoDB, Redis）
- API 集成（Notion, Figma, Google Calendar）
- 开发工具（Git, Docker, Kubernetes）

---

## 版本历史

| 版本 | 日期 | 主要更新 |
|------|------|---------|
| 1.0 | 2024-11 | 初始规范发布 |
| 1.1 | 2025-03 | 增加提示词模板支持 |
| 1.2 | 2025-06 | 改进安全模型 |
| 1.3 | 2025-09 | SSE传输支持 |

---

## 相关资源

- [官方文档](https://modelcontextprotocol.io)
- [GitHub仓库](https://github.com/modelcontextprotocol)
- [规范 specification](https://spec.modelcontextprotocol.io)
- [SDK文档](https://github.com/modelcontextprotocol/sdk)

---

*原文请访问 [https://modelcontextprotocol.io](https://modelcontextprotocol.io)*
