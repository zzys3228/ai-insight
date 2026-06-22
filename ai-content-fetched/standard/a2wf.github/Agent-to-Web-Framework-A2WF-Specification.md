---
title: Agent‑to‑Web 框架（A2WF）规范
source: a2wf.github.io
url: https://a2wf.github.io/spec
date: 2026-06-22
category: standard/a2wf.github
translated: true
fetched_at: 2026-06-22T18:53:34.293253
---
# Agent‑to‑Web 框架（A2WF）规范

**来源**: a2wf.github.io | **日期**: 2026-06-22

---

# 代理到Web框架（A2WF）中文翻译

**Agent-to-Web Framework (A2WF)** 定义了

siteai.json

文件，这是一种机器可读的策略文件，网站运营商通过发布该文件来声明允许、限制或禁止AI代理在其网站上执行的操作。与

robots.txt [[ROBOTS-TXT]]

控制可爬取内容不同，

siteai.json

控制代理可以执行的**操作**：提交表单、完成交易、预约，或提取数据。

本规范定义了

siteai.json

的文件位置、语法、语义和合规性要求，以及支持欧盟AI法案（尤其是第14条、第26条和第50条）下透明度和人工监督义务的字段。

本文档是由

A2WF社区组

开发的**工作草案**。欢迎在

GitHub上的A2WF规范仓库

提交评论、问题和拉取请求。

社区组于2026年3月29日启动。这是该规范的第一个基于ReSpec的修订版，对应于仓库中

specification-v1.0.md

的相同技术内容，并重新组织以满足

W3C社区组规范要求

。

## 引言

AI代理现在以远超传统爬取的方式与网站交互。代理填写表单、完成结账、预约、比较价格，并代表用户操作账户。现有Web标准仅处理相关但不同的问题：

- **robots.txt [[ROBOTS-TXT]]** 控制哪些URL可被爬取，采用二元允许/拒绝模式，不涉及操作。
- **IETF AIPREF** 表达对训练和内容重用的偏好，不控制交互行为。
- **Cookie同意横幅** 管理人类对客户端追踪的管理，而非自主代理执行的操作。

A2WF填补了这一空白。网站运营商将

siteai.json

文档放置在知名位置，并以结构化形式声明AI代理在网站上操作的条件。

## 问题陈述

AI代理越来越多地与网站交互——浏览产品、比较价格、预约、填写表单、提取数据。网站运营商面临一个关键缺口：目前没有标准能够让网站运营商以机器可读的方式声明：

- 代理**允许**执行的操作（读取目录、搜索、比较价格）。
- 代理**禁止**执行的操作（批量抓取、发布虚假评论、完成未授权交易）。
- 需要**人工验证**的操作（结账、预约、联系表单）。
- 代理必须如何**标识**自己（名称、运营商、目的）。
- 适用哪些**法律条款**（服务条款、司法管辖、监管合规）。
- 强制执行哪些**速率限制**（按操作、按分钟、按小时）。

现有代理端标准（MCP [[MCP]]、A2A [[A2A]]、企业IAM）从代理运营商的角度管理代理。A2WF通过从**网站运营商**的角度提供管理来填补这一空白。

## 解决方案

### siteai.json

siteai.json

是一种基于JSON的策略文件，由网站运营商提供，以机器可读的形式声明权限、限制、代理标识要求和法律条款。其设计目的是为代理生态系统的网站端提供一个单一、可发现、结构化的产物——在角色上可比拟

robots.txt

[[ROBOTS-TXT]]对爬虫的作用——但表达的是操作而非仅仅是路径。

### 与Schema.org的关系

本规范在适用的情况下使用Schema.org [[SCHEMA-ORG]]词汇来表达站点级概念（WebSite、Organization、ContactPoint），避免重新发明标准术语。它通过引入Schema.org未涵盖的管理结构来补充Schema.org：权限、抓取策略、代理标识、人工验证和法律执行元数据。

AI代理首先使用

siteai.json

