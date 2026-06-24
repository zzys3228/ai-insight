---
title: Build adaptive widgets for cars, phones, watches, and more
title_zh: 为汽车、手机、手表等设备构建自适应小组件
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: Wear OS
type: 技术演讲
level: Intermediate
speakers: andrelabonte, frankdeschenes, johnzoeller
video: https://www.youtube.com/watch?v=VnjgKzAa0ws
---
# 为汽车、手机、手表等设备构建自适应小组件

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: Wear OS | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: andrelabonte, frankdeschenes, johnzoeller

学习如何构建可在一系列屏幕上扩展的一目了然的体验，从仪表盘到手腕。发现新的小组件功能，包括如何将你的现代移动端小组件添加到 Android Auto，几乎无需额外代码，以及如何使用 Jetpack Glance 和 RemoteCompose 轻松构建 Wear 小组件。

---
## 📝 详细原文

了解如何构建可在多个屏幕（从仪表板到手腕）上扩展的快速浏览式体验。探索新的小组件功能，包括如何将你的现代移动小组件添加到 Android Auto，几乎不需要额外代码，以及如何使用 Jetpack Glance 和 RemoteCompose 轻松构建 Wear 小组件。

**原文（English）**: Learn how to build glanceable experiences that scale across multiple screens—from the dashboard to the wrist. Discover new widget capabilities, including how to get your modern mobile widget onto Android Auto, with little to no extra code, and how to easily build Wear widgets with Jetpack Glance and RemoteCompose.

---
## 📝 内容总结

# 会议演讲总结

**主题：为汽车、手机、手表等设备构建自适应小组件**

## 核心要点

**1. 统一的小组件愿景**
小组件可让用户在不打开应用的情况下即时访问关键内容和功能，是提升用户参与度的重要工具。例如 Gratitude 应用数据显示，使用小组件的用户活跃度高出 25%。

**2. 跨设备统一方案**
Google 正在打破不同设备间的开发壁垒，以最小工作量让应用内容覆盖手机、手表、汽车等多端设备，开发者无需为不同形态学习多套技术。

**3. Android Auto 新支持**
手机小组件将登陆 Android Auto，覆盖超 2.5 亿辆汽车，让用户的个性化体验（如联系人、日程）无缝延伸到车载场景，今年晚些时候推出。

**4. Wear OS 体验升级**
全屏 Tiles 更名为 **Wear Widgets**，提供小卡、大卡两种新布局（对齐手机 2×1、2×2 格式），并以 Jetpack Glance alpha 版 API 推出，向后兼容 Wear OS 4 及以上设备。

**5. 技术架构革新**
新的 Glance Wear Widgets 由 **Remote Compose** 驱动（专为应用外体验设计的远程 UI 框架），带来更强表现力、流畅动效及与 Compose 的一致性。

---

## 📝 完整文字稿

好的，我来帮你把这段内容翻译成中文口语版本：

[音乐]

>>大家好，我是Audrey，我是Android小组件的 产品负责人。今天的主题是如何触达你的用户。我们将带大家了解各种机会，把你应用中最关键的内容和功能直接送到用户指尖，并且轻松覆盖他们所有的Android设备。今天和我一起登台的还有两位非常出色的同事，他们会深入聊聊我们具体是怎么做到的。

大家好，我是Frank，我负责Wear OS的"一瞥即得"体验。很荣幸来到这里，我已经迫不及待想展示手腕上的设备是如何进化成这个全新小组件生态系统中无缝衔接的一部分的。

我是John，来自开发者关系部门。在后面的环节里，我会给大家演示一些代码片段，看看Glance库是如何让构建小组件变得简单轻松的。

谢谢Frank和John。今天我们要聊的是小组件为Android生态系统带来的巨大价值。小组件是应用界面的一部分，可以在主应用之外远程渲染。对用户来说，小组件的核心就是即时访问——他们想把自己喜欢的应用内容和功能放在最显眼的位置，甚至不用打开应用。对你们开发者来说，这代表着巨大的机会。小组件是一个超级强大的工具，能让你的应用在打开之外也保持用户参与度、持续创造价值。

