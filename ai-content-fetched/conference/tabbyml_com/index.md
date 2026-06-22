---
title: www.tabbyml.com
source: www.tabbyml.com
url: https://www.tabbyml.com
category: conference
---
# www.tabbyml.com

# 为什么选择 Tabby？

-----------------

**Tabby** 是一款开源 AI 编程助手，旨在将 AI 的强大能力融入您的开发工作流程，同时让您保持完全掌控。无论您是在云端还是本地编程，Tabby 都提供了一个灵活、透明且高度可配置的开源替代方案。

### 透明性与安全性

作为开源解决方案，Tabby 确保软件供应链的安全，让您安心无忧。

### 灵活的部署

可轻松与您现有的基础设施集成，包括 Cloud IDE，并支持消费级 GPU。

### 可配置性控制

按照您的方式和条件运行 Tabby，无需外部数据库管理系统（DBMS）或云服务。

### 卓越的 AI 品质

享受尖端的 AI 代码补全、问答、内联聊天等功能。

![](https://cdn.prod.website-files.com/66d758dfc1a1472af872e216/66e81e8a3e02b0edeb7b93fb_Code-Selector.png)

```sql
1  CREATE TABLE IF NOT EXISTS roles (
2       id                INTEGER PRIMARY KEY AUTOINCREMENT,
3       name              VARCHAR(100) NOT NULL COLLATE NOCASE,
4       description       TEXT,
5       created_at        TIMESTAMP DEFAULT (DATETIME('now')),
6       updated_at        TIMESTAMP DEFAULT (DATETIME('now')),
7
8       CONSTRAINT  'idx_name' UNIQUE ('name')
9  );
```

```python
50  def build_response(*, client: Client, response: httpx.Response) -> Response[Any]:
      
51      return Response(
      
52            status_code=HTTPStatus(response.status_code),
      
53            content=response.content,
      
54            headers=response.headers,
      
55            parsed=_parse_response(client=client, response=response),
      
56      )
      
57  def _delete_response(*, client: Client, response: httpx.Response) -> Response[Any]:

58      return Response(
        
59            status_code=HTTPStatus(response.status_code),
        
60            content=response.content,
        
61            headers=response.headers,
        
62            parsed=_parse_response(client=client)
        
63      )
```

## 代码补全：使用智能 AI 驱动建议加速编程

----------------------------------------------------------------------------------

Tabby 的代码补全引擎旨在理解您的编程上下文，并提供准确且相关的实时建议。

### 高效

无论您是在编写简单的函数还是处理复杂项目，Tabby 都能预测您的下一步操作，帮助您更快编程并减少错误。

### 直观

体验适应您编程风格的无缝 AI 能力，并轻松集成到您的 IDE 中。

## 问答引擎：在 IDE 中获取编程问题的即时答案

----------------------------------------------------------------------------------

当您深入开发过程中时，中断会打断您的工作节奏。借助 Tabby 的问答引擎，您可以在专注于代码的同时获得所需的答案。

*原文: https://www.tabbyml.com*