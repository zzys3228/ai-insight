---
title: Develop and integrate AI agents with Google Workspace
title_zh: 在 Google Workspace 中开发和集成 AI 代理
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: 云
type: 技术演讲
level: Intermediate
speakers: pierrick
video: https://www.youtube.com/watch?v=erRPuV1EQ_c
---

# 在 Google Workspace 中开发和集成 AI 代理

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: 云 | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: pierrick

将您的 AI 代理的功能扩展到 Google Docs、Google Chat 和 Gmail。探索 Google Workspace 开发者平台，了解如何构建能够充当自定义应用程序与 Google Workspace 生态系统之间无缝桥接的代理。

---

## 📝 详细原文

将你的 AI 代理的能力扩展到 Google Docs、Google Chat 和 Gmail。探索 Google Workspace 开发者平台，了解如何构建能够在你自定义应用与 Google Workspace 生态系统之间实现无缝桥接的代理。

**原文（English）**: Extend your AI agent’s capabilities into Google Docs, Google Chat, and Gmail. Explore the Google Workspace developer platform and discover how to build agents that act as a seamless bridge between your custom application and the Google Workspace ecosystem.

---


---

### 原文

Extend your AI agent’s capabilities into Google Docs, Google Chat, and Gmail. Explore the Google Workspace developer platform and discover how to build agents that act as a seamless bridge between your custom application and the Google Workspace ecosystem.

---

## 📝 内容总结

**《在 Google Workspace 中开发和集成 AI 代理》核心要点**

一、核心主题概述

本演讲介绍如何将AI智能体能力扩展到Google Workspace，探索开发者平台各层能力及集成方式。

**二、关键发布/技术要点**
- 要点1：Google AI生态系统多层架构——从基础设施到智能体和应用程序
- 要点2：三大核心支柱——数据、动作、接口
- 要点3：Workspace AI功能——AI概览、线程摘要、侧边栏Gemini提问、会议笔记
- 要点4：NotebookLM——AI研究伙伴，基于用户提供的可信信息工作
- 要点5：Workspace Studio——构建AI驱动个人工作流
- 要点6：MCP服务器——Workspace工具供智能体调用
- 要点7：Gemini Enterprise Agent Platform——企业级智能体构建部署平台
- 要点8：A2A协议——智能体间通信标准化

**三、落地应用**
- 案例1：差旅管家智能体在Gmail侧边栏帮助规划行程
- 案例2：智能体自动更新Drive文件、处理Gmail紧急请求
- 案例3：智能体监控Docs并通过Chat通知相关人员

**四、总结**
Google Workspace与Google AI深度集成，为开发者提供了从数据访问到智能体部署的完整工具链。通过MCP服务器、Agent Platform和Add-ons，开发者可轻松构建连接企业工作流的智能体。

---

## 📝 完整文字稿

好的，我来用中文口语完整翻译这段内容：

---

[音乐] >> 大家好，我叫Pyarek。今天我们要来探索一下Google Workspace和Google AI是如何结合在一起，实现日常工作流和自动化中的智能代理（agents）功能的。

AI的竞赛并没有放缓，整个领域也在不断演进。感觉每周都有重大的模型、概念、工具、产品协议和框架发布。我们现在已经超越了大多数人熟悉的聊天机器人阶段。这些创新让构建、部署和发布生产级的智能代理变得越来越简单，无论是为了个人使用还是组织使用。

想象一下：如果在命令行界面（CLI）中拥有你自己的智能代理，在你处理问题时能自动用最新的文档更新Drive文件，会怎么样？如果拥有一个能处理收到的Gmail邮件中的紧急请求，并自动在日历中预留时间的代理，会怎么样？如果你的组织能提供一个监控Google Docs并根据角色通过Google Chat通知相关人员的代理，又会怎么样？

嗯，Google Workspace和Google AI让这一切成为可能。

Google的AI生态系统由多个层次组成，从基础设施一直延伸到智能代理和应用程序。这让任何人都可以从任何地方集成各种形式的解决方案。如果你是普通用户，可以使用现成的代理；如果你是构建者，可以使用代理设计器来构建；如果你是开发者，可以使用框架和工具来开发代理；如果你是服务提供商，可以在Google Cloud Marketplace上发布代理；如果你是IT管理员，可以限制用户访问可信的代理和工具。我想你应该明白我的意思了。

但是你知道吗？归根结底，所有AI解决方案仍然是软件。它们的执行方式和依赖的技术确实和以前不同，但它们的潜力仍然依赖于三个核心支柱，就像任何其他软件应用程序一样：**数据、动作和接口**。