获取管理规则，然后使用特定页面上发现的详细Schema.org标记来获取实体信息。

### 与现有标准的关系

| 标准 | 范围 | 与A2WF的关系 |
|------|------|-------------|
| robots.txt | 爬取 | 互补——A2WF通过`discovery.robotsTxt`引用robots.txt。 |
| sitemap.xml | URL列表 | 独立——两个文件可共存。 |
| llms.txt | LLM内容指导 | 互补——A2WF通过`discovery.llmsTxt`引用它。 |
| MCP / A2A | 代理端协议 | 互补——A2WF通过`discovery.mcpEndpoint`/`discovery.a2aAgentCard`引用端点。 |
| Schema.org | 页面级实体词汇 | A2WF在适用时复用Schema.org术语。 |

### 多语言处理方法

siteai.json

是一个单一语言的规范文档，通过

identity.inLanguage

使用BCP 47标签标识。多语言网站应通过站点基础设施（独立来源、Accept-Language协商或区域性siteai.json变体）提供替代语言版本，而非在单个文件内嵌入多语言内容。

## 预期受众

- **网站运营商**：发布面向AI代理的管理策略。
- **AI代理运营商**：实施合规的消费者行为。
- **工具开发者**：为siteai.json文件构建生成器、验证器或审计工具。
- **合规和法律团队**：将声明的策略映射到监管框架。
- **监管机构和合规官员**：了解siteai.json如何实现机器可读的AI管理。

## 约定和术语

格式为JSON [[RFC8259]]，UTF-8编码。本规范使用的数据类型为：String、Object、Array、Boolean、Integer。URL是有效的URI，最好是规范的和绝对的。语言标签遵循IETF BCP 47 [[BCP47]]。日期时间值遵循ISO 8601 / [[RFC3339]]。Schema.org词汇从

https://schema.org/

[[SCHEMA-ORG]]引用。

本文档中的关键词

**MUST**（必须）、

**MUST NOT**（禁止）、

**REQUIRED**（必需）、

**SHOULD**（应该）、

**SHOULD NOT**（不应该）、

**RECOMMENDED**（推荐）、

**MAY**（可以）和

**OPTIONAL**（可选）

应按照BCP 14 [[RFC2119]] [[RFC8174]]中的描述进行解释，但仅当它们以全大写形式出现时（如此处所示）才适用。

本文档定义了两类产品：

**发布站点**（发布

siteai.json

的网站运营商）和

**消费代理**（检索并执行该文件的AI代理）。每个产品的合规性标准在其各自章节中陈述。

## 文件位置和发现

### 首选方法：根URL

发布站点**必须**从其来源根部的知名位置提供

siteai.json

：

```
https://example.com/siteai.json
```

该文件**必须**使用HTTP状态

200 OK

和

Content-Type: application/json

提供服务。

### 替代方案：robots.txt指令

发布站点**可以**使用以下非标准但通用的指令在

robots.txt

中声明其

siteai.json

的位置：

```
SiteAI: https://example.com/siteai.json
```

### 替代方案：HTML <link>标签

发布站点**可以**在文档头部包含

<link>

元素：

```html
<link rel="siteai" href="https://example.com/siteai.json">
```

### 替代方案：知名URI

发布站点**可以**通过知名URI约定 [[RFC8615]]在

/.well-known/siteai.json

提供文件以保持兼容性。当根位置和知名位置同时存在时，它们**必须**指向相同内容。

### 优先级和检索

消费代理**应该**按以下顺序检索

siteai.json

，在首次成功检索时停止：

1. 根URL（`/siteai.json`）
2. 知名URI（`/.well-known/siteai.json`）
3. 首页中的HTML `<link rel="siteai">`
4. robots.txt中的`SiteAI:`指令

### 文件服务要求

- 文件**必须**通过HTTPS提供服务。
- 文件**应该**使用合理的`Cache-Control`头可缓存（例如`max-age=3600`）。
- 文件**应该**最多几百KB；消费代理**可以**截断或拒绝大于1 MiB的响应。

