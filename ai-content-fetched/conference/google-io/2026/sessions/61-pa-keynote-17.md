---
title: What’s new in Go
title_zh: Go 新特性

Given "What’s new in Go", a straightforward Chinese translation is "Go 的新变化". Or "Go 有哪些新特性". Let's consider typical translation: In Chinese, "What's new in Go?" is often translated as "Go 有哪些新特性？". However they likely want a title: "Go 新特性". But "What’s new in Go" might be "Go 的新功能" which is a literal translation. Let's decide.

The phrase "What's new in Go?" is used on the official Go blog: The title is "What’s new in Go (May 2023)". Chinese translation on the Go blog: "Go 新变化". Actually I recall Chinese translations: "Go 新功能" is used. For instance "What’s new in Go" may be translated as "Go 新功能". Let's search memory: In the Chinese version of the Go blog, "What’s new in Go" is translated as "Go 的新变化". But I recall reading Chinese translations: "Go 新特性". For example "What's new in Go 1.21?" is "Go 1.21 的新特性". So "What's new in Go" might be "Go 的新特性". Could be "Go 新特性".

The user didn't ask for the translation of "Go" being capitalized. It's ambiguous. Should we include question mark? Probably "Go 的新特性". Let's provide that.

Thus answer: "Go 的新特性".
</think>

Go 的新特性
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: 云
type: 技术演讲
level: Intermediate
speakers: cbalahan, muncus
video: https://www.youtube.com/watch?v=l4lneZYtjQg
---

# Go 新特性

Given "What’s new in Go", a straightforward Chinese translation is "Go 的新变化". Or "Go 有哪些新特性". Let's consider typical translation: In Chinese, "What's new in Go?" is often translated as "Go 有哪些新特性？". However they likely want a title: "Go 新特性". But "What’s new in Go" might be "Go 的新功能" which is a literal translation. Let's decide.

The phrase "What's new in Go?" is used on the official Go blog: The title is "What’s new in Go (May 2023)". Chinese translation on the Go blog: "Go 新变化". Actually I recall Chinese translations: "Go 新功能" is used. For instance "What’s new in Go" may be translated as "Go 新功能". Let's search memory: In the Chinese version of the Go blog, "What’s new in Go" is translated as "Go 的新变化". But I recall reading Chinese translations: "Go 新特性". For example "What's new in Go 1.21?" is "Go 1.21 的新特性". So "What's new in Go" might be "Go 的新特性". Could be "Go 新特性".

The user didn't ask for the translation of "Go" being capitalized. It's ambiguous. Should we include question mark? Probably "Go 的新特性". Let's provide that.

Thus answer: "Go 的新特性".
</think>

Go 的新特性

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: 云 | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: cbalahan, muncus

Go 在最好的意义上是“无聊”的：稳定、可靠，且专为规模化打造。探索 Go 1.25 与 1.26 的新特性，包括 Green Tea 垃圾收集器、原生向量化指令，以及 “go fix” 命令背后的代码现代化工具。无论你的重点是开发 AI 代理还是传统的微服务，都能发现 Go 持续提供业界领先的进步，使其成为任务关键、高性能应用的最佳选择。

---

## 📝 详细原文

Go 在最好的意义上是“无聊”的：稳定、可靠，且为规模化而生。探索 Go 1.25 和 1.26 的新特性，包括 Green Tea 垃圾回收器、原生向量化指令以及 “go fix” 命令背后的代码现代化工具。无论你专注于开发 AI 代理还是传统微服务，都可以发现 Go 如何持续提供行业领先的技术进步，使其成为关键任务高性能应用的最佳选择。

**原文（English）**: Go is “boring” in the best way: stable, reliable, and built for scale. Explore what’s new in Go 1.25 and 1.26, including the Green Tea garbage collector, native vectorized instructions, and the code-modernizers behind the “go fix” command. Whether your focus is developing AI agents or traditional microservices, discover how Go continues to deliver industry-leading advancements that make it the best choice for your mission-critical, high-performance applications.

---


---

### 原文

Go is “boring” in the best way: stable, reliable, and built for scale. Explore what’s new in Go 1.25 and 1.26, including the Green Tea garbage collector, native vectorized instructions, and the code-modernizers behind the “go fix” command. Whether your focus is developing AI agents or traditional microservices, discover how Go continues to deliver industry-leading advancements that make it the best choice for your mission-critical, high-performance applications.

---

## 📝 内容总结

**《Go 新特性》核心要点**

一、核心主题概述

