---
title: **Translation:**

"opensource.google.com" 是 Google 的开源项目网站。

在中文中通常称为：
- **Google 开源网站**
- **opensource.google.com**（保持原 URL 不变，因为 URL 作为技术标识符通常不翻译）

**注：** 网址/域名属于技术标识符，一般保留原样，不做文字翻译。
source: opensource.googleblog.com
url: https://opensource.googleblog.com/2026/04
date: 2026-06-22
category: standard/opensource.googleblog
translated: true
fetched_at: 2026-06-22T19:05:42.210360
---
# **Translation:**

"opensource.google.com" 是 Google 的开源项目网站。

在中文中通常称为：
- **Google 开源网站**
- **opensource.google.com**（保持原 URL 不变，因为 URL 作为技术标识符通常不翻译）

**注：** 网址/域名属于技术标识符，一般保留原样，不做文字翻译。

**来源**: opensource.googleblog.com | **日期**: 2026-06-22

---

2026年4月的帖子

**征程开启：结识2026年GSoC贡献者！**

2026年4月30日，星期四

作者：Stephanie Taylor、Mary Radomile、Lucila Ortíz，Google Summer of Code

热烈欢迎1,141位Google Summer of Code（GSoC）2026贡献者！能与184个 mentor组织共同开启新版活动，我们倍感兴奋。各组织共审阅了创纪录的23,371份提案，为各自社区寻找最佳匹配。

**2026年申请统计：**

- 来自131个国家的15,245名申请者，共提交23,371份提案
- 超过2,000名mentor和组织管理员

**接下来是什么？**

在编写第一行代码之前，还有**社区融合期**。为期3.5周的GSoC传统远不止配置工具那么简单；它是一种沉浸式体验。这是一个专属空间，让贡献者掌握代码库、遵循社区标准，并理解项目背后的"为什么"。到编码阶段开始时，每位贡献者都已准备好将项目基础转化为实际影响。

官方编码阶段于**5月25日**开始。对于我们的贡献者来说，这一阶段代表着深入协作开发，提供学习新工具的机会，并为开源项目的心跳做出贡献。

**感谢各位Mentor！**

最后，我们想向杰出的**Mentor**和组织管理员表达最深切的感谢。在AI深刻改变开源社区格局之际，GSoC也不例外。你们的耐心、毅力和不懈的志愿者付出是这个项目的心跳，确保其持续成功，让我们欢迎新一代贡献者进入开源生态系统。

---

**AMS发布：用于开源权重LLM安全验证的基于激活的模型扫描器**

2026年4月27日，星期一

作者：Glen Messenger，Google Kubernetes Engine（GKE）

开源权重模型生态系统正在蓬勃发展——其阴影亦然。2025年的一项研究发现，仅在Hugging Face上就存在超过8,000个安全修改过的模型仓库，修改后的模型以74%的不安全请求遵从率应对危险指令，而原始指令微调模型仅为19%。

对于部署开源权重模型的组织而言，一个关键问题浮现：你如何知道你下载的模型可以安全运行？

我们认为防御性安全工具应该广泛可用。AMS代表了我们为更安全AI生态系统的贡献——在这个世界里，开发者可以在部署前验证模型完整性。

今天我们发布**AMS（Activation-based Model Scanner，基于激活的模型扫描器）**，这是一个开源工具，在10-40秒内回答这个问题——无需发送任何提示。

**行为测试的问题**

传统安全验证依赖行为测试：发送有害提示，检查模型是否拒绝。这种方法有三个根本性限制。

**速度慢。** 全面基准测试（如HarmBench）需要数百次查询。对于运行持续集成管道或筛选大型模型注册表的组织来说，这可能不切实际。

**不完整。** 没有任何基准测试能覆盖所有有害行为。模型可能在已知测试集上表现出安全行为，同时在新颖或分布外提示上仍不安全。

**可被操纵。** 模型可以被微调以拒绝基准测试提示，同时遵从新颖攻击——这是纯粹行为评估方法的已知局限性。

**结构化方法**

AMS采用完全不同方法。AMS不是测试模型说什么，而是测量模型如何思考。

安全训练在模型激活空间中产生可测量的几何结构。指令微调模型发展出内部"方向向量"——表示，以高统计置信度（4-8σ分离）分离有害内容与良性内容。当安全训练被移除——通过微调、去激活或对未过滤数据进行训练——这种几何结构就会崩塌。

AMS直接测量这种崩塌。该方法基于表征工程的最新研究，该研究表明高级概念在LLM激活空间中线性编码，可以通过中间层隐藏状态的简单线性探针可靠提取。

**AMS检测什么**

AMS作为两级扫描器运行。第一级测量是否存在安全相关的激活结构——无需基线。第二级将模型的激活指纹与已验证基线进行比较，以检测细微修改，包括供应链替换。

在我们的14个模型配置验证中：

- **指令微调模型**（Llama、Gemma、Qwen）显示3.8-8.4σ分离——与强安全训练一致
- **未审查变体**（Dolphin、Lexi）显示崩塌分离至1.1-1.3σ——标记为严重
- **去激活模型**显示部分退化至3.3σ——标记为警告
- **基模型**（无安全训练）显示0.69σ——确认安全结构缺失
- **量化模型**（INT4/INT8）分离漂移小于5%——可安全扫描生产部署

**用例**

**CI/CD安全门**

将AMS集成到模型部署管道中，在不安全模型进入生产环境前将其阻止。示例GitHub Actions工作流：

**供应链验证**

使用第二级指纹比较确认下载的权重与其声明身份匹配。

**注册表筛选**

在上传或下载时自动筛选模型，在部署前标记退化的安全结构。

**工作原理**

AMS通过待检查模型处理一组对比提示对——仅在是否包含有害内容方面不同的示例。它在中间层（通常为35-40%深度）提取隐藏状态，计算分离两类的方向向量，并测量类别分离为σ分数。

关键洞察是，这种测量不需要生成、基准测试查询或真实标签。整个扫描每个提示对只需一次前向传播，通常在GPU硬件上10-40秒完成。

探针由单个方向向量组成（对于标准4096维模型约16KB）。不修改模型权重。该工具适用于任何Hugging Face兼容模型。

**开始使用**

AMS现已采用Apache 2.0许可证发布：

GitHub：github.com/GoogleCloudPlatform/activation-model-scanner/

我们欢迎贡献、新模型家族的基线添加以及社区反馈。请参阅仓库中的贡献指南了解详情。

---

**认识A2Family**

