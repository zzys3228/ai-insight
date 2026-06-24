---
title: Build custom design systems with Jetpack Compose’s new Styles API
title_zh: 使用 Jetpack Compose 的 Design Tokens 构建自定义设计系统

原句："Build custom design systems with Jetpack Compose’s new Styles API"

这是关于Jetpack Compose的一个技术句子。我需要准确翻译它。

"Build" - 构建/创建
"custom design systems" - 自定义设计系统
"with" - 使用
"Jetpack Compose's new Styles API" - Jetpack Compose 的新 Styles API

翻译结果：使用 Jetpack Compose 的新 Styles API 构建自定义设计系统
</think>

使用 Jetpack Compose 的新 Styles API 构建自定义设计系统
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: 设计
type: 技术演讲
level: Intermediate
speakers: chuckj, magicalmeghan, riggaroo
video: https://www.youtube.com/watch?v=e-wlF3cmJms
---

# 使用 Jetpack Compose 的 Design Tokens 构建自定义设计系统

原句："Build custom design systems with Jetpack Compose’s new Styles API"

这是关于Jetpack Compose的一个技术句子。我需要准确翻译它。

"Build" - 构建/创建
"custom design systems" - 自定义设计系统
"with" - 使用
"Jetpack Compose's new Styles API" - Jetpack Compose 的新 Styles API

翻译结果：使用 Jetpack Compose 的新 Styles API 构建自定义设计系统
</think>

使用 Jetpack Compose 的新 Styles API 构建自定义设计系统

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: 设计 | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: chuckj, magicalmeghan, riggaroo

使用 Jetpack Compose 中的全新 Styles API，解锁并标准化构建自己的自定义设计系统。Styles API 不仅引入了在主题级别覆盖属性的能力，而且相对于 Modifiers 还带来了更佳的性能优势。了解 Material 将如何采用 Styles，使用 Style API 创建有趣的动画，以及如何组合 Styles 来构建自己的设计系统，并使用能够适应不同设备尺寸的主题。

---

## 📝 详细原文

使用 Jetpack Compose 中的新 Styles API 解锁并标准化构建您自己的自定义设计系统。Styles API 不仅引入了在主题级别覆盖属性的能力，还带来了相较于 Modifier 的性能优势。了解 Material 将如何采用 Styles，使用 Style API 创建有趣的动画，以及如何组合 Styles 构建一个能够适应不同设备尺寸的主题的自有设计系统。

**原文（English）**: Unlock and standardize building your own custom design systems with the new Styles API in Jetpack Compose. The Styles API not only introduces the ability to overwrite properties at a theme level, but also brings with it some nice performance advantages over Modifiers. Discover how Material is going to adopt Styles, create some fun animations with the Style API, and how to combine Styles to build up your own design system with a theme that adapts to different device sizes.

---


---

### 原文

Unlock and standardize building your own custom design systems with the new Styles API in Jetpack Compose. The Styles API not only introduces the ability to overwrite properties at a theme level, but also brings with it some nice performance advantages over Modifiers. Discover how Material is going to adopt Styles, create some fun animations with the Style API, and how to combine Styles to build up your own design system with a theme that adapts to different device sizes.

---

## 📝 内容总结

**《使用 Jetpack Compose 的 Styles API 构建自定义设计系统》核心要点**

一、核心主题概述

本演讲预览Jetpack Compose的Styles API，介绍如何构建自定义设计系统，包括基于状态的样式、性能优势和主题集成。

**二、关键发布/技术要点**
- 要点1：Style定义——一种特殊的modifier，提供性能和可重用性优势
- 要点2：四个基础特性——覆盖、继承、复用、合并
- 要点3：基于状态的样式——支持pressed、hovered、focused状态
- 要点4：animate lambda——状态之间平滑过渡动画
- 要点5：自定义样式状态——定义LoadingState等业务状态
- 要点6：自定义Style——限制scope只暴露相关扩展函数
- 要点7：性能优势——分配减少70%，渲染下一帧速度提升2.3倍
- 要点8：主题集成——通过主题公开默认样式

