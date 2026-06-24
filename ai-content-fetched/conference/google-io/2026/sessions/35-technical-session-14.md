---
title: The latest from Google Pay and Google Wallet
title_zh: Google Pay 与 Google Wallet 最新动态
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: Google Pay and Wallet
type: 技术演讲
level: Intermediate
speakers: eyanaga, gokmengoksel, kushpatel
video: https://www.youtube.com/watch?v=prVc7FamKsU
---
# Google Pay 与 Google Wallet 最新动态

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: Google Pay and Wallet | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: eyanaga, gokmengoksel, kushpatel

发现 Google Pay 与 Wallet 在代理 AI 时代的演进。了解提供更高灵活性和投资回报率、同时打造无缝用户体验的新工具和能力。了解 API 更新、扩展的 Digital ID 全球覆盖范围以及全新数字收据支持。

---
## 📝 详细原文

了解在代理式 AI 时代 Google Pay 与 Wallet 的演进。了解提供更高灵活性和投资回报率的新工具和功能，同时提供无缝的用户体验。了解 API 更新、扩展的 Digital ID 全球覆盖范围以及新的数字收据支持。

**原文（English）**: Discover the evolution of Google Pay and Wallet in the age of agentic AI. Learn about new tools and capabilities that offer greater flexibility and ROI, while providing a frictionless user experience. Discover API updates, expanded Digital ID global coverage, and new digital receipt support.

---
## 📝 内容总结

# 会议演讲总结：Google Pay 与 Google Wallet 最新动态

**演讲人**：Kushagra Patel，Google Pay 产品经理

**核心要点**：

1. **通用商务协议（Universal Commerce Protocol）**：现有 Google Pay 商户 ID 和支付后端可完全复用，开发者无需重建核心支付逻辑即可将业务延伸至 AI 驱动的智能体商务场景。

2. **Google Pay & Wallet 开发者 MCP 服务器**：现开放公开预览，支持通过自然语言提示查询集成状态、排查错误、生成代码等，将 AI 辅助直接带入开发环境，缩短集成周期。

3. **Android 快速结账**：通过"支付授权时回调"和"支付数据变更时回调"功能，Google Pay 按钮可上移至商品详情页，实现真正的一键结账，并支持动态配送选项与价格更新，提升授权率与转化率。

4. **跨平台支付扩展**：Google Pay 现已支持社交应用，结合"是否可支付"API，可在移动 Web、桌面及社交平台间提供无缝支付体验。

5. **商户发起交易的生命周期通知**：PSP 可接收支付令牌底层凭证变更通知，便于主动联系客户更新支付方式，保障周期性交易连续性。

6. **卡资金来源信号**：Google Pay API 响应新增资金来源信息（信用卡/借记卡/预付卡），助力商户精细化路由策略，优化交易处理成本。

---

## 📝 完整文字稿

【音乐】

大家好，我叫Kushagra Patel，我是Google Pay的产品经理。很高兴大家能来参加。我们的团队一直在为Google Pay和Google Wallet开发者平台开发各种强大的新功能，所有这些都是为了促进商业交易并提供卓越的用户体验。让我从探索Google Pay的最新更新开始吧。今天，我们将看看Google Pay如何在智能体商务时代不断演进。我们将向您展示全新的通用商务协议（Universal Commerce Protocol）如何让您现有的Google Pay商户ID和支付处理后端能够在AI驱动的场景中完全复用。我们还将推出新的MCP服务器，把AI辅助功能直接带到您的开发环境中。最后，我们会带您了解一系列新功能，从Android上的快速结账到最低成本路由，所有这些都是为了简化您的结账流程，帮助您实现业务目标。让我们开始吧。

