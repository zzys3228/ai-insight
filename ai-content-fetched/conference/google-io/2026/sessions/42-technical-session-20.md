---
title: The latest in Android XR
title_zh: Android XR 最新动态
category: conference/google-io/2026/sessions
date: 2026-05-21
time: PT
track: Android
type: 技术演讲
level: Intermediate
speakers: elijahtaylor, stevans, yasmineevjen
video: https://www.youtube.com/watch?v=1KOO2lqsdaA
source: io.google.com
translated: true
fetched_at: 2026-06-24T10:00:00
---
# Android XR 最新动态

## 📋 演讲摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: Android | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: elijahtaylor, stevans, yasmineevjen

探索 Android XR 生态系统如何提供统一的增强和沉浸式体验平台。了解 Android XR SDK 和 Beta 版 Jetpack XR 库。探索 AI 眼镜的新功能、扩展的 ARCore 地理空间功能以及加速工作流程的工具，以及 Android XR 模拟器和直接预览的最新更新，帮助您在所有 XR 设备上高效构建。

## 📝 内容总结

# Android XR 最新动态 · 会议演讲总结

**演讲人：** Stevan Silva（Google Android XR 团队）

## 核心要点

**一、平台进展**
- Android XR SDK 旨在为 XR 头显、有线 XR 眼镜和 AI 眼镜搭建统一开发桥梁
- **开发者预览版 4（DP4）** 正式推出，带来 AI 眼镜增强体验及 XR 头显沉浸式体验的多项更新
- 核心库（XR Runtime、Jetpack Scene Core、ARCore for Jetpack XR）**即将进入 Beta 阶段**

**二、Galaxy XR 生态亮点**
- **Simply Piano XR**：将钢琴学习应用带入 3D 空间，实现虚实琴键演奏与个性化指导
- **Omy Galaxy**：空间混合现实街机解谜游戏，融合手部追踪与物理玩法

**三、AI 眼镜合作伙伴生态**
涵盖购物、健康健身、媒体（Spotify、Melon）、教育（Pearson）、出行导航（Uber、Naver Map、T Map、GetYourGuide）以及通讯（LINE、KakaoTalk）等领域。

**四、开发者工具更新**
- **Jetpack Projected**：新增设备可用性 API（统一佩戴状态与连接性信号）、Projected Test Rule 测试框架，以及 Gemini 语音启动 Projected Activity 能力
- **Jetpack Compose Glimmer**：推出安全色彩、形状、深度等 UI 原语，新增 Google Sans Flex 字体及语音输入指示器等交互组件

**五、开发者催化剂项目**
公开申请通道开放，开发者可获取 XREAL Project Aura 及 AI 眼镜开发者套件等预发布硬件。

---

## 📝 完整文字稿