2026年4月23日，星期四

作者：Daryl Ducharme，Google Open Source及Alan Blount，Cloud AI

在Google，我们知道基于开源构建让团队能够更快速地使用有意义的技术获得自由和灵活性。开放推动创新和安全，这是我们使命的核心。当我们展望计算的未来时，我们希望确保所有开源社区的开发者都拥有构建安全协作AI系统所需的基础工具。

这就是为什么我们很高兴让您了解"A2Family"——一套旨在帮助您构建、连接和扩展AI代理的开源协议和工具。

**A2A：代理互操作性的基石**

**Agent2Agent（A2A）协议**是一个开放标准，旨在实现AI代理之间的无缝通信和协作。它为代理互操作性提供了确定性的通用语言，在这个世界上，代理由不同框架和不同供应商构建。

# 中文翻译

A2A最初由Google开发，现已捐赠给Linux基金会。正如一句著名的开源格言提醒我们的："如果你想走得快，就独自前行；如果你想走得远，就结伴同行。"A2A将这种协作理念带入AI领域，使代理能够委托子任务、交换信息并协调行动，从而解决单个代理无法解决的复杂问题。

**MCP与Skills：代理需要工具和技能**

从一开始，A2A就热爱MCP，我们也热爱Skills♥️。代理需要发现、协商、对话、制定计划，并在计划失败时进行调整——这是一种与工具完全不同的交互模式，而这正是A2A的设计目标。但为了让您的代理发挥作用，它们需要访问工具，以及关于如何安全可靠地使用这些工具的说明。虽然MCP和A2A可能并非源自同一故事，但它们是一个协同工作更好的大家庭。

当你不确定时——如果是快速确定性资源或操作，那就是工具；但如果你最终可能会进行对话，那就是代理。另一个好的心智模型是："你是使用工具的专家代理吗"（MCP），还是"是否有其他专家代理在与你协作"（A2A）。

**A2UI：面向代理驱动界面的协议**

当代理需要与人类交流时，它们如何才能安全地在信任边界之间发送富文本界面？A2UI不使用纯文本响应或有风险的代码执行，而是采用另一种方式。

A2UI使AI代理能够生成丰富的、交互式的用户界面，这些界面可以在Web、移动和桌面平台上呈现——无需执行任意代码。它采用安全设计，允许代理仅通过声明式组件描述使用您目录中的预批准组件。

您可能也听说过**MCP Apps**（原MCP UI）。它是A2UI的互补替代方案，通过MCP事件和工具调用将您的代理驱动小部件集成在iframe中。A2UI和MCP Apps有一些有趣的配置方式，可以实现iframe内的生成式UI或驱动iframe的生成式UI。

**AG UI协议**由CopilotKit开发，是一个将代理与前端低延迟连接的标准。它让开发者的工作变得轻松许多，集成了大多数代理框架和前端。如果您正在使用AG UI，您已经同时拥有了A2UI和A2A支持！

**AP2：保障代理经济的安全**

当自主代理发起支付时，现有系统在授权、真实性和问责方面面临挑战。为此，我们推出了**代理支付协议（AP2）**，这是一个面向新兴代理经济的开放协议。

AP2可作为A2A协议的开放扩展使用，旨在为开发者、商户和支付行业实现安全、可靠且可互操作的代理商务。该协议使用可验证数字凭证（VDCs）在系统中建立信任——这些凭证是防篡改的加密签名数字对象，构成了交易的基石。

**UCP：代理商务的通用语言**

虽然AP2保障交易安全，但**通用商务协议（UCP）**定义了整个购物旅程的构建模块，从发现和购买到售后体验。UCP为平台、代理和企业提供了一种通用语言，允许多样化的商务生态系统通过单一标准进行互操作，无需定制开发。

UCP使用开放的行业标准无缝连接不同系统，内置支持A2A和AP2协议。它使零售商能够在客户所在的任何地方与他们会面，确保企业保留自己规则的控制权，并作为记录商户完整拥有客户关系。

**使用ADK整合一切**

协议需要一个坚实的基础来运行。这就是**代理开发套件（ADK）**的用武之地。

从技术上讲，ADK不属于A2Family，但它是一个开源代理开发框架，让您能够构建、调试和部署企业级的可靠AI代理。ADK提供Python、TypeScript、Go和Java版本，帮助您构建生产级代理，而不仅仅是原型。它将所有内容整合在一起，让您能够轻松地为代理配备工具、将它们与A2A协议集成，并在您选择的基础设施上实现全球扩展。

Google倡导协作、透明和共同进步，通过开放技术为每个人建设更美好的未来。我们很高兴与您分享这些工具，期待看到我们能够共同创造什么。

您计划使用A2Family构建什么样的多代理工作流？请在下方评论或在我们的社交媒体上@我们！

---

**开源协作一周年：庆祝A2A周年纪念**

2026年4月16日，星期四

作者：Patricia Cruz，Google开源团队

一年前的2025年4月9日，Google宣布了**Agent2Agent（A2A）协议**。我们看到了需要一个"通用语言"的需求，让构建在不同框架上的AI代理能够在多样化系统中良好协作。随后，在2025年6月23日丹佛举行的北美开源峰会上，Mike Smith站在舞台上分享了AI互操作性未来的关键时刻——Google正式将A2A协议捐赠给Linux基金会，将其确立为供应商中立、社区治理的标准。

这一举措的核心信念是：要让AI代理真正改变我们的工作和生活方式，它们必须能够跨框架边界和组织孤岛进行通信，而不被锁定在单一提供商的生态系统中。通过将A2A置于Linux Foundation的中立托管下，我们为整个行业打开了共同构建、贡献和创新的大门。

**合作伙伴基础**

A2A项目的成立离不开我们的创始成员的支持，包括亚马逊云服务（AWS）、思科、微软、Salesforce、SAP和ServiceNow。在过去的12个月里，这个联盟不断壮大，目前已有超过100家科技公司支持该项目。

**从原型到生产**

自捐赠以来的发展势头令人瞩目。这个始于Google主导的项目已演变为横向点对点协作的关键基础设施。就在一个月前的2026年3月，该项目迎来了重要里程碑——发布了**A2A协议v1.0**，这是该标准的第一个稳定、完全可用于生产的版本。

社区今年取得的主要成就包括：

