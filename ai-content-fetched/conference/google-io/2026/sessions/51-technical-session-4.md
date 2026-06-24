---
title: Building agents with real-world reasoning
title_zh: 构建具有真实世界推理能力的智能体
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: AI/机器学习
type: 技术演讲
level: Intermediate
speakers: kwn, moreirac
video: https://www.youtube.com/watch?v=e7gFaim6vLs
---

# 构建具有真实世界推理能力的智能体

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: AI/机器学习 | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: kwn, moreirac

面向旅游、物流和消费类应用的生产级代理需要严格的真实世界推理。学习如何使用 Gemini 3、Maps Grounding Lite 和 Google Maps Platform 构建基于真实世界的投产就绪代理。探索如何将大语言模型与物理世界逻辑相连接，并了解真实世界的用例，将代理概念转化为可扩展的生产级解决方案。

---

## 📝 详细原文

旅游、物流和消费类应用的生产代理需要严格的真实世界推理。学习如何使用 Gemini 3、Maps Grounding Lite 和 Google Maps Platform 构建可靠的生产就绪代理。探索如何将大型语言模型连接到物理世界逻辑，并了解真实世界的使用案例，以将代理概念转化为可扩展的生产解决方案。

**原文（English）**: Production agents for travel, logistics, and consumer apps demand rigorous real-world reasoning. Learn how to build grounded, production-ready agents using Gemini 3, Maps Grounding Lite, and Google Maps Platform. Explore how to connect LLMs to physical-world logic and understand real-world use cases to turn agentic concepts into scalable production solutions.

---


---

### 原文

Production agents for travel, logistics, and consumer apps demand rigorous real-world reasoning. Learn how to build grounded, production-ready agents using Gemini 3, Maps Grounding Lite, and Google Maps Platform. Explore how to connect LLMs to physical-world logic and understand real-world use cases to turn agentic concepts into scalable production solutions.

---

## 📝 内容总结

**《构建具有真实世界推理能力的智能体》核心要点**

一、核心主题概述

本演讲介绍Google Maps Platform的Grounding Light MCP服务器，帮助开发者构建具备真实世界推理能力的生产级智能体。

**二、关键发布/技术要点**
- 要点1：Grounding定义——将AI推理连接到可靠事实来源，避免幻觉
- 要点2：Grounding Light三大工具——地点搜索（3亿+地点）、天气查询、路线规划
- 要点3：MCP服务器接入——任何支持MCP的工具可轻松启用
- 要点4：多智能体架构——编排器智能体+子智能体（地点、路线、天气）
- 要点5：Google ADK——Agent Development Kit管理多智能体系统
- 要点6：3D地图可视化——React Google Maps库渲染照片级真实感地图

**三、落地应用**
- 案例1：行程规划智能体验证地点营业状态和路线可行性
- 案例2：编码折线表示空间路线坐标
- 案例3：3D标记和折线元素在3D世界中放置路线

**四、总结**
Grounding是让智能体保持准确的关键。通过Grounding Light MCP服务器，开发者可轻松获取实时地理空间数据，结合多智能体架构和3D可视化，打造可靠的旅游、物流类智能体应用。

---

## 📝 完整文字稿

