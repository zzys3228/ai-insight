---
title: Vibe design to build incredible web UI
title_zh: 围绕 Gemini 构建公司级现代 Web UI
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: 设计
type: 技术演讲
level: Beginner
speakers: dalmaer, deast
video: https://www.youtube.com/watch?v=nC7TrzUYvig
---
# 围绕 Gemini 构建公司级现代 Web UI

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: 设计 | **🎯 类型**: 技术演讲 | **📊 等级**: Beginner

**👤 演讲者**: dalmaer, deast

了解如何通过将设计和构建合并为一个 Vibe Design 工作流来更快地交付 Web UI。Vibe Design 的核心是以美学而非语法为导向。了解如何使用 Stitch 和 Chrome DevTools MCP 服务器，通过代理工作流将想法直接转化为代码。

---
## 📝 详细原文

了解如何通过将设计和构建合并到一个 Vibe Design 工作流程中来更快地交付 Web UI。Vibe Design 的核心理念是以美学为导向，而非以语法为导向。了解如何使用 Stitch 和 Chrome DevTools MCP 服务器，通过代理工作流程将想法直接转换为代码。

**原文（English）**: Learn how to ship web UIs faster by collapsing design and build into one Vibe Design workflow. Vibe Design is all about leading with aesthetic instead of syntax. Learn how to use Stitch and Chrome DevTools MCP servers to translate ideas directly into code with agentic workflows.

---
## 📝 内容总结

**总结：围绕 Gemini 构建公司级现代 Web UI**

本次演讲介绍了如何借助 Gemini 与 AI 设计工具 Stitch 高效构建公司级现代 Web 界面，核心围绕"用 CSS 词汇驱动设计"的工作流展开。

**核心理念**：凭感觉设计——以专业 CSS 概念（如非均匀 Grid、滚动驱动动画、appearance 属性）替代模糊描述，将意图转化为精确指令，使 CSS 成为连接设计、代码与 AI 代理的通用语言。

**工作流闭环**：① 在 Stitch 中用 CSS 概念提示设计；② 通过 Chrome DevTools MCP 在真实浏览器中检查 DOM 与计算样式；③ 将验证反馈到下一轮提示中迭代打磨。

**实践要点**：
- **布局**：采用 4 列不均匀 Grid，英雄卡片横跨 2 列 2 行建立视觉层级；
- **设计系统**：通过 Stitch 的 design MD 统一颜色、字体、间距等规范，确保多页面风格一致；
- **交互**：基于原生 JS 与指针事件实现拖拽排序，兼顾性能与无依赖；
- **样式**：利用原生 `select` 配合 `appearance` 等属性，无需 JS 即可自定义下拉控件。

该工作流强调"设计→检查→打磨"的迭代循环，以 CSS 知识赋能每一次 AI 生成更精准、更可控。

---

## 📝 完整文字稿