**三、落地应用**
- 案例1：JetSnack渐变按钮通过ButtonStyle + GradientStyle合并实现
- 案例2：按钮悬停时的阴影移动动画
- 案例3：Loading和LoadingError状态的自定义样式

**四、总结**
Styles API是构建自定义设计系统的强大工具。通过覆盖、继承、合并等特性，配合基于状态的样式和内置动画，开发者可轻松创建可主题化、高性能的UI组件系统。Material 3即将采用Styles。

---

## 📝 完整文字稿

大家好，欢迎来到“使用 Jetpack Compose 的全新 Styles API 构建自定义设计系统”的演讲。我叫 Rebecca，今天和我一起站在台上的还有 >> Megan >> 以及 Chuck。>> 我们已经看到 Android 正在不断发展，以支持不同的设备形态，而应用程序也越来越希望通过自定义设计系统定义从众多应用中脱颖而出。我们理解每个应用都是独一无二的。许多应用使用的是 Material 设计系统，从完全基于 Material 的设计系统到完全自定义的设计系统，跨度很大。如果你正好处于这个光谱的中间地带，我们正在构建一个能够覆盖这种范围的框架。Jetsnack 是我们在 Compose 中发布的首批示例之一，它一直是在 Compose 中构建自定义内容并利用底层 Material 组件的优秀展示。但它的设计系统一直有着自己独特的定义，因为在整个系统中广泛使用了渐变效果。组件的设计通常与 Material Design 开箱即用的组件略有不同。它以多种不同的方式使用渐变，例如这个 filter chip 在正常状态下具有渐变边框，而按下状态是实心的渐变效果。另外，当我们查看 Material 组件时，它们内置了非常出色的默认值。这就是我们喜欢使用 Material 的原因。它会为你处理所有这些复杂问题，例如无障碍标准、从右到左的布局、各种不同的交互状态，并且组件通常开箱即用就很好看。但正如我们所见，我们的设计师给我们的东西更加自定义一些。那么通常你会怎么做呢？对于这个 filter chip 示例，你可能尝试导入 Material 的 filter chip，然后立即尝试在选中时设置一个渐变的背景颜色。此时，你可能会发现该 API 在设计时只考虑了单一颜色，并不支持 brush 类型。此时，你可能会做以下几件事之一。在这种情况下，我将颜色设置为透明，然后将 chip 包裹在一个 Box 中，并使用 modifier.background 在 Box 上设置渐变效果。然后将 filter chip 移动到这个 Box 中。看起来还不错，但当我们实际运行它们时，我们可以看到我们还需要将形状应用到容器上。不仅如此，我们现在还需要构建自己的逻辑来处理按下和选中状态。所以，此时你可能也会认为是时候 fork Material 源代码或创建自己的组件版本了。在 JetSnack 中，我们创建了一些自己的组件。但是，这意味着我们的应用正在失去 Material 的所有这些好处。因此，我们一直在研究一些新东西，今天想向你预览一下，它叫做 Styles。Styles 是 Jetpack Compose 中用于自定义元素的新机制。它们旨在将形式与功能分离，并解锁基于状态的简单样式，以及一些额外的性能优势。Styles API 已在 Compose Foundation 1.12 版本中作为实验性 API 发布，Material 的 API 采用也即将到来。你会看到这是你与组件交互方式的一个重大转变。我们将向你展示 Styles 如何通过 JetSnack 的全新版本帮助你以易于使用的方式自定义组件。仍然使用渐变效果，只是更加微妙一些。下面我把话筒交给 Megan，让她来详细介绍。>> 谢谢你，Rebecca。那么，让我们开始吧。正如我们所说，我们正在使用 Styles API 对 JetSnack 进行改造，但你可能都在问：“什么是 style？”Style 是一个定义组件外观的接口。Style 是一种特殊的 modifier，它自动提供性能和可重用性优势。我想强调的是，Styles 不是用来替代 modifier 的，而是用来替代与视觉属性相关的参数的。让我展示一下我的意思。正如我们在本次演讲中提到的，我们将使用 JetSnack，它使用 button 的自定义实现来实现渐变效果。正如你所看到的，button 的这个定义有许多不同的样式参数，例如 disabled state、shape、border 等等。但使用 Styles，我们可以使用一个简单的 style 参数替换所有这些代码行，该参数提供了一组可以在任何组件上设置的标准化属性。好的。现在你知道什么是 style 了，让我们看看如何使用 style。将 Styles 添加到组件中有两种用例。一种是创建自定义组件并使其可样式化，另一种是使用具有 style 参数的 composable。那么，让我们看看如何使自定义组件可样式化。在底层，JetSnack 的 button 实现为一个可点击的 row。为了使 button 可样式化，你可以添加一个 styleable modifier。然后，你将 style 参数添加到方法签名中，以便自定义 button 的实现可以使用 style 参数来自定义 button 的实现。始终建议在设计系统组件上提供一个 style 参数，就像你始终提供 modifier 一样。然后，你将 style state 和 style 参数传递给 styleable modifier，我们现在不深入讨论 style state，我们稍后会在本次演讲中讨论它。现在我们的自定义 button 已准备好使用 Styles 了。另一种用例是使用 style 来对具有 style 参数的组件进行样式化，就像我们刚刚创建的 button 一样。在 JetSnack 中，我们将使用 button 的自定义实现。这是 style 块中没有任何内容时的样子，让我们添加一些样式。这里列出了所有可用的 style 属性，正如你所看到的，它非常全面。不要迷失在细节中。所有这些都在文档中。而且我们 好的，我来把它翻译成中文口语风格：

