---
title: What’s new in Flutter
title_zh: Flutter 的新功能
category: conference/google-io/2026/sessions
date: 2026-05-20
time: 10:00 - 10:45 PT
track: Flutter
type: 技术演讲
level: Intermediate
speakers: katelovett, lite, yenkhanh
video: https://www.youtube.com/watch?v=I1uIbGh1dGE
---
# Flutter 的新功能

## 📋 摘要

**📅 日期**: 2026-05-20 | **🕐 时间**: 10:00 - 10:45 PT | **📂 分类**: Flutter | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: katelovett, lite, yenkhanh

探索最新的Flutter框架更新，从性能改进到新功能。深入了解Flutter GenUI，发现如何即时构建真正自适应的AI生成用户体验。了解这些创新如何塑造快速、多平台应用开发的未来。

---
## 📝 详细原文

探索最新的Flutter框架更新，从性能提升到新特性。深入了解Flutter GenUI，发现如何即时构建真正自适应、AI生成的用户体验。了解这些创新如何塑造快速、跨平台应用开发的未来。

**原文（English）**: Explore the latest Flutter framework updates, from performance improvements to new features. Dive into Flutter GenUI to discover how to build truly adaptive, AI-generated user experiences on the fly. Learn how these innovations are shaping the future of fast, multi-platform application development.

---
## 📝 内容总结

# Flutter 新功能会议总结

本次会议围绕"Flutter 新动态"主题，介绍了 **Flutter 3.44** 和 **Dart 3.12** 的最新发布。

## 核心要点

**生态规模**
Flutter 贡献者已达 **1700 人**，过去一年合并 5800+ 变更；pub.dev 30 天下载量超 **13 亿次**，是移动端第二大主流 SDK，月活开发者达 **150 万**。

**Dart 语言升级**
- 点号简写（dot shorthands）与构建钩子（build hooks）正式发布
- 命名构造参数初始化更便捷，新增主构造器实验性支持
- **Dart Cloud Functions for Firebase** 上线，冷启动仅 10 毫秒，支持纯 Dart 编写 HTTP/可调用函数
- Dart Admin SDK 提供服务端特权访问能力

**开发者体验优化**
- Dart CLI 速度显著提升，分析速度提升约 50%
- 新增自定义分析器插件、pub cache GC 命令
- Widget Previews 全面支持 Flutter Inspector

**代理式开发（Agentic Development）**
- 推出 **Dart/Flutter MCP Server**，赋能 AI 代理
- **代理式热重载**自动连接运行中的应用，实现实时 UI 更新
- 发布 **Dart & Flutter 代理技能**，遵循渐进式披露原则，基于最佳实践提升代码质量

**愿景**：通过社区共建，让 Flutter 和 Dart 为全平台提供最高效、最高品质的全栈动态用户体验。

---

## 📝 完整文字稿