## 格式规范——必需元素

# 顶层结构

## A. siteai.json 文档结构

document MUST consist of a single JSON
对象 [[RFC8259]]。根对象必须包含：

**specVersion**

(String)：必需。

必须为

"1.0"

。

**identity**

(Object)：必需。

核心网站标识。

**permissions**

(Object)：必需。

Agent 访问策略。

根对象应包含：

**@context**

(String)：推荐。

"https://schema.org"

。

**agentIdentification**

(Object)：推荐。

**scraping**

(Object)：推荐。

根对象可包含

可选治理扩展

中定义的其他成员。
消费型 Agent 必须忽略任何无法识别的成员。

---

## identity 对象（必需）

提供关于发布网站的核心标识和上下文信息。适用时，字段使用 Schema.org WebSite 词汇。

| 字段 | 类型 | 需求 | 描述 |
|------|------|------|------|
| @type | String | 推荐 | "WebSite"。Schema.org 类型声明。 |
| domain | String | 必需 | 规范绝对 URL（schema:WebSite.url）。 |
| name | String | 必需 | 官方站点/品牌名称（schema:WebSite.name）。 |
| description | String | 可选 | 一般网站描述（schema:WebSite.description）。 |
| purpose | String | 推荐 | 简洁的 AI 聚焦网站主要目标和受众描述。A2WF 专用。 |
| inLanguage | String | 必需 | 主要语言，使用 BCP 47 标签。 |
| category | String | 推荐 | 网站类型，例如："e-commerce"、"healthcare"、"government"、"saas"。 |
| jurisdiction | String | 推荐 | 法律管辖区域，例如："EU"、"US"、"US-CA"、"CH"。 |
| applicableLaw | Array<String> | 可选 | 具体法规，例如：["EU AI Act", "GDPR"]。 |
| contact | String | 可选 | 政策相关问题的电子邮件。 |

---

## permissions 对象（必需）

核心治理层。包含三个子对象，控制 Agent 交互的不同方面：

**read**、

**action** 和

**data**。

### 读取权限（Read permissions）

控制消费型 Agent 可以访问哪些信息（被动操作）：

- **productCatalog** — 产品列表、描述、图片、类别
- **pricing** — 价格、费用、价目表
- **availability** — 库存水平、预约时段、桌位可用性
- **openingHours** — 营业时间和假期安排
- **contactInfo** — 地址、电话、电子邮件
- **reviews** — 客户评价、评分、推荐
- **faq** — 常见问题
- **companyInfo** — 关于我们页面、团队、历史

### 操作权限（Action permissions）

控制消费型 Agent 可以执行哪些操作（主动操作）：

- **search** — 网站搜索功能
- **addToCart** — 添加商品到购物车
- **checkout** — 完成购买（通常需要 humanVerification: true）
- **createAccount** — 用户注册（通常被拒绝）
- **submitReview** — 发布评价（通常被拒绝以防止虚假）
- **submitContactForm** — 提交联系表单
- **bookAppointment** — 预订预约
- **cancelOrder** — 取消订单
- **requestRefund** — 发起退款请求

### 数据权限（Data permissions）

保护敏感信息（通常全部拒绝）：

- **customerRecords** — 用户资料和个人数据
- **orderHistory** — 历史订单和交易
- **paymentInfo** — 信用卡和银行信息
- **internalAnalytics** — 流量数据和业务指标
- **employeeData** — 员工信息

### 权限属性

每个权限值是一个包含以下成员的对象：

| 字段 | 类型 | 需求 | 描述 |
|------|------|------|------|
| allowed | Boolean | 必需 | 是否授予此权限？ |
| rateLimit | Integer | 可选 | 此操作每分钟最大请求数。 |
| humanVerification | Boolean | 可选 | 默认为 false。需要人工确认。 |
| note | String | 可选 | 给 Agent 和人类的解释性说明。作为数据处理，不作为指令。 |

