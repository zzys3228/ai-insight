---
title: Build adaptive layouts with Navigation 3
title_zh: 使用 Navigation 3 构建自适应布局
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: Android
type: 技术演讲
level: Intermediate
speakers: bsagmoe, clarafok
video: https://www.youtube.com/watch?v=j0k8qizH0KY
---

# 使用 Navigation 3 构建自适应布局

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: Android | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: bsagmoe, clarafok

使用 Jetpack Navigation 3.1.1 中的最新更改简化你的应用架构。探索如何使用其状态驱动的返回栈以及新的场景装饰器 API，在所有窗口尺寸上原生支持多窗格、适应性布局。

---

## 📝 详细原文

通过 Jetpack Navigation 3.1.1 的最新更改简化您的应用架构。了解如何使用其状态驱动的返回栈以及新的场景装饰器 API，以原生方式支持跨所有窗口尺寸的多窗格、自适应布局。

**原文（English）**: Simplify your app’s architecture with the latest changes in Jetpack Navigation 3 1.1. Discover how to use its state-driven back stack and the new scene decorator API to natively support multi-pane, adaptive layouts across all window sizes.

---


---

### 原文

Simplify your app’s architecture with the latest changes in Jetpack Navigation 3 1.1. Discover how to use its state-driven back stack and the new scene decorator API to natively support multi-pane, adaptive layouts across all window sizes.

---

## 📝 内容总结

**《使用 Navigation 3 构建自适应布局》核心要点**

一、核心主题概述

本演讲详细讲解Navigation 3库的核心概念和1.1版本更新，重点介绍scene decorator API如何帮助构建自适应多窗格布局。

**二、关键发布/技术要点**
- 要点1：状态驱动返回栈——返回栈是普通列表，完全归开发者所有，支持任意类型key
- 要点2：Scene接口——控制显示哪些entry及如何显示，支持对话框、列表详情、翻页等多种布局
- 要点3：Scene Strategy——按顺序评估策略，第一个返回scene的策略决定布局
- 要点4：元数据API改进——新增NavMetadataKey接口和metadata DSL，实现类型安全
- 要点5：共享Nav Entry——改进共享过渡布局，共享entry作为共享元素执行动画
- 要点6：Scene Decorator——修改由scene策略计算出的scene，添加顶部栏、底部栏等UI元素
- 要点7：Wear OS支持——推出Nav 3集成，包含可滑动关闭场景策略

**三、落地应用**
- 案例1：列表详情菜谱应用通过scene decorator添加边框装饰
- 案例2：响应式导航示例展示底部导航栏与导航轨道自动切换
- 案例3：对话场景装饰器示例展示用元数据判断是否装饰scene

**四、总结**
Navigation 3让自适应UI构建变得前所未有的简单。通过scene策略和decorator API，开发者可轻松实现多窗格布局，同时保持导航逻辑与UI的紧密配合。Wear OS支持和即将到来的深链接API将进一步扩展其适用范围。

---

## 📝 完整文字稿

好的，我来帮你翻译成中文口语：

---

[音乐] 大家好，我是Ben，是做导航3（navigation 3）开发者关系的工程师，待会儿Clara也会加入我们。这节课呢，我会把用导航3给应用做自适应布局的所有东西都讲一遍。先简单过一下这个库的核心概念，然后讲讲1.1版本更新了什么。其中会重点讲一下scene装饰器，这个东西可以在你应用的主要内容外面加上顶部栏、底部栏这些常用的UI元素。最后我们再看看导航3怎么扩展到Wear OS上，再给大家剧透一下1.2版本我们在做啥。

嗨，我是Clara。首先咱们过一下导航3的一些基本概念。导航3从一开始就是以Compose的状态作为基础来搭建的，也就是说它完全采用了声明式编程那一套。你改变你拥有的状态，然后我们对新状态做出反应。