[音乐] >>这个屏幕使用了动画触发属性，让滚动触发动画顺滑如丝、极其轻松。这个下拉选择框用的是原生 select 元素，通过 appearance base select 样式实现。哦，这个布局用了 CSS Grid，轨道大小不统一，以此引导用户先看哪里，建立起空间层级感。而且这不是用 AI 编程代理搭建的。好吧，也不能说完全没用到，对吧？好吧好吧，确实用了一点点，但我们是用一个设计代理搭建的。这就是 Stitch——一款 AI 设计工具。你描述想要的 App 长什么样、手感如何，它就会生成一份由真实 HTML 和 Tailwind CSS 支撑的设计稿。而这个工作流最重要的一点是，我们今天要讲的每一个 CSS 功能，都直接对应着一条设计原则。Grid 给我们带来结构层级，滚动触发动画则在用户浏览页面的过程中营造出连续感。我们之所以知道如何把控这个设计，是因为我们用了这些 CSS 功能的词汇、描述，甚至语法。我是 Dion，我在 Stitch 工作。>>我、我是 David，你知道，我也也在 Stitch 工作。今天我们来教你如何用 CSS 来"凭感觉"设计。那么，什么是凭感觉设计？就是你带着意图去搭建设计。你描述你想要的——布局、手感、行为，工具就把它做出来。不过这只是基础。真正强大之处在于，当你用上 CSS 的专业词汇，你的意图就会变得具体。与其说"做好看一点"，不如说"用不均匀网格，英雄区横跨两列"。与其说"加点动画"，不如说"把 scale Y 变换绑定到滚动时间线"。你的 CSS 知识能把模糊的意图转化为精确的指令。CSS 是你、设计、代码和代理之间共通的语言。这也是我们今天要讲的工作流。我们会讲如何把一个 CSS 想法变成一个完整的设计，把 Stitch 和 Chrome DevTools MCP 这两个工具结合起来用。首先我们从布局开始。我们要搭建一个轨道大小不均匀的网格，来展示视觉层级——毕竟谁不爱一个漂亮的网格呢？之后，我们会讲如何定义你的视觉风格，并让每个页面都继承它——颜色、字体、间距，全部统一在一处真相之源。然后我们会深入探讨滚动触发动画的基础原理，直接用提示词来创建它们。最后压轴，我们会讲基于外观的选择器——不用任何 JavaScript 或库就能给 select 元素写样式。我们今天用到的所有提示词、工具和全部内容，都会放在视频简介里。所以在开始写提示之前，我们先把开发环境搭起来。我们要用两个 MCP 服务器，配合我们的 IDE Antigravity 一起工作。第一个，Stitch MCP。它把你的编程代理连到 Stitch 上，让代理能以编程方式创建项目、生成页面、编辑设计。打开 Antigravity 的 MCP 插件市场，找到 Stitch，添加它。它会要一个 API key，你可以在 Stitch 的设置页面拿到。把它填进 Antigravity 的界面就连上了。你的代理现在就能调用工具了，比如"用文本生成页面""编辑页面""列出页面"这些。第二个，Chrome DevTools MCP。它让你的编程代理能在 Chrome 里检查一个正在运行的网页，读取 DOM、查看计算样式、看控制台。这个的话，你直接去它的 GitHub 仓库。复制 Antigravity 的配置代码块。然后，打开 Antigravity 的 MCP 设置。切换到原始配置编辑器，把代码粘进去。有个小地方要注意一下——GitHub 上的配置把 server 包在一个 MCP servers 键里。但你的配置里多半已经有这一层了，所以只粘里面的 server 块就行。所以整个工作流是这样的：一、在 Stitch 里设计，用 CSS 概念来提示它。二、在 Chrome 里检查，用 DevTools MCP 验证输出。三、打磨——把你发现的问题反馈到下一轮提示里。所以就是设计、检查、打磨——一个闭环，而你的 CSS 知识会让每一次迭代都比上一次更好。好，环境搭好了，咱们开始动手做吧。我们先从布局开始。关于这个站点有一点要先说一下——这是一个关于 CSS 功能的站点，而且它本身用的就是这些 CSS 功能。所以这是一个"元"站点。网格里的每张卡片，就是我们今天要讲的一个主题，并且就是用它所描述的那个技巧做出来的。所以我提示 Stitch 明确采用这种网格结构：四列，滚动动画那张卡片作为英雄区，横跨两列两行。可定制的 select 放在一个高瘦的单列单元格里，次要功能卡片填补在周围。我们来看看返回了什么。这就是 Stitch 做出来的。但我们得把它放进 IDE 工作流里。所以在 Stitch 里，我右键点击这个页面，就能拿到这个链接。然后我到 Antigravity 里，把链接贴进去，加上一段提示来获取项目信息。Antigravity 去跟 Stitch MCP 通信，把项目详情、页面 ID 和我需要的一切都返回回来。现在我得在真实的浏览器里看到这个页面，这样 Chrome DevTools MCP 才能访问它。所以我为此写了一个小 CLI 工具，你可以通过 NPX @_davide/stitchmcp 来用，用 serve 命令就行。它会把页面的 HTML 拉到本地，然后在 localhost 上跑起来。现在它在本地跑着了，Chrome DevTools MCP 就能访问实时 DOM 了。我们来看看 Stitch 到底生成了什么。看这个网格容器，Stitch 用的是 grid-template-columns: repeat(4, 1fr)。滚动动画那张卡片落在了 colspan=2、rowspan=2，就是英雄卡片。那些小一点的功能卡片就填充在它周围。但是，生成一个静态布局只是故事的一半。这是一个便当网格，还有什么比便当网格更棒的呢？那当然是一个可以拖拽的便当网格。我想看看 Stitch 能不能在这个生成的内容基础上，处理复杂的交互…… 好的，我把它翻译成自然的中文口语：