[音乐] >>大家好，我是Stevan Silva。今天我们非常兴奋地跟大家聊聊，如何通过Android XR SDK在各种XR设备上搭建桥梁，包括XR头显、有线XR眼镜和AI眼镜。去年12月，我们发布了开发者预览版3，带来了用于在AI眼镜上构建增强体验的新API。正如12月分享的，AI眼镜是Android XR家族中令人激动的新形态。带显示屏和不带显示屏的AI眼镜，通过强大的音频和对话体验，将现有的应用和用户与他们周围的世界连接起来。今天我们非常激动地宣布推出开发者预览版4，为AI眼镜上的增强体验，以及XR头显和有线XR眼镜的沉浸式体验，带来了更多开发者解决方案的更新。同时，我们包括XR runtime、Jetpack Scene Core和ARCore for Jetpack XR在内的核心库，即将正式进入Beta阶段。这是我们与大家一起，通过反馈和投入达成的又一个里程碑。看到大家在Galaxy XR上发布的精彩体验，真的让人超级兴奋。为了支持这股势头，我们推出了新功能，旨在加深沉浸感，让头显交互感觉更自然，并给用户提供更多观看、创作和探索的方式。这些能力在实际中的一个例子是Simply Piano XR的精彩工作，它将排名第一的钢琴学习应用带入了全新的维度，让任何人都能在真实甚至虚拟的钢琴上演奏自己喜欢的歌曲，并有指导课程和个人反馈。在专为Android XR构建的完全3D环境中，按键亮起，手指编号引导每一个音符。另外，O my galaxy是一个空间混合现实街机解谜游戏，将你的房间变成一个互动星系。它专为广泛的XR受众设计，结合了自然的手部追踪和基于物理的游戏玩法，创造了一个俏皮、沉浸式的体验，展示了Android XR的力量。今天，我们将主要从AI眼镜的增强体验开始，然后是关于有线XR眼镜和XR头显的沉浸式体验。我们也想宣布我们的Android XR开发者催化剂项目。开发者可以通过我们的公开申请流程，申请获得包括XREAL的Project Aura和AI眼镜开发者套件在内的预发布硬件的访问权限。但更多细节稍后再说。现在，让我们深入了解AI眼镜的增强体验。自12月推出以来，已经有不少合作伙伴正在探索XREAL的能力。这包括购物、健康和健身、媒体（如Spotify、Melon和30 Ninjas）等领域的合作伙伴。通过Pearson进行教育，以及与Uber、Naver Map、T Map、GetYourGuide和Aira在现实世界探索和移动方面的合作。我们也正在与LINE和KakaoTalk等通讯应用展开合作。要了解更多关于我们的合作伙伴正在构建的增强体验，我把话筒交给Yasmin。谢谢，Se Won。与XR一起，LINE的使命是将"拉近距离"带到现实世界。免提消息和即时照片分享，能让你在手机上更顺畅地进行实时交流。例如，想象一下，你想与远方的人分享一个特别的时刻。你们将能够看到同一个场景，就像你们都在现场一样。而在KakaoTalk方面，用户可以体验连接的未来——KakaoTalk on AI Glasses通过直观的语音激活消息和免提实时通知，无缝融合你的数字和物理世界。这些体验专为随时在线的专业人士、懂技术的购物者和移动中的社交达人设计，让你在保持深度社交圈和日常活动的同时，从手机屏幕中解放出来。最后，NAVER地图，韩国领先的数字地图服务，为Google AI Glasses带来了免提步行导航。凭借精确的行人数据和自然的语音引导，它能在任何地方提供安全可靠的导航体验。NAVER也在将更多服务带到Google AI Glasses，包括购物和Papago翻译。在最新一轮更新中，我们继续扩展Jetpack Projected、Jetpack Compose Glimmer和ARCore for Jetpack XR的功能，以支持增强体验。Jetpack Projected允许你为AI眼镜配置和设置你的应用程序。首先，我们来看看如何让你的应用与XR设备交互。设备可用性API将关键信号（包括佩戴状态和连接性）整合到标准的Android生命周期状态值中。这个API可以帮助你管理音频路由、热词激活，并根据XR设备何时可用，知道何时期待用户输入。为了简化你对Jetpack Projected库的测试，我们推出了Projected Test Rule API，在新的Projected Testing构件中可用。这个API自动化了Projected Test环境的设置，让你无需样板代码就能编写干净、可靠的单元测试。现在你还可以使用Gemini的语音命令，将你的projected activity启动到AI眼镜上。要实现这一点，你需要进入你的Android manifest文件，添加XR projected launcher类别和intent过滤器。这告诉Gemini从他们的AI眼镜启动哪个projected activity。在UI方面，我们继续扩展Jetpack Compose Glimmer，带来视觉上的优化和新的交互组件。开箱即用，Glimmer主题提供了附加的安全颜色、形状、深度和间距原语，以优化眼镜UI。调整光学大小可以让字体更清晰、更易读。我们现在在Glimmer组件中加入Google Sans Flex，并对字体样式进行优化，以提高光学透视显示屏上的可读性。除了这些基本原语，我们还引入了几个交互组件。通过语音输入指示器，你可以在麦克风激活时为用户提供视觉反馈……（内容在此处被截断）

*原文请访问 [Google I/O](https://www.youtube.com/watch?v=1KOO2lqsdaA)*