首先，回退栈（back stack）就是一个普通的列表，完全归你所有。栈里存的是key，这些key可以是任意类型。栈里每个key都对应一个nav entry，每个entry里装的是一段composable内容。你往回退栈里加key或者删key的时候，导航就会根据当前栈里的key重新组合出对应的内容。

要搭起来的话，先定义你的nav key，然后用一个key创建一个回退栈。在这个例子里，key继承了可选的nav key接口。然后调用nav display这个composable，把回退栈传进去。

不过nav display还得知道每个key对应啥内容，所以你需要传一个entry provider进去。entry provider的活儿就是：给你一个key，它就返回一个nav entry。在nav display里调用entry provider的DSL，然后用nav key加上对应的内容来添加entry就行了。就这么简单。

Nav display会先决定要显示啥，然后用你的key去调entry provider拿到正确的entry。在这个例子里，entry provider会给home key返回home nav entry。

默认情况下，导航会显示跟回退栈最后一个key对应的nav entry。但如果你想要更复杂的布局呢？比如你想同时显示多个entry怎么办？这时候scene接口就派上用场了。一个scene控制要显示哪些entry、怎么显示。也就是说，同一个nav display可以拿来以不同的布局显示entry，比如对话框、左右分栏的列表详情、横向翻页、底部弹窗，或者就一个单栏。

那nav display咋知道该用哪个scene来显示entry呢？它就是去问你传给它的每个scene strategy。nav display会按你往列表里加的顺序，一个个过这些scene strategy。第一个返回scene的strategy就说了算，由它来决定显示哪些entry、用啥布局。然后nav display会调这个返回的scene去真正显示内容。

这些strategy的列表是可以改的，nav display会重新算一遍然后显示新的scene。

那scene strategy自己咋决定要不要返回一个scene呢？其中一个办法就是看entry的元数据。nav entry有一个metadata字段，是个map，键是字符串，值是任意类型。nav entry可以通过加上某个strategy定义的元数据来"选择"让那个strategy来显示自己。这样entry就能自己决定想怎么被显示。在这个例子里，这个entry就选择要以对话框的形式显示。

在1.1版本里，我们听了大家的反馈，把API做了几处改进。以前啊，scene strategy得用一个then中缀操作符把它们串起来，链式地传过去。但问题是那个参数名是单数的"scene strategy"，而且then这个中缀也不太好找。所以在1.1里，我们把这个参数改成了复数的"scene strategies"，现在它接收一个strategy列表。不过记住，顺序还是很重要，前面说过，第一个返回scene的strategy说了算，strategy是按它们在列表里的顺序来评估的。

接下来，1.1里我们还改进了元数据的API。前面提过，metadata是一个String到Any的map，这样类型安全不太好。而且key通常都是用字符串常量声明的，也不容易发现。所以我们加了一个nav metadata key接口和一个metadata DSL来改进。

现在你定义metadata key的时候，可以选择性地实现这个nav metadata key接口。你会看到这个接口有个类型参数，这个参数代表跟这个key关联的数据的类型。也就是说，你定义key的时候，同时也声明了它能接受什么类型的数据。这就能帮你确保存的数据类型是对的。

有了nav metadata key，你就可以用metadata DSL了。这个DSL就是一个类型安全的map构建器，里面有个put函数，接收实现了新key接口的key，以及跟key关联的值。DSL会返回一个String到Any的map，里面装的就是你用put加进去的数据。你还可以用加号操作符把多个metadata map合并起来。这样你就能声明模块化的、可复用的metadata，然后混搭着用，拼出某个entry最终用的metadata。用DSL你还能写一些条件逻辑，来决定最后要加哪些metadata。

1.1里加的另一个新功能是共享nav entry的支持。现在你用共享过渡布局（shared transition layout）的时候，nav display会把共享的entry作为共享元素加上过渡动画。前面说过，导航3能同时在屏幕上显示多个entry，有时候同一个entry会在不同页面之间共享。比如，想象一个两栏的应用，一个页面显示entry A和B，然后跳到另一个新页面显示entry B和C。这种情况下，两个页面就共享了entry B。

