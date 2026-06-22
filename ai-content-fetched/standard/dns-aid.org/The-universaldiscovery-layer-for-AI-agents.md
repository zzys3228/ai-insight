---
title: **AI智能体的 universal.discovery 层**

备选译法：

- **面向AI智能体的 universal.discovery 层**
- **AI代理的 universal.discovery 层次**
source: dns-aid.org
url: https://dns-aid.org
date: 2026-06-22
category: standard/dns-aid.org
translated: true
fetched_at: 2026-06-22T19:13:47.808317
---
# **AI智能体的 universal.discovery 层**

备选译法：

- **面向AI智能体的 universal.discovery 层**
- **AI代理的 universal.discovery 层次**

**来源**: dns-aid.org | **日期**: 2026-06-22

---

# IETF 草案 · 开源

AI 代理的通用发现层。

将代理发布到 DNS，像网站一样发现它们，并使用 DNSSEC 验证信任。无中心化注册表，只有信号。

立即开始

阅读 IETF 草案

一键安装完整 SDK：

pip

docker

源码

pip install "dns-aid[all]"

复制

docker compose -f tests/integration/bind/docker-compose.yml up -d

复制

git clone https://github.com/infobloxopen/dns-aid-core.git

复制

# 核心能力

DNS-AID 基于 DNS-AID 协议为您提供的能力。

## 核心原则

零新基础设施。

基于您已有的 DNS 构建。

DNS-AID 是现有 SVCB、TXT 和 TLSA 记录之上的命名约定。无新记录类型，无新服务器，无新协议——仅使用 RFC 9460 和 RFC 4033 中的标准。

规范

RFC 9460

安全

DNSSEC

状态

IETF 草案

安全

DNSSEC 信任链

代理记录的密码学证明，确保真实且未被篡改。

协议

协议无关

MCP、A2A、HTTPS，以及通过 alpn 的任何未来协议。

发现

三种发现模式

按名称查找、按能力搜索，或爬取域名索引。

企业

分裂视图 DNS

向内部和外部提供不同的代理。内置租户隔离。

SDK

开源工具包

CLI、Python SDK、MCP 服务器。八个后端开箱即用。

性能

可缓存且去中心化

DNS 自动缓存。无中心化 API。分布式查询。

## DNS-AID 命名空间

代理记录的确定性、可读命名模式。

### DNS-AID 命名模式

```
_<agent-name>._<protocol>._agents.<your-domain>
```

示例：

| 代理名称 | 协议 | 全限定域名 | 说明 |
|---------|------|-----------|------|
| _chatbot | _mcp | _agents.example.com | MCP 聊天机器人 |
| _search | _a2a | _agents.example.com | A2A 搜索代理 |
| _data-cleaner | _a2a | _agents.acme.com | 基于能力的 |
| _index | — | _agents.example.com | 完整代理索引 |

多租户：

```
_analytics._mcp._agents.customer1.saas.com
```

## 代理记录解析

每个代理都是一个包含机器可读元数据的 SVCB 记录。

```
_my-agent._mcp._agents.example.com.
3600 IN SVCB 1 agent.example.com. (
    alpn="mcp"                      ; 通信协议 (mcp, a2a, h2)
    port=443                        ; 服务端口
    cap="https://example.com/cap.json" ; 能力文档 URI
    cap-sha256="abc123..."          ; 防篡改完整性哈希
    bap="mcp=1.0,a2a=0.2"           ; 批量协议版本声明
    policy="https://example.com/policy" ; 治理和使用策略 URL
    realm="production"              ; 租户或环境范围
    ipv4hint=192.0.2.1              ; 地址提示以减少额外查询
)
```

| 参数 | 说明 |
|-----|------|
| alpn | 通信协议 (mcp, a2a, h2) |
| port | 服务端口号 |
| cap | 能力文档 URI |
| cap-sha256 | 防篡改检测的完整性哈希 |
| bap | 批量协议版本声明 |
| policy | 治理和使用策略 URL |
| realm | 租户或环境范围 |
| ipv4hint | 地址提示以减少额外查询 |