[音乐] 嘿大家好，我是 Ken，来自山景城的 Google Maps Platform 团队。我是 Caio，也是 Google Maps Platform 团队的成员，现在从巴西连线上线。今天，我们要在大语言模型和现实世界之间搭建一座桥梁。我们将详细介绍 Google Maps Platform 的 Grounding Light，它以 MCP 服务器的形式提供。在视频结束时，你会清楚地理解"grounding（事实锚定）"对 LLM 到底意味着什么，以及为什么智能体（agent）在没有它的情况下难以保持准确。Grounding Light 提供的具体功能，包括地点摘要、实时天气更新和路线数据。以及使用 Grounding Light 构建智能体体验的详细步骤。好了，让我们开始聊聊"grounding"这回事。我们都见过 LLM 在没人管的情况下尝试指路或查找本地商家时会怎样——它自信满满、表达流畅，但经常完全错误。在 AI 领域，我们说这叫模型在产生"幻觉"。Grounding 本质上就是把 AI 的推理和一个可靠的事实来源连接起来。它让 AI 不再是"有根据的猜测"，而是使用真实可靠的数据。Grounding Light 使用模型上下文协议（MCP），让你的 AI 应用可以轻松地直接从 Google Maps 获取可靠的地理空间数据。你可以在任何支持 MCP 服务器的工具中启用 Grounding Light 立即开始使用。基本上，你不需要经历什么复杂的设置流程，就能把实时的权威位置信息集成到你的工作流中。Grounding Light 给你的 LLM 提供三个主要工具：地点搜索——使用超过 3 亿个地点的庞大全球数据库查找兴趣点；天气查询——获取当前天气状况和预报，让你的智能体可以提醒你出门散步是否需要带伞；路线规划——计算步行或驾车距离及旅行时间，让你的智能体更好地理解时间和距离。现在，来看看到底怎么用这个工具来开发。我们建议使用多智能体编排器架构来构建一个健壮的系统。主智能体是编排器智能体，它负责控制流程并持有全局工具，比如你的地图可视化函数。然后它把特定任务委派给子智能体。要深入了解细节，我把镜头交给 Caio。谢谢 Ken。对于后端引擎，我们为开发者设定了三个关键学习目标：第一，构建一个具有韧性的多智能体系统，专注于创建一个健壮可靠的架构；第二，使用 Grounding Light 消除 AI 幻觉，帮助模型保持准确；第三，利用 Grounding Light 的数据打造沉浸式体验，为 3D 地图增添信息。现在我们来看看真正的引擎。如果你花过时间用标准模型，你可能熟悉"一个巨型 prompt"的方法——试图把所有的指令都塞进一个系统 prompt 里。这种架构是有局限性的。当涉及空间智能时，多智能体系统是一种更有效的策略。我们不再强迫一个模型做所有事情，而是把"在纽约规划一整天"这种复杂问题拆分成更小的独立任务。然后我们把这些任务交给并行工作的子智能体。这是构建更快、更可靠、最终更具可扩展性的方式。为了管理这个架构，我们使用了 Google ADK——智能体开发工具包。ADK 后端的核心是编排器，你可以在源代码里找到它，它就叫 orchestrator_agent。每当有行程规划请求时，编排器就会启动一组协同工作的子智能体工具。首先出场的是地点智能体（place agent）。它是我们主要的验证者，负责确认每一个站点都是经过验证的真实地点——不仅检查该地点是否存在，还要确认它在计划造访时确实开门营业。接着是路线智能体（route agent）。如果站点之间在物理上根本来不及按时到达，那这个行程也没多大意义。所以这个智能体负责处理从 A 点到 B 点的所有出行安排。如果某个地点在计划时间无法造访，编排器智能体会建议其他备选方案。我们还有天气智能体来帮你关注是否会下雨。Ken，这让我想起你借我伞然后弄丢了的那次。如果你要问任何 AI 一个特定的咖啡馆是否真的开门营业，你肯定不希望它基于过时的训练数据来猜。为了确保我们智能体的回复是最新数据，我们使用了 Maps Grounding Light。通过这样做，我们基本上是在确保模型只在掌握了已验证的真实世界事实之后才开口说话。每当我们的编排器智能体需要确认一个地点——比如某家餐厅或公园是否适合带小孩——Grounding Light 就会介入。它在后台向 Google Maps 平台发出实时调用，然后把实时数据直接喂给模型的上下文。这才是构建企业级工具所需信任度的方式。Grounding 确保了像当前营业状态、用户评分和营业时间[音频在此处中断] 好的，我帮你把这段内容完整翻译成中文口语版本：

---

地点上的具体细节信息能保持最新。不过，光是找到一个地方，其实只解决了后勤难题的一部分。真正重要的，也是最关键的部分，其实是能不能准时到达那里。这才是我们路径智能体真正大放异彩的地方。

我们的路径智能体非常依赖 Grounding Light 直接返回的路径数据。当智能体规划好一条路线后，Grounding Light 会返回两点之间最短路径的编码折线。如果你之前没接触过这个，编码折线本质上就是一个压缩字符串，代表了一条空间路线或路径的坐标。我们之后在前端把这个字符串解码出来，就能在地图上完美地给用户画出这条路线。

