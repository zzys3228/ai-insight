---
title: What’s new in Android development tools
title_zh: Android 开发工具的新功能
category: conference/google-io/2026/sessions
date: 2026-05-20
time: 10:00 - 10:45 PT
track: Android
type: 技术演讲
level: Intermediate
speakers: easonj, tnorbye
video: https://www.youtube.com/watch?v=N4GgGBKnHe4
---
# Android 开发工具的新功能

## 📋 摘要

**📅 日期**: 2026-05-20 | **🕐 时间**: 10:00 - 10:45 PT | **📂 分类**: Android | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: easonj, tnorbye

探索 Android Studio 的新功能。了解旨在加速您在各种 Android API 工作流程的演示和功能，并第一时间了解适用于 Android 应用开发的最新 Gemini 功能。

---
## 📝 详细原文

探索 Android Studio 的新功能。探索旨在加速您跨 Android API 工作流程的演示和功能，并第一时间了解最新的 Gemini 功能在 Android 应用开发中的应用。

**原文（English）**: Discover what’s new in Android Studio. Explore demos and features designed to accelerate your workflow across Android APIs, and get a firsthand look at the latest Gemini capabilities for Android app development.

---
## 📝 内容总结

# Android 开发工具新功能总结

**演讲人**：Jamal（产品经理）与 Tor（工程负责人），来自 Android 开发者体验团队。

## 核心要点

**1. 工具演进方向**
Android 开发工具正同时为两类用户服务：开发者本人与代码中的 AI 智能体。在"速度 vs 准确性"的权衡中，Android Studio 仍是兼顾智能体工作流与深度技术开发的首选平台。

**2. Android Studio Otter 关键更新**
- **企业级支持**：通过 Gemini Enterprise 接入企业批准和托管的模型
- **个人用户**：支持 Google One 订阅（AI Pro/Ultra），提供更多额度和高级模型
- **灵活接入**：可接入 Google AI Studio 的 API 密钥，也可自定义远程或本地模型（如 Ollama、LM Studio）
- **推荐本地模型**：Google Gemini 4——支持原生智能体工具调用、针对 Android 优化、可完全离线运行

**3. Android Bench 基准测试**
为帮助开发者选模型而推出，基于真实 Android 任务（非通用编程题），已纳入开源模型，未来将增加长时任务与智能体评估维度。访问 developer.android.com/bench 查看排行。

**4. 核心价值主张**
无论开发者选择纯 AI 智能体编码、亲手架构，还是两者结合，新工具都能提供支持；同时强调专业开发者仍需为代码负责，AI 速度之外，测试验证同样关键。

---

## 📝 完整文字稿

