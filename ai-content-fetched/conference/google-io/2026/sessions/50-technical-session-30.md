---
title: Build beautiful, premium, adaptive apps with Material
title_zh: 使用 Material 打造精美、优质、自适应应用
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: 设计
type: 技术演讲
level: Beginner
speakers: kendricku, rightnao
video: https://www.youtube.com/watch?v=zRBi6oBtpoo
---

# 使用 Material 打造精美、优质、自适应应用

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: 设计 | **🎯 类型**: 技术演讲 | **📊 等级**: Beginner

**👤 演讲者**: kendricku, rightnao

使用 Material Design 系统的激动人心的更新，构建更美观、更高端、更自适应的应用程序。探索组件的全新 Expressive 更新、可自定义性的即将改进等内容。

---

## 📝 详细原文

使用Material Design系统的精彩更新，构建更美观、更高端、更自适应的应用程序。探索组件的新Expressive更新，即将推出的自定义改进，以及更多内容。

**原文（English）**: Build more beautiful, premium, and adaptive applications with exciting updates to the Material Design system. Discover new Expressive updates to the components, upcoming improvements to customizability, and more.

---


---

### 原文

Build more beautiful, premium, and adaptive applications with exciting updates to the Material Design system. Discover new Expressive updates to the components, upcoming improvements to customizability, and more.

---

## 📝 内容总结

**《使用 Material 打造精美、优质、自适应应用》核心要点**

一、核心主题概述

本演讲宣布Material团队全面转向Compose优先战略，并介绍Material 3 Expressive组件、Styles API和增强的自适应集成。

**二、关键发布/技术要点**
- 要点1：Material Views 1.14是最终稳定版——团队全面投入Compose
- 要点2：Material 3进入稳定版——2026年下半年1.5版本发布
- 要点3：Expressive组件扩展——分段列表、搜索栏刷新、菜单动效、时间选择器等
- 要点4：Styles API——简化基于状态的样式设计，性能优于传统Modifier
- 要点5：Navigation 3深度集成——自适应布局通过listDetailScene策略实现
- 要点6：预测性返回手势——自适应导航自动处理返回时的布局变化

**三、落地应用**
- 案例1：Pixiv实现99%登录成功率
- 案例2：分段列表通过简单替换实现不同视觉DNA
- 案例3：天气仪表板和反重力游戏通过一次API调用完成

**四、总结**
Material正在加速转向Compose优先的未来。Expressive组件让UI更有个性，Styles API解锁更深定制，与Navigation 3的集成让自适应布局变得无缝。开发者应关注迁移指南，拥抱Compose的新时代。

---

## 📝 完整文字稿