谢谢，谢谢。Flutter 随处可见，无时不在。它由所有人共同打造，也为所有人服务。非常感谢所有 Flutter 社区成员和展示合作伙伴帮我们一起制作了这段精彩绝伦的视频。大家好，欢迎来到"Flutter 新动态"环节。我是 Kate，Flutter 框架团队的工程经理。我是 Khan，Google Dart 和 Flutter 团队的一名开发者关系工程师。今天我们还请到了来自 Google DeepMind 的 Li-Te Chang。非常感谢所有到场以及在线收看的观众朋友们。"无处不在、无时不在、人人共建、人人享有"这个主题，正是我们今天要聊的核心。Flutter 以及为它提供支持的 Dart，同样致力于提供最高效的开发体验，为任何平台打造最高品质的全栈动态用户体验。今天我们非常激动地宣布 Flutter 3.44 和 Dart 3.12 正式发布。Google I/O 一直是一年中最令人兴奋的时刻之一，它非常适合回顾过去一年里我们取得的成果，也是分享未来发展方向的好时机。当然，它更是介绍最新版本中所有新特性的好时机。今天我们还有两个特别的展示要跟大家分享，分别来自 Google DeepMind 和丰田。今天内容非常丰富，Kate，我们开始吧。好，我们来聊聊 Flutter 的现状。今年我们的贡献者社区比以往任何时候都更强大，Flutter 项目的贡献者人数已达 1700 人。是的。是的。仅过去一年，Flutter 仓库就合并了超过 5800 个变更，量真的很大，希望大家看得过来。pub.dev 生态系统也空前火爆，仅过去 30 天的包下载量就超过了 13 亿次。背景说一下，我原本让同事统计过去 12 个月的 pub 包下载量，但那个数字实在太大了，所以我只好换成过去 30 天的数据。无论是在 App Store 还是 Google Play Store，Flutter 目前都是移动应用开发领域第二受欢迎的 SDK。多年来看到社区不断壮大，真的令人惊叹。就在几周前，每月有 150 万开发者使用 Flutter 进行开发。我知道，真的很棒，对吧？接下来我把话筒交给 Khan 来开始我们的深度分享。Khan，请开始吧。好，谢谢 Kate。我们先从 Dart 聊起，它是开发者喜爱的语言，同时也是 Flutter 的核心。我们致力于让 Dart 在任何地方都易用且高性能，并确保它对每个开发者来说都依然好用且愉悦。在去年的主题演讲中，我们预告了一些特性，比如点号简写（dot shorthands），可以让你省略冗余的类名或枚举名。还有 Dart 构建钩子（Dart build hooks），可以让你编译原生代码或下载原生资源，并直接打包到你的 Dart 包中。对于很多基于 FFI 的包来说，这消除了维护 CocoaPods、CMake 或 Gradle 等平台特定构建文件的需要。这两个特性都已正式发布，从反馈来看大家都很兴奋，那我们继续往前走。在最新的 Dart 3.12 版本中，我们让使用命名构造参数初始化和声明私有实例字段变得更加容易。这意味着 Dart 现在会自动为你生成显式的初始化列表。我们还新增了对主构造器（primary constructors）的实验性支持，实例变量现在可以直接在类头中直接声明。哇！长期以来，Firebase 团队呼声最高的需求之一就是在 Cloud Functions 中支持 Dart。因为大家都知道，开发者都喜欢全栈 Dart，对吧？我说得对吧？太棒了。准备好激动一下吧，Dart in Cloud Functions for Firebase 正式上线了。你现在可以用纯 Dart 编写 HTTP 和可调用函数了。Dart 使用 AOT 编译，所以在 Cloud Functions 中使用 Dart 时，冷启动时间低至 10 毫秒。除此之外，Dart Admin SDK 现在还允许你在服务器端的特权环境中访问 Firebase 服务。好的，我们来聊聊开发者体验。Flutter Dart 一直以无与伦比的开发者体验著称，而我们的使命就是让它不断变得更好。去年，我们通过将分析服务器迁移到 AOT 快照，加快了 Dart CLI 命令的执行速度。现在，Dart 格式化的速度几乎可以忽略不计，Dart 分析的速度也提升了约 50%。我们还新增了对自定义分析器插件的支持，这意味着你现在可以基于分析服务器的现有能力进行扩展，报告自定义诊断信息，并提供符合你团队工作流程的独有功能。我们还新增了 pub cache GC 命令，可以自动识别并清理 pub 缓存中未使用的包，自动帮你回收宝贵的磁盘空间。热重载非常适合快速迭代应用，但有时候你可能想在隔离环境下预览独立的 widget，Widget 预览（Widget Previews）功能正好满足你的需求。你可以在沙盒环境中针对不同的屏幕尺寸、主题和文字缩放比例测试 widget。从本版本开始，它已全面支持 Flutter Inspector。好的，我们已经做了大量工作来优化现有的开发者体验基础。然而在过去一年里，我们见证了改变 Dart 和 Flutter 应用开发方式的新工具如雨后春笋般涌现。Hot code、anti-gravity、Gemini CLI，这些基于智能体的工具正在不断重塑我们作为开发者的角色。我们越来越像架构师…… 嗯，就像委托，还有和代理协作来帮我们构建。好的，这就是为什么我们推出了新工具，让你们使用代理辅助的开发工作流变得更高效。Dart Flutter MCP 服务器去年夏天上线了，它能让代理更深入地了解你的 Dart 代码、Flutter 项目，并给它们提供所需的工具来替你执行操作。好的，我们非常激动地宣布一个新功能，我们称之为代理式热重载。热重载现在会自动在所有地方的每个编程代理上工作。所以，当你让代理做一个修改时，它就能完成修改，然后自动连接到你正在运行的应用并重新加载，让你实时看到 UI 的更新。如果说 MCP 服务器给你的代理提供了工具，那么技能（skills）就是给你的代理提供一步步的指导，教它们如何完成各种任务，比如怎么构建响应式布局，或者怎么添加 widget 预览。这就是为什么我们还要推出一套 Dart 和 Flutter 代理技能。这些技能能帮助你把代理式开发建立在 Dart 和 Flutter 的最佳实践之上，并提升整体的代码质量。另外，技能采用渐进式披露（progressive disclosure）。这意味着你的代理只在需要的时候才会去查阅它们，能帮你省下一些宝贵的 token。