现在，你是否知道一个被数十亿用户和数百万组织信赖的平台，用于日常协作、生产力和完成任务？没错，那就是Google Workspace。

它包含Drive，用于查找、共享和管理文件；包含Docs、Sheets、Slides和Forms，用于实时协作和共同编辑；包含Chat和Meet，可以从任何设备连接；包含Gmail和Calendar，让你随时掌握动态；还有许多其他应用，如Classroom、Sites、Keep、Tasks和Vault。

在过去的几年里，许多这些应用程序越来越多地融入了AI辅助功能。我个人最喜欢的两个功能是Gmail中的AI概览（AI overview）和邮件线索摘要（thread summaries），以及侧边栏中的"向Gemini提问"（ask Gemini）。

如果你隶属于某个组织，你可能还可以通过Gemini in Workspace访问更多AI功能。我个人非常依赖Meet中的"为我做笔记"（take notes for me）功能。我现在可以100%专注于讨论，如果有会议冲突，稍后还可以补上。

说到AI原生应用，Workspace去年增加了NotebookLM，今年早些时候又增加了Workspace Studio。

NotebookLM是一个AI研究和思考伙伴，它基于用户提供的可信信息（如财务报告、市场分析或内部战略文档）来工作。它可以以多种格式创建资源，例如概览、幻灯片或信息图表。

另一方面，Workspace Studio使用户能够通过构建、管理和分享由"启动器"和"步骤"组成的个人AI驱动工作流来简化和管理任务。在这里，我创建了一个工作流，每天自动向我发送Google Chat新闻摘要。看看这个流程如何依赖AI驱动的步骤。"向Gemini提问"步骤依赖于网络搜索来获取最近的新闻，但也可以依赖其他来源并做出更复杂的决策。

此外，这个流程是我自己的，而且可以编辑，所以我可以根据需要随时控制和调整它，比如添加新步骤。

那么，如果Workspace提供的AI解决方案不够用怎么办？在这种情况下，你可以加入现有数千名Workspace开发者的行列，开始构建自己的自定义解决方案。

你可以使用AppSheet采用无代码方法，使用App Script采用低代码方法，或者使用任何其他技术栈采用专业代码方法。还有丰富的API和库可以代表用户检索数据和执行操作，例如访问Gmail邮件或创建日历事件。

在这个具体例子中，我有一个Agent Development Kit（智能代理开发工具包）函数工具，可以为用户创建日历事件。

大多数Workspace应用程序的用户界面都可以使用插件进行扩展，因此可以在用户所在的地方满足他们的需求。在这个例子中，用户在Gmail中打开侧边栏，让他们的差旅管家代理根据当前打开的邮件中的信息来规划行程。然后，如果他们同时还有其他讨论需要处理，他们可以决定切换到Chat。

Google还在持续发布新的模型上下文协议（Model Context Protocol）服务器以及Cloud和Workspace相关的工具，你也可以依赖这些工具。它们专门用于智能代理……

（音频在此结束）

---

这是完整的中文口语化翻译，希望能帮你更好地理解内容！ 好的，我用比较口语化的中文来翻译这段内容哈：

它们用起来比自己去手写 API 包装器要简单得多，也安全得多。值得注意的一点是，这一切其实跟前端客户端是没啥关系的。你并不一定非得用 Google 的那一整套 AI 技术栈，才能去构建依赖这些功能的自定义解决方案。不过话说回来，如果你真用 Google 的技术栈，它会自带一些产品和小工具，让你在搭建能跟 Cloud 和 Workspace 打通的智能体（Agent）时更省事。开发者可以把 Gemini CLI 和 Antigravity（反重力）跟 Google 自带的或者自己搞的 MCP（模型上下文协议，简单的理解就是让 Agent 能调用外部工具和数据的一个标准接口）组合起来，去编排那些能连接本地开发环境跟企业实时数据的工作流。这里 Antigravity 就配了 Workspace 的 MCP 工具，这样智能体和技能在需要的时候就能直接用上这些工具。举个例子，一个智能体干完活儿之后，可以自动往某个指定的聊天群里发一条消息。智能体开发者也完全可以直接用 Workspace 的 MCP 工具。ADK（Agent Development Kit，Agent 开发工具包）这个框架就能很方便地实现这一点，你只要把工具注册进去，然后在指令里写清楚啥时候用、怎么用就行了。

