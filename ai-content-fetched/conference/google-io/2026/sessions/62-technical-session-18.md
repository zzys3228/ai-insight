---
title: Build next-generation UIs with the HTML-in-Canvas API
title_zh: 使用 HTML‑in‑Canvas API 构建下一代用户界面
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: 设计
type: 技术演讲
level: Intermediate
speakers: nattestad
video: https://www.youtube.com/watch?v=TUtKGTeFWjQ
---

# 使用 HTML‑in‑Canvas API 构建下一代用户界面

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: 设计 | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: nattestad

了解 HTML‑in‑Canvas API 如何让你直接将 HTML 元素绘制到画布上，同时保持语义信息（如可访问性和交互性）。随后探索如何操作纹理，以创建仍然像交互式网站的动态效果。我们将涵盖该 API 的广泛功能，回顾潜在用例的演示，并了解初始设置流程。

---

## 📝 详细原文

了解 HTML‑in‑Canvas API 如何让你直接将 HTML 元素绘制到画布上，同时保留可访问性和交互性等语义信息。随后探索如何操作纹理，以创建仍具交互式网站感的动态效果。我们将介绍该 API 的广泛功能，展示潜在用例的演示，并帮助你了解初始设置过程。

**原文（English）**: Learn how the HTML-in-Canvas API lets you draw HTML elements directly into a canvas while maintaining semantic information like accessibility and interactivity. then explore how to manipulate textures to create dynamic effects that still feel like interactive websites. We will cover the extensive capabilities of this API, review demonstrations of potential use cases, and understand the initial setup process.

---


---

### 原文

Learn how the HTML-in-Canvas API lets you draw HTML elements directly into a canvas while maintaining semantic information like accessibility and interactivity. then explore how to manipulate textures to create dynamic effects that still feel like interactive websites. We will cover the extensive capabilities of this API, review demonstrations of potential use cases, and understand the initial setup process.

---

## 📝 内容总结

**《使用 HTML‑in‑Canvas API 构建下一代用户界面》核心要点**

一、核心主题概述

本演讲介绍HTML-in-Canvas API，允许将DOM内容绘制到canvas或WebGL/WebGPU纹理，同时保持可交互性和可访问性。

**二、关键发布/技术要点**
- 要点1：layout subtree属性——告诉浏览器canvas内有哪些内容
- 要点2：drawElementImage（2D）——将DOM元素画到canvas指定位置
- 要点3：texElementImage2D（WebGL）——将元素画到纹理
- 要点4：copyElementImageToTexture（WebGPU）——同样的纹理绘制
- 要点5：CSS transform更新——告诉浏览器元素实际位置，保持交互性
- 要点6：Three.js和PlayCanvas支持——简化HTML-in-Canvas使用
- 要点7：浏览器功能保留——翻译、查找、无障碍、暗黑模式等都可用

**三、落地应用**
- 案例1：Figma、Adobe、Miro、JetBrains正在尝试该API
- 案例2：文字滚动demo展示选中和右键保存功能
- 案例3：WebGL UI demo支持实时编辑和深色模式切换
- 案例4：果冻滑块demo展示WebGPU渲染和折射效果

**四、总结**
HTML-in-Canvas是连接DOM和Canvas的最佳方案。开发者可获得底层渲染能力，同时保留浏览器集成功能。Three.js和PlayCanvas等框架已提供简化接口，Origin Trial阶段可注册试用。

---

## 📝 完整文字稿

[音乐]

>>大家好，我叫Thomas，今天我来给大家介绍HTML in Canvas API。这个API可以让你直接把DOM内容画到canvas上，或者画到WebGL和WebGPU的纹理里，同时还能保持UI的可交互性、可访问性，并且能跟浏览器里那些你喜欢的功能联动。你在这里看到的这些演示，用的都是你熟悉并且应该也很喜欢的HTML，只不过用法可能超出了你以往的想象。我们稍后会再回到这些演示，但先让我再讲讲这个API本身。

这次分享会先讲讲HTML in Canvas的基础知识，以及它们各自的优势，还有结合在一起后更厉害的地方。然后我会给你看几行简单的代码，让你知道怎么今天就开始在自己的项目里用上这个API。最后我还会再秀一下那些酷炫的演示，告诉你怎么直接用这个API去做这些效果。