我们要用 background 属性来把背景改成浅灰色。在 style 代码块里，我们加上 background 然后传个浅灰色进去，就这么简单就能用 style 属性来修改我们的组件。当然啦，这只是皮毛而已，我们接下来要讲的是怎么从这个状态变成带有渐变、动画和基于状态的样式的按钮，这些都会用 style API 来实现。不过在讲这些好玩的东西之前，我们得先打好 style 的基础。来，各位。笑一个。对对对，就是这样。基础一：style 属性之间会互相覆盖。基础二：style 属性是可以继承的。基础三：style 是可以复用的。基础四：style 是可以合并的。接下来我们就要边给新的 JetSnack 按钮做样式，边演示这四个特性。

回到按钮的代码里，我们已经用了 background 属性把背景颜色改成了浅灰色。同样很简单地，我们也可以给按钮加其他属性。语法上呢，直接换一行写新属性就行，不用加逗号。我们加上 width（宽度）、height（高度）、shape（形状）、font weight（字体粗细）和 text alignment（文本对齐）。然后再加个外边距 32 DP。如果我只想改顶部的内边距，就加个 padding top 传 16 DP。你可能以为这样会得到 32 DP 加 16 DP 的内边距，但实际你只能得到 16 DP 的顶部内边距。这是因为当同一个属性被设置两次时，style 属性会互相覆盖。按钮本来有 32 DP 的内边距，但因为 padding top 是最后定义的，所以它会把顶部内边距覆盖成 16 DP。如果用 modifier 的话，它会把两个内边距加起来，得到 48 DP 的顶部内边距。

在 Jetpack 里，我们还有一个自定义的 text composable，它接受一个 style 参数。你可能会问：既然 font weight 和 text align 这些属性影响的是文字而不是按钮，为什么我们要通过按钮来设置，而不是直接在 text style 里设置呢？咱们来研究一下 text align。如果把 text align 从按钮的 style 里去掉，直接加到 text style 上，得到的效果是一样的。根据使用场景不同，有些情况下我们会把 text align 放在按钮这一层，因为某些文字样式属性是可以继承的。通过在按钮层设置 text align，里面的文字内容就会从父 composable 继承这个对齐方式。当只有一个子 composable 的时候差别不大，但如果我们传一列 text composable 作为按钮内容，它们就都会继承居中对齐。但如果你在某个 text composable 上直接加了 text align style 参数，那就会覆盖从父 composable 继承来的对齐方式。这里"加入购物车"这几个字就覆盖了居中对齐，而"二"没有覆盖，所以它还是继承按钮的居中对齐。

优先级最低的是父级定义的样式。如果你在组件上用 modifier 设置样式，那它的优先级比父级定义的样式高。最后，直接设置 style 参数的优先级最高。再次提醒，这只针对那些可继承的文字样式属性。

