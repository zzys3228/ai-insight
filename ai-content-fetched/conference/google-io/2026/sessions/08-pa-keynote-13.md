---
title: What’s new in Firebase
title_zh: Firebase 有什么新功能
category: conference/google-io/2026/sessions
date: 2026-05-19
time: 16:30 - 17:15 PT
track: 云
type: 技术演讲
level: Intermediate
speakers: arthurthompson, sebag
video: https://www.youtube.com/watch?v=16jTqLC66PU
source: io.google.com
translated: true
fetched_at: 2026-06-24T10:00:00
---
# Firebase 有什么新功能

## 📋 演讲摘要

**📅 日期**: 2026-05-19 | **🕐 时间**: 16:30 - 17:15 PT | **📂 分类**: 云 | **🎯 类型**: 技术演讲 | **📊 等级**: Intermediate

**👤 演讲者**: arthurthompson, sebag

Firebase正演变为面向智能体原生的平台，介绍Data Connect升级为SQL Connect的新功能（自定义解析器、离线缓存、完整SQL支持、实时同步），以及Firebase AI Logic的更新。

---

## 📝 内容总结

## 会议演讲总结：Firebase 有什么新功能

**核心要点：**

1. **Data Connect 升级为 SQL Connect**：保留原有强类型 SDK、无服务器安全访问等特性，并新增四大能力——自定义解析器、离线缓存、完整 SQL 表达支持（含 PostGIS 等扩展）、实时同步功能。

2. **实时功能演示**：通过 `subscribe` 方法订阅查询，服务器端缓存查询并在数据更新时自动推送前端刷新，无需手动执行查询，实现关系型数据的实时 App 功能。

3. **Refresh 指令**：可在 schema 中声明，每次数据变更时自动刷新查询结果，简化实时数据流处理。

4. **多数据源整合（自定义解析器）**：通过 Cloud Functions 桥接 BigQuery 等外部服务，在 SQL 查询中直接调用云函数返回预计算指标，实现 SQL 与数据仓库的无缝结合。

5. **生态集成**：可调用任意 Google Cloud 或第三方 API，极大扩展 Firebase SQL 方案的应用场景。

**总结**：Firebase SQL Connect 让开发者用熟悉的 SQL 即可构建具备实时性、离线能力和复杂数据集成（如 PostGIS、BigQuery）的现代应用，显著降低全栈开发门槛。

**核心更新：Data Connect升级为SQL Connect、实时同步功能、Firebase AI Logic更新、App Functions支持**

---