要真正理解这个API，我们得先仔细看看DOM和Canvas，搞清楚它们各自擅长什么。我会把DOM和HTML这两个词说得比较随意一些，但一般来说，HTML是你写的静态源代码，DOM是浏览器从这份代码构建出来的、活的、可以交互的模型。你后面会看到，这个API既会改变页面上的静态HTML，也会更新活的DOM结构，好让交互功能跑起来。

DOM是网页UI的基石，浏览器给它接入了非常多强大的能力。它自带很棒的UI和文字排版方案，会基于语义化的内容去生成丰富的、可交互的界面。它让用户可以在网页之间做那些我们习以为常的常见操作，比如选中文字去复制，或者右键图片去保存。还有一大堆浏览器集成功能，比如无障碍、翻译、页内查找、阅读模式、扩展、暗黑模式、浏览器缩放、自动填充——这些对用户怎么用网页来说都是至关重要的。

而Canvas，加上WebGL和WebGPU，给开发者提供了底层访问能力，可以做出非常高级的2D和3D图形。Canvas的强大之处在于它是个底层系统，可以用各种渲染栈，比如WebGPU，或者渲染框架，来驱动那一整块像素。游戏和很多像Google Docs这种UI很复杂的网页应用，都需要这种高性能的底层访问能力。不过，因为Canvas本质上就是一块像素加一些基本功能，你得自己处理很多逻辑，比如响应式的文字排版，或者借助框架来做，但这又会增加你打包出来的体积。另外，我刚才念叨的那些DOM的功能，一旦UI被画到Canvas里，就全都不灵了。

直到现在，这个情况改变了。HTML in canvas API就是一座桥梁，它把两边的优点都给你了——你能把DOM元素画到canvas或者WebGPU纹理里。最棒的是，你只要把HTML放到canvas标签里面，再更新一下变换，内容的可交互性就能保留下来，而且我刚才提到的那些浏览器功能也照样能用。

这个API现在Chrome里就能用，我们也正在和其他浏览器一起推动它成为开放标准，希望未来能在各个浏览器里都上线。

用这个API分三步：先设置好你的canvas，把内容画到canvas或者纹理里，最后更新元素的变换，告诉浏览器它实际在哪个位置。我来用代码带你过一下每一步。

第一步，在你想要画进去的那个canvas标签上设置layout subtree这个属性。这样浏览器就会知道canvas里有哪些内容，并且把它纳入命中测试，开放给无障碍系统和浏览器功能用。接下来，你就可以直接在canvas标签里写HTML代码了，比如加个form元素或者input，你可以直接写HTML，也可以用JavaScript动态加进去。

把HTML放在canvas标签里是渲染的前提条件，但光这样还不够。要真正渲染元素，还得通过一个明确的API调用才行，比如用2D context、WebGL或者WebGPU，我们接下来就看看这些。

对于2D context来说，调用的方法是drawElementImage，它接收DOM元素和一个x、y坐标，告诉浏览器要把这个元素画到canvas的什么位置。在这个例子里，我们是在onPaint事件里做的这件事——只要元素被重绘，这个事件就会触发，包括用户或者像"页内查找"这种功能高亮文字的时候也会触发。这是最稳妥的方式，能保证UI始终是最新的，不过你也可以根据你的应用需要，在别的地方调用。

这个API方法会返回一个变换矩阵，你可以把它赋给DOM元素的CSS style transform属性，告诉浏览器这个元素被画在了哪里。这样交互性和浏览器的那些功能就能自动跑起来，不用再做额外的集成。每当你重绘元素的时候，一定要记得更新这个变换，这点非常重要。如果你不画这个元素了，那也必须把它从canvas元素里拿掉，不然它会一直被告诉给浏览器和无障碍系统，让他们以为这个东西还在页面上。

还有一个重要的步骤，就是要根据正确的缩放比例设置canvas的宽度和高度，这样渲染出来才不会糊。要做这件事，你只需要加这几行代码，设置一个ResizeObserver就行了。

对于WebGL来说，你同样需要设置layout subtree这个属性，把你想渲染的HTML加到canvas里面。要把元素画到纹理里的话，你可以用texElementImage2D这个方法，它跟WebGL里那个texImage2D方法是对应的，参数也一样，只不过传进去的不是图片源，而是一个DOM元素的引用。