现在我们有了一个很好看的按钮样式，可能想在 App 里多个按钮上用这个样式。所以我们可以创建一个叫 ButtonStyle 的样式对象，在里面加上我们之前在按钮 style 里加的那些属性。然后就可以把按钮的 style 属性全部替换成 ButtonStyle。因为 style 是可以复用的，所以这个样式可以传给多个不同的按钮，给它们提供统一样式。

接着我们再加一个新的样式叫 GradientStyle，用来放一些更特别的样式，比如阴影和渐变。在里面我们可以加 drop shadow（外阴影）和 inner shadow（内阴影）。如果把按钮的 style 换成 GradientStyle，ButtonStyle 里的所有东西就都没了——宽度、高度、形状、内边距、文字对齐全没了。但我们其实想要的是 ButtonStyle 和 GradientStyle 的组合效果。这时候就要用到 style 合并了。在 style 参数里，我们同时传 ButtonStyle 和 GradientStyle，只要再加一个参数就行。现在我们就能看到 GradientStyle 里的阴影效果了，给按钮增加了很多立体感。

接下来我们再加个背景渐变。在 GradientStyle 里，我们可以用 linear gradient（线性渐变）来加个 brush。但是你可能还记得，ButtonStyle 里有 background，GradientStyle 里也有 background。不过我们看到的还是 GradientStyle 的背景。这是因为在 style 参数里 GradientStyle 排在 ButtonStyle 后面。还记得我们说过的 style 属性可以覆盖这个特性吗？最后定义的样式属性会胜出。因为 gradient 传在后面，它的 background 属性是最后定义的，所以我们就看到了这个。如果把 GradientStyle 和 ButtonStyle 的顺序换一下，看到的就是灰色背景了。阴影还在，因为 GradientStyle 还在生效，只是 background 属性被覆盖了。注意，因为样式是可以覆盖的，所以渐变背景直接把灰色背景替换掉了，不是叠加在灰色上面。另外语法上还可以用中缀 then 操作符来合并样式。

这一节我们学了 style 的四个基础特性：可覆盖、可继承、可复用、可合并，并且用这些特性做出了一个漂亮的渐变按钮。太棒了！