*原文请访问 [Google I/O](https://www.youtube.com/watch?v=16jTqLC66PU)*

好的，我来把这段话翻译成口语化的中文：

[音乐] >> 今天我们要给大家展示一下，怎么用Firebase快速搞定你的应用开发。哦天呐，我太激动了。我好兴奋啊。我也是。咱们开始吧。你们都兴奋吗？必须的！ >> [欢呼声] [掌声] >> 在2026年的IO大会上，我们的目标就是帮你更轻松、更快速、更灵活地构建和扩展应用。不管你是在做下一个要爆火的手机App还是网站，也不管写代码的是AI智能体还是人类程序员，我们都想确保Firebase能给你提供客户端开发所需的所有工具和服务，而且能顺滑地接入Google Cloud的各种强大能力。今年，我们很兴奋地继续把那些超能扩展的服务，比如Firestore、Cloud SQL还有Agent Platform，变得更容易集成到你的应用里。还有像Firebase手机号验证这种服务，也更安全了。用过Firebase NoSQL方案的举手。好的好的。用过Firebase SQL方案的举手。好的。知道Firebase还有SQL方案的举手。Arthur，得了吧你。我是说，我自己有时候都忘了我们还有个SQL方案。就跟洗牛仔裤的时候突然发现里面塞了张20块钱一样。而听完今天这场，你的感觉会是：哎哟我牛仔裤里塞的是一整个ATM机。 >> 对。一年前，我们正式发布了Firebase Data Connect，也就是基于Cloud SQL打造的Firebase SQL方案。今年，我们把Data Connect升级成了Firebase SQL Connect。Firebase SQL Connect保留了你们喜欢Data Connect的所有功能，比如对Cloud SQL的无服务器安全访问，还有自动生成的强类型SDK，另外还多了几样好东西要跟大家分享。第一样是自定义解析器（custom resolvers）。有了它，你可以在Cloud SQL的基础上，扩展SQL Connect能用的数据源。这样一来，你能在查询和变更操作里直接用上这些数据源的数据。离线功能。离线缓存让你的应用在没网或者网很差的情况下依然能流畅响应。支持原生SQL。现在你可以用SQL的全部表达能力来写查询和变更操作，而且能用上所有可能的扩展。最后但同样重要的是——实时功能！哇哦！来吧。有了实时同步，你可以把关系型数据变成活的App功能。要不咱们直接来看看效果？走，去看笔记本。好。这里我有一个我们开发好的应用。你可以把它想象成表情包交易所，就像股市一样，你可以买卖表情包。表情包，不是ETF哈。ETF那是2020年的事了。逻辑差不多对吧？我买入表情包，价格就涨。卖出表情包，价格就跌。我这里开了两个应用实例。左边是我的个人账号。右边是我的工作账号，我用两个不同的用户登录了。所以，第一步，我来操作一下，比如我要买一个树的emoji，对吧。我买了一个树的emoji。啥也没发生对吧。但是当我刷新页面，树的价格涨了，你看，有人买了树，价格就上去了。右边啥也没变。我得刷新页面才能看到价格涨了。咱们用一点Firebase的魔法加上SQL Connect实时功能来搞定这个问题。现在这个仪表盘的运作方式是，它订阅了一个SQL Connect的查询，叫get dashboard data。我用的是execute query执行查询的方法，大家如果用过一段时间SQL Connect或者Data Connect的话，应该都用过这个。我们做的改动之一呢，我把这行注释掉。我们做的第三个改动就是新增了一个叫subscribe（订阅）的方法。现在呢，你不用执行查询了，而是可以直接订阅一个查询。这样做的效果是，这个查询会在服务器端缓存起来，每次这个查询有更新——比如有人手动执行了一次——前端就会收到一个流、一个信号，然后自动刷新页面。代码我都保存好了。我两边都刷新一下，确保加载到最新的JavaScript代码。好，现在我再买一棵树对吧。啥也没发生。但是我刷新页面，能看到价格变了。很神奇对吧。它变化的原因是因为我手动刷新了一下。挺酷的对吧？嗯。我们可以让它更好。好很多。今年我们在Data Connect和SQL Connect里还推出了一个新东西，叫refresh指令（refresh directive）。现在我可以告诉这个get dashboard data查询，每次有数据变更的时候自动刷新。比如每次有人买股票或者卖股票的时候。我来改一下这个，然后部署到生产环境。它现在做的事情就是扫描我的数据库，编译查询，检查schema结构是不是对的，查询写的是不是对的，还要看有没有schema变动需要自动推到SQL数据库上。这个得多花几秒钟。等一下，再等一秒。快好了。好了。我回到我的应用，两边都刷新一下。现在我买一杯咖啡。再买一杯。好了！哇哦！很神奇对吧！ >> [掌声] >> 非常非常酷。还有一个功能我想给大家演示一下，就像我刚才说的，现在你可以直接写SQL查询了，可以用SQL的全部表达能力。我们做了一个能显示地理位置的页面。基本上就是基于坐标，在地图上显示大家都在哪里买表情包。想象一下，你要是用传统的手写GraphQL，或者得用各种扩展才能实现这个功能。但现在你直接用SQL就能写。比如用GIS，PostGIS那个SQL extension。就像你看到的，我可以传给extension。我用的是PostGIS的extension。我只是传入了经度和纬度，然后基于这个进行搜索。所以，想象一下现在的这个能力——你可以写SQL，还能用PostGIS生态系统里的任何extension。

最后我想给你看的是这个功能。比如说，对于某个emoji，我喜欢这个——看看，我喜欢火焰emoji。我有点偏心。我想能够展示一些更复杂的指标，对吧？我有emoji的实时价格从我的SQL数据库里进来，但我想展示预先计算好的、你知道的、已经预计算好的指标。有没有哪个服务比SQL更适合做预计算指标？BigQuery怎么样？没错。那如果我能通过Data Connect把SQL和BigQuery的数据结合起来呢？现在你可以通过自定义resolver来做到这一点。自定义resolver会给你一个可以运行的方法，就是Firebase init data init data connect resolver。我们得把它改名叫SQL connect resolver。它会帮你生成一些东西。第一件它会生成的是一个基础schema。在这个基础schema里，你要定义自定义resolver的输入和输出数据是什么样的。第二件它会帮你生成的是在cloud function里打一个桩。所以比如说，这里你可以看到通过一个cloud function，我直接通过BigQuery Cloud SDK调用BigQuery。

所以现在想象一下这个能力，对吧？因为我是在cloud function里执行这个，用的是SDK，但你可以调用任何你想要的API，任何你想要的云服务，任何你想要的API，不管是Google Cloud的一部分还是第三方的。

我在这里做的最后一件事就是在query里用它。所以我有这个get emoji analytics，它基本上是调用我的自定义服务器，把emoji作为参数传进去，在这个query里面我有从SQL来的数据，还有现在从我的自定义服务器来的数据——它在调用BigQuery。很强大对吧？

>> [掌声]

>> 好的，我们可以回到幻灯片了。我准备自己买几个emoji了。这个演讲我之前看过，我觉得还有更多的数据库更新。还有几个我想跟你们分享的。

有时候SQL是构建你应用的最好方案，有时候NoSQL能给你需要的一切，而且才是正确的方案，对吧？为此我们持续演进Firestore，特别是在它的企业版里。我们最近正式发布了query pipelines。有了query pipelines，我们完全重新构想了我们的query agent引擎，帮助你更高效地构建应用。今天，还有几件事我想跟你们分享。

第一个是数据操作语言，也就是DML。DML能压缩你对pipeline写入变更所需要的步骤数。比如，如果一个用户离开了你的应用，你可以用一个pipeline query就删掉所有该用户生成的内容。

第二个是子查询。子查询让你能够在一个query里组合多个文档和过滤器。能解锁复杂的查询场景，比如这个例子，从一个collection里抓取某本书的所有评论，然后把数据upsert到books collection里。子查询既能用于查询数据，也能用于修改和插入数据。

地理搜索。有了地理搜索，现在在Firestore里，你可以用longitude、latitude和distance这样的地理字段来进行排序和搜索。

最后但同样重要的，它来了，朋友们。来，给点掌声。你们一直在等这个。

>> [掌声]

>> 我很激动地宣布Firestore Enterprise现在原生支持全文搜索了。全文搜索让你可以搜索你的collections和documents中的内容，比如精确的词、短语，或者语义匹配。现在你不再需要extension或者第三方服务了。非常非常激动。太多数据库好东西了。这些功能会加速人类和agent开发的方式。

Firebase也帮你把AI体验带给你的用户。Firebase AI logic帮你无需任何服务端设置就能把生成式AI的力量带给你的用户。如果你曾经想过要给你现有的app加个AI功能，举个手。做这些功能可以非常有吸引力。但是，做好它其实并不简单。而Firebase简化了往你的app里加AI功能的过程，并且允许你用你熟悉的语言，比如Java、Kotlin、Swift、Flutter、Android等等。

是吗？是的，下一张。给你。Gemini模型是真正的多模态。这是Gemini的一个巨大价值主张。它们接受多模态输入，也支持多模态输出。Firebase AI logic两者都支持。它能为你的用户带来愉快的体验，让实现聊天、图像生成这样的功能变得简单，还支持tool use和function calling这样的高级模型特性。它们也支持流式输入和输出。

在app里实现AI功能时，保护你的Gemini资源不被滥用是使用Firebase AI logic的一个关键价值主张。服务端prompt模板能保护你的prompt不被暴露在客户端。Firebase AI logic的集成能防止非app访问你的模型，内置的用户速率限制能防止少数用户滥用你app的AI配额。

Gemini模型在持续进步，Firebase AI logic也扩展了它的能力，确保你的app能够充分利用Gemini提供的一切。在I/O大会上，Firebase AI logic正在推出一系列更新，改进模型支持，为你的AI功能提供更多安全性，并提高你app里AI功能的效率。

F Firebase AI Logic 现在支持最新的 Gemini 3 GA 模型了。我们还增加了对 Google Maps 接地（grounding）的支持，让 Gemini 模型能够连接 Google Maps 的地理数据，从而打造 AI 并构建具备位置感知能力的 AI 功能。通过 AI Logic 还可以使用 Nano Banana 图像生成的各项控制，比如以编程方式控制长宽比和图片尺寸。我们也对外暴露了完成原因（finish reason），这样图像生成完成时——不管是失败还是成功——你都能在 app 里进行相应的处理。Firebase AI Logic 一直把 AI 资源的安全性放在首位。在 I/O 大会上，我们推出了一次性令牌（one-time tokens），帮助防止恶意攻击者截获并重放令牌，避免消耗掉你 app 的 AI 配额。纯模板模式（Template only mode）会把 AI Logic 限制为只能执行服务端存储的提示词，忽略来自客户端的自定义提示词。你还可以把 AI Logic 的调用限制为仅认证模式（authentication only mode），也就是只有携带有效 Firebase 认证令牌的调用才能执行 AI Logic。我个人最喜欢的是——跨 iOS、Chrome 全面开放正式版（GA），Android 也支持 Gemma 4 的本地及混合推理。借助 Firebase AI Logic，你可以实现本地运行的 AI 功能，必要时还能自动回退到云端。&gt;&gt;【掌声】&gt;&gt;在座有谁需要填报销单？我今天早上看到你拿着一张褪色得厉害的纸在那儿折腾。那可是个相当重要的三明治啊，我得记下来。不过说正经的，我们来看看怎么用 AI Logic 搭配本地模型，把云端配额省下来用在真正需要的地方。配置你的 app 优先使用端上模型、并在需要时回退到云端模型，其实只需要这么一小段代码就够了。我这里有一个扫描小票的 demo app——小票这种内容相对标准化，正适合用本地模型去处理，把宝贵的云端配额省下来。你可以在 demo 里看到，店名和小票的最终金额都直接从图像里提取出来了，整个过程完全没有把任何数据发到云端。&gt;&gt;【掌声】&gt;&gt;你可以用多种方式配置混合推理，对应到你希望 app 优先使用端上模型还是云端模型的不同策略。借助 Firebase AI Logic，为你的 app 添加 AI 能力这件事，权力就在你手中。哇！耶！&gt;&gt;【掌声】&gt;&gt;能力越大，责任越大。（这可不是我的话，别误会。）过去，企业客户在把自己的 Firebase 资源跟其他云基础设施一起管理时，总会遇到各种复杂的问题。为了解决这个，我们推出了 Firebase 与 Application Design Center（应用设计中心，简称 ADC）的集成。ADC 提供了一个统一模型，可以把客户端 app 使用的资源和你的其他云基础设施一并部署和管理。比如，你可以用 ADC 部署 App Check、Firestore、身份验证等等，用和管理其他云服务一样的方式来管理。ADC 还能与 Cloud Hub、App Hub 以及 Gemini Cloud Assist 无缝且原生集成。它还提供大量 AI 辅助工具来帮你落地最佳实践、部署模板。今天你就可以开始在 Application Design Center 里使用 Firebase 了。哇！&gt;&gt;【欢呼声】【掌声】&gt;&gt;在座有 Flutter 开发者吗？哇！我对这一个真的超兴奋。真的超兴奋。Firebase Dart 和 Flutter 一直就是天作之合。你们一直在呼吁，我们听到了——今天我非常高兴地宣布：Cloud Functions for Firebase 的 Dart 支持，现以实验预览版正式发布。哇！&gt;&gt;【掌声】&gt;&gt;对我们亲爱的 Flutter 开发者来说，再也不需要在前后端代码之间来回切换了。在 Firebase 我们超爱 Flutter 开发者，简直是天作之合。说真的，这是我人生中唯一一段允许我周末还能写代码的关系。&gt;&gt;【笑声】&gt;&gt;Firebase 的另一个心头好是身份验证（authentication）。基本上——甚至可以说——所有 app 都需要某种形式的身份验证，而短信验证（SMS）是非常常见的一种方案。SMS 确实能用，但我们觉得可以做得更好。所以去年我们推出了 Firebase 手机号验证（Firebase Phone Number Verification）。一种又快又安全的手机号验证方式。相比单纯的 SMS，Firebase 手机号验证（简称 FPNV）有不少优势。首先，它完全不需要发送短信，这样就彻底消除了短信钓鱼攻击的风险。FPNV 在任何网络连接下都能工作——无论是蜂窝网络、Wi-Fi、有线还是移动热点——这意味着你可以覆盖到你所有联网的用户。运营商是信息的权威来源，也就是说你的 app 可以直接从运营商那里拿到手机号，再也不用依赖用户手动输入。手机号验证既可以单独使用，也可以配合身份提供方一起使用——有时候你只是想要一个有效的手机号，而另一些时候你希望用户真的用这个手机号来注册并登录。手机号验证两种场景都能支持。截至目前，我们已经和超过 10 家运营商达成了合作，而且数量还在持续扩大。我们最近还推出了一种全新的"无 SIM 卡"测试模式，降低了测试 Firebase 手机号验证流程的门槛。最后，也是最重磅的消息——手机号验证今天正式 GA（全面开放）了！哇！既然大家这周都在出差，我想现场演示一下怎么用 FPNV 订一张餐位。我的 demo 礼宾助手 agent——如你所料——是基于 Firebase AI Logic 构建的，并且用 FPNV 来帮我在我虚构的餐厅里订位。我们能不能切到手机画面？嗨，我想订一张今晚的晚餐位，你能帮帮我吗？当然可以。您有特别想去的餐厅吗？还是想看看有哪些可选的？嗯，看看有什么可选的吧。以下是一些选项，这些有您中意的吗？好的，那就试试…… Agave Algorithm餐厅，很棒的选择。要在Agave Algorithm预订，请问您想要什么日期、时间和人数？预订要用谁的名字？预订就用Seba的名字吧，毕竟他买单。五个人，今晚9点半左右吃饭。请看屏幕上的手机验证弹窗。验证完成后，预订就确认了。哇！预订成功。祝您用餐愉快。那个弹窗让我同意把我的手机号发到服务器端，也就是发给餐厅。这样我到那儿的时候，他们就有我的手机号，我就能验证身份了。我们能回到幻灯片吗？验证手机号只需要几行代码。注意用Firebase控制台的测试令牌开启测试会话。这样你就能像我刚才那样测试整个流程，不用真的用SIM卡或真实手机号。也要感谢Seba主动提出要付我这顿虚构的晚餐账单。我们得拿到收据才行。当然，我们扫一下就行。聊聊Agent吧。Agent能做一些很厉害的事。Vibe coding（氛围编程）的应用太棒了。我敢说你们很多人都在做氛围编程的应用。可能现在讲的时候就有一些人在做。有时候你想做氛围编程的应用只是为了验证想法，或者当个demo。但有时候你想让氛围编程的应用留下来，有真实用户，有真实持久数据。看看Firebase怎么帮你用Google AI Studio搭建全栈应用。我们最近宣布Firebase原生集成到Google AI Studio了。只要一句提示，anti-gravity agent就能主动识别需要Firebase集成的地方。anti-gravity agent，用你给它的合适提示，能识别出需要用户特定功能，然后开启Firebase auth。也能识别出需要持久数据，然后开启Firestore。配合写得好的安全规则一起用。这是我用来做下一个爆款应用的提示。要做一个众包的表情翻译应用。提示是这样的：创建一个表情翻译应用，用户可以提交日常的句子，其他用户用emoji来最好地表达这些句子。用户能给自己最喜欢的翻译投票。应用要做得五彩缤纷、好玩有趣。你看，这句提示里根本没提数据库或认证。用这句提示的Antigravity agent自己就识别出需要Firestore和Firebase Auth。然后就弹出对话框问我确认开启Firebase。开启Firebase之后，Antigravity agent就继续帮我搭建带Firebase集成的翻译应用了。用户可以用Google登录。他们的句子、emoji翻译和投票都存在Firestore里，对应Firebase认证的用户ID。数据用Antigravity agent写的严格安全规则存着，很安全。从今天开始，AI Studio可以连接你的Google Workspace了，这样用户就能在应用里使用他们Google表格、文档、Gmail和日历里的数据。Firebase认证为这个集成流程提供Google登录支持。用户可以安全地授权应用使用他们的数据，做一些个性化功能，比如把文档翻译成幻灯片、自动分类收件箱、或者用emoji表示我的日历安排。一如既往，你可以去Firebase控制台在Firebase Auth里看你应用的所有用户。Arthur，感谢你给我们介绍了AI Studio的所有新发布。不客气。我的荣幸。能给我们剧透一下Firebase Studio还有什么要来吗？简直像提前对过台词一样。对过。我就是负责讲段子的。好，简单跟一下。这些是接下来几个月要发布到AI Studio的后续功能。首先要发布的是用Firebase服务创建真实Android应用的能力。哇！第二个功能是能用Firebase AI logic给Android应用加AI能力。第三个也很重要，所有AI logic调用默认都用Firebase app check保护起来，防止token滥用。哇！很酷吧？>> [鼓掌] >> 记得跟着我们。记得看我们的博客，及时了解AI Studio发布的新功能。如果你想用完整功能的IDE，比如Antigravity、Android Studio或其他热门选择，我们也支持。Antigravity的话，Firebase集成在引导流程里了。只要勾选一下，Firebase agent技能就自动装好了。Android Studio里Firebase技能默认就有。所以你让Android编码agent加Firestore或Firebase auth，它自己就全搞定了，不用离开Android Studio就能拿到配置好的Firebase环境。很酷吧？其他选择，其他你想用的编码agent和IDE，你可以去GitHub拿agent技能，也可以直接用NPX从CLI装。我们要让你的agent不管在哪儿、用什么方式开发，都有所有需要的技能用Firebase搭建应用，用更少的token、更短的时间。今天我激动地宣布，Firebase agent技能现在支持Android、iOS、Web和Flutter了。哇！>> [鼓掌] >> 我们也在扩展支持的服务。现在Firebase agent技能也支持崩溃分析和远程配置了。鼓掌鼓掌。>> [鼓掌] >> 软件开发正在转向由人类创造力引导的agent执行方式，我们的重点是确保Firebase在你用新方式、新地方开发的时候都能陪着你。帮你…… 将Google Cloud的所有强大功能带给您的应用和终端用户。正如我们今天所展示的，我们希望帮助您在开发中取得成功。如果您想了解更多，请查看I/O大会上所有其他与Firebase相关的会议，并别忘了查看我们的博客和代码实验室，亲自动手体验我们今天发布和重点介绍的所有内容。谢谢大家。>> [音乐]
---
