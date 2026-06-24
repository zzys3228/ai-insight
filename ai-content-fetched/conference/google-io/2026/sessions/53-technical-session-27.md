---
title: How to write really good Flutter code
title_zh: 如何写出真正优秀的Flutter代码
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: 云
type: 技术演讲
level: Intermediate
speakers: ewindmill, mariamhas, ryjohn
video: https://www.youtube.com/watch?v=O0UjId1VoRU
---

# 如何写出真正优秀的Flutter代码

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: 云 | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: ewindmill, mariamhas, ryjohn

探索高质量、可维护 Flutter 代码的编写原则，以及 Widget Previews、DevTools、MCP 服务器和 Skills 等工具如何让编写高质量代码比以往更轻松。

---

## 📝 详细原文

探索编写高质量、可维护的 Flutter 代码的原则，以及 Widget 预览、DevTools、MCP 服务器和 Skills 等工具如何让编写高质量代码比以往更加轻松。

**原文（English）**: Explore the principles of writing high-quality, maintainable Flutter code, and how tooling like Widget Previews, DevTools, MCP server and Skills make it easier than ever to write high-quality code.

---


---

### 原文

Explore the principles of writing high-quality, maintainable Flutter code, and how tooling like Widget Previews, DevTools, MCP server and Skills make it easier than ever to write high-quality code.

---

## 📝 内容总结

**《如何写出真正优秀的Flutter代码》核心要点**

一、核心主题概述

本演讲分享七个Flutter最佳实践技巧，结合Widget Previews、DevTools、MCP服务器和Skills等工具，帮助开发者写出可读、可扩展、可测试的代码。

**二、关键发布/技术要点**
- 要点1：按约束设计——使用LayoutBuilder获取局部约束，避免固定尺寸
- 要点2：使用DevTools调试——Flutter DevTools Inspector高亮布局溢出错误
- 要点3：构建可复用Widget——Widget接收渲染所需参数，不修改数据，逻辑延迟到回调
- 要点4：分层架构（MVVM）——UI层、逻辑层、数据层分离，ChangeNotifier通知刷新
- 要点5：Repository模式——集中数据访问逻辑，唯一真实数据源
- 要点6：跨平台设计——使用pub.dev插件（如pay包）支持Apple Pay和Google Pay
- 要点7：编写测试——单元测试、Widget测试、集成测试配合checks包

**三、落地应用**
- 案例1：Dash Shop应用逐步添加结账体验
- 案例2：MCP服务器让智能体搜索pub.dev获取最新包文档
- 案例3：Flutter集成测试Skill帮助智能体自动生成测试

**四、总结**
高质量Flutter代码需要遵循架构原则和最佳实践。通过分层架构、可复用组件和完善的测试策略，配合AI智能体和MCP工具，开发者可更轻松地维护和扩展大型Flutter项目。

---

## 📝 完整文字稿

[音乐] >> 大家好，我是 Maryam，Flutter 的产品经理。今天，我们将分享七个工具和技巧，你现在就可以使用它们来让你的 Flutter 代码更具可读性、可扩展性和可测试性。Eric 和 John 也加入了，他们将帮助我演示这些技巧，在我们的 Dash Shop 应用中构建一个结账体验。Dash Shop 是一个销售 Dash 周边商品的独家在线商店，有玩偶、键盘，应有尽有。这些技巧将帮助你构建具有可扩展和可维护架构的 Flutter 应用，让它能经得起时间的考验。我们还会分享一些可以用来给应用添加功能的工具，以及一些 AI 用它们来协助你的酷炫方法。好的，让我们开始看代码。

第一个技巧是关于构建一个出色的 UI。设计时要使用约束而不是固定尺寸。Flutter 让我们可以使用同一套代码库，让 Dash 商店在任何设备、任何屏幕上都能使用。但正如一只聪明的鸟曾经告诉我的，便捷伴随着责任。作为开发者，我们的工作是确保 UI 在视觉上具有响应性，同时保持代码的可读性和无错误。使用约束进行设计可以让你的 widget 比使用固定尺寸时更灵活、更可重用。这样，你就可以轻松地将它们复用于手机、桌面或网页。本质上，这归结为三个步骤：抽象、测量和分支。