用WebGPU来渲染的话，canvas的设置方式也是一样的。然后我们用copyElementImageToTexture这个方法，它跟WebGPU里你可能已经很熟悉的copyExternalImageToTexture方法也是类似的。

所以，这两个函数就是把DOM元素画上去…… 变成一张贴图，但就像在 2D 例子里一样，关键还是要更新元素的 CSS transform，这样浏览器才知道它在屏幕上的位置。在 3D 空间里做这个要复杂一点，我这里就不展示完整代码了，但你可以在这段代码示例里看到。大概来说，我们先做一个视口变换，把 3D 坐标空间映射到 CSS 坐标空间，然后调用 canvas 提供的一个叫 getElementTransform 的方法，拿到一个 transform，再像 2D 那样用同样的方式应用上去就行。听起来有点绕，也确实有点难懂，但好在有非常棒的开源框架可以帮我们扛这些脏活累活，你只需要专心用好这个特性就行。很高兴告诉大家，Three.js 已经实验性地支持 HTML 和 canvas 了，感兴趣可以点这个链接深入了解。用 Three.js 的 API 非常简单：建一个材质，然后用新的 THREE.HTMLTexture 方法，把要渲染的 DOM 元素传进去，把它设成材质的 map。接着随便拿一个几何体，比如一个盒子，把材质套上去，搞定。还有一个也已经支持了的框架是 PlayCanvas，它可以帮你做出非常酷炫的 HTML5 游戏和可视化。配置起来也很简单：先建好你的 canvas，创建一个 layout subtree，再创建一个 HTML 元素，然后建一个 PlayCanvas 贴图。我们再加一个事件监听，把贴图的 source 设成想要渲染的那个 HTML 元素。最后再加一个事件监听，在浏览器重绘元素的时候把贴图重新上传一下，这样它就能一直保持最新。拿到 HTML 贴图之后，就可以把它当作物体的漫反射贴图，套到一个立方体上，又搞定一次。值得一提的是，这个示例还会自动检测 API 是否可用，如果不行就回退用一个 polyfill 来渲染。虽然这不算真正用上了浏览器原生的特性，但给自己的项目留个兜底方案始终是一个好习惯。完整代码示例可以看这个链接。想看更复杂的例子的话，可以看这个鞋子的 demo：那个样式选择器会跟着鼠标走，配合简单的 HTML UI，做出了非常惊艳的 3D 效果。当然了，现在像 anti-gravity 之类的强大 AI 编程工具也能帮你写很多代码。不过因为这是一个全新的 API，很多编程工具还不认识它，除非你给它一些上下文。你可以丢给它 explainer 链接，并建议它去参考官方示例；更好的是利用这个 modern web guidance，它能帮 AI 工具把用这个 API 需要的知识都搞清楚。好，既然 API 的基本用法我们已经了解了，那现在看几个例子，来展示一下这个 API 在实际中的真正威力。所有例子都可以在这个页面里找到。第一个例子里有一段文字，既能左右滚，也能上下滚。我们打开 DevTools 看一眼，可以确认这段文字确实是放在 canvas 元素里面的。我们依然可以拖动这张图，也可以右键保存。甚至连里面那个小 SVG 也正常工作。可访问性信息现在也都暴露出来了，尽管这些元素其实是放在 canvas 里的。打开无障碍树视图，你可以看到所有这些内容，屏幕阅读器之类的工具都能读得到。再看 Lighthouse 这边，即使所有内容都是放在 canvas 里的，可访问性评分照样能拿到 100 分。再来一个稍微更贴近实际一点点的例子，这是一个简单的 WebGL 演示，你可以看到这个 UI 是被画到一张贴图里的。但我其实照样可以选中文本、拖动滑块，甚至自己输入文字。因为它整个都通过 DevTools 接通了，我甚至可以右键选“检查”，直接看到这段 UI。我还可以现场改一下，比如“这其实是个非常简单的控件”，你会看到 UI 会自动跟着更新，同时依然保持完全可交互，浏览器所有其他功能也都正常用。最后，如果你的 CSS 支持深色模式的话，你完全可以进到浏览器设置里把外观切换到深色模式，这个 UI 就会自动跟着变。如果你想要那种更像真实广告牌的效果，你也可以做出这种东西来。这个也挺有意思的：你看到的这支小铅笔，其实是一个带动画的 SVG，它不仅在 canvas 里作为动画 SVG 在播放，而且是直接渲染到 WebGL 贴图里的。所以现在你不用写任何额外代码就能直接放这种带动画的 SVG，文字和交互当然也都完全正常。想做那种炫酷的、套在 3D 模型上的视觉浮层？也可以。可以看到你照样能用滑块，而且效果还会透过 3D 模型产生折射。同样地，如果我想要“页面查找”这种功能，我可以直接搜一个词，比如 specimen，可以看到搜索结果也是透过 3D 模型相应地折射出来的。你还可以做出这种很酷的文字扭曲效果，鼠标拖动的时候跟着变形，顺便还能顺便了解一下这个把 HTML 直接渲染到 WebGL 贴图里的实验性 API。这个例子里的 UI 本身也是普通 UI，能正常用。如果你想的话，还可以选中一段文字，你会看到效果就作用在被选中的那一段上。页面查找也照样能用，因为这些全都是通过你熟悉的那套 HTML 接通的。再来一个稍微再实用一点的例子，可能更接近大家真正会想做的场景。可以看到一个 3D 翻页书的效果…… 好的，我用比较口语化的方式翻译一下：