- **增强安全性**：实现代理卡片签名（Signed Agent Cards）以进行加密身份验证，确保多代理工作流中的信任。
- **Web对齐架构**：完善规范，支持企业级部署中熟悉的负载均衡和安全模式。
- **生态系统互操作性**：展示如何使用ADK、LangGraph、AG2和CrewAI构建的多样化代理无缝委托任务和协调复杂工作流。
- **专家教专家**：我们从开放协作中学习，并分享了我们的知识。

**展望未来**

这个蓬勃发展的代理协议生态系统有助于标准化代理的通信方式、与世界的交互方式以及解决实际问题的方法。A2Family包括AP2（代理支付协议）、A2UI（代理到用户界面）和UCP（通用商务协议），这些是利用A2A开放可扩展性模型为代理通信创建的新协议示例。

在我们庆祝这一周年之际，我们比以往任何时候都更加致力于"A2Family"。A2A协议被设计为与现有标准（如模型上下文协议MCP）互补——MCP管理内部工具集成，而A2A处理自主实体之间至关重要的外部协调。

我们要感谢充满活力的开发者、贡献者和合作伙伴生态系统，感谢他们在过去一年中帮助将这一协议打造成世界级标准。

## 加入A2April庆典！

我们整个四月都在庆祝A2A一周年，举办"A2April"活动。您可以通过在社区分享带有#A2April标签的照片来参与其中。为了帮助您营造节日气氛，我们准备了一个纪念派对帽模板，包含完整的组装说明。

**为创新和开放协作的更多岁月干杯！**

## 致谢

感谢以下贡献者：Mike Smith、Alan Blount、Kassandra Dhillon、Daryl Ducharme和April Kyle Nassi

---

## Jaspr：为什么用Dart进行Web开发可能是个好主意

**2026年4月15日，星期三**

**作者：Kilian Schulte，Netlight**

大多数开发者知道Dart是因为它是Flutter（多平台应用框架）的驱动语言。但Dart生态系统能提供的远不止于此。例如：Jaspr，一个提供类似Flutter体验的Web框架，但专门用于在Dart原生环境中构建快速、对SEO友好且动态的网站。

Dart在Web上的应用并非新想法。最初，Dart被设计为在浏览器中本地运行，类似于JavaScript。Google甚至开发了AngularDart——一个流行的JS框架的纯Dart版本。虽然该框架现已不再受支持，但它为Dart带来了一些令人惊讶的强大Web工具。回溯到2016年，Google团队选择Dart是因为其强大的类型安全性和卓越的开发体验，从那时起Dart就在不断改进。

然而，当我2022年开始构建Jaspr时，这些对我来说都是未知的。作为一名从Web开发转型到Flutter的开发者，我逐渐爱上了Dart，并想探索将其用于Web开发。因此，Jaspr始于一个个人挑战：如果一个现代Web框架完全用Dart构建，它会是什么样子？

将Jaspr作为开源项目创建是我职业生涯中最具挑战性但也最有价值的旅程之一。作为独立维护者起步确实很辛苦，但这带来了绝对的创作自由。我可以探索非传统的想法，按照我设想的方式设计API，并整合其他框架中的现代特性。所有这些都不受流程或路线图的阻碍。我在这个框架上投入了三年多的深夜和周末时间。这种奉献最终以一种我从未想象过的方式得到了回报：Google选择Jaspr来完全重建并驱动官方的Dart和Flutter网站。

### 架构与设计

要理解Jaspr的实际工作原理，让我们看看它的底层设计。Jaspr主要面向正在探索Web开发的Flutter开发者。拥有这样一个明确定义的细分市场极大地帮助我塑造了框架并确定了功能优先级，同时也避免了作为维护者被过度分散精力。

Jaspr的核心设计原则之一是它应该看起来和感觉上对Flutter用户来说是熟悉的，同时依赖原生Web技术如HTML和CSS。这使它与Flutter区分开来——Flutter自2021年起也可以面向Web，但 대신 优化的是跨平台渲染一致性。Flutter完全依赖Canvas API进行渲染，这以较慢的加载时间和较低的SEO为代价。因此，对于想要构建快速、优化且SEO友好的网站的Flutter开发者来说，Jaspr正是缺失的那块拼图。

Jaspr产生的语法与Flutter非常接近，而功能更接近于React那样的高效、基于DOM的渲染算法。

如您所见，Jaspr的**StatelessComponent**反映了Flutter的**StatelessWidget**，但像React和JSX一样构建HTML。Jaspr还提供了类型安全的API，可直接在Dart中编写CSS规则。

客户端渲染只是Jaspr能做到的一个方面。Jaspr被构建为一个全栈通用框架，同时支持服务端渲染（SSR）和静态站点生成（SSG）。在JavaScript生态系统中，您通常会发现渲染库（React、Vue）和元框架（Next、Nuxt、Astro）之间存在硬性划分。Jaspr将这些概念组合成一个多功能且连贯的框架。

为了用有限的资源实现这一系列功能，我自然需要做出权衡。由于我不想限制任何功能的质量，我的策略更侧重于限制功能到重要的内容上。我还学会了优先考虑简单的解决方案，并设计灵活且可组合的API。

例如，我构建了**jaspr_content**作为开发内容驱动网站的插件，支持Markdown和其他来源，类似于Astro或VitePress。它提供了构建大型文档网站所需的所有核心功能，而且不是开箱即用地满足所有用例，而是足够灵活和开放，可以完全定制。事实上，**jaspr_content**目前为新的**flutter.dev**和**dart.dev**文档提供支持，这些文档包含超过3,900页。

### 工具链与开发者体验

在我看来，一个框架的好坏取决于它的工具链，而这正是Dart真正闪耀的地方，为Jaspr开发者提供了出色的开发体验。例如，Flutter以其状态热重载而闻名，使您能够即时替换代码而不会丢失客户端状态。但热重载实际上是Dart的特性，由其独特的编译器架构实现。

对于浏览器开发，**dartdevc**编译器执行模块化和增量编译为JavaScript。它支持状态热重载并提供无缝的调试体验。通过巧妙地利用source-map（源码映射），您可以在浏览器中直接逐步调试原生Dart代码，完整体验断点、值检查和运行时表达式求值。

对于生产构建，Dart使用**dart2js**编译器生成高度优化的、经过tree-shaken（摇树优化）的JavaScript包，或者使用更新的**dart2wasm**编译器通过WebAssembly实现更好的运行时性能。在服务器端，Dart的JIT编译器提供相同的热重载和调试能力，而其AOT编译器将服务器代码编译为优化的、平台特定的原生二进制文件，用于生产环境。