目前的 UI 使用了 Flutter 的弹性布局，比如 row、column 和 flex 等 widget，来确保 widget 根据约束的大小进行缩放。但当屏幕太小无法显示所有内容，或者屏幕太大造成空间浪费时，你需要用一个完全不同的、适合该屏幕尺寸的布局来替换它。所以，第一步是识别需要更改的 UI widget，并抽象它们共享的底层数据。在这个例子中，购物车屏幕布局需要根据屏幕大小进行更改。我们将通过构造函数参数传入它需要渲染的数据。Widget 不应该关心数据来自哪里，只知道它需要显示这些数据。

接下来，让我们测量显示区域的大小。使用 media query 的 size 来获取整个应用窗口的尺寸，或者使用 layout builder 来获取局部约束。由于这是一个我们想要复用的较小的 widget，我们将使用 layout builder。

最后，我们可以读取 layout builder 给我们的约束，并根据可用大小返回不同的 widget。要了解更多信息，请查看描述中链接的布局文档。

如果我们的 UI 布局坏了或者应用卡住了，我们可以反复调整容器的高度、热重载、再调整高度、再热重载，或者我们可以通过使用 dev tools 来节省时间，跳过所有这些猜测工作，从而提供对应用的可见性，比如父 widget 强制执行的精确约束。

我们的第二个技巧是使用 dev tools。考虑到无障碍性，让我们把结账购物车里的图片和文字放大，让它们更清晰可见。让我看看。这应该很简单。我会打开 anti-gravity，输入一个我想要更改的 widget 的提示。好的，anti-gravity 做了更改。现在，我让它重新加载。然后我们遇到了一个经典问题——那个可怕的布局溢出错误。为了帮助我们理解发生了什么，让我们使用 dev tools 看看是哪个 widget 导致了错误。Flutter dev tools 检查器会高亮显示这些错误，这样我们就能看到是哪个 widget 引起了问题。这个 row widget，就是它溢出了。我们可以自己深入研究细节，或者我们可以使用 Dart 和 Flutter MCP 服务器来帮助我们修复这个问题。MCP 服务器让 AI 助手可以使用 Flutter 的开发者工具。要在 Antigravity 中安装它，我们会打开代理面板，在附加选项下拉菜单下选择 MCP 服务器，然后搜索 Dart。安装完成后，Antigravity 会显示可用的工具。当我们运行应用时，我们的代理可以直接连接到它。一旦连接成功，代理就可以使用 get runtime errors 工具读取布局错误消息。布局错误包含很多 Gemini 非常擅长理解的细节。代理知道如何使用热重载和 get widget tree 工具来确保它修复了布局错误。

将业务逻辑和 UI 混合在一个 widget 中，会产生庞大的、难以阅读的、深度嵌套的 build 方法。通过将业务逻辑与 UI 分离，你的 widget 变得更易于重用、修改和测试。所以，第三个技巧是构建可复用的 widget。

如前所述，一个 widget 应该接收它需要渲染的所有配置作为参数。它不应该修改或格式化任何数据。它唯一的工作是渲染数据和监听用户事件。根据经验，如果你的 widget 在引入底层库、发起远程请求或与数据库交互，那它很可能就不是可复用的。

在 Dash Store 应用中，当用户点击购买时，widget 不会反过来直接调用支付 API。因此，为了保持 widget 的可复用性并只专注于显示 UI，那部分逻辑被延迟到另一个对象处理，通过一个作为参数传递给 widget 构造函数的回调来实现。