我们知道您已经在支付栈上投入了大量工作。Google Pay SDK负责前端界面，而真正繁重的工作发生在后端，处理安全令牌化的凭证。好消息是，开发者朋友们，您现有的Google Pay后端，甚至您当前的商户ID，都与全新的通用商务协议支付处理程序完全兼容。这意味着您可以使用与现在相同的Google Pay基础设施和PSP关系，来为新的智能体商务体验提供支持。这样一来，您无需重建核心支付逻辑或重新配置商户身份，就能将业务延伸到智能体场景中。想了解更多，请查看视频描述中的链接，开始集成Google Pay，为未来的智能体体验做好准备。

现在，让我们更详细地看看Google Pay和Wallet开发者MCP服务器的实际使用效果。这是一个可以让您的AI智能体简化集成过程、帮助您在首选开发环境中完成端到端API集成的工具。Google Pay和Wallet开发者MCP服务器包含管理集成、排查错误、分析趋势或生成代码（用于将Google Pay和Google Wallet添加到您的应用程序）的工具。所有这些都是为了简化您的集成工作流程，缩短首次交易的时间。您可以使用类似"我的Google Pay集成状态如何？"或"列出过去7天的Google Pay交易错误"这样的提示来操作。Google Pay和Wallet开发者MCP服务器今天已开放公开预览版，并将在今年晚些时候推出正式版。访问 google/pay-wallet-mcp 了解详情。

虽然MCP服务器旨在消除开发工作流中的障碍，我们同样致力于消除买家购物流程中的障碍。毕竟，结账时的卡顿对谁都没有好处。因此，我们很高兴将"支付授权时回调"和"支付数据变更时回调"的能力带到Android平台，与Web端实现功能对等。通过这些更新，您现在可以将Google Pay按钮上移，直接放在商品详情页或商品卡片页上，提供真正的快速结账体验。这将把您Android应用中的购物流程转变为简洁的一键流程——Google Pay在支付界面中提供用户的收货地址、支付凭证和联系方式，带来真正的一键体验。

使用"支付数据变更时回调"，您可以根据用户的收货地址动态展示配送选项，包括根据税费计算的总价，并在用户与支付界面交互时，在支付界面中显示更新后的最终价格。使用"支付授权时回调"，您可以授权交易、处理重试，并提供即时反馈，整个过程无需关闭支付界面，这有助于提高授权率，从而提升转化率。通过集成Play Services Wallet SDK 20.0.0或更高版本，开发者现在可以在他们的应用程序中实现处理这些特定DPU事件回调的逻辑。

继去年我们宣布Google Pay支持Android Web视图（可通过设备令牌实现安全购买）之后，我们正在进一步扩展能力，将Google Pay支持扩展到社交应用。这一单一集成现在可以在应用程序、移动Web、桌面环境和社交平台之间提供无缝的支付体验。为了确保Google Pay在您的所有数字平台上都能正常运行，请使用"是否可支付（is ready to pay）"API。这允许您以编程方式验证是否应在基于Web的实现中向用户显示Google Pay按钮。

接下来，我们将更新对商户发起交易的支持。您或您的PSP现在将能够接收Google Pay支付令牌在底层凭证变更时的生命周期通知。这使您能够主动联系客户，请求他们在下一个计费周期前更新支付方式，确保周期性交易的连续性。这些通知将包括令牌的更新状态（如果自初始交易或上次更新以来发生了任何变化）。请查看下方链接获取更多信息。

除了促进快速交易，我们还致力于帮助您优化每一笔支付的经济效益。我们知道，管理处理成本是任何成长型企业的首要任务。因此，我们推出了新工具，为您提供更高的透明度和控制力，让您掌握交易的路由和处理方式。首先是卡资金来源信号（card funding source signal）。Google Pay的卡资金来源信号可帮助您定制结账流程并管理交易处理成本。Google Pay API响应现在包含卡资金来源信息，您将能得知该卡是信用卡、借记卡还是预付卡，从而让您能够实施更精细的策略……

（音频在此处中断） 下面给你一个比较口语化、通顺自然的中文翻译，保留了原意但读起来像在听人讲话：
---
