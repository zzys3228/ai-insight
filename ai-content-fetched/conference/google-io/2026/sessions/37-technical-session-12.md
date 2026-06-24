---
title: Build native Android experiences for web apps using WebView
title_zh: 使用 WebView 为 Web 应用构建原生 Android 体验
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: Android
type: 技术演讲
level: Intermediate
speakers: alukin, semyers
video: https://www.youtube.com/watch?v=4_Sw2jfzOuc
---
# 使用 WebView 为 Web 应用构建原生 Android 体验

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: Android | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: alukin, semyers

利用您现有的网络资产，在每台 Android 设备上提供感觉原生的顶级体验。无论您是在移动应用中嵌入动态网络组件，还是将复杂的网络应用扩展到可折叠设备、平板和 Chromebook，Android WebView 组件都是一个强大的桥梁。学习使用它的最佳实践，了解如何与 Android 原生功能集成，包括双向通信、原生文件处理、无缝 UI 集成以及灵活的离线策略。

---
## 📝 详细原文

利用您已有的 Web 资产，在每台 Android 设备上提供原生般的一流体验。无论您是在移动应用中添加动态 Web 组件，还是将复杂的 Web 应用扩展到折叠屏、平板和 Chromebook，Android WebView 组件都是一个强大的桥梁。学习使用它的最佳实践，以便与 Android 原生功能集成，包括双向通信、原生文件处理、无缝 UI 集成以及灵活的离线策略。

**原文（English）**: Leverage your existing web investment to deliver a first-class experience that feels native on every Android device. Whether you are adding dynamic web components to a mobile app or scaling a complex web application to foldables, tablets, and Chromebooks, the Android WebView component is a powerful bridge. Learn best practices for using it to integrate with Android’s native features, including two-way communication, native file handling, seamless UI integration, and a flexible offline strategy.

---
## 📝 内容总结

# 会议演讲总结

**演讲主题**：使用 WebView 为 Web 应用构建原生 Android 体验

**核心要点**：

1. **WebView 的定位**：基于 Chromium 引擎的嵌入式 Web 渲染组件，可作为原生组件集成到 Android 应用中，实现 Web 内容的无缝显示。WebView 拥有独立的配置文件（Cookie、存储与系统浏览器隔离），并由应用完全控制。

2. **多选项卡实现**：通过 Compose 的 `AndroidView` 集成 WebView，并结合原生 Android UI 元素（Material Design 卡片、`LazyRow`）。关键技术点是将每个 WebView 包装在自定义数据类中并存储于有状态列表，避免垃圾回收导致状态丢失；切换时保持 WebView 活跃，仅用 `offset` 隐藏非选中项。

3. **双向通信机制**：
   - **原生 → Web**：使用 `evaluateJavaScript` 执行 JS 代码或操作 DOM（如隐藏按钮）。
   - **Web → 原生**：通过 `addWebMessageListener` 创建 JS 对象，Web 端调用 `postMessage` 即可触发原生功能（示例中通过 AlarmManager 设置提醒通知）。

4. **进阶方向**：演讲还涉及 Service Worker 与离线支持等高级 API（具体内容未在摘要中展开），用于打造类原生应用体验。

**核心价值**：开发者可复用现有 Web 代码库，同时通过原生能力（如推送通知、系统集成）增强用户体验，实现代码效率与产品体验的平衡。

---

## 📝 完整文字稿