现在，AI 驱动的功能在日常用户体验中越来越突出，从简单的内容摘要，到完全代理式的个人 AI 助手——它们能替用户检索信息并采取行动。我们一直在着力扩展 Dart Flutter 生态系统，这样你们在为各个平台的用户构建这些 AI 驱动的体验时，就能拥有所需的全部工具。

我自己呢，一直在用 MacroFactor 来记录我的饮食和宏量营养素。它对我来说特别好用，因为我不想自己去算那些宏量营养。只要拍一张我盘子里食物的照片，应用就帮我记下来了。MacroFactor 应用就是一个 Flutter 应用，它用 Firebase AI Logic 直接调用 Gemini 模型的 API，利用它的多模态视觉能力来简化记录饮食的用户流程。Firebase AI Logic 现在有了服务端提示模板，这意味着你不再需要把提示词直接写死在应用里。而且从今天开始，你可以通过全新的 Firebase 代理技能 for Flutter，给你的代理提供一步步的指导，教它们如何构建全栈的 Flutter 和 Firebase 应用。

我们还很激动地宣布 GenKit Dart 的预览版发布，这是一个用于构建全栈 AI 驱动和代理式应用的开源框架。它有模型无关的 API，支持 Google、Anthropic、OpenAI 等多种提供商。它包含了你从原型到生产所需的一切，包括类型安全的结构化输出、工具调用、多轮对话，以及内置的可观测性。

接下来，我想花点时间恭喜两位 Flutter 开发者——Gemma Vision 的作者 Tommaso 和 Vitai Verai 的作者 Guido，他们在 Gemma 3N Impact Challenge 中获得了第一名和第二名。这个挑战要求开发者使用 Gemma 3N（一个本地的端侧大语言模型）来构建让世界变得更美好的产品。挑战允许开发者选择任何技术栈。Tommaso 和 Guido 都选择了 Flutter 来构建两款改变人生的工具。Gemma Vision 帮助视障人士感知世界，而 Vite Veri 则帮助有认知障碍的人士独立完成日常任务。谢谢。恭喜 Tommaso 和 Guido。

现在，我个人一直在测试 Gemma 4，这个模型是为高级推理和代理式工作流专门打造的。它把工具调用串联起来的能力非常强，而且开箱即原生支持视觉和音频输入。它是一个轻量又能力强的模型，很棒的一点是，如果你有成本限制、端侧数据限制，或者网络连接限制，它都能派上大用场。但是，如果你的应用跑在多个不同的平台上，因为底层硬件的多样性，事情可能会变得复杂。所以，当我去看 Gemma Vision 和 Vite Veri 的 GitHub 仓库，看到它们都在用 pub 上的 Flutter Gemma 插件来做 Gemma 集成时，一点都不意外。

嗯，我非常激动地宣布：完整的 LiteRT-LM 支持即将登陆 Flutter Gemma 包。LiteRT-LM 是 Google 面向生产环境、高性能的开源推理框架。它把硬件差异抽象掉了，这样你就能跨平台跑端侧模型，并通过 GPU 和 NPU 加速确保最佳性能。更棒的是——我最喜欢的部分——它支持 Flutter 全部六个稳定平台：Android、iOS、Web、Windows、Linux 和 macOS。

说到 AI 驱动的用户体验，我觉得我们都同意，已经受够了那一坨一坨的 markdown 文本。更糟糕的是纯文本。Gen UI，也就是生成式 UI，是一种用户体验范式：AI 用 UI 而不是大段文字来实时构建和回应。过去一年，Flutter 一直在作为项目合作伙伴推动 Gen UI 的发展，参与制定了新兴的 A2UI 协议。A2UI 是 Google 创建的一个开源协议，它定义了代理和客户端如何协作来完成用户界面的组合和状态管理。我们去年晚些时候上线了 Flutter Gen UI SDK。它建立在 A2UI 之上，为你在 Flutter 应用中构建动态的 Gen UI 体验提供了基础，就像这个例子一样。从年初到现在，这个包的下载量增长了 500%。

另一个很好的 Gen UI 例子是 Çağatay Ulusoy 用 Flutter 开发的 Finish It 应用，它不仅能为用户生成定制课程计划来学习芬兰语词汇和语法，还会针对每个课程实时组合出合适的界面。

如果你看了上个月的 Cloud Next 开发者主题演讲，你可能已经看到 Flutter Dev……（后续内容未给出） 好的，我把它翻成比较口语化的中文：
---