本演讲介绍Go 1.25和1.26版本的新特性，包括Green Tea垃圾回收器、SIMD向量化指令、go fix现代化工具等。

**二、关键发布/技术要点**
- 要点1：go fix重建——支持持续现代化改造，基于分析框架
- 要点2：源码级内联器——API迁移时自动替换已弃用函数调用
- 要点3：testing/synctest包——Bubble概念简化并发测试，虚拟时钟自动前进
- 要点4：new表达式扩展——从表达式创建指针
- 要点5：Green Tea垃圾回收器——以page为工作单元，GC CPU开销降低10-50%
- 要点6：CGo调用优化——速度提升30%，降低跨边界成本
- 要点7：SIMD正式支持——向量化数组操作，Green Tea内部使用
- 要点8：Flight Recorder——环形缓冲区追踪日志，按需刷新

**三、落地应用**
- 案例1：Google内部go fix促成18000+代码提交
- 案例2：5秒超时测试用synctest几毫秒完成
- 案例3：大多数应用GC CPU开销降低10%

**四、总结**
Go保持”无趣”特性但持续进化。Green Tea GC、SIMD、CGo优化等性能改进自动生效无需改代码。go fix帮助代码库保持现代，兼容性承诺保证代码长期可维护。Go仍是高性能、关键任务应用的理想选择。

---

## 📝 完整文字稿

好的，我来帮你翻译成中文口语风格：

[音乐] 

>> 大家好，我是 Cameron，我是 Google Go 编程语言的产品负责人。我是 Mark，负责 Go 的开发者关系工作。几十年来，开发者们一直面临一个艰难的选择。你可以选择用 Python 或 JavaScript 这种动态解释型语言来提高生产力，写起来很快，但在大规模应用和可靠性方面往往力不从心。或者你也可以选择 C++ 或 Java 这种强类型编译语言，能提供强大的性能，但复杂度也相当高。这正是 Google 大约 20 年前遇到的难题。当时 Robert Griesemer、Rob Pike 和 Ken Thompson 站在白板前，想看看有没有更好的办法。他们一起创造了 Go 编程语言。如今，数百万开发者再也不用在生产力和生产就绪度之间二选一了，鱼和熊掌可以兼得。

但在 AI 时代，这个难题还重要吗？事实是，AI 反而让这些基础变得更加关键。对人类清晰的语言，对 AI 模型也更友好。而最终，还是需要人类来验证 AI 的输出。当 AI 加速了我们编写和上线代码的速度，让 AI 和人类都能更轻松地写出更安全、性能更好、更易维护的代码，就变得前所未有地重要。Go 是一种"无趣"的语言，但这是它最好的特质。

Go 真正与众不同的地方在于，它不仅仅是一门语言，而是一个端到端的软件工程平台。软件工程是团队协作的事情，是与他人——现在还包括 AI——合作，设计和实现能够随时间演进的持久系统的过程。编程只是软件工程的一部分。Go 的目标是服务整个软件工程，通过一个强大的端到端平台，在软件开发生命周期的各个环节提供确定性的工具。这也是我们为什么优先考虑简洁性、性能、安全性和可靠性。这些原则是构建系统的基石，让代码在原作者离开后的几年甚至几十年，依然保持良好的可维护性。

今天，我们将向您展示如何在延续这些基础原则的同时，持续演进 Go 平台。正如您将看到的，Go 在诞生近 20 年后，依然在生产力和生产就绪度方面保持着行业领先的改进。下面有请 Mark 来开始介绍。

谢谢 Cameron。Go 每年发布两个主要版本，分别是 2 月和 8 月。在过去一年里，我们在 1.25 和 1.26 版本中发布了许多令人兴奋的新功能，帮助你和你的团队更高效地工作。所有语言都会随时间演进，随着语言的发展，老代码会显得不够地道、可读性变差，维护起来也更困难。这也会影响 AI 生成的代码，因为较新的功能和模式在训练数据中出现得较少。为了解决这个问题，我们重建了 `go fix` 命令，支持持续现代化改造。

`go fix` 基于 Go 的分析框架，能深入理解你的代码，并应用确定性的修改，让你得到充分利用最新语言特性的代码。这个新引擎的核心是现代化框架（modernizer framework），它能进行代码转换，并优先保证正确性，确保更新后的代码保持原有的行为。目前 `go fix` 已经包含超过 20 种现代化转换器，帮助你的代码保持清晰和可读。