Jaspr在这些和其他能力之上构建，例如为开发者提供全栈调试、自定义lint和代码辅助，以及我称之为**component scopes（组件作用域）**的功能。这是一个简洁的编辑器特性，为您的组件添加内联提示，显示它们是在服务器端、客户端还是两端渲染。当构建全栈应用时，这使得推理在特定文件中可以安全使用哪些平台API或库变得更加容易。我还在开发更多功能，使全栈开发体验更加流畅。例如，全栈热重载——在任何服务器端更改时，无论是更新代码还是（例如）编辑markdown文件，新的预渲染HTML都会被"热重载"到页面中，同时保持所有客户端状态。像这样的功能只有在Jaspr将服务器端和客户端渲染结合到一个框架中的方法下才成为可能。

### 影响与展望

去年，Google选择Jaspr用于Dart和Flutter网站，包括**dart.dev**、**flutter.dev**和**docs.flutter.dev**（[仓库链接](repo)），这些网站每月有超过一百万活跃用户。这些网站从基于JS和Python的静态站点生成器迁移到Jaspr和**jaspr_content**，实现了统一配置，减少了上下文切换和贡献体验的难度。转向Jaspr还简化了**dart.dev/learn**和**docs.flutter.dev/learn**上全新交互式教程的开发。对我来说，这不仅是对Jaspr能力的难以置信的信任，也是在大规模上dogfood（吃自己的狗粮）Jaspr的好方法；它让我能够投入更多时间和资源来改进Jaspr。

# 翻译

随着人工智能不断改变软件开发领域的范围，我认为严格的“领域专家”概念（纯移动端或纯Web端开发者）将变得不那么重要。然而，开发者和团队将越来越重视统一的技术栈，以减少上下文切换并利用统一的工具链。正如React Native因其允许Web开发者复用其技能进行移动开发（或让公司“复用”其开发者）而大受欢迎一样，Jaspr非常适合同时使用Flutter和Web的团队。除了复用现有技能外，Jaspr和Flutter项目还可以共享高达100%的业务逻辑、模型和验证代码。

Dart的类型安全性和高质量工具使其非常适合现代Web开发。Jaspr进化成了缺失的那块拼图——一个具有现代功能和完善开发体验的内聚框架。

我个人将Jaspr视为人工智能趋势的对立面，这种趋势导致所有人趋同使用相同的技术栈，尤其是在Web开发领域。虽然这也有一定好处，但我认为探索替代生态系统具有巨大价值。这可以突破边界、产生新想法，并保持我们行业的活力。

如果我的历程有一个关键收获，那就是：**不要害怕构建你想要使用的工具**。你永远不知道那个代码库会带你走向何方，而这可能带来难以置信的回报。

