---
title: WebMCPStay organized with collectionsSave and categorize content based on your preferences.
source: developer.chrome.com
url: https://developer.chrome.com/docs/ai/webmcp
category: standard
---
# WebMCPStay organized with collectionsSave and categorize content based on your preferences.

# 翻译

* [首页](https://developer.chrome.com/)
* [文档](https://developer.chrome.com/docs)
* [Chrome 上的 AI](https://developer.chrome.com/docs/ai)
* [WebMCP](https://developer.chrome.com/docs/ai/agents)

WebMCP

使用收藏夹保持井井有条

根据您的偏好保存和分类内容。
================================================================================================

![Alexandra Klepper](https://web.dev/images/authors/alexandraklepper.jpg)

Alexandra Klepper

[GitHub](https://github.com/alexandrascript)
[Bluesky](https://bsky.app/profile/alexandrascript.com)

发布于：2026年5月18日，最后更新：2026年6月9日

[WebMCP](https://github.com/webmachinelearning/webmcp?tab=readme-ov-file) 是一个拟议的 Web 标准，旨在帮助您构建和暴露结构化工具供 AI [代理](https://web.dev/articles/ai-agents) 使用。WebMCP 提供 JavaScript API 并为 HTML 表单元素添加注解，使代理能够精确了解如何与页面功能进行交互，从而提升用户体验。这可以显著提高代理操作的性能和可靠性。

**关键术语：** *操作（Actuation）* 是指代理模拟手动鼠标点击和文本输入的行为，仿佛它是与您的网站互动的人类用户。这些可以是单一任务，如点击链接或在表单中输入内容，也可以是复杂任务，如完成购买。

AI 代理是一项较新的技术。它们可以帮助人类用户更好地完成高度复杂和技术性的任务。WebMCP 为代理任务完成提供更高的准确性，并且可以作为渐进式增强来添加。

| 解释文档 | Web | 扩展程序 | Chrome 状态 | 意图 |
| --- | --- | --- | --- | --- |
| [GitHub](https://github.com/webmachinelearning/webmcp) | [源试验](https://developer.chrome.com/origintrials/#/register_trial/4163014905550602241) |  | [查看](https://chromestatus.com/feature/5117755740913664) | [实验意图](https://groups.google.com/a/chromium.org/g/blink-dev/c/gmYffo5WOE8/m/OJxuQRP3AAAJ) |

为什么选择 WebMCP？
-------------------

WebMCP 可以帮助您弥合 Web 应用程序与代理之间的差距，通过提供交互规则来提高效率、可靠性和任务完成度。代理无需审查元素（如按钮或字段）来理解其用途，网站可以直接声明元素的用途，从而确保正确使用。

这比操作更可靠，因为操作可能涉及多个步骤，每个步骤都可能被代理误解。

网站可以通过定义 `工具` 来共享明确的用途（如搜索或购买）。工具在您的网页上可见地执行，因此用户可以信任任务按预期完成。这也可以保持您的品牌和以人为中心的设计选择完整。

WebMCP 支持：

* **发现**：页面向代理注册工具的标准方式，如 `checkout` 或 `filter_results`。
* [**JSON Schema**](https://json-schema.org/understanding-json-schema/reference)：明确的

*原文: https://developer.chrome.com/docs/ai/webmcp*