所有的内容都是用 WebGL 渲染出来的。而且呢，这些都是通过 canvas API 里的 HTML 排版来实现的文字。因为整个页面都是用 DOM 和 HTML 来排版的，所以我可以直接进去改个字体——比如我想用更古典一点的字体来写《福尔摩斯探案集》，它就直接在那边更新了。然后我说："好吧，这个字体可能不太好读，我还是想要那种方方正正、看起来有点搞笑的字体。"我就可以在下面选另一种文字样式，砰的一下，整个字体就全换掉了，你想用啥字体都行。那我们还是换回一个比较正常的字体，这样看起来更舒服一点。

接下来我想聊聊这个 API 里我个人最喜欢的部分之一。因为我住在一个语言不太通的国家，所以对我而言，浏览器自带的翻译功能真的超级重要。我可以直接在这里用翻译功能，把内容翻译成德语来读《福尔摩斯探案集》，然后页面上所有的文字就自动更新了。这意味着我可以一边展示这些超酷的 3D 场景，一边让用户选择他们想用的任何语言来体验。

既然是 Google I/O 大会，那肯定得提一下 AI，对吧？这其实也是这个 API 很厉害的地方。因为这里所有内容都是以文字的形式暴露在 HTML 树里的，所以像爬虫或者 AI 智能体这些东西，都能直接把它当文字来处理。假设我想让我的 AI 助手把不同页面里所有的文字都提取出来，而不是一页一页翻着看，或者我想让它把这些文字念给我听。我就可以用一个 AI 智能体，甚至就用一个简单的扩展程序，比如文字提取工具，直接读取这些文字就行了。因为都是纯文字，所以我的手机助手就能把这些文字复制出来，然后念给我听。

最后一个例子是 WebGPU 的演示，大家可能见过这个好玩儿的果冻滑块，但现在它真的能正确地产生折射效果了，就像这个小小的部分一样。当然啦，因为它是通过一个滑动条来控制的，所以我可以直接打开开发者工具，把步长从 1 改成 5，砰的一下，它就自动更新了，会四舍五入到最近的 5，既好玩又流畅，而且还能跟浏览器的各种功能完美配合。

虽然这个 API 还在早期阶段，但已经有一些超棒的应用开始用它了，比如 Figma、Adobe、Miro 还有 JetBrains，他们都在尝试用这个 API 来给自己的网页应用开发新功能。到 2026 年 5 月，这个 API 已经进入了 origin trial 阶段，也就是说你可以试着用它部署到正式版的 Chrome 上跑跑看，但你得在这个链接里注册你的网站才能启用这个 API。

希望这些能让你对这个 API 有一个整体的概念，知道怎么用、能做出什么。现在就差你们去创造出一些超酷的东西啦，记得分享出来哦！我们有一个超棒的 HTML and Canvas 的 Readme 文件，希望能把大家做的一些厉害作品都收集起来，里面还有一个提交链接，你可以把自己的作品或者发现的好东西分享出来。

那我就说到这里啦，谢谢大家今天听我讲，我已经迫不及待想看到你们用这个 API 玩出什么花样了。谢谢！

> [音乐响起]
---
