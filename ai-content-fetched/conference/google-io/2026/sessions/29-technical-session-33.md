---
title: Build new features using built-in AI in Chrome
title_zh: 在 Chrome 中使用内置 AI 构建新功能
category: conference/google-io/2026/sessions
date: 2026-05-21
time:  PT
track: Web
type: 技术演讲
level: Intermediate
speakers: tsteiner
video: https://www.youtube.com/watch?v=ddBxvuH35tI
---
# 在 Chrome 中使用内置 AI 构建新功能

## 📋 摘要

**📅 日期**: 2026-05-21 | **🕐 时间**:  PT | **📂 分类**: Web | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: tsteiner

踏上由 Chrome 内置 AI API 驱动的旅行博客应用的旅程。跟随 Gemini Nano 将非结构化写作转化为自动化工作流。学习部署 Summarizer、Writer、Rewriter、Language Detector 和 Translator——全部在本地运行，实现最大隐私和零服务器成本。然后深入了解 Prompt API，使用 JSON schema 进行结构化数据标记和多模态 alt‑text 生成，以将这些模式迁移到自己的 Web 应用中。

---
## 📝 详细原文

踏上由 Chrome 内置 AI API 驱动的旅行博客应用之旅。跟随 Gemini Nano 将非结构化写作转化为自动化工作流。学习部署 Summarizer、Writer、Rewriter、Language Detector 和 Translator——全部在本地运行，最大限度保护隐私且无需服务器成本。然后深入了解 Prompt API，使用 JSON schema 进行结构化数据标记以及多模态 alt 文本生成，进而将这些模式迁移到你自己的 Web 应用中。

**原文（English）**: Take a journey through a travel blogging app powered by Chrome’s built-in AI APIs. Follow along as Gemini Nano transforms unstructured writing into automated workflows. Learn to deploy the Summarizer, Writer, Rewriter, Language Detector, and Translator—all running locally for maximum privacy and zero server costs. Then dive into the Prompt API for structured data tagging with JSON schemas and multimodal alt-text generation to extrapolate these patterns into your own web apps.

---
## 📝 内容总结

**会议演讲总结：使用 Chrome 内置 AI 构建新功能**

演讲者 Thomas Steiner（Chrome 团队开发者关系工程师）介绍了如何利用 Chrome 内置 AI API 开发创新功能。他通过虚构案例 "Trail Blazers" 博客（由旅游博主 Maya 和 Ashok 运营）展开说明。

**核心要点：**

1. **Chrome 内置 AI 的优势**：模型运行于设备端，敏感数据不离开浏览器，可离线使用，借助硬件加速性能优异，某些场景比云端更快。

2. **博客痛点与解决方案**：该博客使用静态站点生成器（性能评分 95），但缺乏可视化编辑器。团队借助 Chrome 内置 AI 开发了"所见即所得"编辑器，集成暗黑模式，支持拖拽图片。

3. **重点 API 介绍**：
   - **Summarizer API**（Chrome 138+）：用于自动生成文章标题和 SEO 元描述，支持流式输出。
   - **Prompt API（结构化输出）**：通过 JSON schema 约束响应格式，可自动为博客文章推荐标签并归类（如 Travelettes 案例），防止模型生成未定义内容。

4. **实际应用**：Drupal 团队已将 Summarizer API 集成到 CKEditor，Travelettes 则用 Prompt API 实现智能标签。

---

## 📝 完整文字稿

下午好，Shoreline。我叫Thomas Steiner。我本来是德国人，但现在住在西班牙。我大老远从巴塞罗那飞过来，是为了跟大家聊聊怎么用Chrome内置的AI来开发新功能。作为Chrome团队的开发者关系工程师，我经常出差。虽然我确实挺享受这个过程的，但说实话出差不是我的本职工作。不过我想先给大家介绍一个人——他的工作就是环游世界。接下来的故事是虚构的。但它完全可能成真。不过，我提到的所有代码示例和API都是真实存在的，今天的Chrome里就能用。听完之后，你们就能直接上手，用这些API开发你们想要的超棒应用了。在故事每个虚构的章节里，我都会提到一些真实合作伙伴，他们真的用我们的API做了实际开发。演讲最后，我还有一份非常实在的惊喜送给大家带回家。

我先讲Summarize API（摘要API）。接下来，我会讲Prompt API，包括结构化输出和多模态输入。然后是Writer API（写作API）、Rewriter API（改写API）和Translator API（翻译API）。好了，咱们正式开始。