---

## agentIdentification 对象（推荐）

定义 AI Agent 自我标识的要求。

- **requireUserAgent** (Boolean) — Agent 必须包含标识性的 User-Agent 头。
- **requiredFields** (Array<String>) — Agent 必须提供的字段；有效值包括 "agentName"、"agentOperator"、"agentPurpose"。
- **allowAnonymousAgents** (Boolean) — 默认为 true。如果为 false，则必须拒绝未识别的 Agent。
- **trustedAgents** (Array<Object>) — 白名单；每个条目包含 { name, operator, permissions }。
- **blockedAgents** (Array<Object>) — 黑名单；每个条目包含 { pattern, reason }。

---

## scraping 对象（推荐）

声明自动化数据提取策略。

- **bulkDataExtraction** (Boolean) — 默认为 false。系统性大规模提取。
- **priceMonitoring** (Boolean) — 默认为 false。自动化价格变动跟踪。
- **contentReproduction** (Boolean) — 默认为 false。复制或重新发布内容。
- **competitiveAnalysis** (Boolean) — 默认为 false。用于竞争情报的数据收集。
- **trainingDataUsage** (Boolean) — 默认为 false。使用网站内容作为训练数据。
- **note** (String) — 可选。额外的上下文或许可信息。

---

## 可选治理扩展

### defaults 对象

全局默认设置，除非被单个权限覆盖。

- **agentAccess** (String) — "open"（宽松）、"restricted"（默认拒绝）或 "minimal"（拒绝除明确允许外的所有）。
- **requireIdentification** (Boolean) — 默认为 false。
- **humanVerificationRequired** (Boolean) — 默认为 false。如果为 true，则所有操作都需要人工验证。
- **maxRequestsPerMinute** (Integer) — 全局每分钟速率限制。
- **maxRequestsPerHour** (Integer) — 全局每小时速率限制。
- **respectRobotsTxt** (Boolean) — 默认为 true。

### humanVerification 对象

定义敏感操作的人工介入要求。

- **methods** (Array<String>) — 可接受的方法："redirect-to-browser"、"email-confirmation"、"sms-otp"。
- **requiredFor** (Array<String>) — 需要人工验证的操作名称。
- **note** (String) — 额外的人类可读说明。

### legal 对象

引用服务条款和监管框架。

- **termsUrl** (String) — 推荐。AI 专用服务条款的 URL。
- **complianceNote** (String) — 可选。人类可读的合规声明。
- **dataRetention** (String) — 可选。Agent 数据保留规则。
- **euAiActCompliance** (Object) — 可选。EU AI Act 特定元数据，支持《欧盟人工智能法案》(EU) 2024/1689 [[EU-AI-ACT]]：
  - **transparencyRequired** (Boolean) — Agent 必须标识自身为 AI。
  - **riskClassification** (String) — "minimal"、"limited"、"high" 或 "unacceptable"。
  - **humanOversightMandatory** (Boolean)。

### discovery 对象

链接到补充网络资源。

- **mcpEndpoint** (String) — MCP 服务器卡的 URL。
- **a2aAgentCard** (String) — A2A Agent 卡的 URL。
- **robotsTxt** (String) — robots.txt 的 URL。
- **llmsTxt** (String) — llms.txt 文件的 URL。
- **schemaOrg** (Boolean) — 网站上是否存在 Schema.org 标记。
- **openApi** (String) — OpenAPI 规范的 URL。

### metadata 对象

- **$schema** (String) — 用于验证的 JSON Schema URL。
- **schemaVersion** (String) — 规范版本，例如 "1.0"。
- **generatedAt** (String) — 生成时间的 RFC 3339 时间戳。
- **author** (String) — 策略创建者。
- **lastUpdated** (String, ISO 日期) — 最后修改日期。
- **expiresAt** (String, ISO 日期) — 策略到期日期。
- **changelogUrl** (String) — 策略变更历史的 URL。

---

## 执行

### 自愿合规