接下来我们来聊聊交互状态和样式。我们确实有 th……（未完待续） 这个按钮样式已经做得很漂亮了，但我们想根据不同的交互状态来添加样式。Styles API 默认内置了几个状态：默认状态（也就是没有交互发生的时候）、按下状态、悬停状态和聚焦状态。悬停和聚焦会在有鼠标连接的设备上触发，聚焦还会在像电视这种有方向键导航的设备上触发。为每个可交互元素定义所有这些状态是个好主意，因为你的用户会使用各种不同的配置来操作你的应用。所以，我们已经把 button style 和 gradient style 传入了 style 参数，我们可以通过样式对象来添加基于状态的样式，也可以通过在括号后面添加一个内联样式块来添加，我们决定用后一种方式。在那个块里，你可以添加一个 press 块。在我们的 press 块中，语法跟样式块里的一样。为了定义按钮被按下时的样式，我们添加一个 background 属性，把它设置为浅紫色。现在你可以看到，当按钮被按下时，它会变成浅紫色。现在，我们来添加 hover 和 focus。Hover 是淡紫色背景，就这里，然后 focus 是浅紫色边框。等它转一下。我们所有的状态都好了，耶！基本上要做基于状态的样式——按下、悬停和聚焦，就是这么简单。回到 Rebecca 那里。现在，我们简单聊一下动画和样式。这是我最喜欢的话题。我们能够添加基于状态的样式，这给你的应用增色不少，但状态之间的过渡并不像我们想要的那样平滑或优雅。它只是直接跳到最终状态，没有任何平滑的过渡。为了在这些不同的状态之间缓和过渡，你可以用 animate lambda 把任何样式属性包起来，这样它就会在 lambda 块内的起始状态和最终状态之间自动执行过渡。在这个例子里，我们一开始把内阴影的 DP 偏移量设置为 0。然后当它处于悬停状态时，我们把 DP 偏移量改成向内偏移 -6 DP 和 -2 DP。我们也用同样的方式移动投影，这样在悬停时就有了风格的阴影移动动画效果。我们可以添加很多不同的属性一起做动画。比如，我们也可以给背景颜色做动画，让按钮在悬停时变色。好的地方是，这就不用自己去跟踪状态变化，也不用创建以前可能需要创建的那么多各种动画状态变量了。要自定义这些动画，你也可以在这个 animation 块里传一个 animation spec 进去。这里我们传入一个 tween spec，把 duration 设得长一点，这样可以看到动画变慢一点。但你可以传入任何你喜欢的 animation spec。现在把它交给 Chuck 来讲下一部分。>> 现在我们来聊聊自定义样式状态以及为什么要使用它们。让我们回到按钮定义那里，我们在那里定义了样式状态并把它传给 modifier 的 style。这个样式状态到底是什么呢？样式状态表示 UI 元素的当前状态，用来跟踪像按下、悬停和聚焦这样的交互状态，并且用于基于状态的样式，根据该状态来选择不同的样式属性。它允许把交互源和样式本身关联起来。如果不把状态和样式关联起来，代码仍然能编译，但当你按下按钮时，什么都不会发生。这就是样式状态的定义。这个定义你可以看到有一些内置的状态。你可能已经注意到最后有一个 get 操作符。这个 get 操作符之所以能实现自定义状态，是因为样式状态是从样式状态键到值的一个映射。我们来看一个怎么使用它的例子。在 JetSnack 里，我们希望"加入购物车"按钮在加载时或出错时有不同的外观。这里有一个更新过的设计，展示了不同状态应该长什么样。注意 loaded 状态的设计没有变。这很合理，因为它是我们的默认状态。但 loading 和 error 状态的设计是不一样的。要实现这些设计，我们需要以某种方式把加载状态传给样式，这样我们就可以改变按钮的外观来匹配设计。这正是自定义状态的用途。要创建一个自定义状态，首先你需要为这个状态创建一个类型。对于 JetSnack，我们想跟踪加载状态。所以，我们创建了一个 enum class，它有三个我们关心的值：loading、loaded 和 error。接下来，我们需要创建对应的样式状态键。这个键被组件用来把加载状态的当前状态记录到样式状态里。之后我们会用同样的键在状态本身中读取样式。创建样式状态键时，你需要提供一个默认值。这个默认值应该是在状态没有特殊时使用的值。在我们的例子里，就是已经 loaded 的时候。所以，我们用 loading state.loaded 作为默认值。要让样式能够读取这个自定义状态，我们需要给 style scope 添加一个扩展函数，这个扩展函数只有在自定义样式状态或自定义状态是 loading 时才会执行它的块。这个比如就是 pressed 的实现方式。它只在 is pressed 为 true 时才调用它的块。Style scope 是样式 lambda 的接收者作用域，它引入了像 padding、background 和 border 这样的样式属性。通过扩展它，我们就可以根据加载状态用 loading 来自定义样式了。Style scope 包含一个叫 state 的辅助函数，给像 loading 这样的扩展函数使用。它需要一个 key、一个 block 和一个 active 表达式。Key 就是我们刚刚创建的 key，也就是 loading state key。Block 就是 block 参数。我们直接把它传给 state。这 好的，我来把它翻译成自然的中文口语：

---

“is”这部分说的是：这个 block 参数设置的是只有在加载状态下才有的属性。最后呢，我们还有一个叫 active 的 lambda，它在加载状态下会返回 true。这里我们就直接把当前状态跟 loading 状态做比较就行了——`loadingState.Loaded` 或者 `loadingState.Loading`，也就是用来设置只在加载状态下才有的那些属性。

然后我们可以再加一个扩展函数，也就是在错误状态下的，我们叫它 `loadingError`，跟刚才那个 loading 是一样的套路。

现在我们回到 Button，把它改成接收 loading state，并且把这个状态传给 style。

首先，把 Button 改成接收一个 loading state 作为参数，默认值设成 `LoadingState.Loaded`，这样就跟 style state 的 key 对上了。