## 工作原理

从发布到连接的四个步骤。

**1. 发布您的代理**

使用 CLI 或 SDK 在您域名的 _agents 区域下创建 SVCB 记录，包含端点、协议和能力。

**2. DNSSEC 签署区域**

您的权威 DNS 签署记录，创建从根到您代理的密码学信任链。

**3. 代理发现您的**

远程代理通过名称、能力类型或完整域名索引查询 DNS 获取您的 SVCB 记录。

**4. 验证并连接**

发现者验证 DNSSEC + DANE，然后通过您 SVCB 记录中的协议直接连接。

## 快速入门

使用 dns-aid-core Python 包快速启动和运行。

### CLI

Python

MCP 服务器

Docker

#### 安装

```bash
pip install "dns-aid[all]"          # 全部功能
pip install "dns-aid[cli]"          # 仅 CLI
pip install "dns-aid[route53]"       # AWS 后端
pip install "dns-aid[cloudflare]"   # Cloudflare 后端
pip install "dns-aid[nios]"          # Infoblox NIOS 后端
pip install "dns-aid[mcp]"           # MCP 服务器
```

#### 发布

```bash
dns-aid publish \
  --name my-chatbot \
  --domain example.com \
  --protocol mcp \
  --endpoint agent.example.com \
  --capability chat
```

#### 发现

```bash
dns-aid discover example.com
dns-aid discover example.com --json
dns-aid discover example.com --use-http-index
```

#### 验证与诊断

```bash
dns-aid verify _my-chatbot._mcp._agents.example.com
dns-aid doctor --domain example.com
```

#### 调用代理

```bash
# 列出 MCP 代理上的工具
dns-aid list-tools https://mcp.example.com/mcp

# 调用特定工具
dns-aid call https://mcp.example.com/mcp analyze_security \
  --arguments '{"domain":"example.com"}'

# 向 A2A 代理发送消息（先发现）
dns-aid message "What is DNS-AID?" \
  -d ai.infoblox.com \
  -n security-analyzer
```

#### 管理

```bash
# 从 DNS 中删除代理
dns-aid delete -n my-chatbot -d example.com -p mcp
```

### Python

#### 发布

```python
from dns_aid import publish

result = await publish(
    name="my-chatbot",
    domain="example.com",
    protocol="mcp",
    endpoint="agent.example.com",
    capabilities=["chat", "summarize"],
    description="通用聊天代理",
)
print(f"已发布: {result.agent.fqdn}")
print(f"记录:   {result.records_created}")
```

#### 发现

```python
import asyncio
from dns_aid import discover, verify

async def main():
    result = await discover("example.com")
    for agent in result.agents:
        print(f"  {agent.name} — {agent.protocol} @ {agent.endpoint_url}")

    check = await verify("_my-agent._mcp._agents.example.com")
    print(f"DNSSEC 有效: {check.dnssec_valid}")

asyncio.run(main())
```

#### 发现后调用

```python
from dns_aid import discover, invoke

async def find_and_call():
    result = await discover("partner.com", protocol="mcp")
    agent = result.agents[0]
    resp = await invoke(agent, method="tools/list")
    print(f"延迟: {resp.signal.invocation_latency_ms}ms")
    print(f"数据: {resp.data}")
```

### MCP 服务器

```bash
# stdio 传输 (Claude Desktop)
dns-aid-mcp --transport stdio

# HTTP 传输
dns-aid-mcp --transport http --port 8000
```

#### 工具