"我跟它说把这些卡片做成可以拖动并能重新排序的。我在提示词里说得很具体，让它用标准的原生 JavaScript 和指针事件，这样代码就是纯高性能的。来看看效果怎么样。Stitch 生成了一个可拖拽排序的便当盒布局，我们能重新排列这些卡片，同时保持它们原本的网格跨度。"

"在开始生成界面之前，我们需要先聊聊设计系统。在 Stitch 里，每个项目都有一个东西叫 design MD。把它想象成是给 agent 用的 AGENTS MD，但是是给设计用的。它定义了你的配色、字体、间距规则、组件模式。当设计 agent 读到它之后，生成的每个界面都会遵循同一套视觉规范。没有它的话，每个界面就是一座孤岛；有了它，所有界面才能融为一体。"

"生成界面的时候，Stitch 会自动帮你创建一套设计系统。这里 Stitch 创建了一个叫 technical curator 的设计系统。每个设计系统都有配色方案、字体层级和组件可视化。它还会生成一份叫 design MD 的文字说明文档。这是一份可读的规范，把你的视觉风格和设计语言写成了 agent 能读懂的文档。里面包含了带 hex 值的颜色和对应的角色、字体规则、组件的使用规范、什么该做、什么不该做。你可以把这个文件连同项目一起导出，下游的开发或者 AI agent 都能读懂它。"

"我让你看看这对代码来说意味着什么。Stitch 导出界面的时候，设计系统的 token 会变成一份 Tailwind CSS 配置。我们有四个颜色角色——主色、次要色、第三色、中性色——每个都会生成对应的 Tailwind CSS 设计 token，比如 bg-primary、primary-container、on-primary-container。字体也有对应的 token，比如 font-headline、font-body、font-label。连圆角尺寸都成了 token，比如 rounded-large、rounded-extra-large、rounded-4。我用自然语言描述的每个设计决策，现在都变成了工具类。"

"最关键的是，从现在开始我们生成的每个界面都会自动继承这些 token。颜色、字体、间距，全都内置好了。当然，如果之后我想改点什么，比如想换个强调色，我就在设计系统里改一次，然后应用到所有界面上，一切都会更新。这就是 CSS 自定义属性的模式——一份真相源，多处使用。"

"导出项目的时候，design MD 文件也会一起导出，这意味着你的设计意图在交接过程中不会丢失。"

"来看看我们接下来要做什么。我们要深入讲滚动驱动的动画。注意看我滚动这个页面的时候会发生什么——有一件事很关键：这条细细的竖线从页面顶部一路长到底部。我往回滚，它也跟着缩回去。这是一个直接绑定到滚动条的进度指示器。没有用 JavaScript 的 scroll 监听器，全是纯 CSS。一个属性就干了所有活儿，它就是 animation-timeline。"

"下面是实现这个效果的 CSS：一个 fixed 定位的元素，加上一段 scaleY 的关键帧，从 0 变到 1。神奇之处就是这条规则：animation-timeline: scroll。这一行声明把动画进度绑定到了滚动位置，而不是时间。transform-origin: top center 保证了它是从上往下生长的。"

"现在我们在 Stitch 里把它做出来。第一步是文档结构。我让 Stitch 创建一个左右交替的两栏布局。四个章节，每个都是两列网格，交替分配"优点"和"代码块"在哪一边。暂时还没有动画，这只是骨架。"

