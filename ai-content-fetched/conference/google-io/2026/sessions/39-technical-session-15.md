---
title: Engineering memory-performant Android apps
title_zh: 构建内存高效的 Android 应用
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: Android
type: 技术演讲
level: Intermediate
speakers: ajeshr, chofung, yuanalice
video: https://www.youtube.com/watch?v=fOXJR5qLq54
---
# 构建内存高效的 Android 应用

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: Android | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: ajeshr, chofung, yuanalice

<think>The user says: "翻译成中文，只返回翻译结果，不要解释：" (Translate into Chinese, only return the translation result, no explanation.)

The text: "Learn about critical tools like R8 for code shrinking and best practices for bitmap optimization to slash native memory usage. We’ll also explore how to use the new ProfilingManager triggers for identifying OOMs and memory anomalies in the wild."

We need to translate this into Chinese. There's no further instructions. Just the translation. We need to output only the translation, no extra explanation or tags. Probably keep it as a Chinese sentence.

We should ensure that the translation is accurate. Let's translate:

"了解像 R8 这样的关键工具用于代码压缩以及位图优化的最佳实践，以大幅削减原生内存使用。我们还将探讨如何使用新的 ProfilingManager 触发器来识别在生产环境中出现的 OOM 和内存异常。"

Alternatively, "OOMs" is "Out Of Memory" errors. Use "内存溢出（OOM）" perhaps. Also "in the wild" could be "在实际环境中" or "在生产环境中". Could use "在野外" but more likely "在实际运行环境中". We can use "在实际使用中" or "在实际环境中". Let's produce final translation.

We must ensure to not include any extra explanatory text, only the translation. So just the Chinese sentence.

Potential translation: "了解 R8 等关键工具的代码压缩功能以及位图优化的最佳实践，以大幅削减原生内存使用。我们还将探讨如何使用新的 ProfilingManager 触发器来识别在实际环境中出现的 OOM 和内存异常。" That seems good.

Thus final answer: Provide the Chinese translation.

We should not add any extra punctuation beyond normal Chinese punctuation. Also avoid any extra explanation.

Thus answer: "了解像 R8 这样的关键工具用于代码压缩以及位图优化的最佳实践，以大幅削减原生内存使用。我们还将探讨如何使用新的 ProfilingManager 触发器来识别在实际环境中出现的 OOM 和内存异常。" We'll output that as final.
</think>

了解像 R8 这样的关键工具用于代码压缩以及位图优化的最佳实践，以大幅削减原生内存使用。我们还将探讨如何使用新的 ProfilingManager 触发器来识别在实际环境中出现的 OOM 和内存异常。

---
## 📝 详细原文

了解像 R8 这样的关键工具用于代码压缩以及位图优化的最佳实践，以大幅降低原生内存占用。我们还将探讨如何使用新的 ProfilingManager 触发器来识别 OOM 和现场内存异常。

**原文（English）**: Learn about critical tools like R8 for code shrinking and best practices for bitmap optimization to slash native memory usage. We’ll also explore how to use the new ProfilingManager triggers for identifying OOMs and memory anomalies in the wild.

---
## 📝 内容总结

## 会议演讲总结：构建内存高效的 Android 应用

**核心要点：**

**为什么内存优化至关重要**
内存是流畅 UI、快速启动等性能指标的隐形基石。内存不足会引发频繁 GC（导致卡顿）、内核回收页面（造成 ANR 和耗电）、低内存杀进程（引发冷启动和后台进程被杀），甚至触发 Google Play 的"不良行为"阈值，影响应用曝光。

**三大优化方案**

1. **启用 R8 优化器**：R8 不仅能缩减 APK 体积，还能通过移除未使用代码、压缩类名方法名、方法内联、合并类等手段降低内存占用。关键配置包括：`isShrinkResources=true`、`isMinifyEnabled=true`，并使用正确的 `proguard-android-optimize.txt`（AGP 9 起旧文件将不再支持）。Monzo 启用完整 R8 后，ANR 率下降 35%，冷启动改善 30%，应用体积缩减 9%。

