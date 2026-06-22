---
title: The universal.discovery layer for AI agents.
source: dns-aid.org
url: https://dns-aid.org
category: standard
---
# The universal.discovery layer for AI agents.

# IETF草案·开源

AI代理的通用.discovery层。
=============================================

将代理发布到DNS，像网站一样发现它们，并用DNSSEC验证信任。无集中注册表，只有信号。

[立即开始](#quickstart)
[阅读IETF草案](https://datatracker.ietf.org/doc/draft-mozleywilliams-dnsop-dnsaid/)

一键安装完整SDK：

pip
docker
源码

```
pip install "dns-aid[all]"
```

```
docker compose -f tests/integration/bind/docker-compose.yml up -d
```

```
git clone https://github.com/infobloxopen/dns-aid-core.git
```

核心能力
-----------------

DNS-AID协议赋予您的能力。

核心原则

### 无需新基础设施。基于您已有的DNS构建。

DNS-AID是现有SVCB、TXT和TLSA记录之上的命名约定。无新记录类型、无新服务器、无新协议 — 仅使用RFC 9460和RFC 4033中的标准。

规范**RFC 9460**

安全**DNSSEC**

状态**IETF草案**

安全

### DNSSEC信任链

代理记录真实性和完整性的加密证明。

协议

### 协议无关

MCP、A2A、HTTPS以及未来任何通过`alpn`定义的协议。

发现

### 三种发现模式

按名称查找、按能力搜索或爬取域索引。

企业

### 分裂视图DNS

对内外部署不同代理。内置租户隔离。

SDK

### 开源工具包

CLI、Python SDK、MCP服务器。八个后端开箱即用。

性能

### 可缓存且去中心化

DNS自动缓存。无中心API。分布式查找。

DNS-AID命名空间
---------------------

代理记录的确定性、人性化命名模式。

### DNS-AID命名模式

```
_<agent-name>._<protocol>._agents.<your-domain>

示例：
_chatbot._mcp._agents.example.com        MCP聊天机器人
_search._a2a._agents.example.com         A2A搜索代理
_data-cleaner._a2a._agents.acme.com      基于能力的命名
_index._agents.example.com               完整代理索引

多租户：
_analytics._mcp._agents.customer1.saas.com
```

代理记录结构
-------------------------

每个代理都是一条包含机器可读元数据的SVCB记录。

```
_my-agent._mcp._agents.example.com. 3600 IN SVCB 1 agent.example.com. (
    alpn="mcp"                           ; 协议
    port=443                             ; 服务端口
    cap="https://example.com/cap.json"   ; 能力文档
    cap-sha256="abc123..."               ; 完整性哈希
    bap="mcp=1.0,a2a=0.2"                ; 协议版本声明
    policy="https://example.com/policy"  ; 治理URL
    realm="production"                   ; 租户范围
    ipv4hint=192.0.2.1                   ; 地址提示
)
```

`alpn` 通信协议（mcp、a2a、h2）

`port` 服务端口号

`cap` 能力文档URI

`cap-sha256` 防篡改的完整性哈希

`bap` 批量协议版本声明

`policy` 治理和使用策略URL

`realm` 租户或环境范围

`ipv4hint` IPv4地址提示

`ipv6hint` IPv6地址提示

*原文: https://dns-aid.org*