当你的 widget 可复用时，你可以利用像 widget previews 这样的工具。Widget previews 是一个与热重载互补的开发者工具，让你可以实验 UI 的变化和状态，而无需运行整个应用程序。我可以不必运行应用、导航到特定屏幕、将应用置于特定状态来测试按钮样式，而是为该按钮编写一些 widget previews 并传入它们，从而让我能够快速迭代设计。由于我们的 widget 是按可复用的方式构建的，这非常简单。而且如果你正在使用 AI 辅助构建，Flutter 团队发布了一个技能——Flutter add widget previews，它会指导你的编码代理如何为你的应用 widget 目录构建预览。这个技能是作为...的一部分发布的。 好的，以下是这段内容的中文口语化翻译：

这部分内容是 Flutter 官方技能仓库里的一些东西，在 GitHub 上能找到。它给 AI 智能体提供了一套指令，这些指令可以共享、可以重复使用，这样它就能可靠地帮你完成任务。我们写这套技能的时候，是基于我们的官方文档来写的，所以它跟官方文档保持一致，永远是最新的，以官方文档为准。每个技能都有名字和说明，告诉智能体它是干嘛的、什么时候用。智能体只有觉得跟你要做的事相关的时候，才会去读它。你可以在 GitHub 上找到 Dart 和 Flutter 团队发布的技能，今天就能用到你自己的项目里去。

但我们可不是写完就拉倒了。我们用 e val 框架做了严格的验证，确保它在各种场景下都能稳定运行。我们的目标就是持续不断地给开发者提供工具，帮你们做出更好的 App。现在 AI 发展这么快，我们也想确保每一个技能、MCP 工具、模型的更新，都能真的让你们的 App 变得更好。所以我们想用数据说话。实际上，我们正在公开做 e val 方面的实验，代码全部开源，你们可以去 github.com/flutter/evals 看看。

现在你能看到，我们给这个 widget 加了个预览功能。预览能让你在各种状态下测试 widget，看看它们放在一起是什么效果。我们可以用这个技能，给所有重要的 widget 都生成预览。

Widget 这块搞定了，接下来我们要在 App 里用上它们。那就得聊聊 App 的架构了。关注点分离是软件开发的一个核心原则。在 App 开发里，它一般就体现成分层架构。所以第四个技巧就是：搭一个分层架构。我们用的是 MVVM 架构来分层。所有 MV 开头的模式，套路都差不多，都是三层，对应到不同模式里名字可能不一样：UI 层、逻辑层、数据层。在 MVVM 里，UI 分成视图（也就是你的 widget），逻辑放在 view model 里。view model 就像是 UI 和数据层之间的看门人。逻辑和 UI 分开之后，代码更好测试，也更容易看懂。

view model 有三个活儿：把 App 的数据转换成可以直接渲染的格式；告诉数据层用户操作需要改哪些数据；告诉 UI 什么时候要刷新。我们用 ChangeNotifier 来做这件事。在 Dash Store 这个 App 里，购物车的 view model 给购物车页面提供配置，有 cartItems（购物车商品）、subtotal（小计）这些属性，还有 addToCart（加入购物车）、onPurchase（点击购买）这些方法。onPurchase 就是前面提到的回调，传给 widget 的。用户点购买按钮的时候，view model 处理本地状态，比如切换 isLoading（是否加载中），调用 notifyListeners（通知刷新），但真正改数据的逻辑，它会交给另一层——数据层去处理。

这就引出了下一个技巧：用 Repository 模式。Repository 模式把数据访问的逻辑集中起来、做一层抽象，靠的是叫 Repository 的对象。Repository 负责管理数据层的数据，是你的 App 和外部数据（比如服务器、数据库、插件）之间的接口。在我们这个例子里，它把服务里的原始数据暴露给 view model。这个模式能在你的 App 里给每种数据源建立唯一的真实数据源，而且它应该是唯一能从外部读写数据的东西。把数据逻辑这么隔离出来之后，整个代码库都更好测试、更好扩展了。如果你想在自己的 App 里试试这些架构技巧，可以用 Flutter 团队发布的官方架构技能，让你的 AI 智能体秒变专家。