2. **编写精的 Keep 规则**：避免使用 `-dontoptimize`、`-dontshrink`、`-dontobfuscate` 等全局规则及大范围包级通配符规则。AGP 和 R8 会自动保留 Fragment、View、Activity，无需手动添加。库开发者应区分消费者规则文件和内部规则文件，绝不在消费者文件中添加全局禁用规则。

3. **内存可观测性工具**（后续讲解）以及保持内存轻量化的最佳实践（由 Fung 介绍）。

**核心理念**：主动优化内存，才能持续保证应用的高性能与优质用户体验。

---

## 📝 完整文字稿

[音乐] >> 大家好，我是Alice，我和我的同事们将一起分享如何开发高性能应用。说到性能，我们通常会想到一些可见的指标，比如流畅的界面和快速的启动速度。但其实，内存才是这些指标背后的隐形基石。如果你的内存使用没有优化好，应用的性能和用户体验都会受到负面影响。

你可以把手机的物理内存想象成这个有限的网格，这里展示的是设备上内存页面使用的一个简化模型。每开启一个屏幕、高清视频缓冲，或者加载一个端侧AI模型，都会占用这些页面。只要还有空闲页面，一切都运行得很顺畅。但如果所有内存页面都被占满、没有空闲页面了，会发生什么呢？

系统在后台就会拼命寻找更多空间，这种"挣扎"会带来一系列代价高昂的性能问题，比如界面卡顿、耗电、ANR（应用无响应），以及应用突然被杀死。

比如，系统可能会频繁触发垃圾回收（GC），去扫描堆中不再使用的对象。这种频繁的GC会导致UI出现明显的卡顿。

当可用内存降到某个阈值以下时，内核进程会回收并压缩内存页面。这会消耗大量CPU算力，导致应用出现不可预测的ANR和严重的耗电。

如果可用内存已经极低，低内存杀手机制就会介入，按照严格的优先级层级开始终止整个进程。这是冷启动的主要原因——用户不得不面对漫长的加载界面，等应用完全重建状态。它还可能造成高度干扰的进程突然被杀，比如后台正在播放的音乐播放器突然被关掉，因为系统的后台进程已经杀无可杀了。

不优化内存占用，还可能导致应用触发ANR或崩溃的"不良行为"阈值，这会影响应用在Google Play上的曝光度。

最后，Android正在开发新的系统级优化方法，以在整个生态系统中实现更强的内存管理和设备稳定性。

在本次分享中，我和我的同事将介绍三种帮助开发者优化内存的方案，最终提升应用的用户体验。

我会先讲如何配置R8规则；Fung会介绍一些保持内存轻量化的最佳实践；最后，我还会分享可观测性工具，帮助大家在实际环境中发现内存问题。

听完这次分享，你将拥有一份主动优化内存的路线图，确保应用持续保持高性能。

要提升应用性能，最有效的改动之一就是开启R8优化器。虽然R8在缩减APK体积方面广为人知，但它也有助于降低内存占用。因为从APK加载到RAM的代码越少，应用占用的内存也就越少。

R8会移除应用中未使用的代码和资源，从而减少加载应用所需的内存。这一点很重要——因为如果堆内存使用不优化，就会频繁触发GC，导致UI卡顿。

R8会把类、方法和字段的名称压缩成更短的名字，进一步降低内存使用。这一点也很关键，因为栈内存问题会让运行时变得复杂、低效。

R8还会执行一系列优化，比如方法内联——把方法调用替换成实际代码，还会合并多个类，从而减小堆大小和栈内存占用。

对用户来说，这意味着更快的启动速度、更流畅的渲染，以及更少的ANR。

了解了这些好处之后，我们来看看如何在代码中开启R8。