大家好，欢迎来到 Android 开发工具最新动态。我是 Jamal，Android 开发者体验的产品经理。>> 我是 Tor，负责 Android 开发工具与库的工程工作。>> 今天，我们来聊聊 Android 开发工具的演进。无论你是完全依赖 AI 智能体来写代码，还是亲力亲为、亲手设计应用的每一个架构细节，又或者介于两者之间——我们都会介绍最新的功能更新，助你成为一名成功的 Android 开发者，无论你采用怎样的开发方式。本次分享中，我会先讲讲我们近期的路线图，然后 Tor 会现场演示最新的工具，最后我再回来介绍一些最新动态。首先，我来聊聊你可能错过的产品路线图更新。去年 Google I/O 大会上，我们推出了 **Agent 模式（Agent mode）**，让你的开发流程从单纯的 AI 助手升级为半自主的智能体，它能借助最新的 AI 模型为你生成代码。此后，我们收到了大量积极的反馈。基于此，Android 开发工具团队改变了我们打造功能的方式——我们现在的目标是同时为两类用户服务：一是你这位 Android 开发者本人，让你更高效；二是你在代码中部署的那些 AI 智能体。我们知道，对于大多数专业的应用开发者来说，目标就是把应用或游戏发布到 Google Play，送到全球用户手中。我们会持续投入 Android 开发工具，帮助你高效地达成这个目标。作为 Android 开发者，你最终要为自己的应用代码负责。如果你的 AI 编码智能体出了错或跑偏了，受影响的是你的业务。我们清楚这份责任在你身上。所以，这里存在一个权衡：一方面是速度——你的编码智能体生成代码有多快；另一方面是准确性——你如何有信心地去测试和验证你的应用代码，避免积累技术债。在这个速度与准确性的权衡中，我们相信 Android Studio 仍然是兼顾智能体工作流和深度技术应用开发的最佳平台。虽然现在有很多开始 Android 开发的新方式（我们今天也会展示），但对于专业开发者来说，要把应用扩展到生态中的所有设备，我们仍然推荐使用 Android Studio。接下来，我来说几个你可能错过的 Android Studio Otter 版本的未来更新。首先，我们让在 Android Studio 中直接使用最新的 Gemini 模型变得更加方便。此前我们已经支持企业账号（现在叫 Gemini Enterprise），你可以在 Android Studio 里用 Google Workspace 或企业联合登录邮箱登录，通过 Gemini Enterprise 访问企业批准并托管的模型。在 Android Studio Otter 中，我们还新增了对 Google One 的支持。如果你使用个人 Google 账号开发，只要你有 Google AI Pro 或 Ultra 方案，就可以登录 Android Studio，获得比免费默认层级更多的数据额度和更高级的 Gemini 模型。对于那些需要超出 Google AI 方案限额更大额度，或者在模型选择上需要更高灵活性的 AI 重度用户，你也可以把 Google AI Studio 的 Gemini API 密钥接入 Android Studio。我们理解大家有各种各样的 AI 需求，所以我们致力于让 Android Studio 的工具对所有 Android 开发者都可用。所以在 Android Studio Otter 中，我们现在支持把自定义模型接入 Android Studio。你可以选择本地模型或远程模型。远程模型选择这个功能很实用——比如公司可能强制要求使用某个 LLM 模型，这时你就可以直接把它接入 Android Studio。说到模型选择，我们都知道市场上的能力几乎每周都在变化。所以我们最近发布了 **Android Bench**，帮你决定该用哪个模型。这个基准测试有两大特点：第一，它不是依赖通用的编程谜题或编码挑战，而是用你日常会遇到的真实 Android 任务构建的。第二，它能推动选择的多样化。随着各家 LLM 厂商针对 Android Bench 优化他们的模型，你也会看到越来越多的模型可供选择，用来开发 Android 应用。除了专有模型之外，本周我们还在 Android Bench 中加入了开源模型，让你在挑选最适合自己的模型时有更多选择。很快我们还会加入长时任务——也就是可能要花一两天才能完成的任务，以及智能体评估。这样你就能评估不同的智能体模型在各种其他模型上的表现。想了解更多关于 Android Bench 的信息，或查看最新排行榜，请访问 developer.android.com/bench。好的，看完 Android Bench 之后，如果你需要在笔记本或局域网内使用本地模型，Android Studio 也支持指向本地 LLM 运行器，比如 Ollama 或 LM Studio。这样你就可以下载社区里各种各样的开源权重模型。如果你的笔记本性能足够，我们在 Android Studio 上推荐的本地模型是 Google 的 **Gemini 4**。它有以下几个优点：一、它支持原生的智能体工具调用（agentic tool calling），也就是说它内置了推理能力，能兼容像 Agent 模式这样的功能；二、它针对 Android 做了优化，这个模型是用 Android API 和 Kotlin 编程训练的；三、它集成度高，我们确保这个模型能在 Ollama、LM Studio 等主流运行器上顺利运行。而且和别的开源模型一样，你完全可以离线运行这个本地模型，并利用笔记本的安全防护。根据 Android Bench 的结果，Gemini 4 的表现与顶级的专有模型相比也相当扎实。好的，当你连上远程或本地模型之后，它就会出现在模型选择……（录音在这里结束） 以下是这段英文的中文口语化翻译：
---