接下来要更新 style state，把 loading state 也加进去。这个是在创建 style state 的同一个表达式里做的。`rememberUpdatedStyleState` 后面可以接一个尾随 lambda，每次 Button 重组的时候都会被调用。我们就用 loading state 这个 key 把 loading state 记到 style state 里面去。

现在就可以自定义 Button 了。这里是一个简化版的完整 Button，包含了 focused、pressed 和 hovered 三种状态。我们把它改一下，让它在加载状态下看起来不一样，用的就是我们刚才写的那些扩展函数。这就是 style state lambda 的作用——让我们可以像覆盖 pressed、hovered、focused 一样，去覆盖 loading 和 loading error 的值。

还记得我们一开始要实现的那些设计吧？我们是这样实现的：加载的时候颜色从浅灰色变成浅橙色，出错的时候就变成浅红色。

就这样，我们实现了一个自定义的基于状态的样式。

我挺喜欢看着这些代码的，哈哈。Anyway，反正呢，通过把 loading 也加到 style state 的扩展里，现在任何用 style 的组件也都能用 loading state 了。比如说，JetSnack 的卡片或者 filter chip 都用得上。

但这样做有个问题——对于那些很多组件都会用到的通用状态来说还行，但 style 的 scope 里会塞一堆可能根本用不上的 style state 函数。比如 JetSnack 卡片和 filter chip 其实都不会去更新 loading state。`loading` 和 `loadingError` 这两个函数应该只在 loading state 适用的地方才出现。理想情况下，我们希望 loading 在那些没有 loading state 的组件的 style 里直接报语法错误。

这就是 custom style 能干的事了。自定义 style 让一个组件可以把 style scope 限制在只适合它的那些属性上，并且可以控制哪些扩展函数能用。在我们的例子里，我们就想控制 loading 和 loading error 在什么时候能用。来看看怎么做。

要创建一个自定义的 style，第一步是先想好你想在 scope 里看到什么。对于 Button 来说，我们只想控制 style 是怎么被扩展的，不做任何限制。所以我们让 loading style scope 直接继承自 style scope。

接下来，用刚才创建的 scope 来创建一个自定义 style，叫 `LoadingStyle`。然后把之前写的那些扩展函数改成扩展这个新的 scope，而不是 style scope。这样一来，这些扩展函数就只能在 `LoadingStyle` 里面用，在普通的 style 里就用不了了。

最后，我们回到 Button 那里，把它改成用这个新的自定义 style。因为自定义的 LoadingStyle 本身不是 style 类型，所以在传给 styleable 属性之前要先转一下，调一下 `.toStyle()` 就行。

现在 loading 和 loading error 就能用来定制 Button 了，但是不能用它们来定制 filter chip——这正是我们想要的效果。

你可能会问：“这么多灵活性，代价是什么？”嗯，挺意外的，style 通常比直接用对应的 modifier 还便宜。主要是 style 让我们更容易遵循 Compose 的性能最佳实践。

来看个最佳情况的例子吧。这段代码是在改一个 Box 的 border 颜色，还设了一些别的属性。我们写的所有基准测试都跟这个差不多——一个用 modifier 实现的组件，和另一个用 style 实现的同样的组件。在这个基准测试里，style 的分配少了大概 70%，渲染下一帧的速度最高快了 2.3 倍。

要理解为什么，我们来仔细看一下 style 是怎么工作的。Style 是一种只影响布局和绘制的 modifier。当布局属性（比如 content padding）变化的时候，只有 layout 和 draw 会跑。当绘制属性（比如 background）变化的时候，只有 draw 阶段会跑。在上面那个基准测试里，渲染下一帧的时候只跑了 draw 阶段。

style 的性能优势主要来自三点：

1. style 是在 composition 阶段创建的，但只有在 composition 之后才会被求值。就像前面说的，这样就把 modifier 的工作挪到了 Compose 更后面的阶段，让 style 变化的时候可以跳过 composition。

2. style 只用一个 modifier。同样的功能下分配次数更少。

3. 在 composition 阶段不会创建任何动画，只有真正需要的时候才创建，这就降低了创建 composable 本身的开销。

