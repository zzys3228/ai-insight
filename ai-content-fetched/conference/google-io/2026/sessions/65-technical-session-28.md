---
title: Build agent-native apps with Firebase and Google AI
title_zh: 使用 Firebase 和 Google AI 构建原生代理应用
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: 云
type: 技术演讲
level: Advanced
speakers: karay, samphillips
video: https://www.youtube.com/watch?v=nq55ERaUQpw
---

# 使用 Firebase 和 Google AI 构建原生代理应用

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: 云 | **🎯 类型**: 技术演讲 | **📊 等级**: Advanced

**👤 演讲者**: karay, samphillips

使用代理原生开发将原型转化为可投产的应用，充分利用与 Firebase、Google AI Studio 和 Google Antigravity 的深度集成。了解 Firebase 如何让编码代理处理构建强大后端的最困难部分，包括配置数据库、实现用户身份验证、管理安全性以及无需手动配置即可部署应用。

---

## 📝 详细原文

使用原生代理开发，将原型转化为生产就绪的应用，深度集成 Firebase、Google AI Studio 和 Google Antigravity。了解 Firebase 如何帮助编程代理处理构建稳健后端中最困难的部分，包括配置数据库、实现用户身份验证、管理安全性以及无需手动配置即可部署应用。

**原文（English）**: Transform prototypes into production-ready apps with agent-native development, leveraging deep integrations with Firebase, Google AI Studio, and Google Antigravity. Learn how Firebase empowers coding agents to handle the toughest parts of building a robust backend, including provisioning databases, implementing user authentication, managing security, and deploying apps without manual configuration.

---


---

### 原文

Transform prototypes into production-ready apps with agent-native development, leveraging deep integrations with Firebase, Google AI Studio, and Google Antigravity. Learn how Firebase empowers coding agents to handle the toughest parts of building a robust backend, including provisioning databases, implementing user authentication, managing security, and deploying apps without manual configuration.

---

## 📝 内容总结

**《使用 Firebase 和 Google AI 构建原生代理应用》核心要点**

一、核心主题概述

本演讲展示Firebase与Google AI Studio的深度集成，帮助开发者将原型快速转化为生产级应用。

**二、关键发布/技术要点**
- 要点1：Firestore全文搜索——新Search API支持任意数据查询和相关性排序
- 要点2：AI Studio Firebase集成——一键添加Firestore和身份验证
- 要点3：Firebase蓝图文件——记录应用架构和数据模型
- 要点4：自动安全规则生成——AI Studio生成并部署规则
- 要点5：实时同步和离线支持——默认提供，无需额外开发
- 要点6：一键部署Cloud Run——从AI Studio直接发布到生产
- 要点7：Firebase Skills——在Antigravity、Cursor、Cloud Code中使用
- 要点8：小程序应用画廊——可改造现有应用或从提示词开始

**三、落地应用**
- 案例1：团队规划看板App——从提示词到完整应用
- 案例2：添加Firestore后团队成员可共享项目状态
- 案例3：几分钟内完成带数据库和登录的全栈应用

**四、总结**
Firebase与AI Studio的结合让原型到生产的路径变得极短。通过一键配置Firestore、Auth、安全规则和部署，开发者可快速构建可扩展、实时同步的应用。Firebase Skills让本地IDE也能享受同样的便利。

---

### 原文

**一、Firebase 核心能力**
- 数百万活跃开发者
- 无服务器架构，Google Cloud 支持
- 实时同步、离线支持、自动扩展

**二、Firestore 新功能**
- 全文搜索 API：支持任意数据查询
- 相关度评分：按相关性排序

**三、AI Studio + Firebase 集成**
- 从 prompt 到生产最快路径
- 一键配置 Firestore 和身份验证
- 自动生成 Firebase 蓝图和安全规则

**四、演示案例**
- 团队规划看板应用（几分钟完成）
- 实时多人协作、数据共享
- 一键部署到 Cloud Run

**五、Firebase Skills**
- 支持 Antigravity、Cursor、Cloud Code

**总结**
Agent-native 开发让原型直接变生产应用。

---


## 📝 完整文字稿