在应用的build.gradle文件中，将`isShrinkResources`设为`true`，这能让R8移除未使用的资源和代码。将`isMinifyEnabled`设为`true`，则让R8优化代码、移除未使用的类，并对类进行重命名以减小代码体积。

最后，记得指定默认的ProGuard文件，其中包含优化规则。

这里有一个关键点：一定要用正确的默认ProGuard文件。一些遗留的旧文件会阻止R8对应用应用优化。

请注意，从Android Gradle Plugin 9开始，遗留的`proguard-android.txt`文件将不再受支持。所以，请用平台工具中打包好的`proguard-android-optimize.txt`替换掉那个错误的默认文件。

这个看似很小的配置改动，能显著提升多项性能指标。

如果你的Gradle properties文件里有禁用R8全模式的flag，请把它删掉，让R8发挥全部潜力。

由于这个改动会开启强大的优化，请务必对应用进行全面测试。

这些改动能对多项性能指标产生巨大影响。

举个例子：Monzo是一家拥有1500万用户且仍在增长的英国数字银行。随着应用规模扩大，团队把启动时间定为关键优化点，但又担心会需要对代码库做大量改动。他们希望找到一种方案，在不彻底重写代码的情况下提升性能。

通过完整启用R8优化，Monzo的应用无响应率大幅下降了35%。你知道吗？他们的冷启动慢速问题也改善了30%，整体应用体积缩减了9%。

总结一下：开启R8的同时，配合资源压缩、正确的ProGuard文件，并启用全模式，才能获得最大的优化效果。

当R8优化应用时，可能会误删一些通过反射等机制间接使用的代码，这会导致应用崩溃。为了解决这个问题，你可以使用keep规则（keep rules）。Keep规则的作用是告诉R8不要优化那些依赖反射的代码部分。

要添加keep规则，创建一个新文件，并在ProGuard文件的DSL中引用它。Keep规则是R8配置的核心，所以我们花点时间讲讲一些最佳实践。

我们的第一条、也是最重要的一条是……

（译注：原文到这里就截断了，最后一句话没说完。如果你需要后续内容，可以继续发给我，我帮你翻译。） 好的，我来把它翻译成自然的中文口语：

**实用建议**是确保你没有使用任何全局选项，因为这些选项会限制整个应用的优化效果。有几个全局保留规则要尽量避免：

- **"don't optimize"**（不优化）：这会关闭整个应用的优化功能，导致应用变得明显更大、更慢。
- **"don't shrink"**（不缩减）：这会阻止移除未使用的代码和资源，强迫用户下载一个臃肿的应用。
- **"don't obfuscate"**（不混淆）：这会阻止把人类可读的类名、方法名、字段名改成短名称，妨碍 R8 减少内存占用，尤其是对大型应用来说影响很大。

另一个常见的坑是使用带有通配符的、大范围的包级别保留规则。比如这样的规则会把整个包里的所有类、字段、方法全部保留。这样 R8 就没办法移除包内没用的类或方法，没法优化内部逻辑，也没法压缩任何名称。这种大而宽的保留规则会导致应用性能下降，所以建议删掉它们。

因为 AGP 和 R8 会协同工作，自动识别那些在优化后需要保留的 Fragment、View 和 Activity，所以你根本不需要为这些 Android 组件写保留规则。

**总结一下**：只添加那些能阻止 R8 优化依赖反射代码的规则。规则的作用范围要尽量精确，不要用全局选项，不要用大范围的包级别保留规则，也不要为 Android 组件写保留规则。

如果你是**库开发者**，有两个地方可以定义保留规则：消费者规则文件（consumer rules file）和内部规则文件（internal rules file）。