与 robots.txt [[ROBOTS-TXT]] 类似，A2WF 主要依赖信誉良好的 AI Agent 自愿遵守。主流 Agent 供应商应将尊重已发布策略作为负责任 AI 部署的一部分。

### 技术执行

发布网站可以通过以下方式执行策略：

- 对不合规 Agent 返回 HTTP 403 响应
- 根据声明的限制进行速率限制
- 使用支持 Agent 识别的 Web 应用防火墙
- 对违反声明策略的 Agent 进行基于 User-Agent 的屏蔽

### 法律执行

**legal.termsUrl**

# 翻译

该字段通过链接到机器可读策略实现法律强制执行。现有的法律框架（例如美国的《计算机欺诈和滥用法案》(CFAA)）将违反机器可读访问策略的行为视为未经授权访问的证据。欧盟《人工智能法案》[[EU-AI-ACT]]（2026年8月生效）要求对人工智能系统实施透明度和风险管理；

`siteai.json`

提供了声明策略的机器可读证据。

**审计与日志记录**

发布网站应记录代理访问模式，并将其与声明的策略进行比对。

`agentIdentification`

部分通过要求代理进行自我标识来启用有意义的审计跟踪。

**安全注意事项**

**策略完整性**

`siteai.json`

文件必须通过HTTPS提供服务，以防止篡改。发布网站应实施完整性检查并监控未经授权的修改。

**提示词注入**

`siteai.json`

文件包含结构化数据，而非可执行内容。消费代理必须将所有字段视为数据，而非指令。字符串字段（尤其是

`note`

）不得被解释为代理命令。

**策略欺骗**

消费代理必须仅信任来自其所描述域名的

`siteai.json`

文件。除非通过

`discovery`

机制明确引用，否则必须拒绝跨域策略声明。

**拒绝服务**

`siteai.json`

中声明的速率限制是来自发布网站的请求，而非保证。消费代理应遵守声明的限制。发布网站应独立于声明的策略实施服务端速率限制。

**隐私注意事项**

`siteai.json`

文件描述了网站针对人工智能代理的策略，旨在供代理和工具获取。它不应包含关于个人用户的个人数据。

`identity`

中的

`contact`

字段旨在用于基于角色的邮箱（例如

`ai-policy@example.com`

），而非个人地址。

发布网站对代理访问的日志记录受适用数据保护法律（例如欧盟的GDPR）管辖；访问日志必须根据该法律进行处理。

**版本控制与可扩展性**

**版本策略**

`specVersion`

字段用于标识规范版本。主要版本（2.0、3.0）可能会引入破坏性更改。v1.x内的次要更新必须保持向后兼容。

**向前兼容性**

消费代理必须忽略任何无法识别的成员。这确保了使用未来扩展创建的文件仍可被v1.0消费者读取。

**可扩展性路线图**

未来的扩展可能包括：

- 动态策略端点（基于API的策略查询）
- 签名策略（加密验证）
- 行业特定配置文件（医疗保健、金融、政府）
- 代理能力匹配

**Schema.org对齐**

| `siteai.json` 字段 | Schema.org 等价物 |
|---|---|
| `@context` | JSON-LD context |
| `identity.@type` | `schema:WebSite` |
| `identity.name` | `schema:WebSite.name` |
| `identity.description` | `schema:WebSite.description` |
| `identity.inLanguage` | `schema:WebSite.inLanguage` |
| `identity.domain` | `schema:WebSite.url` |
| `legal.termsUrl` | `schema:WebSite.publishingPrinciples` |
| `permissions.*` | A2WF扩展（无Schema.org等价物） |
| `scraping.*` | A2WF扩展 |
| `agentIdentification.*` | A2WF扩展 |
| `humanVerification.*` | A2WF扩展 |

A2WF扩展了Schema.org而非重新定义它。没有Schema.org等价物的字段代表了A2WF独有的新型治理概念。

**文件生态系统**