技术栈的下一层就是 Gemini 企业级智能体平台。这是个统一的平台，专门用来在 Google Cloud 上从零开始构建、部署、管理、规模化生产企业级的模型和智能体。它自带一百五十多个预训练好的模型，里面当然也包括 Gemini 系列，同时你也支持用自己的模型去做微调、训练、跑实验这些操作。智能体设计器和智能体运行时这些工具，让开发者能基于开源框架、对话会话、记忆功能、MCP、代码执行等等，搭建出能协同工作的智能体。治理和监控方面的工具呢，能让你持续不断地去观察效果、做评估、发现问题、追踪链路。搜索工具则支持 RAG（检索增强生成，简单说就是让大模型在回答前先去查相关资料）、向量搜索和 AI 搜索这些玩法。其实在 Workspace 这个场景下，智能体平台的搜索功能是个特别关键的集成点，因为现在已经有针对 Gmail、Chat、Drive、日历还有通讯录这些的连接器了。这么一来，智能体开发者就能在程序运行的时候，通过专门的智能体搜索 API 或者 Google 自带的 MCP 服务器，去搜用户的工作数据了。ADK 框架跟上文一样，只要把工具注册一下，在指令里讲清楚使用场景和方式就行了。

哎，你有没有发现我到现在都还没聊用户界面（UI）这块？那是故意的哈，因为在智能体平台里压根就没有自带 UI 的，你得自己调 API，然后把智能体接到你自己写的界面里。在 Workspace 这个场景下，咱们可以用插件（Add-ons）来实现。你之前已经见过那个"差旅管家"智能体了，它就是个特别好的例子。它就是用 App Script 写的一个插件，底层调用的是智能体平台的 API 来管理会话和对话轮次。我们专门做了一个实操代码实验室（Codelab），里面一步步教你怎么搭建这种智能体，有兴趣的话可以去看看。

要是你不想自己搞 UI 去接智能体，那就可以用技术栈最上面那一层——Gemini Enterprise。它的目标是让公司里每个员工、每种业务场景都能享受到 Google 最顶级的 AI 服务。它的 Web 应用是实现这个目标的一个核心组件，但 Gemini Enterprise 可不止是个 Web App 那么简单，它其实是一个完整的平台，能在整个企业范围内发现、创建、分享、编排各种智能体，而且底层有安全的基础设施，还有企业全局的业务上下文做支撑。它自带安全管控相关的治理能力，各种类型的智能体都能用：不管是无代码、低代码还是专业代码开发出来的都行；不管是 Google 官方出的、公司内部自己搭的、合作伙伴做的还是第三方开发的，都支持；而且不管这些智能体是跑在哪儿、用的是不是 Google 的 AI 技术栈，都能整合到一起用。

在 Cloud Console（Google Cloud 的管理后台）里，管理员可以配置数据存储。这里给你看个例子，就是把 Workspace 的数据存储连到一个 Gemini Enterprise 应用上。管理员还可以通过 A2A 协议（Agent-to-Agent，智能体之间的通信协议）或者 Cloud Marketplace，把跑在任何智能体平台上的智能体注册进来。这些智能体可以调用基于 Workspace API 或者是 Google 自带 MCP 的工具，并且统一用 Gemini Enterprise 的身份认证机制。

在 Gemini Enterprise 的 Web 应用这一端，用户则可以跟管理员配置好的智能体、模型、工具和数据存储进行交互。用户自己也能通过智能体设计器，用自然语言提示词或者手动编辑的方式，搭一个只属于自己用的无代码智能体。比如我现在演示的这个，就是依赖 Drive 连接器工具搭出来的。

那如果你想把 Gemini Enterprise 的智能体直接嵌到 Workspace 应用的界面里去用呢？办法跟之前接智能体平台上的智能体差不多——你得去调 Gemini Enterprise 提供的 API。我们也做了一个专门的 Codelab，把这个事讲得清清楚楚的，一步一步带着你做，有空可以试试看。

好的，上面讲的这些东西现在都已经能用得了。不过你可能也会好奇，接下来还会有啥新东西。我建议大家可以重点关注这几块：连接器和 MCP 服务器——它们能让智能体调用越来越多的工具；A2A 协议和 Agent-to-UI 协议——它们能把智能体之间的通信、还有那种能根据需要动态生成的界面给标准化，以后大家协作和分发智能体会更方便；还有像 Gemini Live 这种全双工的模型——能解锁一大堆全新的交互方式和应用场景。 最后但同样重要的是，技能（skills）。它们越来越受欢迎，而且已经证明是对智能体（agent）MCP 工具的一个很好的补充。我在这里再分享几个有用的链接，帮大家入门。祝大家探索这些工具和解决方案玩得开心。下次再见，咱们线上见！
---