[音乐] >> 大家好。很高兴能和大家相聚在这里。今天我们要聊聊 Material Android 团队即将推出的所有激动人心的更新，以及这些更新如何帮助你们用 Material 构建出精美、高级且自适应（adaptive）的应用。多年来，我们一直在重新定义 Android 上的 UI 构建方式。我们见证了 Jetpack Compose 从一个雄心勃勃的想法，成长为全球最精美应用背后的引擎。作为 Android 现代的声明式工具包，它旨在用更少的代码和强大的原生工具来简化并加速 UI 开发。我是 Kendrick，Material Android 团队的软件工程师。我很幸运能够亲眼见证这场演变。今天我们正在迎来这段旅程中一个决定性的里程碑——一个为 Android 开发者开启新篇章的里程碑。我们迎来了一个重大里程碑：Material Views 1.14 稳定版发布。这个版本为 View 系统带来了新的表达性（expressive）组件。但你可能已经注意到势头的变化。虽然 Compose 持续发展加速，但我们在 Views 上的更新变得更加聚焦。这是因为过去几年，我们一直在为一次根本性的转变做准备。为了更详细地告诉大家我们接下来的方向，我把话筒交给 Naomi。谢谢 Kendrick。大家好，我是 Naomi，Material Android 团队的软件工程师。为了有效地面向未来构建，我们必须聚焦。从今天起，我们正式全面投入 Compose。今后，我们团队将转向对 Jetpack Compose 的独家支持，并将所有精力转移到 Material Compose 库上。这意味着 Material Views 1.14 将是 Views 库的最后一个稳定版本。我们知道你们在 Views 上构建了大量东西，但从来没有比现在更好的时机迁移到 Jetpack Compose。如果你一直在等待一个合适的时机来全面采用 Compose，现在就是了。随着 2026 年下半年即将发布的 1.5 版本（提升 M3 实验性 API），Compose 中的 Material 3 将正式进入稳定版。除了 Material 3 进入稳定版，我们还在推出 Material 3 表达性（expressive）组件。M3 表达性 API 构成了 M3 的一个扩展包。你可以选择使用它们来提供更高级的体验。我们认真倾听了你们的反馈，接下来将展示我们如何让 Compose 上的 Material 3 更有表现力、性能更优、适应性更强。我们将深入探讨新的 Material 3 表达性组件特性，为你的 UI 带来更多个性和动态效果。Styles API——我们面向性能的全新方法，简化了基于状态的样式。增强的自适应（adaptive）集成，帮助你的应用在任何屏幕尺寸下都如鱼得水。去年，我们展示了许多超酷的新表达性组件，比如浮动工具栏（floating toolbar）、新的进度指示器、按钮组等等。在去年表达性组件成功的基础上，我们正在扩展这个工具包，让它比以往更加多样化。我们的列表已经演变为两种变体，包括一种精致的分段（segmented）视觉风格，并通过支持点击、切换（toggle）和不同的选中状态来引入更多交互性，容器会自动随之变换。最棒的是什么？如果你已经在使用标准的列表项，那么切换到分段外观只是一个无缝替换。我们来看一下代码中这两种列表变体：标准版和分段版。首先，这是我们的标准列表。各个列表项之间用水平分隔线隔开，每个列表项都有用于选中状态、内容和图标的参数。现在是分段列表。只需简单地将那个列表项换成分段列表项，并在列表列上使用纵向排列规范（vertical arrangement specification）添加一点间隙间距（gap spacing），框架就会处理剩下的事情。它会自动管理自适应的圆角形状和颜色更新，给你一种完全不同的视觉 DNA。搜索（Search）迎来了重大的视觉刷新，与应用栏（app bar）结合，引入了专门的导航和操作插槽（slot），它们位于搜索容器之外，并配有令人兴奋的动画，让体验更具交互性。我们来一起看看搜索组件的代码。我们引入了一个新的带搜索的应用栏可组合项（app bar with search composable），它为搜索栏前后的内容引入了专门的插槽。导航图标提供了一个用于放置返回按钮等内容的插槽，而操作内容插槽则提供了一个用于放置过滤或语音搜索等图标的插槽。我们还引入了新的展开式搜索栏，比如带间隙（gap）的展开式停靠搜索栏（expanded docked search bar），你可以将它与带搜索的应用栏结合使用，在两者之间平滑地动画切换。在菜单组件的基础上，我们引入了更精细的子菜单动效，以及更广泛的形状和颜色样式调色板。我们还新增了间隙（gaps），这是一种新的布局特性，提供了视觉呼吸空间和灵活性。现在，让我们花点时间一起看一个使用更新后菜单组件的示例。我们从一个扁平的下拉菜单项列表开始。虽然能用，但随着应用的增长，扁平列表很快会变得拥挤，并缺乏层次结构。为了增加结构感，可以使用下拉菜单组（drop-down menu group）。这能在视觉上将"修改"等项与"导航"分开，并且菜单默认值（menu defaults）的组形状（group shape）会自动处理圆角容器。为了让菜单具有表现力并响应状态，可以使用 checked 参数和 checked leading icon。当某个选项被切换（toggle）时，这会将图标从轮廓样式切换为填充样式，提供即时、清晰的视觉反馈。你们要求更多的触觉输入（tactile inputs），我们做到了。来认识一下这个新的、高度交互的 time picker（时间选择器），它即将更新以适配我们的表达性设计系统。我们将首次推出一个专用的、基于滚动的输入组件，为时间选择提供一种新的触觉变体（tactile variant）。它被设计为一个独立的基础组件，同时也让你能够将同样的精确滚动体验带到应用中任何基于数字的界面上。所有这些表达性组件都已经作为实验性 API 在 1.5 alpha 版本中提供。还有什么在酝酿中呢？Wel（……文本在此处中断） 好的，我来给你翻译成比较口语化的中文版本：

---

我们知道大家都想让自己的应用看起来独一无二。所以我们现在正在把 Material 组件和全新的实验性 Jetpack Compose Styles API 整合起来，让你能做到比以前更深入的定制。这次更新能帮你跳出那些千篇一律的模板，摆脱默认样式，打造出符合你品牌调性的、高品质又吸引人的体验。