| 文件 | 用途 | 起始年份 |
|---|---|---|
| `/robots.txt` | 抓取权限 | 1994 |
| `/sitemap.xml` | 搜索引擎URL列表 | 2005 |
| `/llms.txt` | 大语言模型内容指南 | 2024 |
| `/.well-known/mcp.json` | MCP服务器发现 | 2024 |
| `/siteai.json` | AI代理访问治理（A2WF） | 2025 |

每个文件都有其独特的用途。

`siteai.json`

是位于所有这些文件之上的治理层。

`siteai.json`

的

`discovery`

部分可以引用这些文件中的每一个，为AI代理创建一个统一的入口点。

**完整示例：电子商务商店**

```json
{
  "@context": "https://schema.org",
  "specVersion": "1.0",
  "identity": {
    "@type": "WebSite",
    "domain": "https://www.example-store.com",
    "name": "Example Online Store",
    "description": "Premium widgets and gadgets",
    "purpose": "E-commerce store selling premium widgets to consumers in the EU.",
    "inLanguage": "en",
    "category": "e-commerce",
    "jurisdiction": "EU",
    "applicableLaw": ["EU AI Act", "GDPR"],
    "contact": "ai-policy@example-store.com"
  },
  "defaults": {
    "agentAccess": "restricted",
    "requireIdentification": true,
    "maxRequestsPerMinute": 30,
    "respectRobotsTxt": true
  },
  "permissions": {
    "read": {
      "productCatalog": { "allowed": true, "rateLimit": 60 },
      "pricing": { "allowed": true },
      "availability": { "allowed": true, "rateLimit": 30 },
      "reviews": { "allowed": true, "rateLimit": 20 },
      "faq": { "allowed": true }
    },
    "action": {
      "search": { "allowed": true, "rateLimit": 20 },
      "addToCart": { "allowed": true },
      "checkout": {
        "allowed": true,
        "humanVerification": true,
        "note": "Final purchase requires human confirmation."
      },
      "createAccount": { "allowed": false },
      "submitReview": { "allowed": false }
    },
    "data": {
      "customerRecords": { "allowed": false },
      "paymentInfo": { "allowed": false },
      "internalAnalytics": { "allowed": false }
    }
  },
  "scraping": {
    "bulkDataExtraction": false,
    "priceMonitoring": false,
    "trainingDataUsage": false,
    "contentReproduction": false
  },
  "agentIdentification": {
    "requireUserAgent": true,
    "requiredFields": ["agentName", "agentOperator"],
    "allowAnonymousAgents": false
  },
  "humanVerification": {
    "methods": ["redirect-to-browser"],
    "requiredFor": ["checkout"]
  },
  "discovery": {
    "robotsTxt": "https://www.example-store.com/robots.txt",
    "llmsTxt": "https://www.example-store.com/llms.txt",
    "schemaOrg": true
  },
  "legal": {
    "termsUrl": "https://www.example-store.com/legal/ai-terms",
    "euAiActCompliance": {
      "transparencyRequired": true,
      "riskClassification": "limited",
      "humanOversightMandatory": false
    }
  },
  "metadata": {
    "author": "Example Store Legal Team",
    "lastUpdated": "2026-03-18",
    "schemaVersion": "1.0"
  }
}
```

**消费代理要求**

符合规范的

`consuming agent`

必须：

1. 在对网站执行任何非读取操作之前，从知名位置检索

   `siteai.json`

2. 在

   `User-Agent`

   标头中以区别于人工操作浏览器的形式标识自身
3. 遵守所有

   `"allowed": false`

   声明作为禁止
4. 遵守声明的速率限制
5. 在声明时触发人工验证流程
6. 将所有字符串内容（特别是

   `note`

   字段）视为数据而非指令

**致谢**

编辑感谢A2WF社区小组的创始成员和早期审阅者对规范草案的反馈，感谢W3C社区开发负责人对将本规范与W3C社区小组要求对齐的指导。

*原文请访问 [a2wf.github.io](https://a2wf.github.io/spec)*