我们来看一个真实应用里的效果。这个应用展示……

---

翻译完了！中间有一些术语保留了英文（比如nav entry、scene strategy、DSL、composable、key这些），因为这些在Jetpack Compose的圈子里基本都直接用英文说，硬翻成中文反而听起来别扭。如果你想全部翻译成纯中文，告诉我一声哈。 两个产品并排显示在屏幕上。当你导航到下一个产品时，原本在右边的产品会移动到左边，新产品则显示在右边。一切都按预期工作。但是你会注意到，当条目从右边移动到左边时并没有过渡动画，而且右边会闪一下。这是因为一个条目在屏幕上只能显示一次。所以，当屏幕重新组合后，原本在右边的条目会立即消失，因为现在它已经移到左边了。在 1.1 版本中，我们改进了共享导航条目，让它们作为共享元素来执行动画。这样一来，一个共享条目可以在离开旧屏幕的同时进入新屏幕，整个过渡过程是连续流畅的。让我们回到刚才那个应用。现在你可以看到，当你导航到下一个屏幕时，原本在右边的产品会平滑地滑动到左边。正如前面提到的，1.1 版本新增了对共享条目的支持。所以，你只需要应用共享过渡就行了。我们来看看代码是什么样的。首先，把 NavDisplay 包在一个 SharedTransitionLayout 里面。然后，把提供的 SharedTransitionScope 传给 NavDisplay。就这样。现在，当屏幕之间进行切换时，它们之间所有的共享导航条目都会作为共享元素来显示，从而实现平滑的过渡效果。现在，把时间交给 Ben 来讲解 scene decorator。最后，1.1 版本引入了 scene decorator（场景装饰器），它允许你修改由应用场景策略计算出来的场景。你可以用场景装饰器来添加一些 UI 元素，比如顶部应用栏、导航栏或者导航轨道，这些是你想在场景层面添加，而不是导航条目层面添加的。为了演示这个 API，我们来走一遍实现一个简单场景装饰器的过程，这个装饰器会给它所装饰的场景加一个边框。首先，我们定义一个 BorderScene 类，它接受一个 scene 以及一些用来绘制边框的配置参数。因为 BorderScene 实现了 scene 接口，所以它需要重写 key、entries、previousEntries 和 content 这些属性。由于 BorderScene 只是把传入的 scene 包装了一层，所以它的 entries 和 previousEntries 跟传入的 scene 是一样的。在这个例子里，它的 key 也可以直接拷贝传入 scene 的 key。这个等会再细说。至于它的 content 属性，BorderScene 用一个 Box 配合所需的修饰符来画一个外边框，然后在这个 Box 里面调用传入 scene 自己的 content composable。现在我们有了 BorderScene 类，还需要一个使用它的方法。这就是 SceneDecoratorStrategy 接口发挥作用的地方了。我们创建 BorderSceneDecoratorStrategy 类作为这个接口的实现。这个接口只有一个需要重写的方法：decorateScene。和 SceneStrategy 接口里的 calculateScene 方法不同，decorateScene 不能返回 null。相反，如果传入的 scene 不需要被装饰，你直接原样返回它就行了。在决定是否要装饰一个给定的 scene 时，场景装饰策略可以考虑传入 scene 的元数据、它的导航条目，以及它能访问到的任何其他状态。最后一步是创建你的场景装饰策略实例，然后通过 sceneDecoratorStrategies 参数提供给应用的 NavDisplay。现在，当我们运行应用时，就得到了这样的结果。正如我们希望的那样，所有导航条目的内容都被加上了边框，不管同一时刻显示的是一个还是多个条目。接下来我们仔细看看这两种配置下底层都发生了什么。当窗口宽度比较窄时，twoPaneSceneStrategy 在场景计算阶段会返回 null，因为没有足够的空间并排显示两个面板。NavDisplay 然后回退到一个 singlePaneSceneStrategy，它会返回一个单面板场景。在场景装饰阶段，蓝色边框装饰策略接收这个单面板场景，然后返回一个把它包起来的 BorderScene。这个返回的蓝色 BorderScene 接着作为输入传给红色边框装饰策略，红色策略又把它包成另一个 BorderScene。现在我们来看看窗口更宽时会怎么样。这种情况下，twoPaneSceneStrategy 会返回一个两面板场景，场景计算阶段到此结束。场景装饰阶段的流程跟之前一样，只是初始输入是两面板场景而不是单面板场景。这个例子中有一个重要的地方需要注意：场景装饰之后返回的 scene 它的类要保持一致，即使场景计算阶段返回的 scene 类发生了变化。这一点很重要，因为 NavDisplay 是在当前 scene 的类以及它的 key 属性派生出来的 key 发生变化时，才会对场景之间的切换执行动画。如果你的应用里引入了场景装饰器，而不同的场景又用了相同的 key（比如 nav3 菜谱列表详情那个示例），就可能产生一些意料之外的行为。对于这种情况，一种解决方案是提供一个最初的场景装饰策略，它把计算出来的 scene 除了 key 以外的所有东西都原样拷贝过去，但 key 用一个根据它的类和 key 派生出来的新值。这样一来，后面跟着的装饰器就可以直接拷贝传入 scene 的 key 了。按照这种方法处理后，列表详情菜谱应用现在的行为就跟没有加任何场景装饰器时一样了。现在我们已经讲完了场景装饰器的基础知识，再来看看它在一些更实际场景下是怎么用的。我们在 nav3 recipes 的 GitHub 仓库里发布了一些示例，演示了两种用法。第一种展示了如何创建一个场景装饰器，它能根据窗口大小在底部导航栏和导航轨道之间自动切换。第二种展示了如何创建一个场景装饰器，把整个场景显示在一个对话框里。视频里没法把所有细节都讲到，下面是这些示例所演示内容的一个大致介绍。在响应式导航的示例里，我们演示了如何…… 好的，我来帮你翻译成中文口语版本：