`go fix` 也能帮助你处理代码库自身的演进，这要归功于源码级内联器的强大能力。你只需在已弃用的 API 上添加一个 `gofix:inliner` 指令，`go fix` 就会在整个代码库中把这个函数的所有调用替换为新的实现。借助 Go 编译器的分析能力，`go fix` 即使在存在副作用的情况下，也能保持代码的原始行为。`go fix` 可以帮助你加速 API 迁移，让你能够更早地移除已弃用的方法，保持整个代码库的整洁。在 Google 内部，`go fix` 已经在我们的代码库中促成了超过 18,000 次代码提交，让这个最古老的 Go 代码库之一也用上了现代的 Go 特性。

Go 的核心理念之一是：源代码应该易于机器读取、编写和编辑，以支持自动化的重构。这一理念造就了 Go 易于阅读的语法和标准化的格式，也持续激励着我们在 `go fix` 和现代化转换器方面的工作。这一原则如今又回到了它的起点，极大地增强了 AI 代码编写能力，并解锁了像现代化转换器这样复杂的源码工具，让它们能够以我们刚开始时难以想象的规模运行。

接下来，我们聊聊 Go 最受欢迎的测试功能之一——`testing/synctest` 包，它在 Go 1.25 中正式发布（GA）。并发天然就是复杂的，因为操作可能乱序执行。因此，测试并发代码也很复杂，往往需要依赖超时或 sleep 调用，这会导致测试结果不稳定（flaky）。`synctest` 通过引入 **"bubble"（气泡）** 的概念，极大地简化了并发测试——这是一个隔离的环境，goroutine 在其中使用一个虚拟的合成时钟。在 bubble 内部，当所有 goroutine 都被阻塞时，时间会自动前进。这个测试原本需要等待 5 秒超时，但用 `synctest` 之后，只需几毫秒就能确定性地、始终如一地完成。`synctest` 让调整并发测试中事件的顺序变得更简单，并确保所有 goroutine 在 bubble 结束时都已完成。

Go 是有意保持"无趣"的。我们很少直接修改语言本身，所以 Go 1.26 的代码和 Go 1.0 的代码看起来几乎一模一样。在 Go 1.26 中，我们对语言本身做了一个小但影响巨大的改变——新的 `new` 表达式。Go 用户注意到，在处理深度嵌套的 struct（特别是大量使用指针的情况，这在 protobuf 等数据交换格式中很常见）时会有些别扭。为此，我们扩展了 `new` 内置函数，让它可以从表达式创建指针，包括基本数据类型和函数返回值……

（翻译到这里就结束了，后面的内容你没有提供） 好的，我帮你翻译成自然的中文口语版本：

---

一些用户和库自己写了一些辅助方法来实现同样的效果，比如 proto.string。说回到 go fix 和现代化工具，很多情况下，go fix 能自动识别这些辅助方法，直接替换成新方法的调用。这些工具配合起来用，能让你的代码库保持现代、易读，更重要的是——保持正确。不过写代码只是第一步。接下来，Cameron 会给你们讲讲我们是怎么让这些代码在生产环境里跑得更快的。

Mark 刚才带你们看了 Go 1.25 和 1.26 里一些能让你效率更高的新特性。但别忘了，Go 不只是让你写得快，它还关心你的代码在生产环境跑得怎么样。Go 从一开始就是为解决 Google 这种规模的问题设计的。所以 Go 成为现代云服务的基石一点都不意外。世界上最知名的云技术很多都是用 Go 写的，包括 Kubernetes、Docker、Terraform 等等。这种普遍性是 Go 长期坚持生产可用（production readiness）的直接结果。而支撑这种坚持的一个重要原因就是 Go 的兼容性承诺——Go 团队正式承诺：按照 Go 规范编写的代码，在未来所有版本的 Go 中都能继续正确编译运行，不用改一行代码。

正是因为这个兼容性承诺，很多东西在新版本里会变得更好，你基本不用操心。升级一下，重新编译，系统就自动变强了。在其他生态里，代码越老越成负担；在 Go 里，代码越老越值钱。如果你确实需要改点代码才能用到新特性，Mark 之前演示的 go fix 会帮你搞定。

基于这个思路，我们来看看过去几个版本我们在平台上做了哪些性能优化。今年性能方面最重磅的就是新的 Green Tea 垃圾回收器——Go 1.25 里以实验特性引入，Go 1.26 开始默认开启。Green Tea 是对传统 GC 设计的一次重大突破，它跳出了传统算法被硬件限制的框框，把工作的基本单元从零散的对象换成了大块的连续内存（我们叫它 page）。这跟现代硬件设计是配合的，不是对抗的，能最大限度减少高延迟的内存读取，还能让运行时用上超高吞吐的向量加速。带来的效果就是：大多数应用的 GC CPU 开销降低了 10%，内存布局复杂的应用甚至能降 50%——你一行代码都不用改。