举个例子，我给大家说说Gratitude这个应用。这是一款正念冥想应用，最近推出了一套全新升级的小组件，可以很好地融入壁纸，适配各种尺寸，更重要的是，提供了多种方式帮助用户紧跟自己的心理健康和个人成长目标。Gratitude发现，添加了至少一个小组件的用户，活跃度比没有添加的高出25%。你有没有想过，作为用户留存策略的一部分，小组件能为你的应用带来什么好处？

要想真正抓住这个机会，我们得先解决你们目前面临的难题。以前，为不同设备开发需要完全不同的库和技术。比如手机上要用Glance和Remote Views，但是到了Wear上就得学Tiles和Proto Layouts。而且，小组件并不能在所有Android设备形态上使用，这限制了你投入的回报。所以我们正在推动一个统一的方案，让应用内容以最小的开发工作量跟随用户穿梭在各种Android设备之间。

作为开篇，我非常自豪地宣布：我们要把手机小组件带到Android Auto上！没错。你已经在手机小组件上的投入，很快就能在你的用户在汽车场景下使用了。在超过2.5亿辆支持Android Auto的汽车上，这将解锁全新的用户旅程。我来演示一下实际效果。

Android Auto最棒的一点就是你的个性化设置会跟你一起走。我这次飞过来参会，一连上租来的车，我平时的设置就已经在那儿等着我了。滑一下就能看到我最喜欢的一个——联系人小组件。你看，我把我的伴侣置顶到了仪表盘上，界面完美适配了汽车屏幕。这点特别重要，因为他的生日正好和今天这场演讲是同一天。多亏了这个贴心的屏幕提醒和一键拨号功能，我可以放心地确保自己在通勤去看主题演讲之前，不会忘记祝他生日快乐。

我们非常激动能在今年晚些时候在Android Auto上解锁这些全新的"一瞥即得"的用户旅程，而且很快也会在搭载Google内置系统的车辆上推出。我们的愿景是让你的小组件出现在用户所在的每一个场景。

下面请Frank来给大家展示手表上的体验是如何进化的。

谢谢Audrey。手表真的是最理想的"一瞥即得"设备。多年来，全屏Tiles一直是Wear OS上的主流界面，让用户一眼就能看到重要的更新。但随着Android生态系统朝着统一愿景迈进，我们也在重新思考手腕上的设备该怎么做。今天，我们让手表更贴近Android 8大家族，目标就是尽量减少手表开发者的负担。

作为第一步，我们正在从独立的全屏Tiles，转向更统一的体验。我们推出了两种新的卡片布局——小卡和大卡，刚好和手机上的2×1和2×2格式对齐，确保你的设计在所有设备上看起来都很统一。因为这些体验现在和手机上、车里的小组件有着相同的基因，是时候给它一个能体现这点的名字了。

今天，我们正式把Tiles更名为**Wear Widgets（可穿戴小组件）**，新的Wear Widgets API作为Jetpack Glance的一部分推出alpha版。这些新布局在所有Wear OS设备上都能很好地工作。值得一提的是，使用这个API的小组件现在可以填充三星Galaxy Watch的多信息Tiles，而以前这些位置只能显示三星自家的小组件。不过不用担心开发碎片化的问题——我们的新API向后兼容运行Wear 4及以上的设备。在支持水平轮播的设备上（比如Pixel Watch），你的大尺寸小组件会像传统Tile一样直接全屏显示。

我们一直在和早期接入的合作伙伴紧密合作，把这个功能做出来。你可以看到，这些Wear Widgets依然承载着丰富的"一瞥即得"内容。但这次的改变不仅仅是名字或布局，而是底层的引擎。

长期以来，Tiles是由Proto Layout驱动的，但开发者们希望有更多的表现力、更流畅的动效，尤其是希望和Compose保持更高的一致性。新的Glance Wear Widgets由**Remote Compose**驱动——这是一个全新的Android远程UI框架。它的API和Compose高度一致，但专门为应用外体验（比如小组件）设计。

我们做这次架构升级有几个原因。首先，Remote Compose解锁了全新的表现力，包括差异化的交互、炫酷的动画，还有形态变换，这些以前是……（内容未完）
---