"现在用 Chrome 开发者工具来看看效果。Antigravity 会拿到界面 ID 并在 Chrome 里打开它。骨架看起来不错。"

"好，现在我们来加点动画。这是第二步——滚动联动的进度脊柱线。我想要这条细竖线固定在视口的正中央，随着用户滚动而增长。我让我的编程 agent 写一段提示词，用上这段 CSS。我指定用 animation-timeline: scroll 配合 root block 轴，把 scale 变换直接映射到滚动百分比上。我还特意指定了 transform-origin: top center，这样缩放就是从原点往下，而不是从中心。来看看它给了什么。"

"在跑这段提示词之前，先看看 Antigravity 给了什么。agent 理解了意图，精确地拆成了两块：第一，一个空的 div，editorial spine，作为 body 的直接子元素。这一点很重要，因为它不能嵌在某个相对定位的容器里，否则 fixed 定位就失效了。第二，CSS 部分。agent 用 left: 50% 加 margin-left: -0.5px 来居中，而不是用 translateX——这个选择很妙，因为它把 transform 属性完全留给了 scaleY 用。"

"然后是三行关键的：transform-origin: top center；animation: spine-draw linear；以及 animation-timeline: scroll root block。注意 agent 特别提到了性能：因为只有 opacity 和 transform 在变，浏览器把它交给合成线程处理。零 JavaScript 监听，零布局重算。跟原版一样，我往回滚的时候，它通过 scroll timeline 持续追踪我的滚动位置。"

"而写出这段效果的提示词，对机制、关键帧、动画类型都说得很具体。是这套 CSS 词汇让提示词足够精确，才拿到了正确的结果。"

"好，最后一个演示。看屏幕左边，这是一个普通的原生 select 元素。默认系统字体、默认边框、还有一个无法自定义的操作系统原生下拉箭头。几十年来，这是 HTML 里最难样式的元素之一。真的，有人专门写一整个 JavaScript 组件库，就为了一个像样的下拉框。"

"但现在，看看右边。同样是这个元素，它是一个真正的 select——" 好的，我来把它翻译成自然的中文口语风格：

但是它是用 appearance-base select 来做样式的。它有自定义的背景、自定义的图标、自定义的字体，还有那条蓝色的底部边框。你在这里看到的所有东西，都只是一个原生表单元素上的纯 CSS。这就是我们要做的东西。下面来看看原理。一个 CSS 属性，appearance-base select，就这一句声明，告诉浏览器别再画它自己那套样式了，把控制权交给你。这时候 select 就变成了一个框。真的是个框，你想往里面放什么就放什么。你可以设置边框、可以设置字体，跟操作其他任何元素一样。但浏览器的无障碍支持和键盘交互全都还在，你只需要管它的视觉样式就行了。

好，我们来搭右边那个。我跟 Stitch 说得特别具体——设置 appearance-base select，暖灰色背景，蓝色底部边框，还有那个 layers 图标。我对设计变量写得很细，因为提示词越精确，Stitch 第一遍生成的成品就越接近你想要的效果。喏，就是这个。还记得分屏里右边那个吧？就是这个，活生生的，就跑在这儿。一模一样的——那个暖灰色背景，蓝色重点边框，layers 图标，全都是从那一段提示词生成出来的。你用键盘 Tab 切到它，直接就能用，可以用方向键在选项里切换，焦点环也正常显示——因为它本质上就是一个长得像自定义组件的原生 select，全都是 CSS。所以，你学的那些 CSS 知识可不仅仅是用来写代码的了，它就是你的设计语言。从 grid 到滚动驱动动画，到自定义 select 样式，到自定义属性，到 clip path mask，等等等等，每学一个特性，你就多了一个词。对了，简介里有所有的链接、工具、提示词，记得去看。有什么问题的话，我本人会出现在这条视频的第一条评论里，真的，到时候你直接问就行。非常感谢你花时间看这个，拜托，去做点设计吧。评论里见。
---