- 你必须放进**消费者规则文件**里的，是那些需要提供给使用你库的应用的规则。这些规则会自动打包并应用到任何引入你库的应用里，确保通过反射或其他间接方式访问的代码能被保留。
- 在消费者文件里添加 `dont shrink`、`dont optimize`、`dont obfuscate` 这类规则是一个**严重的错误**。因为这些规则会合并进应用的整体配置里，相当于你强制让所有用你库的应用都彻底关掉 R8 优化。
- 为了防止这种情况，从 **AGP 9** 开始，如果库的代码里包含这些全局保留规则，就**不能再发布**了。

**ProGuard 规则或 profile** 文件里应该放那些只应用于你库本身的保留规则。这个文件不会传递给使用你库的应用，它的用途是在你的库自己构建的过程中，保护那些库对外公开的 API 实现不被 R8 移除。

想了解更多如何为你的库写保留规则，可以去看我们更新过的库作者指南。

为了帮你**最大化 R8 优化效果**、写出更精确的保留规则，我们推出了**R8 配置分析器**（R8 configuration analyzer），它集成在新版 R8 里。运行一个启用了 R8 的构建就可以生成它。

R8 配置分析器会展示你应用里有多大比例的代码可以被优化。它提供三个指标：

- **混淆分数（Obfuscation score）**：显示应用里有多少代码被重命名以节省内存。
- **优化分数（Optimization score）**：告诉你有多大比例的代码被优化过。
- **缩减分数（Shrinking score）**：显示有多少资源被移除了。

你可以看这三个指标来监控、检查、改进你的应用配置。

通过这个分析器，你可以看到每条保留规则影响了多少个类、方法或字段。还能看到因为某一条保留规则，导致应用里有多大比例的代码无法被优化。

保留规则的详情页面会告诉你具体是哪些类、方法或字段被阻止了优化。如果你发现某条保留规则阻碍了那些本可以被优化的方法或字段，就把这条规则替换成更具体、更精确的。

用 R8 配置分析器，你还能看到哪些保留规则**包含了**其他规则——意思是一条更宽泛的保留规则已经覆盖了同一些代码，使得更精确的规则变得多余。一定要把那条影响范围更大的保留规则删掉，这样才能从 R8 获得最大的收益。

**AndroidX、Kotlin 库**以及很多主流的开源库本身都已经做了相当好的优化，并且包含了精确的注解。所以，记得把那些覆盖到这些库的保留规则删掉。

配置分析器还能告诉你**哪些库在引入大范围的保留规则**。可以向这些库的开发者提 issue，或者换一个能实现同样功能、但已经做过优化的替代库。

想了解更多，可以看看屏幕上的链接，今天就来试试 R8 配置分析器吧。

**总结一下**：R8 是构建高性能 Android 应用的基础工具。用 R8 做优化是打造更小、性能更好的应用的第一步。要想获得最大收益，就要用正确的配置启用 R8，定义好保留规则来解锁最大程度的优化，并用 R8 配置分析器来检查和改进你的配置。

为了**加快你的开发流程**，我们新增了一个 agent skill，你可以在 Android Studio agent 或其他 AI 工具里使用。这个新的 agent skill 能通过解决配置错误来优化你现有的 R8 设置，然后利用配置分析器来清楚地展示保留规则是如何影响你的代码库的，最后给出优化这些规则的具体建议。这个 agent skill 能让你以最小的努力提升应用性能。你可以在这个链接里找到关于 agent skill 的更多详情和使用方法。

接下来，Fang 会演示如何进一步优化你应用的内存使用。

我们来说说**优化内存使用最有效的事情之一：位图（Bitmap）**。在这个多媒体时代，用户花大量时间在手机上浏览图片——刷社交媒体、分享照片、找餐馆，位图无处不在。这正是你应该重点关注的地方。

位图是你的应用需要处理的最大、最常见的内存对象。位图的解码以及其他跟位图尺寸成比例的操作，经常都处在绘制的关键路径上……

（句子在这里被截断了，没说完。需要的话我可以继续翻。） 好的，下面是这段英文的中文口语化翻译：
---