认识一下Maya——来自悉尼的旅游博主，最近刚去中国旅行，被中国的长城震撼到了。她的好搭档是来自海得拉巴的Ashok，同样是旅游博主，上次旅行去了里约。他们俩一起经营着一个非常成功的旅游博客，名字叫"Trail Blazers"（开路先锋）。他们在博客上记录旅行、分享攻略，还建立了一个社群。作为经常出门旅行的人，他们深知网络数据不是随时都有的。漫游费贵得吓人，酒店Wi-Fi又特别不稳定，有时候断网甚至是自己主动选择的。正因为如此，他们把博客做成了静态站点。他们用一个叫Build Awesome的静态站点生成器，也就是以前的11ty。Build Awesome能确保他们把优秀的性能直接交付给用户，不会塞进多余的冗余代码或者臃肿的JavaScript依赖。

这倒不是说Trail Blazers博客完全不用JavaScript。他们也用JavaScript，不过是非常基础的那种。比如他们的分享按钮就用了JS，但Build Awesome会逼着他们把内容放在第一位。一切都很值得。Trail Blazers博客的Lighthouse性能评分达到了95分，用户也都非常喜欢，不管是在市中心5G网络下访问，还是在某个荒郊野岭青年旅舍里用巨烂的Wi-Fi连着，体验都还不错。

他们唯一不喜欢Build Awesome的地方就是没有可视化编辑器。每次想写新博客或者改旧的，都得打开IDE去编辑Markdown代码，完全没有即时的视觉反馈。而且要加图片这种多媒体内容，麻烦得要死。

奇迹就这样发生了。除了旅行，Maya和Ashutosh还有个共同的爱好——Web开发。去年他们去Google I/O玩的时候，遇见了Julia。Julia是Trail Blazers博客的长期客座博主之一。他们在活动上玩得特别开心。当他们听说Chrome内置AI的时候，对视了一眼，突然灵光一现——这些API正是他们一直苦寻而不得的那块拼图。

简单提醒一下，Chrome内置AI的优势就在手边。AI模型跑在设备端，敏感数据根本不用离开用户的浏览器，隐私保护直接拉满。因为不涉及服务器，模型下载下来后完全可以在离线状态下运行。而且因为有硬件加速，性能永远都很给力。某些情况下，甚至比云端还快。想了解完整背景的，可以看看我去年I/O的演讲，里面讲得非常详细。

回到Trail Blazers博客。短短几周内，三个人合作开发了他们称之为"Build Awesome——那个缺失的编辑器"的项目。Julia是主要开发者，Anshul和Maya是首批用户。于是，Julia打造了一个完全切合他们需求的博客文章编辑器。

首先，它几乎是个所见即所得的编辑器。你用Markdown写文章，实时预览会马上让你看到博客上的渲染效果。你不用记Markdown的图片语法，只要把图片拖到想要的地方，或者在光标位置粘贴图片，编辑器会自动处理正确的标记。当然，它还有超赞的暗黑模式，这样他们不管在哪儿——哪怕是合住的宿舍里——都能写新博客，还不会晃瞎自己或者吵醒整间宿舍。

好了，咱们来聊第一个内置AI API，以及它在Trail Blazers博客上怎么用的——Summarizer API（摘要API）。

Julia、Ashok和Maya对亲手打磨的博客特别自豪。但就算是他们，偶尔也会卡文。这正是他们接入Chrome 138版本发布的内置AI API的原因——Summarizer API。在编辑器里，他们用它的方式有两种：一是给博文起标题，二是让写元描述这种苦差事变得轻松一点。

实现这个功能的实际代码稍微复杂一点，但本质上逻辑是这样的：先拿到博文文本和标题的引用。因为AI马上要返回一个新的标题，所以先把原来的删掉。然后，创建一个Summarizer。假设是英文博客，把期望的输入语言设成只支持英文。给模型提供英文上下文——就像我刚才说的，把期望的上下文语言设成英文。我们希望标题用英文生成，所以把输出语言也设成英文。

（注：原音频在最后一句话中间被截断了，所以翻译到此为止。） 我们相应地设置语言。摘要类型应该是标题。我们的偏好是速度，所以内部会使用一个较小的 AI 模型。最后，我们给模型提供一些上下文，明确告诉它要生成吸引点击的标题，而不是标题党。现在我们只需要调用摘要器的流式摘要方法，把博客文章文本传进去，然后遍历返回的可读流中的各个数据块，把它们追加到标题后面。元描述的生成过程几乎一样。唯一的区别是类型，现在设置为 teaser（引子），还有一个共享的上下文，这次是提示模型写出对 SEO 友好的文本。摘要器 API 在桌面版 Chrome 和 Edge 中可用，版本是 138。作为真实案例，Drupal AI 团队的新版 CKEditor 集成了摘要器 API，让编辑可以完全掌控 AI 生成的内容，比如 SEO 标签和描述的生成。