| 工具 | 描述 |
|-----|------|
| publish_agent_to_dns | 发布代理的端点和能力 |
| discover_agents_via_dns | 通过 DNS 在任意域名上查找代理 |
| verify_agent_dns | 验证代理的 DNSSEC、DANE 和端点 |
| call_agent_tool | 调用已发现 MCP 代理上的工具 |
| list_agent_tools | 列出远程 MCP 代理上的可用工具 |
| send_a2a_message | 向已发现 A2A 代理发送消息 |
| diagnose_environment | 检查 DNS-AID 配置和连接性 |
| delete_agent_from_dns | 删除代理的 DNS 记录 |
| list_published_agents | 列出您自己 DNS 区域中的代理 |
| list_agent_index | 读取域名的代理索引记录 |
| sync_agent_index | 从实时记录重建域名的代理索引 |

### 本地游乐场 — 无需凭据

```bash
git clone https://github.com/infobloxopen/dns-aid-core.git
cd dns-aid-core
pip install "dns-aid[cli]"

docker compose -f tests/integration/bind/docker-compose.yml up -d

# 为本地 BIND9 配置 .env（参见 .env.example）
dns-aid publish --name test-agent --domain test.dns-aid.local \
  --protocol mcp --endpoint localhost --backend ddns \
  --capability chat

dns-aid discover test.dns-aid.local
```

## 三种发现代理的方式

全部通过标准 DNS 查询。无需特殊客户端。

**定向查找**

按名称查询

您知道代理。直接查询其 SVCB 记录获取端点详情。

```
dig SVCB _chatbot._mcp._agents.example.com
```

**能力搜索**

按功能搜索

通过功能查找代理。查询代理区域下的能力类型。

```
dig SVCB _data-cleaner._a2a._agents.example.com
```

**索引爬取**

爬取目录

从已知索引入口点获取域名的完整代理清单。

```
dig TXT _index._agents.example.com
```

## 架构

跨组织代理发现流程。

组织 1（发现方）

组织 2（发布方）

# DNS-AID 技术文档中文翻译

## 架构图

```
+----------------+                                    +-------------------+
  |   AI 代理      |---- 1. DNS SVCB 查询 ------------->|   权威 DNS         |
  |   (org1)       |     _search._a2a._agents.org2.com   |   DNS 服务器      |
  |                |<--- 2. SVCB 响应 -----------------|   (DNSSEC签名)     |
  +-------+--------+     alpn="a2a" port=443          +-------------------+
          |               ipv4hint=198.51.100.10
          |
          |   3. DNSSEC + DANE 验证
          |
          |   4. 直接 A2A / MCP / HTTPS 连接
          v
  +----------------+
  |   AI 代理      |   运行于 198.51.100.10:443
  |   (org2)       |
  +----------------+
```

## DNS 服务提供商

| 缩写 | 名称 | 说明 |
|------|------|------|
| R53 | Amazon Route 53 | AWS 托管区域 |
| CF | Cloudflare | 全球边缘 DNS |
| IB | Infoblox NIOS | 企业 DDI |
| UD | Infoblox UDDI | 通用 DDI 云 |
| AZ | Azure DNS | 微软云 |
| GC | Google Cloud DNS | GCP 托管 |
| NS1 | NS1 | 托管 DNS 和流量调度 |
| RFC | RFC 2136 DDNS | 任何符合标准的 DNS |
| B9 | BIND9 | 自托管和本地开发 |

## 策略执行

### 概述

发现机制将代理引导到正确的端点。策略帮助部署表达谁可以调用、需要什么认证，以及应用哪些运行时检查，而无需将主页变成协议备忘录。

### 当前状态

### 运行时策略现状

DNS-AID 学习材料已描述了运行时策略评估，包括发现元数据、认证要求和部署特定的策略包（如 `policy.json`）。

### 层次结构

调用方、目标方和基础设施层面

团队可以从调用方端和目标端检查开始，然后仅在其 DNS 或流量基础设施支持的情况下添加解析器或代理执行。

### 扩展功能

本地检查模式

某些部署可以添加本地请求或响应检查，用于 PII（个人身份信息）、提示注入或数据处理检查，而无需通过中央策略服务路由流量。