如果你是一名好奇的Dart或Flutter开发者，想用你已经掌握的技能构建网站，现在是最好的时机。在其[在线 playground](https://jaspr.dev/playground)（也是用Jaspr构建的！）上试用Jaspr，或按照[Jaspr快速入门](https://jaspr.dev/docs/guides/quickstart)开始。

在《[我们用Dart和Jaspr重建了Flutter的网站](https://medium.com/flutter/rebuilding-flutters-websites-with-dart-and-jaspr-5f9b23e8fa86)》中了解更多关于Flutter迁移的信息。

哦，如果你想知道"Jaspr"这个名字的由来——它是以我的狗Jasper命名的。如果你碰巧在[jaspr.site](https://jaspr.site)上浏览并想要[见见Jasper](https://jaspr.site/meet-jasper)，请留意……你可能会发现一个献给他小小的彩蛋。

---

# 利用CPU内存实现更快、更具成本效益的TPU大语言模型训练

**2026年4月10日，星期五**

作者：
Keyur Ruganathbhai Ranipa、Qinglan Xiang、Vrushabh Sanghavi、Ramesh AG、Weilin Wang（英特尔）
以及 Penporn Koanantakool（谷歌）

---

## 在英特尔至强处理器上进行基于JAX的主机卸载

随着大语言模型（LLM）持续扩展到数千亿参数规模，设备内存容量已成为训练的主要限制因素，因为在反向传播过程中需要用到前向传播中每一层的中间激活值。为了减轻设备内存压力，这些激活值可以在反向传播过程中重新计算，通过牺牲内存来换取重新计算。虽然重计算使得更大的模型能够装入有限的设备内存，但它会显著增加训练时间和成本。

配备高级矩阵扩展（AMX）的英特尔至强处理器（第五代和第六代）能够在JAX训练工作流中实现对选定的内存密集型和计算密集型组件进行实际的主机卸载。这种方法可以帮助团队训练更大的模型，减轻加速器内存压力，提高端到端吞吐量，并降低总拥有成本——特别是在基于TPU的谷歌云实例上。

通过发布这些结果和实现细节，谷歌和英特尔旨在促进透明度并与社区分享实践指导。本文描述了如何在TPU平台上启用JAX的激活卸载，并概述了构建可扩展、注重成本的CPU-加速器混合训练工作流的注意事项。

### 主机卸载

传统的LLM训练通常仅在设备加速器上完成。然而，现代主机拥有比加速器大得多的内存容量（512GB或更多），并可提供额外的计算能力，例如配备AMX功能的英特尔至强可扩展处理器的TFLOPS。利用主机资源可以是重计算之外的一个很好的替代方案。**主机卸载**在主机和设备之间有选择性地移动计算或数据，以优化性能和内存使用。

**主机内存卸载**将频繁访问的张量保留在设备上，其余的溢出到CPU内存作为额外级别的缓存。

**激活卸载**将在前向传播中在设备上计算的激活值传输到主机，存储在主机内存中，并在反向传播期间将其带回设备进行梯度计算。这解锁了训练更大模型、使用更大批量大小和提高吞吐量的能力。

在这篇博客文章中，我们提供了通过JAX卸载激活值的实用指南，以便在配备英特尔至强可扩展处理器的TPU上高效训练更大的模型。

### 在JAX中启用内存卸载

JAX为卸载激活值、模型参数和优化器状态到主机提供了**多种策略**。用户可以使用`checkpoint_names()`为张量创建检查点。下面的代码片段展示了如何创建检查点`x`：

用户可以提供`checkpoint_policies()`来为中间值选择适当的内存优化策略。有三种策略：

1. 在反向传播期间重新计算（默认行为）
2. 存储在设备上
3. 在前向传播后卸载到主机内存并在反向传播期间加载回来

下面的代码将`x`从前向传播后的设备移动到固定的主机内存。

```python
from jax import checkpoint_policies as cp
```

### 在TPU v5p上测量主机卸载的效益

我们在微调和训练工作负载上检验了基于JAX的TPU主机卸载。我们所有的实验都在谷歌云平台上运行，使用单个**v5p-8 TPU**实例，配备单台主机第四代英特尔至强可扩展处理器。

**微调PaliGemma2**：使用基础PaliGemma2 28B模型进行视觉语言任务，我们对语言模型（Gemma2 27B）的注意力层进行了**微调**，同时保持所有其他参数冻结。在微调期间，我们将LLM序列长度设置为256，批量大小设置为256。

默认检查点策略是`nothing_saveable`，它在前向传播期间不会在设备上保留任何激活值。激活值在反向传播期间为梯度计算进行重新计算。虽然这种方法减少了对TPU的内存压力，但增加了计算时间。为了应用主机卸载，我们使用`save_and_offload_only_these_names`卸载Q、K和V投影权重。这些激活值在前向传播期间传输到主机内存（D2H），并在反向传播期间（D2H）取回，因此设备既不存储也不重新计算它们。图2显示主机卸载使训练时间减少了10%。这直接转化为类似的TPU核心小时减少，产生有意义的成本节约。完整的微调方案可在[JAX主机卸载]获取。

**使用MaxText训练Llama2-13B**：MaxText提供了多种可在训练配置文件中指定的**重计算策略**。我们使用策略`remat_policy: 'qkv_proj_offloaded'`来卸载Q、K和V投影权重。图3显示，与完全重新计算所有激活值（`remat_policy: 'full'`）相比，每个训练步骤的时间减少约5%。

### 何时卸载激活值

当跨主机和设备传输激活值的时间低于重新计算它们的时间时，激活卸载是有益的。时间取决于多种因素，如PCIe带宽、模型大小、批量大小、序列长度、激活张量大小、设备的计算能力等。另一个因素是数据移动可以在多大程度上与计算重叠以保持设备忙碌。图4展示了在PaliGemma2 28B训练期间反向传播中设备到主机传输与计算的有效重叠。

# 中文翻译

较小的模型变体（如 PaliGemma2 3B 和 9B）并未从主机卸载中获益，因为重新生成所有张量的速度比将其传输到主机和从主机传输回来更快。因此，识别适当的工作负载和卸载策略对于从主机卸载中获得性能提升至关重要。

## 行动呼吁

如果您在 TPU 上进行训练且受设备内存限制，请考虑评估激活卸载。首先标记候选激活（例如 Q/K/V 投影），然后在代表性工作负载上比较步长时间、内存余量和总体成本。

在我们的实验中，我们观察到较大工作负载的端到端训练时间提升高达约 10%，这可以通过缩短训练时间或在小规模实例上运行相同工作负载来降低总体拥有成本（TCO）。

## 致谢

感谢 Google 的 Emilio Cota 和 Karlo Basioli，以及前 Google 员工 Eugene Zhulenev。

## 庆祝 A2April！

2026 年 4 月 9 日，星期四

作者：Patricia Cruz 和 Daryl Ducharme，Google 开源部门

祝 A2A 一岁生日快乐！与社区一起庆祝 A2A 一周年及其最近的 1.0 版本发布。4 月 9 日是正式生日，我们将整个月都与 #A2April 一起庆祝。为了帮助您庆祝，我们使用 Gemini 制作了一顶派对帽。

使用下面的模板和说明来制作您的纪念派对帽。

### 装配说明

**打印：**
在厚卡纸上打印此文档以获得最佳效果。

**裁剪：**
小心地沿半圆模板的实线外边框裁剪。

**折叠：**
轻轻地将模板弯成圆锥形，将"胶带/胶粘标签"叠压在对面边缘下方。

**固定：**
沿着标签使用双面胶带或胶棒来固定圆锥形状。

**完成：**
在底座两侧打两个小孔，穿过松紧绳或丝带，将帽子固定在头上。

### 派对帽可视化

### 庆祝方式

**社交媒体：**
戴上帽子的照片并添加 #A2April 标签分享，帮助产生社交媒体热度。

**博客系列：**
关注即将推出的 A2April 博客系列，其中包含团队引言和开源社区的故事。

**社区引言：**
如果您在生产环境中使用 A2A，请通过社交媒体联系我们，分享您的故事用于生日帖子。

---

## Kubernetes 迈向 AI 优先：解读新的 AI 一致性计划

2026 年 4 月 6 日，星期一

作者：Duncan Campbell、Kaslin Fields（Developer Source & Signal）和 Janet Kuo、Federico Bongiovanni（Google Kubernetes Engine/GKE）

随着 AI 工作负载从实验笔记本进入大规模生产环境，行业正在围绕一项新标准团结起来，以确保这些工作负载保持可移植性、可靠性和高效性。

这一转变的核心是**认证 Kubernetes AI 一致性计划**的推出。

这一举措代表了对通用、可访问的行业级标准的重大投资，确保 AI 优先 Kubernetes 的优势惠及所有人。

传统 Kubernetes 是为无状态、云优先应用构建的。然而，AI 工作负载引入了标准一致性无法完全覆盖的独特复杂性：

**特定硬件需求：**
AI 模型需要对 GPU 和 TPU 等加速器的精确控制。

**网络和延迟：**
推理和分布式训练需要低延迟网络和特殊配置。

**有状态特性：**
与传统 Web 应用不同，AI 通常依赖复杂的有状态数据管道。

AI 一致性计划充当标准 Kubernetes 一致性的**超集**。要成为 AI 一致性平台，必须首先通过所有标准 Kubernetes 测试，然后满足专门针对 AI 的额外要求。

### AI 一致性计划的关键支柱

Kubernetes AI 一致性计划通过 **AI Conformance** 计划在开放中推动。这项跨公司努力由行业专家 Janet Kuo（Google）、Mario Fahlandt（Kubermatic GmbH）、Rita Zhang（Microsoft）和 Yuan Tang（RedHat）领导。该计划是开源生态系统内的协作努力，涉及多个组织和个人。通过开放开发该计划，社区确保标准建立在信任基础上，并直接满足全球生态系统的多样化需求。该计划建立了一套经过验证的能力集，行业内的平台（如 Google Kubernetes Engine/GKE 和 Azure Kubernetes Service/AKS）已经在采用。

#### 动态资源分配（DRA）

DRA 是新标准的基石。它将资源分配从简单的加速器数量转移到通过属性的细粒度硬件控制。对于数据科学家而言，这意味着他们现在可以根据内存容量或特殊能力等特性请求特定硬件，确保环境完美匹配模型需求。

#### 全有或全无调度

分布式训练作业经常面临"死锁"，其中一些 pod 启动而其他 pod 等待资源，浪费昂贵的 GPU 时间。AI 一致性要求支持 **Kueue** 等解决方案，允许开发者确保作业仅在所有必需资源可用时才开始，提高集群效率。

#### AI 工作负载的智能自动扩展

一致性集群必须支持基于自定义 AI 指标（如 GPU 或 TPU 利用率）的**水平 Pod 自动扩展（HPA）**，而不仅仅是标准的 CPU/内存。这允许集群在重型推理需求时扩展，在空闲时缩减以节省成本。

#### 高性能标准化可观测性

要在规模上管理 AI，您需要深入的可视性。该计划要求平台直接公开丰富的加速器性能指标，使团队能够以标准化方式监控推理延迟、吞吐量和硬件健康状况。

### 接下来的发展

AI 一致性的推出只是一个开始。随着我们进一步迈入 2026 年，社区正在为认证添加**自动化测试**，并扩展标准以包括更高级的推理模式和更严格的安全要求。

最终目标？让"AI 就绪"成为 Kubernetes 标准的固有、无形的一部分。

要参与并帮助塑造 Kubernetes 上 AI 的未来，请考虑加入**开源 Kubernetes 中的 AI Conformance**。我们欢迎不同的观点，因为您的专业知识和反馈对于为所有人构建强大且包容的标准至关重要。

---

## Gemma 4：以 Apache 2.0 扩展 Gemmaverse

2026 年 4 月 2 日，星期四

作者：Nia Castelly 和 amanda casari（Google 开源）和 Olivier Lacombe（Google DeepMind）

## Gemma 4：以 Apache 2.0 扩展 Gemmaverse

20 多年来，Google 一直保持着对开源社区的坚定承诺。我们的信念很简单：开放技术**对我们的公司有益，对我们的用户有益，对我们的世界有益**。这种培养协作学习和严格测试的承诺一直比追求孤立改进更为有效。自从 2005 年推出 **Google Summer of Code** 以来，以及我们开源 **Kubernetes**、**Android** 和 **Go** 以来，这一直是我们的方法，并且仍然是我们在与维护者和组织者的日常持续工作中坚持的核心。

今天，我们在那段旅程中迈出了重要的一步。自首次发布以来，社区已下载 Gemma 模型超过 4 亿次，并构建了一个由超过 100,000 个令人振奋的变体组成的活跃宇宙，这在社区中被称为 **Gemmaverse**。

**Gemma 4** 以 **Apache 2.0 许可证**发布——我们最强大的开放模型，涵盖从边缘设备到 31B 参数的范围——为这个开发者社区提供尖端 AI 模型。行业标准的 Apache 许可证拓宽了 Gemma 4 的适用性和实用性的视野，为修改、重用和进一步开发提供了易于理解的条款。

### 开放研究的悠久传统

**译文（中文）**

我们致力于打造实用、易获取的 AI 技术和研究，使每个人都能创新并成长。因此，我们的许多创新都免费可用、易于部署，并对全球开发者大有裨益。我们拥有悠久的历史，将包括 **word2vec**、**Jax** 以及开创性的 **Transformers 论文** 在内的基础机器学习研究向公众开放，供任何人使用和学习。

去年我们进一步加速了这一承诺。通过分享能够解读复杂基因组数据并识别肿瘤变异的模型，我们为 **“magic cycle”**（研究突破的“魔法循环”）贡献力量，将科研成果转化为实际影响。然而，本周标志着一个关键时刻——**Gemma 4** 模型是 **Gemmaverse** 中首批在 **OSI 批准的 Apache 2.0** 许可证下发布的模型。

### 赋能开发者和研究者，推动突破性创新

自从 2024 年首次推出 **Gemma** 以来，早期采用者的社区已成长为庞大的建设者、研究者和问题解决者生态系统。Gemma 已经在支持主权数字基础设施，从自动化乌克兰的州级许可，到在印度 22 种官方语言中推广 **Project Navarasa**。我们深知，开发者需要自主性、控制权和许可证的清晰度，以充分发挥进一步 AI 创新的潜力。

**Gemma 4** 将 **自由开源软件（FOSS）** 的三个核心要素直接带给社区：

- **自主性**：通过允许人们基于并修改 **Gemma 4** 模型，我们赋予研究者和开发者自由，以按自己认为合适的方式推进突破性创新。  
- **控制权**：我们理解许多开发者需要对开发和部署环境进行精细控制。**Gemma 4** 支持本地、私有执行，而不依赖仅限云端的基础设施。  
- **清晰性**：通过采用行业标准的 **Apache 2.0** 许可证条款，我们为开发者的权利与责任提供明确说明，使他们能够从零开始自由且自信地进行构建，而无需遵循规定性的服务条款。

### 共同构建，推动实际影响

**Gemma 4** 的发布本身是一份邀请。无论您是探索海豚语言的科研人员、开发下一代开放 AI 智能体的行业开发者，还是希望为公民提供更高效、更有效、更本地化服务的公共机构，Google 都期待与您继续共建。**Gemmaverse** 是您的游乐场，而在 **Apache 2.0** 的加持下，可能性比以往任何时候都更加无限。

我们迫不及待想看到您的作品。

The user asks: "Translate to Chinese, keep technical terms accurate:" and then shows a structure that seems like an archive listing of posts, likely from a forum or a site. The data is organized by years (2014, 2013, 2012, 2011, 2010, 2009, 2008). For each year, there are monthly counts with brackets showing the number of posts in each month. The user wants the translation of this structure to Chinese, preserving technical terms accurate. The phrase "keep technical terms accurate" presumably refers to technical terms such as "January", "February", etc., which are proper nouns, but could be translated to Chinese month names: 一月, 二月, etc. Also the year and number counts should be the same.

We need to output the Chinese translation preserving the structure.

We have to translate each line: "September (6)" etc to Chinese "九月 (6)" and preserve the hierarchy:

► 2014 (104)
 ► December (6)
 etc.

But note the given structure uses "►" as bullet points. Should we preserve those? Probably yes. The bullet "►" can remain as is. The user may want the output as Chinese but same formatting.

Thus we should translate "September", "August", etc to Chinese month names, with parentheses same.

But what about the "Share"? Possibly they want the "Share" at the end also translated? Actually it's "Share". This might be a UI button. It might be translated to "分享". Should we do that? The user said "Translate to Chinese, keep technical terms accurate:" So yes, "Share" is a UI label, could be "分享".

We need to handle each year block: For each year, we have a bullet line "► 2014 (104)" - that should be "► 2014 (104)". The year is numeric, so not transliteration needed. Then for each month, bullet "► December (6)". The month names: "December" -> "十二月". "November" -> "十一月". "October" -> "十月". "September" -> "九月". "August" -> "八月". "July" -> "七月". "June" -> "六月". "May" -> "五月". "April" -> "四月". "March" -> "三月". "February" -> "二月". "January" -> "一月". Keep the parentheses as numbers.

Now let's ensure we preserve the structure of each block with the indentation. The structure includes a hierarchy: year level, then month level, and month-level entries repeated after year-level? Actually the given source includes:

►
September
(6)

But it's basically a summary. Let's examine the original text:

```
►
September
(6)

►
August
(4)

►
July
(1)

►
June
(6)

►
May
(6)

►
April
(10)

►
March
(10)

►
February
(11)

►
January
(8)

►
2014
(104)
►
December
(6)
►
November
(12)
►
October
(7)
►
September
(8)
►
August
(9)
►
July
(7)
►
June
(10)
►
May
(8)
►
April
(8)
►
March
(11)
►
February
(8)
►
January
(10)

►
December
(6)

►
November
(12)

►
October
(7)

►
September
(8)

►
August
(9)

►
July
(7)

►
June
(10)

►
May
(8)

►
April
(8)

►
March
(11)

►
February
(8)

►
January
(10)

►
2013
(100)
...
```

So there is an initial block at top: something like "► September (6)" etc before the year. Possibly that's a list of months with their counts for some period preceding the years? It might be a "Archive" summary showing month counts for the most recent year? The format is "►" and then month name and count. The months are listed from September (6) down to January (8). This appears to be for the current year maybe? Actually after this block, they show "► 2014 (104)" and then the months December (6) to January (10). Then there is a blank line and then a second block identical to the first, likely representing the same months as the current year but again? Actually they have two identical blocks: one before the year, then one after the year (maybe for "2014"?). The repeated block is exactly same as before the year: "► December (6)", "► November (12)", etc. Actually after "► 2014 (104)", they list months: December (6), November (12), October (7), September (8), August (9), July (7), June (10), May (8), April (8), March (11), February (8), January (10). Then a blank line and then the same block again: "► December (6)", "► November (12)", etc. Then after that, they go to "► 2013 (100)" and list months again.

Thus the structure is: Year header, then months list, then a duplicate months list (maybe for some reason), then next year.

Thus for translation we should preserve exactly this structure: Year header line (with bullet), months list with bullet, blank line, then duplicate months list with bullet, blank line, next year header line, etc.

But we also need to translate the initial block before the first year header (the block with September, August, etc). Actually the top block includes months from September to January; maybe it's the months for "2015"? But there is no year label. It might be the most recent months that haven't been aggregated under a year? The content appears to start with "► September (6)", "► August (4)", etc. The month names might be English. We must translate those to Chinese. So the top block will be:

► 九月 (6)
► 八月 (4)
► 七月 (1)
► 六月 (6)
► 五月 (6)
► 四月 (10)
► 三月 (10)
► 二月 (11)
► 一月 (8)

Then "► 2014 (104)", then the months list: "► 十二月 (6)", "► 十一月 (12)", "► 十月 (7)", "► 九月 (8)", "► 八月 (9)", "► 七月 (7)", "► 六月 (10)", "► 五月 (8)", "► 四月 (8)", "► 三月 (11)", "► 二月 (8)", "► 一月 (10)". Then blank line, then repeat the same months list. Then "► 2013 (100)" and its months list.

We need to maintain bullet formatting. The bullet "►" is a right pointing triangle (Unicode). We can preserve that.

Now we need to ensure that we keep technical terms accurate. Month names are not technical but can be considered proper nouns; we should translate them as Chinese month names (Chinese characters). The numbers are unchanged.

Thus the translation is straightforward.

Potential nuance: "Share" at the end is a UI element. Should we translate "Share" to "分享"? Yes.

Thus output all lines in Chinese.

The final output will be a block with the Chinese translation, preserving formatting.

We need to ensure that each bullet is preceded by a "►" and a space? The original formatting includes "►" then space then month name? Actually in the original text:

```
►
September
(6)
```

But the representation in the snippet is maybe multi-line. However the original appears to show each bullet on a separate line. Actually it's like:

```
►
September
(6)
```

But I think it's "► September (6)" combined? The given text is weird: it shows "►" line, then "September", then "(6)" on separate lines. But the structure in the later parts like "► 2014 (104)" seems to be on same line.

Let's examine original again:

```
►
September
(6)

►
August
(4)

►
July
(1)

►
June
(6)

►
May
(6)

►
April
(10)

►
March
(10)

►
February
(11)

►
January
(8)

►
2014
(104)
►
December
(6)
►
November
(12)
►
October
(7)
►
September
(8)
►
August
(9)
►
July
(7)
►
June
(10)
►
May
(8)
►
April
(8)
►
March
(11)
►
February
(8)
►
January
(10)

►
December
(6)

►
November
(12)

►
October
(7)

►
September
(8)

►
August
(9)

►
July
(7)

►
June
(10)

►
May
(8)

►
April
(8)

►
March
(11)

►
February
(8)

►
January
(10)

►
2013
(100)
►
December
(7)
...
```

Thus the formatting is inconsistent. However, for the translation, we can preserve the same line breaks and bullet formatting as they appear.

Given that the user didn't specify a particular format, but "Translate to Chinese, keep technical terms accurate:" and gave a big block. We should replicate the structure with Chinese translations. It may be acceptable to produce a single block where each bullet line includes month name and count on the same line: "► 九月 (6)". That would be a cleaner translation.

But perhaps the original format uses separate lines for month name and count. But it's ambiguous. We can present the translation in a similar style: each bullet line includes month name and count in parentheses on the same line, which is typical for such archives.

Thus we produce:

```
► 九月 (6)
► 八月 (4)
► 七月 (1)
► 六月 (6)
► 五月 (6)
► 四月 (10)
► 三月 (10)
► 二月 (11)
► 一月 (8)

► 2014 (104)
► 十二月 (6)
► 十一月 (12)
► 十月 (7)
► 九月 (8)
► 八月 (9)
► 七月 (7)
► 六月 (10)
► 五月 (8)
► 四月 (8)
► 三月 (11)
► 二月 (8)
► 一月 (10)

► 十二月 (6)
► 十一月 (12)
► 十月 (7)
► 九月 (8)
► 八月 (9)
► 七月 (7)
► 六月 (10)
► 五月 (8)
► 四月 (8)
► 三月 (11)
► 二月 (8)
► 一月 (10)

► 2013 (100)
► 十二月 (7)
► 十一月 (10)
► 十月 (8)
► 九月 (9)
► 八月 (10)
► 七月 (7)
► 六月 (7)
► 五月 (8)
► 四月 (10)
► 三月 (9)
► 二月 (7)
► 一月 (8)

► 十二月 (7)
► 十一月 (10)
► 十月 (8)
► 九月 (9)
► 八月 (10)
► 七月 (7)
► 六月 (7)
► 五月 (8)
► 四月 (10)
► 三月 (9)
► 二月 (7)
► 一月 (8)

► 2012 (93)
► 十二月 (4)
► 十一月 (6)
► 十月 (9)
► 九月 (8)
► 八月 (8)
► 七月 (5)
► 六月 (7)
► 五月 (10)
► 四月 (5)
► 三月 (15)
► 二月 (9)
► 一月 (7)

► 十二月 (4)
► 十一月 (6)
► 十月 (9)
► 九月 (8)
► 八月 (8)
► 七月 (5)
► 六月 (7)
► 五月 (10)
► 四月 (5)
► 三月 (15)
► 二月 (9)
► 一月 (7)

► 2011 (117)
► 十二月 (7)
► 十一月 (14)
► 十月 (13)
► 九月 (10)
► 八月 (6)
► 七月 (13)
► 六月 (11)
► 五月 (5)
► 四月 (11)
► 三月 (10)
► 二月 (10)
► 一月 (7)

► 十二月 (7)
► 十一月 (14)
► 十月 (13)
► 九月 (10)
► 八月 (6)
► 七月 (13)
► 六月 (11)
► 五月 (5)
► 四月 (11)
► 三月 (10)
► 二月 (10)
► 一月 (7)

► 2010 (123)
► 十二月 (9)
► 十一月 (12)
► 十月 (10)
► 九月 (14)
► 八月 (10)
► 七月 (7)
► 六月 (10)
► 五月 (11)
► 四月 (14)
► 三月 (13)
► 二月 (8)
► 一月 (5)

► 十二月 (9)
► 十一月 (12)
► 十月 (10)
► 九月 (14)
► 八月 (10)
► 七月 (7)
► 六月 (10)
► 五月 (11)
► 四月 (14)
► 三月 (13)
► 二月 (8)
► 一月 (5)

► 2009 (124)
► 十二月 (6)
► 十一月 (5)
► 十月 (11)
► 九月 (11)
► 八月 (8)
► 七月 (13)
► 六月 (6)
► 五月 (11)
► 四月 (16)
► 三月 (17)
► 二月 (10)
► 一月 (10)

► 十二月 (6)
► 十一月 (5)
► 十月 (11)
► 九月 (11)
► 八月 (8)
► 七月 (13)
► 六月 (6)
► 五月 (11)
► 四月 (16)
► 三月 (17)
► 二月 (10)
► 一月 (10)

► 2008 (167)
► 十二月 (10)
► 十一月 (11)
► 十月 (13)
► 九月 (16)
► 八月 (12)
► 七月 (20)
► 六月 (14)
► 五月 (21)
► 四月 (16)
► 三月 (17)
► 二月 (17)

► 十二月 (10)
► 十一月 (11)
► 十月 (13)
► 九月 (16)
► 八月 (12)
► 七月 (20)
► 六月 (14)
► 五月 (21)
► 四月 (16)
► 三月 (17)
► 二月 (17)

Share
```

That would be a straightforward translation.

We need to check counts: We must ensure that the month counts match the original numbers exactly.

Original initial block:

September (6)
August (4)
July (1)
June (6)
May (6)
April (10)
March (10)
February (11)
January (8)

So after translation:

九月 (6)
八月 (4)
七月 (1)
六月 (6)
五月 (6)
四月 (10)
三月 (10)
二月 (11)
一月 (8)

Yes.

Now check the months for 2014: Provided counts: December (6), November (12), October (7), September (8), August (9), July (7), June (10), May (8), April (8), March (11), February (8), January (10). Yes.

We have repeated that block after a blank line.

Now for 2013: counts: December (7), November (10), October (8), September (9), August (10), July (7), June (7), May (8), April (10), March (9), February (7), January (8). Yes.

Now for 2012: December (4), November (6), October (9), September (8), August (8), July (5), June (7), May (10), April (5), March (15), February (9), January (7). Yes.

Now for 2011: December (7), November (14), October (13), September (10), August (6), July (13), June (11), May (5), April (11), March (10), February (10), January (7). Yes.

Now for 2010: December (9), November (12), October (10), September (14), August (10), July (7), June (10), May (11), April (14), March (13), February (8), January (5). Yes.

Now for 2009: December (6), November (5), October (11), September (11), August (8), July (13), June (6), May (11), April (16), March (17), February (10), January (10). Yes.

Now for 2008: December (10), November (11), October (13), September (16), August (12), July (20), June (14), May (21), April (16), March (17), February (17). Note: In 2008, there is no January entry; we should reflect that. In the original for 2008, there is no January line. The original for 2008 ends with February (17). So we should not include January for 2008. Also there is no duplicate block after 2008? The original includes a duplicate block of months for 2008: After the main list, they have another block similar: "► December (10)", "► November (11)", "► October (13)", "► September (16)", "► August (12)", "► July (20)", "► June (14)", "► May (21)", "► April (16)", "► March (17)", "► February (17)". So we need to include the duplicate block as well, but no January. Also we need to check if there is a duplicate block for 2008 after the main list. The original includes after "► February (17)" (end of main block) there is a blank line and then the duplicate block with same numbers. So we include that.

Thus for 2008 we need two blocks, each with 11 months (December to February). In my translation above, I included a duplicate block with the same months, but I need to ensure no January appears. Let's check my translation above for 2008: I wrote:

```
► 2008 (167)
► 十二月 (10)
► 十一月 (11)
► 十月 (13)
► 九月 (16)
► 八月 (12)
► 七月 (20)
► 

*原文请访问 [opensource.googleblog.com](https://opensource.googleblog.com/2026/04)*