接下来，我给大家展示一下 Travelettes 旅游博客是如何使用带结构化输出的 Prompt API 来生成标签的。根据博客文章的文本，AI 模型可以自动推荐标签，把相似的文章归类到一起。比如，关于城市的所有文章，或者关于巴塞罗那的所有文章。你也可以选择把标签限制在一个预定义的现有标签列表里。它是怎么实现的呢？这个功能内部是由带结构化输出的 Prompt API 驱动的，所以模型返回的响应格式是可预测的。为此，Prompt API 使用了 JSON schema。在这种情况下，它把模型的输出限制在一组预定义的标签内，以 JSON 对象的形式返回，键是 tags，值是一个标签数组。你可以在右下角看到一个响应示例：这是一个 JSON 对象，tags 字段的值是 adventure、Australia 和 beach。把响应限制在枚举列表内，可以防止模型自己造出新标签。我们也可以放心，响应一定会是符合要求格式的 JSON 对象。

现在看实际实现。我们先把 JSON schema 存到一个叫 responseConstraint 的变量里。接着获取要打标签的博客文章正文。然后用 AI 模型创建一个会话，调用 LanguageModel.create()。我们传入期望的输入和输出，两边都是一个只含一项的数组，项是一个对象，type 为 text，languages 是一个数组，这里只有英语。最后调用会话的 prompt 方法，给它一段文本提示，让它为这篇博客生成标签。我们把 JSON schema 作为 responseConstraint 选项传给模型，这样它返回的结果就会严格符合这个 JSON 对象的形状。所以我们还得用 JSON.parse 解析一下。现在，我们就可以把标签显示在编辑器里了。当然，用户可以自行增删不合适的标签。Prompt API 早在 Chrome 128 就已经面向桌面版 Chrome 扩展开放了，常规网页应用则是在桌面版 Chrome 148 上线。在线网站 Cafe24 已经在生产环境中使用了类似的标签推荐系统。编辑创建产品页面时，可以从 AI 推荐的标签中选择。他们产品生成组的组长 Jerry Young Lee 分享了内置 AI 给他们带来的质量提升。他对我们说："通过一次设备端的调用，把图片和文字一起处理，我们能把'蓝色连衣裙'这样简单的标签，变成'夏日约会造型、蓝色中长连衣裙'这样对 SEO 至关重要的语境。对我们来说，多模态不仅仅是一个附加功能，它是质量提升的关键所在。"

你刚刚看到的是带结构化输出的 Prompt API。现在，到了给大家演示带多模态输入的 Prompt API 的时候了。Markdown 语法是出了名的难记。我连普通的链接语法都记不住，更别说图片语法了。而且，虽然 Markdown 图片语法支持 alt 文本，但不支持图片标题（caption）。这就是 Julia 和她的 Trailblazers 团队决定改进的地方。你可以只通过文件选择对话框添加图片，甚至可以直接在当前光标位置粘贴图片。这两种情况下，图片都会被标记成一段规范的 HTML figure 元素，带有 AI 建议的 alt 文本和图片标题，如果不合适都可以轻松修改。它是怎么工作的呢？和前面标签一样，秘诀还是 JSON schema。这次更简单一点，我们只要求返回一个包含 alt 和 caption 属性的 JSON 对象。这样模型就会返回类似右下角示例的结果。

和之前一样，我们先把 JSON schema 存到一个变量里。接着用大语言模型创建会话，但这次需要多传一个期望的输入类型：image。系统提示告诉模型扮演 alt 文本和图片标题的撰写者。最后创建会话。现在我们就可以跟会话交互了。提示内容稍微复杂一点，因为是多模态的，但第一部分还是普通的文本提示。第二部分就是实际的图片。和之前一样，我们把 responseConstraint，也就是 JSON schema，作为参数传进去。这段代码会返回一个 JSON 对象，我们需要在编辑器中使用前用 JSON.parse 解析它，然后放进 figure 标签里。Drupal CMS 已经按照你刚才在代码示例中看到的模式，实现了图片的 alt 文本生成。

从 Prompt API 的应用场景，我们再来看一下使用 Writer API 的写作辅助场景。毕竟这是一个写作博客。Julia 为 Trailblazers 团队打造的编辑器是全响应式的，所以团队在外出时也能用。Julia 基于 Writer API 开发的一个很酷的功能是"帮我写"（help me write）。通常情况下，Ashock 或 Maya 会在手机上随手记下一些要点来回顾一天的工作，以免忘记发生了什么。然后"帮我写"功能会把这些要点扩展成…… 好的，我来把它翻译成自然流畅的中文口语版本：
---
