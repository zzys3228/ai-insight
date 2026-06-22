---
title: **Translation:**

WebMCP 使用收藏集保持井井有条 根据您的偏好保存和分类内容。
source: developer.chrome.com
url: https://developer.chrome.com/docs/ai/webmcp
date: 2026-06-22
category: standard/developer.chrome
translated: true
fetched_at: 2026-06-22T19:06:46.560334
---
# **Translation:**

WebMCP 使用收藏集保持井井有条 根据您的偏好保存和分类内容。

**来源**: developer.chrome.com | **日期**: 2026-06-22

---

# 翻译

主页
文档
Chrome 上的 AI
WebMCP

Alexandra Klepper
GitHub
Bluesky

发布时间：2026年5月18日，最后更新：2026年6月9日

发布时间：2026年5月18日，最后更新：2026年6月9日

WebMCP
是一个
拟议的 Web 标准，用于帮助您为 AI
代理
构建和公开结构化工具。WebMCP 提供 JavaScript 并
标注 HTML 表单元素，使代理能够准确了解如何与
页面功能进行交互，以支持用户体验。这可以显著提高
代理操作的性能和可靠性。

AI 代理是一项较新的技术。它们可以帮助用户更好地完成
高度复杂和技术性的任务。WebMCP 为代理任务完成提供更高的准确性，
可以作为渐进式增强功能添加。

概述
Web
扩展
Chrome 状态
意向
GitHub
原始试用
查看
实验意向

## 为什么选择 WebMCP？

WebMCP 可以帮助您弥合 Web 应用程序与代理之间的差距，
通过提供交互规则来提高效率、可靠性和任务完成度。网站不是让代理查看元素
（如按钮或字段）来理解其目的，而是声明元素的目的，
以确保其被正确使用。

这比操作更可靠，因为操作可能有许多步骤，并且每个步骤都会
给代理留下解释的空间。

网站可以通过定义一个
工具
来共享明确的目的，例如搜索或购买。工具在您的网页上可见地执行，
以便用户相信任务按预期完成。这也可以保持您的品牌和
以人为中心的设计选择完整。

WebMCP 支持：

**发现**
：页面向代理注册工具的标准方式，例如
checkout
或
filter_results
。
**JSON Schema**
：输入和预期输出的明确定义，减少幻觉或误解。
**状态**
：当前页面上下文的共同理解，使代理知道有哪些资源可以实时操作。

我们的目标是构建任何具有代理功能的浏览器都可以
实现并受益的 API，以便用户可以更轻松地完成任务。您可以在
GitHub
上关注此过程。

## 使用案例

您可以在 Web 上通过多种方式使用 WebMCP。例如：

**帮助您的客户获得支持**
。如果您向客户提供软件，您可能有一个复杂的支持流程来解答
许多不同的问题。您可以使用 WebMCP 帮助代理更快地导航到正确的表单，
并用用户提供的信息填写字段。
**改进旅行预订**
。帮助代理以更少的步骤预订复杂的多城市和多乘客行程。

某些操作可能是敏感的，例如进行购买。您可以包含一个
命令来请求用户与确认对话框进行交互。

实际上，您的工具可以完成以下任务：

**填写结构化表单**
：构建一个
submit_application
工具来帮助代理将
从与用户的对话中收集的数据正确映射到表单字段。例如，您可以区分
字段是需要全名还是单独的名和姓。
**支持以人为本界面中的代理交互**
：某些字段是
为人用户设计的，但代理可能无法理解。您可以构建一个
date_pick
工具，允许在预订或活动预订中进行复杂的日期和时间选择。
**更快的应用程序调试**
：您可以在开发者设置页面上构建一个
run_diagnostics
工具，
以便代理可以触发隐藏在嵌套菜单后面的修复。

您的使用案例缺失了吗？或者您有想要分享的
关于 WebMCP 的想法？加入
早期预览计划
并分享您的反馈。

## 开始使用

从 Chrome 149 开始加入
WebMCP 原始试用
。了解更多关于如何
开始使用原始试用
的信息。