那个 border 的基准测试是专门为了体现 style 最擅长的场景设计的。在更贴近真实场景的例子上，我们也看到了改进。在 Material Button 的一个原型实现里，我们换成基于 style 的版本之后，分配减少了大概 30% 到 37%，Button 渲染下一帧的速度也快了 1.6 倍。

好了，交给 Rebecca 来讲讲主题。

> 谢谢 Chuck。到现在我们学了不少 Compose 里新 API 样式方面的内容。接下来看看怎么把这些集成到你的主题里。开头也提过，material 这块儿其实是有个谱系的……

---

翻译中为了口语化，对一些地方做了语序和措辞的调整，像 lambda、style state、modifier、composition 这些 Compose 里的核心概念我直接保留了英文原词，这样更贴近实际开发语境，也方便你对照代码理解。 你的应用可以采用的样式。以及你在主题中采用样式的方式可能会因你的级别而有所不同。那么，你究竟该如何采用样式呢？样式与你的应用集成的方式应该是通过你的主题，方法是公开一个样式对象，该对象包装你的组件的默认样式组件默认样式。这是一个位于你的设计系统可能提供的当前子系统之上的新层。例如，在 JetSnack 中，我们在主题级别定义了颜色、形状和排版。我们现在在主题中引入一个组件默认样式层，这是一组访问子系统的样式，用于访问颜色、形状和排版的标记。然后，我们的按钮组合函数将使用主题中的默认样式，而不是像以前那样直接访问子系统。现在，当按钮被渲染时，它将使用 Megan 之前谈到的优先级层次结构来解析样式。通过获取按钮上的传入样式参数、主题的按钮样式以及树中向上继承的属性，来解析该按钮的计算样式。因此，如果你没有使用 Material Design，你今天就可以在自己的设计系统中试用样式。如果你属于以下两类中的一类：要么完全不使用 Material，要么有一个自定义主题包装了 Material 组件。我们的建议是在你自己的主题组件中使用样式。当 Material 组件公开一个样式参数时，你可以在你的包装组件定义中使用它。让我们看看 JetSnack 的例子。这个应用有自己的自定义主题，并使用了一些 Material 组件。因此，我们已经有了自己的自定义主题，其中子系统（如颜色、排版和形状）都与 Material 不同。因此，为了采用样式，我们添加了新的 JetSnack 样式对象作为主题上的一个属性来公开，该属性公开静态对象。我们还添加了样式作用域扩展函数，以便能够轻松地在样式本身中访问子系统标记。样式可以访问组合本地变量。然后在我们的 Jetpack 样式对象中，我们为我们的组件创建默认值。例如，我们将之前定义的按钮样式移到这个类中。并且我们将硬编码的颜色切换为使用来自每个子系统的主题级标记。例如，此处的背景设置为使用我们颜色自定义设计系统颜色集中定义的颜色列表的线性渐变画笔。这意味着当子系统切换时，样式将自动更改。在这种情况下，我们正在从深色模式切换到浅色模式，颜色会自动适应。对于另一个设计系统组件定义，我们现在访问主题级样式，并通过将传入的样式参数与主题样式组合来解析样式的效果，使我们的按钮可主题化。现在我们能够轻松地使用此按钮，并通过传入额外的样式来定制它，以覆盖特定参数。在这个例子中，我们传入了不同的形状。这与位于主题级别的默认样式组合在一起。你可以看到，由于它使用了底层的组合本地变量，按钮也有正确的浅色和深色模式主题。那么，如果你使用的是 Material 组件呢？Material 正在其 UI 组件中采用样式，这将在未来的版本中可用，从 Material 3 开始。如果你仍在使用 Material 2 组件，我们鼓励你在此期间迁移到 Material 3。使用 Material 时，你可能正在使用整个 Material 设计系统。在这种情况下，你只需在组件提供样式参数时使用它。如果你的设计系统基于 Material 3，但你有一两个全局差异，那么你将能够在主题级别覆盖它们。对于公开样式参数的 Material 组件，你将能够随心所欲地定制这些组件。例如，这个 Material 3 按钮将在其上提供一个样式参数。因此，你将能够使用 Material 组件而无需 fork 实现，而是根据你的需求使用自定义背景、形状、内边距等进行定制。这允许你更改 Material 组件上以前可能无法更改的其他属性。你可以了解更多关于 Material 如何发展以确保你在带来自己的定制的同时受益于 Material 的信息，请查看这个演讲。回到 Megan 那里。>> 所以，我们已经详细讨论了样式 API、如何进行设置以及如何集成到你的主题中，但还有一种方法可以使你的主题适应不同的设备特性。我们引入了另一个名为 media query 的实验性 API。此 API 提供的是一种访问窗口特性的简单方法，这可以解锁构建仅一个主题以跨设备频谱使用。该 API 与样式 API 携手合作，提供易于使用的查询，可以根据设备属性更改样式。让我们看一个快速的例子。因此，随着 Android 能够适应越来越多的设备，你可能想知道如何能够轻松地添加对这些不同适配的支持。例如，如果你连接了鼠标，你的指针位置变量现在会报告精确的指针位置。这意味着你能够点击较小的设备目标。要根据媒体查询更改样式属性，你可以使用以下示例。它仅返回一个布尔值，并且当条件更改时，样式将在组合后失效并被重新解析。在这里，你可以看到这组按钮在插入鼠标的设备上更改了内边距和大小。最右边的按钮 最右边的按钮 让我们再试一次。最底部的按钮整体看起来更小，即使我们使用的是完全相同的组合函数。样式现在会自动调整 好的，我来帮你翻译成中文口语化版本：