[音乐] >> 大家好，我是 Cara，今天我要向你展示 Firebase 和 Google AI Studio 如何帮你把任何 app 创意变成现实。我是 Sam，我也会一起帮忙操作。首先，在我们进入演示之前，先来回顾一下 Firebase 是什么。Firebase 是 Google 的应用开发服务套件。我们帮助移动端和网页端的开发者构建、发布并增长他们的应用。使用 Firebase，你可以借助 AI 加速应用开发，发布后还能通过测试和监控提升应用质量。最后，你还可以通过分析和消息推送工具来提升用户参与度。Firebase 目前有数百万活跃开发者。Firebase 让构建应用变得简单。我们安全的客户端 SDK 让你可以在网页和移动端平台上构建应用，同时共享云端同一个后端。你可以从客户端只写一次应用逻辑。使用 Firebase Auth，你可以轻松实现用户登录并管理用户对后端的访问。还有实时同步和离线支持这些开箱即用的功能。还不止于此。你不需要担心扩展问题。Firebase 是无服务器的，背后由 Google Cloud 提供支持。应用会随着你的用户量自动扩展，你完全不需要操心。最后，AI 能力是我们服务的核心部分，Firebase 让集成 Gemini API 调用、把向量嵌入存入数据库等操作变得轻而易举。还有一个好消息！我非常激动地宣布 Firestore 现在支持全文搜索了。我们有了一个全新的搜索 API，让你可以针对任意数据（包括字符串）查询文档。搜索查询会返回文档以及相关度评分，这样你就可以按相关性对文档排序。我们还在 API 里加了一些好用的控制选项，让你能够控制检索深度、排序方式以及是否包含同义词。这些都是对 Firestore 很大的改进，我们在 Google AI Studio 里也同样提供了这些功能。Google AI Studio 是 Google 让你从 prompt 到上线最快的方式。AI Studio 是一个"氛围编程"（vibe coding）解决方案，帮你用 Google 最新的 Gemini 模型构建和部署应用。AI Studio 能用智能上下文管理和编码最佳实践来帮你写 prompt，所以你可以用自然语言来构建应用。用 AI Studio 构建应用很棒，但当你想存储数据，或者让用户登录并拥有自己的账号时该怎么办？这就是我们把 Firebase 集成进 AI Studio 的原因。如果需要的话，AI Studio 可以帮你搭建 Firestore 和 Firebase 身份验证，把你的原型变成一个真正可以面向用户的应用。嘿 Sam，说真的，我其实有点压力。我们一直在筹备这个演讲，事情太多了，我都搞不清楚我们是不是落后了。更别提我还想确保我们记得庆祝每一个里程碑。我们能不能做一个东西来帮帮忙？嘿 Kara，当然可以。那我们来做一个 app 吧。我喜欢这些新 AI 工具的地方在于，它们让开发应用变得平易近人得多。它打开了很多以前觉得太重或太复杂而不敢想 的可能性。Kara 和我这些年在 Firebase 一起做过很多项目，我们用各种方式跟踪过进度。用过计划加文档，计划加电子表格，计划加 bug 和评论。有一次，我们用我写在一张收据上的计划来跟踪一个项目。但我个人最喜欢的是看板。我喜欢把卡片从"想法"拖到"进行中"，再从"进行中"拖到"已完成"。要不我们就专门为这次演讲做一个自己的进度跟踪工具？我现在在 Google AI Studio 里，这里有一个输入框，我可以输入我的想法，然后让 Gemini 来搞定剩下的。我们来试试看吧。我这里提前写好了一段 prompt。我把它粘贴进去，一边让模型跑起来，一边念给大家听。我们来做一个团队规划应用来规划项目。做成看板样式。让用户创建项目，然后在项目里创建任务，并把任务在"待办"、"进行中"和"已完成"之间拖动。当一个项目里所有的任务都完成时，来一个有趣的庆祝效果。先从简单的开始，不要额外的集成。点一下"构建"，Gemini 就开始干活了。AI Studio 把我带进了开发环境，Gemini 在这里解读这些产品需求并搭建应用。在这个聊天窗口里，我可以看到正在做的修改，包括它的思考过程和需要做的准备工作。接下来，它会安装必要的包并给应用起个名字。我很喜欢看这些小细节，能看到它是如何一步步思考问题的，考虑需要哪些功能，搭建核心功能。在这个过程中，我能看到代码开始出现，比如把任务和项目类型作为核心数据结构创建出来。当更多代码写好之后，我可以切换到预览模式实时查看应用效果。就这样，我的全新团队项目跟踪器就出来了。我们来试试看它好不好用。我创建一个新项目，叫"测试一下新的项目跟踪器"。现在我可以创建一个测试任务……（音频在此处结束） 好的，就像试用一下。看，它就在待办列表里了。我可以把它从待办拖到进行中。我把窗口拉宽一点，这样所有行都能看到。然后我把它从进行中拖到已完成。哇，还出现了一个超酷的庆祝动画！这个项目追踪器看起来运行得不错，但目前它只能一个人用。如果我想跟我的团队一起共享呢？借助 Firestore 和 Firebase 身份验证，我们可以加一个后端数据库和登录流程。这样我团队里的人就能用各自的账号登录，看到一模一样的项目视图。我们现在就来试试，只要输入“给这个项目加上 Firestore，把进度存到数据库里”。AI Studio 识别到了这个请求，然后弹出了一个专门针对这种情况的对话框。里面详细说明了它打算怎么用 Firestore 存数据，然后就开始了 Firebase 的配置流程。在后台，它其实做了好几件事来让这个功能跑起来：如果还没有 Firebase 项目，它会创建一个；开通 Firestore 服务；开启支持 Google 登录的 Firebase 身份验证。然后它会把所有这些配置自动写进这个小程序里。在它操作的过程中，你能在代码视图里看到一个个新文件被创建出来。其中很关键的一步是，它生成了一个 Firebase 蓝图文件。这个蓝图会记录下应用的架构，包括小程序里用到的所有数据模型和数据结构。AI Studio 还会自动生成安全规则，并部署到数据库上。数据库配好之后，它会把身份验证也接好，这样每个用户都能登录，然后看到属于自己的个性化界面。看起来生成已经完成了。我们来试试看吧。我新建一个项目，就叫“试用版本二”，然后建一个任务，发给 Cara。我们看看这样行不行。我点一下分享按钮，把这个小程序分享给 Cara。谢谢 Sam，我来手机上试试。好的，我正在登录。我切到 Sam 刚才那个叫“试用版本二”的项目里。我现在看到那张“发给 Cara”的卡片了。我点一下“开始任务”，把它拖到进行中。然后我把它标记成完成。看到没，项目进展一目了然，太方便了。而且你看，你刚做的修改也实时同步到我屏幕上了。就这么几分钟，我们就用 AI Studio 搭出了一个带数据库和登录功能的 App，让整个团队能共享数据状态。我们特别期待看到大家用 AI Studio 和 Firebase 一起做出什么好玩的东西，也很想看看你们接下来的创意。只需点一下按钮，我们的应用就被 Firestore、Firebase 身份验证和 Firebase 安全规则全面武装了。这些产品已经存在快十年了，背后有 Google Cloud 的规模和可靠性做支撑。用上这套 Firebase 集成，意味着你的原型可以直接变成一个完整的应用，不用再重新设计架构。你刚才注意到了吗？我一点“完成”，Sam 那边立刻就看到了。实时同步和离线功能是默认就带的，所以你的 Vibe 应用用起来会跟你平时用的那些应用一样丝滑、反应快，给用户带来很棒的体验。好了 Sam，我觉得我们准备好正式发布了。同意。用 AI Studio，你可以通过输入提示词和聊天来不断打磨和迭代你的应用，但就这个项目来说，我觉得功能已经很完善了。我们发布吧。你可以直接在 AI Studio 里一键部署到 Cloud Run。我点一下发布按钮，嗖的一下，搞定了，已经发布到网上了。AI Studio 还有一个完整的小程序应用画廊，里面的东西你都可以拿过来改造变成自己的，你也可以完全从一个提示词开始做。今天就去 aistudio.google.com/apps 逛逛吧，链接在视频简介里有。作为 Firebase 来说，不管你是在哪里写代码、做开发，我们都想跟着你走、为你服务。这次跟 AI Studio 的集成就展示了做一个带云数据库和身份验证的全栈应用有多简单。如果你更喜欢在本地环境里干活，比如用 Google anti-gravity、Cursor 或者 Cloud Code 这种 IDE，我们同样提供了 Firebase 技能包，让你在自己熟悉的工具里也能完成我们刚才演示的所有功能。点开下面的简介，了解更多关于 Firebase 技能包的信息，以及怎么把它装到你顺手的 IDE 里。感谢观看，欢迎在评论区告诉我们你们正在用 AI Studio 和 Firebase 做什么样的应用。>>【音乐】【音乐】
---