### 本地 WebMCP

WebMCP 可作为 Chrome 标志用于本地开发：

1. 打开 Chrome 并导航到
chrome://flags/#enable-webmcp-testing
2. 将标志设置为
Enabled
。
3. 重新启动 Chrome 以应用更改。

### 使用 WebMCP API

您可以使用两个 API 来设置网站工具：

**命令式 API**
：使用标准 JavaScript 定义不同类型的
工具，例如表单输入、导航工具、状态
管理或其他功能。
**声明式 API**
：向标准
HTML 表单添加标注以创建 WebMCP 工具。

## 局限性

虽然 WebMCP 旨在使代理和人类的复杂任务更简单，但仍有一些
局限性：

**需要浏览上下文**
：由于工具调用在 JavaScript 中处理，
必须打开浏览器标签页或 webview 以提供可见界面和
浏览器上下文。换句话说，不支持代理或辅助工具在无头状态下调用工具。
**复杂界面的更多开销**
：如果您的网站高度复杂，
您可能需要重构或添加 JavaScript 来处理应用程序和界面状态。
**工具可发现性**
：客户端和浏览器必须直接访问网站才能
知道它是否有可调用的工具。

## 安全和权限

WebMCP API 受源隔离要求和权限策略的限制。

### 源隔离

WebMCP 仅在
源隔离
文档中可用。这确保文档的源在工具的整个生命周期中保持稳定。

如果文档启用了
document.domain
（例如，通过使用
Origin-Agent-Cluster: ?0
HTTP 头），WebMCP API 将被禁用。

### 权限策略

两个 API 都受
tools
权限策略的限制。
该策略默认为
self
，允许在顶级和同源上下文中注册工具，
并在跨源 iframe 中禁用它。

要在跨源 iframe 中允许 WebMCP 工具，请将
allow="tools"
属性添加到 iframe。

## 演示

涵盖命令式和声明式实现的演示示例
可用：

**WebMCP zaMaker**
使用 WebMCP 命令式 API。
**旅行演示（React）**
使用 WebMCP 命令式 API。
**Le Petit Bistro 演示**
使用 WebMCP 声明式 API。

您也可以在
GitHub
上查看和探索演示源代码。

## 使用检查器扩展模拟代理聊天

安装
Model Context Tool Inspector 扩展
来体验代理并查看 WebMCP 工具如何
在实时演示或您自己的应用程序中工作。使用自然语言提示来确定代理
是否按预期与 WebMCP 工具交互。

使用扩展，您可以：

查看页面上注册了哪些工具，方法是监控 WebMCP API。
手动调用工具并执行函数。
验证您的 JSON Schema 是否正确定义，以及浏览器是否能够解析
工具期望的数据。
查看工具返回的结构化输出或错误消息，以确保它们写得清晰
且格式正确，以便代理能够理解。

使用自然语言与代理交谈，看看它是否能正确识别
并调用适当的 WebMCP 工具。您的提示默认发送到
gemini-3-flash-preview
模型。

## 参与并分享反馈

WebMCP 正在积极讨论中，未来可能会有变化。如果您
尝试这些 API 并有反馈，我们非常乐意听取。

阅读
WebMCP 概述
，
提出问题并参与讨论。
加入
WebMCP 原始试用
阅读
WebMCP 最佳实践
。
在
Chrome 状态
上查看 Chrome 的实现。
阅读我们的
WebMCP 工具安全指南
和
最佳实践
。
加入早期预览计划
以抢先了解新 API 并访问我们的邮件列表。
如果您对 Chrome 的实现有反馈，请提交
Chromium bug
。

除非另有说明，否则本页内容采用
Creative Commons Attribution 4.0 License
许可，代码示例采用
Apache 2.0 License
许可。有关详细信息，请参阅
Google Developers Site Policies
。Java 是 Oracle 和/或其附属公司的注册商标。

最后更新于 2026-06-09 UTC。

*原文请访问 [developer.chrome.com](https://developer.chrome.com/docs/ai/webmcp)*