---

这部分是基于设备属性的。你可以在这个链接里了解更多最新的媒体查询 API。一定要去看看用 Android Studio 的 AI 智能体来让你的 UI 自适应，或者直接问 Don 和 Jose。现在把时间交回给 Chuck。

>> 我能站到那个讲台后面吗？哦，谢谢。到了这里，你可能正在问自己，什么时候该用 modifier（修饰符），什么时候该用 style（样式）呢？正如我们看到的，这两个系统之间确实有一些重叠。提醒一下，style 并不是要取代 modifier，而是要取代那些和视觉效果相关的参数。

把两者对比一下的话，modifier 是设计成底层能力的，它仍然是用来处理行为、语义、可叠加属性以及复杂布局的方式。而 style 是更高一层的 modifier，是为视觉外观、单独的尺寸以及可主题化的属性设计的。Style 比 modifier 高一层，它是构建在 modifier 之上的。

从逻辑上看，modifier 是叠加式的，而 style 是覆盖式的。对于主题化来说，用 modifier 会比较麻烦，因为它们本来就不是为提升到主题层面而设计的。而 style 在主题中使用是天生就支持的。

从性能方面来看，这当然要分情况，但 style 在设计上跳过了组合（composition）阶段，而 modifier 通常需要走完三个阶段。关于动画方面，modifier 需要单独的动画原语，而 style 是内置动画的。

那什么时候该选 style，什么时候该选 modifier 呢？如果想覆盖现有组件的默认设置、要高性能的交互状态动画，或者要为组件定义整个主题的属性集，那就选 style。如果要定义像 clickable（可点击）这样的行为、或者其他手势，定义独特的一次性布局，或者需要在你的可组合函数上有叠加式的属性，那就选 modifier。现在把时间交回给 Rebecca 来做总结。

>> 那就讲到这儿吧。我们想鼓励大家去试试 Compose 里的 styles，也欢迎你们对 API 提出反馈。提醒一下，这些 API 还是实验性质的，可能会根据大家的反馈而改变。我们已经准备了一整套文档，可以在这个链接里看到。另外，如果你想用新的 style 技能搭配你自己的智能体来帮你迁移到使用 styles——不管是你自己的自定义设计系统，还是 Compose 里的基础用法——你都可以通过下面这个链接来获取这个技能，或者用新的 Android CLI 来下载。非常感谢大家的参与！记得看看链接里的资源，也欢迎告诉我们你对 styles API 的想法。

---

翻译的时候我把一些术语（比如 modifier、style、clickable、composition）保留了英文，因为这些是技术专有名词，在实际技术交流中大家一般都是直接说英文的。如果你想全部翻译成中文，我也可以再调整一遍，告诉我一声就行！
---