Green Tea 是我们运行时的一次进化，目的是更高效地利用现代多核系统。同时它也是一个全新的基础架构，给将来实现一些以前做不到的透明优化打开了大门，比如现代服务器 CPU 架构里的 NUMA 感知。

类似地，在 Go 1.25 和 1.26 里，我们还做了运行时优化，把更多内存分配从堆上挪到栈上。栈分配便宜得多，而且不会给 GC 增加负担，还能快速复用，缓存局部性也更好，内存访问更快。又是一个白送的性能提升，你啥都不用干。

但我们不只是让已有代码跑得更快，我们还在打开全新类型工作负载的大门。Go 1.26 里我们优化了 Go 和 C 之间的切换，让 CGo 调用快了 30%。对于那些依赖底层系统 API 或专用硬件库的高性能系统来说，跨边界的成本大大降低了，这让机器学习、游戏、图形界面这些领域出现了全新的可能性。换句话说，我们把 CGo 从一个"没办法才用"的东西，变成了一个能让你开发全新类别应用的机会。我们很期待看到大家用它做出什么。

再往底层看，Go 1.26 里我们正式支持了 SIMD（单指令多数据）。SIMD 让现代 CPU 能做向量化的数组操作，让某些循环并行跑起来。这种能力对很多性能优化都至关重要，包括一些 AI 基础设施里需要的排序操作。其实我们自己就在用 SIMD，让 Green Tea 垃圾回收器更高效。

说到 AI，去年我们发布了一个官方的 SDK，用来支持模型上下文协议（也就是 MCP）。MCP 让你的服务能通过统一协议给大模型提供上下文和工具。有了这个 SDK，你就可以放心地利用 Go 的招牌能力，把数据和功能开放给你的 AI 应用。我们自己也在用 MCP SDK 搭服务器，把更多 Go 工具链的能力开放给各种 AI agent 和 AI 开发工具。你们可能已经在 Go 官方的语言服务器 Go please 里看到一个 MCP 服务器的原型了，明年会有更多。

接下来，我们用全新的 Flight Recorder（飞行记录器）让可观测性用起来更顺手。追踪日志成本不低，所以新的 Flight Recorder 让你可以一直开着追踪，写到一个环形缓冲区里，只在需要的时候才刷出来。这样你既能拿到需要的数据，又不会给生产环境带来太多开销。

最后，我们还在为未来十年保驾护航，扩展了后量子加密支持，加了基于堆地址的随机化，还增强了 FIPS 140 支持。这些主动的安全特性让我们一直走在前面，确保 Go 能继续用在最关键的业务场景里。还有很多内容你可以去 go.dev 的发布说明里看。

所有这些加在一起，都是我们一贯的坚持：让 Go 既高效又生产可用。而且不管我们现在还是将来做什么改动，你都可以放心——Go 的兼容性承诺我们一定会兑现。Go 从过去、现在到将来，都会对 Go 1.0 保持完全向后兼容。

就像你们刚才看到的，Go 一直（讲话到这里被打断了）——

---

翻译的时候我把一些术语做了口语化处理，比如 "green tea garbage collector" 保留了 "Green Tea" 加上简短解释，"CGo" 保留了英文，"Flight Recorder" 用了"飞行记录器"并解释了一下功能。整体读起来会更顺一些。 用于提升生产力和生产就绪度，并持续适应不断变化的软件工程需求以及我们创建的工作负载。经过这么多年，我们仍然在带来重大且突破性的改进。我们是怎么做到的呢？嗯，是我们一起做到的。如今，我们的生态系统比以往任何时候都更庞大、更稳健，我们继续看到大量真正高质量的工具和库涌现出来，尤其是围绕生成式 AI 的新用例方面。我们看到全球数十万的 Go 开发者们聚集在一起，参加 Go 大会，在线上协作，这一切都是因为他们热爱 Go。所以，感谢 Go 社区。正是因为你们的贡献，Go 才得以发展壮大，超越以往任何时候。我们非常自豪能与你一起踏上这段旅程。有关我们在本期视频中讨论的任何内容的更多信息，请务必访问我们的主页 go.dev。感谢你今年加入我们的 Google I/O。我们迫不及待地想看到你在今年以及未来几年用 Go 构建出什么。
---