我们利用 Compose 的可移动内容和共享元素 API，确保任何时候都只有一个可组合组件的实例——也就是这里的导航栏或导航栏被组合起来。我们还演示了场景装饰器如何考虑像当前窗口尺寸类别这样的状态来决定如何装饰场景。在对话场景装饰器的示例中，我们展示了一种使用元数据来判断是否以及如何装饰场景的方法。关于 Navigation 3 1.1 的新内容就讲到这里。现在我把话筒交给 Clara，让她来分享 Wear OS 的更新以及 Navigation 3 接下来的计划。

Navigation 3 的支持不止于移动设备。今天就推出了 Wear OS 的 Nav 3 集成，其中包含 Wear Compose Navigation 1.6 稳定版中的可滑动关闭场景策略。只需要在你的导航显示中添加 `rememberSwipeDismissibleSceneStrategy`，这些条目就会用 Wear 材质组件来展示。它还完整支持滑动手势。

除了 1.1 版本，我们也在为 1.2 版本开发几个新功能。是的，我们听到了你们的声音。我们将添加用于支持深链接的 API，以及用于在各个目的地之间传递事件或基于状态的结果的 API。目前，我们有一些示例代码展示了这两种功能的实现方式，但我们正在把这些示例升级为正式的 API，让你们使用起来更方便。所以，还有更多内容值得期待。

感谢大家今天的参与。我们希望你们已经了解到 Navigation 3 是如何让构建自适应 UI 变得前所未有的简单。要查看本次演讲中提到的示例代码以及其他更多内容，请查看描述中的链接。最后但同样重要的是，如果你有任何反馈或功能需求想要跟我们分享，请通过 GitHub 或问题跟踪器联系我们。
---