[音乐] >> 大家好，我是 Scott，是 Android Web 团队的开发者关系工程师。我是 Sasha，是笔记本电脑和平板团队的开发者关系工程师。如果你已经有一个 Web 应用，想通过利用现有的 Web 资源来创建一个 Android 应用，那这个视频就适合你。我们将向你展示如何在 Android 应用中显示你的 Web 内容，并通过强大的原生 Android 体验来增强它。这可以让你在复用大量现有 Web 代码的同时，创建一个高度优化的应用。我们来看看为这个视频制作的网站吧。这是一个简单的笔记应用。这是基于它构建的 Android 应用。用户可以看到他们创建的笔记列表，可以点击其中任何一条来添加文本。使用键盘快捷键可以加粗文字、添加图片、以 PDF 格式下载笔记，甚至可以设置提醒，触发原生的 Android 推送通知。那么，它在底层到底是如何工作的呢？你怎样才能为你的 Web 应用做到同样的事情呢？我们将涵盖你需要了解的所有内容：WebView 基础知识、如何实现选项卡、如何在 WebView 和 Android API 之间建立双向通信，最后还会介绍高级 WebView API、Service Worker 和离线支持，以打造精致的类应用体验。Sasha，你来给我们讲讲 WebView 的基础知识吧。谢谢 Scott。那么，WebView 到底是什么呢？把它想象成一个基于与 Chrome 相同的 Chromium 代码的专业化 Web 渲染引擎，你可以像原生组件一样直接嵌入到 Android 应用中。这是一种无缝显示 Web 内容的方式，无需用户离开你的应用上下文。开发者使用 WebView 来做各种各样的事情，比如显示服务条款或隐私政策页面，或者在原生 UI 中嵌入动态 Web 内容。在我们的示例应用中，我们使用了全屏 WebView，它适用于移动设备形态，在大屏设备上看起来尤其出色。请记住，WebView 在自己独立的配置文件中运行。这意味着它不与设备上的 Chrome 或任何其他浏览器共享 Cookie 存储或本地存储。这种隔离是有意为之的设计选择，确保你的应用数据保留在自己的沙箱中。由于应用拥有这个 WebView，你的原生代码能够与 WebView 进行通信并修改其内容。这就是在我们的 Web 应用中启用原生 Android 功能的关键。我们来看看代码。你可以通过用 AndroidView 包装的方式来将 WebView 添加到你的 Compose 布局中，我们正在研究未来如何让它更简单。使用 factory 代码块来初始化引擎、更改 WebView 设置并加载 URL。对于我们的 Web 应用，我们需要的关键设置包括：启用 JavaScript（默认是禁用的）、启用 DOM 存储（这可以访问 session storage 和 local storage），以及修改用户代理字符串，这样当我们的应用运行在大屏设备上时，服务器会给我们返回桌面版而不是移动版。现在你已经了解了基础知识，Sasha 将展示我们如何使用一些原生 UI 元素为应用添加选项卡支持。使用 WebView 的一大优势是，我们可以将其与原生 Android 元素混合使用，以创建更强大的应用。我们来看看我们的应用。主要部分是 WebView。它显示 Web 内容并提供主要功能。在顶部，你可以看到选项卡。它们是使用原生 Android 结构实现的。我们通过将整个应用包装在一个 Android Column 中来实现这一点，WebView 占据底部空间，顶部行位于其上方。选项卡栏是另一个原生 Android 元素，在我们的案例中是一个 LazyRow。其中的每个项目都是一个 Material Design 卡片。它将内容与背景分离，并提供清晰的视觉结构。当点击"创建新选项卡"按钮时，会初始化一个独立的 WebView 并将其添加到我们的状态中。但是，我们如何存储这些 WebView 呢？如何在不丢失内存、JavaScript 上下文或滚动位置的情况下在它们之间切换呢？为了解决这个问题，我们做了两件事。首先，我们将每个 WebView 包装在一个称为 tab instance 的小型自定义数据类中。然后，我们将所有 tab 实例存储在一个有状态列表中。这保持了对 WebView 的稳定引用，并防止它们在屏幕外时被垃圾回收。其次，在选项卡之间导航时，我们不会销毁未选中的 WebView。相反，我们始终保持它们的活跃状态，只是简单地将它们隐藏起来。我们将它们堆叠在一个 Box 内部，并使用 modifier offset 将隐藏的移到屏幕外。如果我们重新创建 WebView，页面将重新加载并丢失其状态。这就是我们实现选项卡的方式。现在，Scott 将解释如何在 Android 和 Web 之间建立双向通信。WebView 的另一个好处是，它不仅仅是你 Web 内容的容器。你的原生 Android 代码实际上可以直接与你 Web 应用的 JavaScript 引擎通信，让你能够执行诸如触发 JS 函数和操作 DOM 之类的操作。而你 Web 应用的 JavaScript 代码可以调用原生函数，这让你的 Web 应用能够访问 Android 功能。我们将要使用的两个 WebView 函数是 evaluateJavaScript（处理原生代码到 JavaScript 的通信）和 addMessageListener（添加可以调用原生代码的 JavaScript 函数）。让我们从 evaluateJavaScript 开始，做一些简单的 DOM 操作。在我们的笔记应用中，我们有一个功能想在 WebView 中运行时从应用中移除。具体来说，就是这个按钮。我们可以使用 WebView 的 evaluateJavaScript 命令来执行我们想要的任何 JavaScript 代码。现在那个按钮消失了。顺便说一下，如果你对 JavaScript 调用的返回值感兴趣，evaluateJavaScript 可以接受一个回调函数来获取该信息。接下来，我们来看看 addMessageListener 如何能够使我们 Web 应用的 JavaScript 调用我们的原生代码。我们的笔记 Web 应用有一个功能，允许用户在笔记上设置提醒并在特定时间收到通知。 指定的时间。要用原生安卓功能实现这个，我们更新了 JavaScript 代码来检查一个叫 my native reminder 的对象是否存在。如果存在，我们就用它的 post message 函数把提醒数据发过去。你可能在想，这个 my native reminder 对象是从哪儿来的？我们在原生代码里用 add web message listener 创建了它。你把 web view、要创建的 JavaScript 对象名称、你的 web 应用托管的域名集合，以及一个接收 JavaScript 调用数据的回调函数传进去。我们的回调函数会把 JSON 数据字符串转换成一个原生提醒对象，然后发给安卓的闹钟管理器，在后台安排时间。可选地，我们还可以用传给回调的 reply proxy 对象往我们的 web 应用回传一条消息。这条消息会被 my native reminder.onMessage 函数收到，我们在 JavaScript 端实现了这个函数。现在我们的 web 应用可以安排原生提醒了，但这只是一个例子。如果用户给我们的 app 授了相应的权限，我们可以用这个技术来触发优先级通知、通过 work manager 安排后台任务，甚至直接把设备传感器的数据读进我们的 web 逻辑里。现在我们的原生代码和 web 应用已经能互相通信了，Sasha 会展示一些策略，讲我们的 web view app 在设备离线时该怎么响应。现在来聊聊离线支持。这是一个很关键的用户使用场景，也是理解几个 web view 基本概念的好方法。任何联网 app 都有一个常见场景，就是网络连接断了。默认情况下，这种时候 web view 就只显示一个错误页面，但我们完全可以提供更好的体验。比如，用户就算没网也能新建一条笔记并编辑，等设备重新联网，所有修改自动同步。实现这个有好几种办法。第一个选择是用 service worker。它是一段独立于网页运行的 JavaScript，相当于网站和互联网之间的网络代理。它能拦截请求、缓存资源、跑后台任务。好消息是 web view 里支持 service worker。所以如果你选这个方案，给你的网站和基于 web view 的 app 都能加上离线支持。另一个选择是在 app 里缓存页面。web view 提供了一个 API，能让我们拦截任何网络请求，比如 HTML、CSS、JavaScript、图片、视频或者 API 调用。每个请求都会经过一个叫 should intercept request 的函数。在那儿我们可以决定是照常进行，还是拦截下来用本地存的资源。这个方法既可以用来替换或屏蔽某些特定资源，也能在用户离线时提供缓存好的网页。不过对我们这个 app 来说，可能最干净的方案就是直接检测 web view 加载页面什么时候失败。web view 为此提供了一个很方便的 API。要实现这个，我们建一个 is offline 状态变量，web view 开始加载页面时把它设成 false。如果加载失败，就在 on received error 回调里检查错误码。如果我们发现问题是没网导致的，就把 is offline 状态变量更新一下。这个变量决定用户看到什么，要么是 web view 内容，要么是一个叫 no internet screen 的原生安卓界面，上面有个重试按钮。这就是一个很好的例子，说明你可以通过加入原生安卓元素来改善 web 体验。最后一个话题，Scott 会演示怎么用 web view 的原生钩子。现在我们来看看 web view 让我们接入的一些原生钩子。我们先讲我们的 app 怎么处理文件上传，比如用户点击插入图片按钮的时候。我们需要重写 web view 的 on show file chooser 钩子，每当网站要打开文件上传对话框时它就会被调用。默认情况下，这个钩子只会拒绝文件上传请求，但对我们这个 app 的场景来说，我们想显示原生的图片选择器。首先，我们要在 web chrome client 里重写 on show file chooser。接下来，我们用现代安卓图片选择器，这个很好，因为它不需要用户同意任何权限对话框。用户选好图片之后，我们把那个 URI 传回 web view 的 file path callback。根据你的 app 场景，你也可以把图片选择器换成文件选择器，甚至用代码方式处理文件选择。我们的 app 还有一个下载功能，能给用户的笔记生成一个 PDF。要处理这个，我们调用 web view 的 set download listener 函数，每当网站要下载文件时它就会被调用。同样，默认情况下它只会拒绝文件下载请求，但对我们这个 app 的场景来说，我们想把它交给原生的下载管理器，这样它就会出现在通知栏里，并保存到默认的下载文件夹。web view 的 download listener 会提供文件 URL 和 mime type 这些信息，帮助你的 app 决定怎么处理它。不像我们这样发给下载管理器，你的 app 也可以自己下载文件，存到临时缓冲区里做后续处理，或者放在 app 的存储空间里。下面看看我们怎么把下载请求传给原生安卓下载管理器。首先，我们用 WebView download listener 给的 URL 建一个 download manager request 对象。我们指定下载时要显示通知，并且保存到默认下载文件夹。然后，我们把这个请求加入队列，下载管理器就接手了。我们的示例 app 没用上这些，但你的 web 应用可能会请求相机、麦克风或位置之类的权限。这种情况下，你要记得 web view 的 on geolocation permission show prompt 和 on permission 权限请求钩子。这些钩子可以让你向用户显示这些功能的原生权限请求，或者直接使用你的原生应用已经被授予的权限。现在，我把话筒交回给Sasha来收尾。我们今天讲了很多内容。如果你想看看你的Web应用在Android上的效果，可以去GitHub上看这个示例应用。用Android Studio打开它，把链接从notice under dev改成你的网站，就能看到效果。虽然我们今天主要讲的是如何利用你在Web端的投入，但如果你想专门为大屏折叠屏设备打造完全原生的体验，一定要去看看“为大屏设备设计和构建桌面级Android体验”这个视频。感谢大家的参与。让我们一起继续打造伟大的产品。编码愉快。 >> [音乐]
---