### 强制执行内容

本文档记录的策略示例包括：

- 调用方域名限制
- 必需的认证类型
- 可用性时间窗口
- 速率限制
- DNSSEC 敏感决策
- CEL 表达式以实现更紧密的运行时检查

### 重要性

您可以从当前的运行时策略模型开始，稍后再扩展到解析器或代理执行，而不是在第一天就承诺采用重量级的集中式安全架构。

## 开放策略指南

### 继续交互式课程

## 使用场景

真实世界的代理发现场景。

### 企业场景

跨组织代理协作

内部代理查询 DNS 以发现合作伙伴的授权代理，验证委托，并自动发起安全会话。

### 学术场景

研究联盟

大学在其自己的域名下发布代理。合作者在尊重机构信任边界的同时按能力发现服务。

### SaaS 场景

多租户平台

SaaS 提供商在租户特定区域下托管代理。DNS 区域委托为每个客户提供自然的隔离和作用域发现。

### 边缘场景

物联网和边缘代理

受限设备上的轻量级代理受益于 DNS 的分布式、可缓存架构，以及用于低延迟引导的 SVCB 提示。

## 安全与信任

建立在互联网久经考验的安全基础设施之上。

### DNSSEC

公共区域强制要求。加密信任链防止欺骗和篡改。

### DANE / TLSA

将 TLS 证书绑定到 DNS 记录。无需证书颁发机构信任问题即可进行端点验证。

### 域名控制验证

代理通过 DCV TXT 记录证明授权。适用于临时代理的范围化、可验证授权。

### 能力完整性

cap-sha256 哈希确保能力文档未被篡改。

### 分裂视野 DNS

内部代理对外界不可见。为不同的解析器上下文提供不同的视图。

### 作用域授权

TXT 记录定义针对特定服务和操作的每个代理角色和权限。

## 常见问题

### DNS-AID 是否需要更改我的 DNS 服务器？

不需要。DNS-AID 不引入新的 DNS 记录类型、操作码或消息格式。它是在现有 SVCB、TXT 和 TLSA 记录之上的命名约定。任何支持 DNSSEC 和 SVCB 的 DNS 服务器都可以工作。

### 它支持哪些代理通信协议？

DNS-AID 与协议无关。代理在 SVCB alpn 字段中声明协议。SDK 支持 MCP、A2A 和 HTTPS。新协议通过使用新的 alpn 标识符即可工作。

### 这与集中式代理注册中心有何不同？

DNS-AID 是去中心化的。每个组织在其自己的域名下发布记录。没有中央注册中心，没有供应商锁定，没有单点故障。

### 支持哪些 DNS 提供商？

AWS Route 53、Cloudflare、Infoblox NIOS 和 RFC 2136。包含用于本地开发的 Docker BIND9 操场。后端架构可扩展。

### 是否需要 DNSSEC？

对于公共代理区域，是的。没有 DNSSEC，发现代理就无法验证记录是真实的。对于私有区域，网络级控制可能就足够了。

### 如果我的 DNS 提供商不支持自定义 SVCB 参数怎么办？

SDK 自动处理此问题。自定义参数会优雅地降级到带有 dnsaid_ 前缀的 TXT 记录。所有元数据都会无损保留。

### 我可以在没有云账户的情况下试用吗？

可以。仓库包含一个 Docker Compose 设置，带有位于 `tests/integration/bind/` 的本地 BIND9 服务器。运行：

```bash
docker compose -f tests/integration/bind/docker-compose.yml up -d
```

并在本地计算机上使用 DDNS 后端进行完全实验。

---

## 开始发现代理

安装 SDK，发布您的第一个代理，并在开放的通用 AI 发现层上构建。

**在 GitHub 上查看**

**阅读 IETF 草案**

*原文请访问 [dns-aid.org](https://dns-aid.org)*