第六个技巧是：为所有平台做设计。当你要用到支付这种原生功能的时候，数据层怎么办？Flutter 用的是 Dart，Android 和 iOS 这种平台暴露的原生功能，用的是 Kotlin 和 Swift 的 API。好在 Flutter 有超庞大的插件和包生态，都在 pub.dev 上，开发者能很方便地用上原生设备功能和第三方 API。对开发者来说，最大的好处是：插件让你写一遍 Dart 代码，所有平台都能跑，底层实现细节都封装成 pub.dev 上的一个包了。以前我要找支付插件，得先退出 IDE，打开浏览器，在 pub.dev 上一个一个翻，再读文档。但你知道吗？你的编程智能体也能帮你干这事儿。我给你演示一下。我的 Dart 和 Flutter MCP 服务器已经准备好了，我问它一句：帮我写一个结账功能，要支持 Apple Pay 和 Google Pay。智能体就找到了官方的 pay 包，你能看到，它正在用 MCP 服务器安全地跟外部数据源交互。这个 MCP 服务器让智能体能实时搜索 pub.dev、拿到最新的包文档，还能分析你当前的工作区。这就很关键了——给智能体的上下文越多，它写出来的代码就越对。看结果，智能体还写好了支持 Apple Pay 和 Google Pay 的结账代码。当然，如果你不喜欢它选的方案，可以拒绝，再给它更多上下文。因为 MCP 服务器查的是最新的包文档，所以代码用的是最新的 API 版本，而不是靠训练数据。

这就是 Android 和 iOS 上的结账功能。新结账功能跑得挺好，但我们得保证它一直能稳定运行。最好加上自动化测试，这样出了毛病我们能马上知道。不管我们多不想写测试，第七个技巧就是：写测试吧。我们已经吃下了这碗"蔬菜"，把 App 也设计好了……（后面内容未完） 使用好的架构模式会让添加测试变得容易得多。首先，我们来添加一个单元测试。单元测试可以非常快速地并行验证 Dart 代码的行为。它们非常适合用来测试单个类或函数在不同输入下的表现，确保它们在隔离环境中能正确工作。我们来看一下购物车视图模型，看看怎么给它写个测试。可以看到它把一个依赖作为参数传进来，所以我们需要 mock 它。然后我们用一下新的 checks 包，像这样。你现在可能用的是 matcher 包来写测试断言，比如 equals 或者 is greater than。用 checks 包的话，所有东西都是强类型的，所以你的 IDE 知道对于你正在测试的数据类型哪些检查是合法的。我们还提供了一个 agent 技能，帮你可以从 matcher 包迁移到 checks 包。

Widget 测试，顾名思义，非常适合用来测试 Flutter 组件。它们也跑得很快，因为它们不需要物理设备或模拟器，可以点击组件、验证屏幕上的文字等等。这是我们按钮的 widget 测试。我们可以验证点击时它显示的是正确的值。

最后，我们用集成测试来验证这个功能在物理设备上能不能正常工作。集成测试实际上用的是和 widget 测试一样的 API，所以你不用去学新的测试框架。多亏了我们的 MCP 服务器，编程助手也能帮你做这个。我来给你演示一下。我们创建了一个 Flutter 集成测试的技能来帮大家写集成测试。首先，它会启用 Flutter driver，让编程助手能跟我们的应用交互。然后它会运行应用并跟它交互，走一遍我们要在真机上测试的用户流程。最后，它会把这些步骤捕获成一个集成测试，这样我们就能稳定地重复运行了。现在我们的集成测试可以跟其他测试一起维护了。

来总结一下。我们讲了七个写出优秀 Flutter 代码的技巧：按约束来设计，不要固定尺寸；用 dev tools 来调试；构建可复用的组件；把架构做成千层蛋糕；使用 repository 模式；为所有平台做设计；以及写出好的测试。不管是你自己手写代码，还是跟编程助手一起迭代，我们都希望这些能帮你写出比以往更可读、可扩展、可测试、更快速的 Flutter 代码。想了解更多 Flutter 最佳实践和我们的开发工具，访问 flutter.dev。[音乐]
---