Style 是一种全新的定制方式，它是对传统 Modifier 的升级。设计它的目的就是让定制变得更简单、更深入。Styles 带来了不少好处：更新样式时能跳过组合（composition）阶段，所以性能更好；而且创建统一品牌风格的体验也更省事了。想了解更多的话，可以去看看"Building Custom Design Systems with the new Styles API"这个演讲。

我们正在把 Styles API 和 Material 组件整合起来，定制会比以前更简单、范围也更广。给你先剧透一下：

比如说，你想要一个按钮，平时是深蓝色背景，按下去的时候变成浅蓝色，而且还要带过渡动画。现在要做到这个效果，你得写一大堆样板代码——比如手动追踪按下的状态、还要新建一个 button colors 类。

那如果想让按下时的背景变成渐变色呢？现在用 Material 按钮根本没有现成的方法能搞定。但用 Styles 就很简单了。等 Styles API 集成完成后，你只需要传一个 style 进去，把这些属性设置好就行了。Styles 不光让定制变简单，还解锁了以前根本做不到的定制效果。这些更新很快就会在 Material 组件里推出。

不过，光好看还不够。"高端感"还得看你的应用在整个生态系统里表现怎么样。我们知道一直以来，做折叠屏、平板和桌面端的适配都是个老大难问题。现在 Material Adaptive 库已经和 Navigation 3 集成在一起了，做大屏幕设备的适配布局会简单很多。

以前要做自适应布局，意味着你得切换不同的导航框架，这导致进出自适应区域特别难管理。为了解决这个问题，我们把 Material Adaptive 库和 Navigation 3 深度集成在了一起。这可是个重磅变化——这意味着你的导航逻辑和自适应布局终于能"对上话"了。从手机屏幕扩展到大屏折叠设备，整个过程在你的 Compose 代码里就能无缝、简单地完成。

这次集成有个核心点，就是 Navigation 3 的"场景（scenes）"概念。不再是简单地在孤立的"目的地"之间跳转，自适应布局现在可以按"视觉场景"来思考。通过 adaptive-navigation3 这个 artifact，我们可以更方便地使用 list-detail 场景策略。你可以把它理解成导航返回栈和 UI 之间的大脑——它会看你返回栈里的条目，根据当前屏幕大小，自动决定是显示单栏布局，还是并排显示列表和详情。

使用方法也很简单：给你的条目打个标签，比如 `listDetailScene.listPane` 或 `listDetailScene.detailPane` 就行。导航库会通过这些元数据理解每个屏幕的意图，重活儿它都帮你干了。而且因为这是直接构建在导航状态里的，预测性返回手势也直接免费送你。

比如用户在折叠屏上从详情页往回滑，库会自动知道要把详情栏收掉，同时列表栏保持显示。整个过程非常流畅、非常直观，最重要的是——整个应用就一份真理来源，再也不用维护好几套了。

这次会议可不光是讲讲库更新而已。我们认真倾听了大家的反馈，下定决心要让 Material 3 更强大、更灵活，而且在日常开发中用起来更顺手。

你也看到了，我们一直在努力让 Compose 变得更有表现力、性能更好、更可定制、也更自适应。今天聊到的这些内容，你都可以在我们的设计指南、设计套件、alpha 代码和 API 文档里找到。

如果你正从 View 系统迁移到 Compose，可以看看我们的迁移指南。如果想深入了解 Styles API，也有专门的概述文档可以读。这两个资料都在 Android 开发者网站上。

我们超级期待看到大家做出什么好东西！你可以上 Google 的工作页面读读 Material 转 Compose 优先的进展，也可以在社交媒体上用 **#M3Expressive** 这个话题标签，或者在 Instagram 和 X 上 @**GoogleDesign**，跟我们互动、提反馈。敬请期待，这只是个开始——接下来几个月还会有更多 Compose 更新推出。

最后一点，如果你喜欢我们今天的演讲，强烈推荐去看看 Bradley 和 Liam 的设计演讲：**"Make Material Your Own"**。谢谢大家！

---

翻译的时候我尽量保留了原视频那种演讲的口吻，口语化一点，读起来更自然。如果你想要更书面一点或者更简洁的版本，可以告诉我～
---
