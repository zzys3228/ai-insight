---
title: Build next-gen AI experiences with Google AI Studio and Google Antigravity
title_zh: 使用 Google AI Studio 和 Google Antigravity 构建下一代 AI 体验
category: conference/google-io/2026/sessions
date: 2026-05-19
time: 16:30 - 17:15 PT
track: AI/机器学习
type: 技术演讲
level: Intermediate
speakers: aramacha, joanafilipa
video: https://www.youtube.com/watch?v=orudZzP8vUc
source: io.google.com
translated: true
fetched_at: 2026-06-24T10:00:00
---
# 使用 Google AI Studio 和 Google Antigravity 构建下一代 AI 体验

## 📋 演讲摘要

**📅 日期**: 2026-05-19 | **🕐 时间**: 16:30 - 17:15 PT | **📂 分类**: AI/机器学习 | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: aramacha, joanafilipa

探索从AI Studio快速探索到Antigravity自主开发的转变，展示如何从Prompt到App快速实现，包括Google Workspace集成和Cloud Run一键部署功能。

---
## 📝 内容总结

**会议演讲总结（约200字）**

本演讲由Google V团队产品经理Sona Karashkevich和反重力（Antigravity）项目负责人Mitchell共同主讲，主题聚焦于Google AI Studio与Google Antigravity的最新进展。

**核心要点：**

1. **使命愿景**：Google DeepMind致力于负责任地构建AI，让技术造福全人类，无论地域或语言。

2. **生态升级**：Google AI Studio正从单纯的模型测试Playground，进化为"一站式"开发平台，集成Google Workspace和Cloud Run一键部署功能，实现从Prompt到App的最快路径。

3. **智能体赋能**：平台引入多种智能体（如数据分析师、客服、文档处理等），帮助开发者快速完成复杂任务。

4. **快速迭代**：团队以极高速度推出新功能，大量改进源自开发者社区反馈。

5. **现场演示**：以"开宠物寄养酒店"为案例，展示如何借助"研究智能体"进行市场调研，体现AI Studio的实用性与易用性。

**核心要点：AI Studio进化为一站式开发平台、智能体赋能、快速迭代、现场演示展示市场调研能力**

---

*原文请访问 [Google I/O](https://www.youtube.com/watch?v=orudZzP8vUc)*

[音乐] 大家好啊！嗨，你们怎么样？好，好，这才对嘛。会场气氛怎么样？大家好，我是 Sona Karashkevich，是 Google V 团队的产品组经理。你们可能今早也看到过我们的节目了。我是 Mitchell，我负责反重力（anti-gravity）项目。好的！接下来我们要给你们讲讲 Google AI Studio 和 anti-gravity 都有哪些新东西。就在我们上台之前，Amar 和 Paige 已经带你们全面体验了 Google AI Studio。现在我们要再讲深一层。这安排可以吧？听起来不错，我觉得大家应该都准备好了。准备好了吗？好的，那我们就正式开始！准备好了吗？好嘞！

在 Google DeepMind，我们的目标是负责任地构建 AI，让它造福全人类。我们做的每一件事都是围绕着这个目标。我们始终要确保，我们构建的所有东西——无论是模型、产品还是服务——都能让每个人受益，让每个人无论身处何地、说什么语言，都能从我们的技术中获得良好的体验。带着这个非常宏大的目标，我们在 DeepMind 做了非常多不同的事情，把最好的、最棒的都推向市场。现在我们正处在一个非常特殊的时代——你们什么都能造出来。在这个什么都能造出来的时代，软件开发的那套规则已经被重新改写了。要做什么、怎么做，都在发生翻天覆地的变化，而你们怎么应对，真的非常重要。所以这就是为什么在 Google，我们搭建了一个技术栈、一个生态系统，让你们能根据自己想打造的不同体验，拿到对应的工具。我们有非常强大的生态系统，能让你从探索到开发，再到云端，再到云端部署，一路走得非常顺滑。我们的产品永远都由最新、最强的模型驱动。

所以，Google AI Studio 现在正在变成一个"一站式"的地方——你可以在 Playground 里找到模型，还有可以帮你打造体验的智能体，我马上就会展示给你们看。但现在我们还在做更多产品集成。你们已经听说过的，Google Workspace 集成要进 AI Studio，Cloud Run 要进 Antigravity。所以，Google 的整个生态系统正在越建越完整，不管你想做什么，它都能给你一个解决方案。我们经常说，Google AI Studio 真的是从 prompt 到 app 的最快路径，真的是这样。马上我就给你们演示一下。这就是 Google AI Studio 现在的样子和真正内涵。它已经进化了太多太多。就在几年前，我们展示的 Google AI Studio 还只是一个让你试用、测试模型和不同能力的 Playground；现在它已经变成了一个你不仅能尝试自己的想法、还能把应用一键部署到 Cloud Run 的地方。我们一直在做更多这类产品集成，比如我之前提到的 Google Workspace，还有 Cloud Run 的一键部署等等。我们正在打造一个非常强大、非常贴心的产品，让你们能造出任何你们想造的东西。团队的迭代速度简直不要命。我们说这句话，是认真的，你得信我。一切发生得太快了。新东西几乎每天都在上线。我就想把这次 IO 大会上我们宣布的所有东西列出来给你们看看，让你们知道我们每天爱用的这些产品，背后到底有多少工作量。从移动应用，到直连部署到应用商店，到 Google Workspace 集成，到 Google 反重力编程智能体……每天都有太多太多的新东西涌进我们的产品里。这里面很多都来自你们的反馈——开发者社区一直在告诉我们哪里要改进、怎么改进才能让你们有更好的体验。

不过，光在屏幕上给你们看，还不如直接上我电脑，给你们演示一下它到底是怎么在 Playground 里跑的。可以吗？好，那我们开始！打开笔记本，进入 Playground，好嘞，到了。这就是 Google AI Studio 的样子。Paige 和 Omar 已经给你们做了非常深入的讲解，所以这块我就不啰嗦了。我就想带你们看看 Playground——这里有我们的模型、有我们的新智能体，而且现在有越来越多不同类型的智能体进驻 AI Studio。比如，有一个我特别喜欢的，就是数据分析师。还有一堆其他的，你们都可以去试：客服智能体、文档处理智能体……不管你想做什么场景，都有合适的智能体。今早你们可能看到 Josh 在台上介绍了 Louis Cinnamon。还记得吗？对吧。他的故事真的让我很受触动——他得给宠物找寄养酒店，这样出门度假时宠物才安全。所以我就有了一个想法：要不我干脆自己开一家宠物店吧，开一家能接待所有宠物、让它们来寄养的酒店。但问题是，我对宠物店生意一窍不通。你们有人懂吗？有人能帮我吗？没有？没关系！好在 AI Studio 里就有智能体，我可以请它们帮忙。所以我已经准备好了一段 prompt，我之前还在 Gemini app 里精修过。我要用这段 prompt 请"研究智能体"帮我做点市场调研，看看我这个点子在湾区到底行不行得通。我的 prompt 是这样的：你是湾区的顶级零售市场分析师，专长是……

（到这里内容就被截断了，完整的 prompt 后面应该还有。）
---