我的后台助手团队整理了规则、检查了地点，还拿到了精确的路线细节和路径信息。我把所有这些有用的信息打包进了一个简单的 JSON 文件里。但光有原始数据，用户体验并不好。为了展示我们是怎么呈现这些智能信息的，我把画面交回演播室，让大家一起看视觉效果。

谢谢，Kyle。那我们接下来看看怎么用 Maps 和 Vis GL React Google Maps 库，把这些 Grounding Light 的返回结果变成沉浸式的 3D 体验。React Google Maps 库是一套高性能的 React 组件，让 Maps JavaScript API 用起来就像 React 应用自带的功能一样。而其中的明星功能，就是照片级真实感的 3D 地图。

用 3D 地图组件，我们看到的就不只是一张俯视图，而是在实时调用 Google Maps 的 3D 建模。这意味着我们不仅可以在平面地图上放东西，还可以在 3D 世界里放到特定的高度。我们来看看怎么把这些子智能体的返回结果渲染出来。

这里有两个主角：3D 标记元素和 3D 折线元素。当你的地点智能体返回图森市的一家墨西哥卷饼店时，你会得到一个地点 ID 和精确的坐标。下面就是我们怎么在上面放一个真正属于 3D 环境的 3D 图钉。通过把高度模式设置成“相对于地面”，我们就能确保标记刚好落在建筑物所在的水平面上，而不是埋在地形里。我们还把拉伸属性设成 true，这样就会从图标往下画一条垂直的牵引线一直到街道，即使用户在城市里高速飞行时也能一眼看清楚。

接下来，当路径智能体给出从 A 点到 B 点的路线时，我们用 3D 折线元素来画。我们甚至可以让它支持遮挡，意思就是如果中间有建筑挡着，路线会智能地画在建筑后面。在 3D 地图里这点特别关键，因为它能避免你的路线直接穿墙而过、穿过实体高楼，保持那种真实的物理深度感。有了遮挡功能，地图引擎就能处理好那些复杂的几何关系，让你的路径完美地绕着城市建筑走、跨过地形特征。

交回给你，Caio。

好，我们退一步来总结一下今天到底完成了什么。我们从一个简单的想法出发——每天核对日程表上的地点清单——然后用 Google Maps Platform 把它彻底改造了一遍。

在后端，我们摆脱了又大又脆弱的提示词。通过采用 Google ADK 和 Gemini 工具调用，我们把逻辑拆分到了不同的 AI 智能体上。再通过使用 Maps grounding light，我们彻底消除了基于位置的幻觉，确保模型只严格按照地理空间事实来运行。

在前端，我们把所有这些支持实时路况的坐标直接叠加显示在照片级真实感的 3D 地图上。对于各地的开发者团队来说，把有根据的智能和真实世界的可视化结合起来，就是把生成式 AI 安全地应用到企业生产环境的关键。

把 Gemini 强大的推理能力和 Google Maps Platform 绝对的真实地理数据结合起来，你做的就不再只是一个简单的地图应用了，而是在打造真正的交互式空间智能。

最后来总结一下今天讲到的内容：我们看了 grounding 对大语言模型来说到底意味着什么，以及为什么它对准确性如此重要。我们也完整走了一遍在多智能体架构里怎么实际使用 Maps grounding light。

我向在座的各位发起一个挑战：把这些概念拿去用，试试我们的资源，看看你们能做出什么来。今天讲到的所有内容，你都可以在 AI Studio 里找到完整的源代码。你甚至可以重新混合改造成你自己的项目。欢迎直接到我们的 Discord 上联系我们，分享你们的成果。

非常感谢大家抽出宝贵的时间。对了 Caio，我可没弄丢你的雨伞，我把它开源了。我把它放在了一个能让整个社区都受益的地方。祝大家玩得开心，地图绘制愉快！

---

这样翻译下来应该比较顺口自然，你可以直接拿来当中文演讲稿或者讲解视频的字幕使用~
---
