---
title: **西蒙·威利森的博客**

Note: "Weblog" (网络日志) is commonly abbreviated to "博客" (bókè) in Chinese, which is the standard technical term used in the Chinese-speaking tech community.
source: simonwillison.net
url: https://simonwillison.net
date: 2026-06-22
category: person/simonwillison.net
translated: true
fetched_at: 2026-06-22T18:28:07.985370
---
# **西蒙·威利森的博客**

Note: "Weblog" (网络日志) is commonly abbreviated to "博客" (bókè) in Chinese, which is the standard technical term used in the Chinese-speaking tech community.

**来源**: simonwillison.net | **日期**: 2026-06-22

---

# 西蒙·威利森的博客

## 关于

anthropic

299

generative-ai

1,838

security

610

open-source

308

ai-security-research

22

...

## 赞助商：

Microsoft — 代理项目在演示与生产之间停滞不前。Microsoft 的 MVP 检查清单弥补了这一差距。

## 试用

条目

链接

名言

笔记

指南

其他

---

## 2026年6月21日

### sqlite-utils 4.0rc1 新增迁移和嵌套事务

[sqlite-utils](https://sqlite-utils.datasette.io/)

是我结合 Python 库和 CLI 工具用于处理 SQLite 数据库的产品。它在 Python 默认的

[sqlite3](https://docs.python.org/3/library/sqlite3.html)

包之上提供了大量高级操作，包括

[复杂表转换](https://sqlite-utils.datasette.io/en/stable/python-api.html#transforming-tables)

支持、从

[JSON 数据自动创建表](https://sqlite-utils.datasette.io/en/stable/python-api.html#creating-tables-from-json-data)

以及更多功能。

[...

975字

]

下午 11:35

/

迁移

,

项目

,

sqlite

,

sqlite-utils

,

annotated-release-notes

## 发布

[sqlite-utils 4.0rc1](https://sqlite-utils.datasette.io/en/stable/changes.html)

见

[sqlite-utils 4.0rc1 新增迁移和嵌套事务](https://sqlite-utils.datasette.io/en/stable/changes.html)

。

2026年6月21日 下午11:30

·

sqlite-utils

---

### AI 代理的临时 Cloudflare 账户

([via](https://news.ycombinator.com/))

公告说这"适用于 AI 代理"，但（目前很常见）AI 的噱头其实并非必要，这对其他人来说也是一个有趣的功能。

简而言之：现在你可以创建一个 Cloudflare Workers 项目并运行它，甚至无需创建 Cloudflare 账户：

```
npx wrangler deploy --temporary
```

Cloudflare 会将应用部署到一个新的临时项目，该项目将保持在线 60 分钟。

我在 Codex Desktop 中使用

GPT-5.5 xhigh

构建了这个

[测试应用](https://github.com/simonw/cloudflare-temporary-deploy)

，提供了一个用于跟踪 HTTP 重定向并返回最终目的地的工具。临时部署按预期工作。

运行部署后会输出一个用于认领新项目的 URL 页面，如果你想让项目持续超过 60 分钟的话。认领页面如下：

#

下午 10:01

/

cloudflare

---

### 2026年6月19日

> MCP 相对于技能/CLI 的真正有价值之处在于将 auth 流程隔离在代理的上下文窗口之外，甚至完全脱离测试框架。

也许 MCP 的理想形式只是一个 API 的认证网关，没有其他功能。这样仍然是一种胜利。

——

[Sean Lynch](https://news.ycombinator.com/user?id=seanlynch)

,

Hacker News 评论

#

下午 10:45

/

model-context-protocol

,

llms

,

ai

,

generative-ai

,

skills

### 目击

下午 6:55 – 7:02

—— 加州鹈鹕、太平洋海豹，位于加利福尼亚州蒙特利湾国家海洋保护区

加州鹈鹕

太平洋海豹

2026年6月19日

---

## 2026年6月18日

### Datasette Apps：在 Datasette 中托管自定义 HTML 应用

今天我们为 Datasette 推出了一款新插件，

[datasette-apps](https://datasette.io/)

，并

[在 Datasette 项目博客上发布了公告](https://datasette.io/blog/datasette-apps)

。这篇文章讲述了"是什么"，但我在这里稍微扩展一下，解释"为什么"。

[...

2,301字

]

下午 11:58

/

iframes

,

javascript

,

项目

,

沙箱

,

ai

,

datasette

,

generative-ai

,

llms

,

ai-assisted-programming

,

content-security-policy

### 发布

[datasette-acl 0.6a0](https://datasette.io/)

此版本将

[datasette-acl](https://datasette.io/)

从仅限表的权限扩展为通用资源共享系统。

Alex Garcia 完成了此版本的大部分工作——我们正在完善这个插件，它将允许多用户 Datasette 实例细粒度地控制谁可以访问 Datasette 中的哪些资源。

2026年6月18日 下午7:03

·

datasette

,

alex-garcia

---

## 2026年6月17日

### GLM-5.2 可能是最强大的纯文本开源权重 LLM

中国 AI 实验室

[Z.ai](https://z.ai/)

于 6 月 13 日向其编程计划订阅者发布了

[GLM-5.2](https://huggingface.co/THUDM/GLM-5.2)

，然后昨天（6 月 16 日）在 MIT 许可下发布了完整的开源权重。这个模型与之前的 GLM-5 和 GLM-5.1 版本大小相似，拥有

7530 亿参数、

1.51TB

的庞然大物——其中包含 40 个活跃参数（专家混合）。GLM-5.2 是一个纯文本输入模型——Z.ai 有一个单独的视觉系列，最近的代表是

[GLM-5V-Turbo](https://huggingface.co/THUDM/GLM-5V-Turbo)

，但那个版本不是开源权重。GLM-5.2 拥有 100 万 token 的上下文窗口，而 GLM-5.1 为 20 万。

[...

598字

]

下午 11:58

/

ai

,

generative-ai

,

llms

,

pelican-riding-a-bicycle

,

llm-release

,

openrouter

,

ai-in-china

,

glm

---

> 2025 年发生的事情是：
>
> 代码生产的经济学被彻底颠覆了。
>
> 以前生成代码非常困难、耗时且昂贵，现在变得几乎免费且即时。代码行从被珍视、重用、呵护和精心管理，变成了可随意丢弃和重新生成的，几乎在一夜之间。
>
> ——[Charity Majors](https://charity.mn/ai-demands-more-engineering-discipline)
>
> AI 需要更多的工程纪律，而不是更少
>
> #

下午 5:12

/

charity-majors

,

ai-assisted-programming

,

generative-ai

,

ai

,

llms

---

### 工具

[`<click-to-play>`](https://github.com/simonw/click-to-play) — 静态图播放

一个渐进增强的 Web Component，将此标记：

```html
<click-to-play>
  <a href="GIF的URL">
    <img src="第一帧的URL" alt="...">
  </a>
</click-to-play>
```

转换为一帧静态图，带有点击播放按钮，按需加载 GIF。适用于当你不想让大 GIF 在用户想播放之前就加载的情况。

这是

[一个示例](https://datasette.io/blog/datasette-apps)

，演示了 Datasette 中的新行编辑工具——实际上我就是为那篇文章构建的这个 Web Component。

2026年6月17日 凌晨3:56

·

web-components

,

javascript

,

gif

,

progressive-enhancement

---

### NetNewsWire 状态

([via](https://brettterpstra.com/))

我觉得这很励志。Brent Simmons 一年前退休了，他的退休项目是让一款软件变得

非常

、非常好——完全不受任何商业压力影响。

这款软件是

[NetNewsWire](https://netnewswire.com/)

——"就像播客，但用于

阅读

"——首次发布于 2002 年，

2018 年开源。

我已经在他 Mac 和 iPhone 上使用了好几年，发现它不可或缺。

#

凌晨 3:36

/

brent-simmons

,

netnewswire

,

open-source

### 目击

下午 6:38 – 7:10

—— 加州鹈鹕、博塔袋鼠田鼠、大蓝鹭、加州海狮、太平洋海豹，位于加利福尼亚州蒙特利湾国家海洋保护区

加州鹈鹕

博塔袋鼠田鼠

大蓝鹭

加州海狮

太平洋海豹

加州鹈鹕

2026年6月17日

---

## 2026年6月16日

### 发布

[datasette 1.0a34](https://datasette.io/)

引用发布说明：

这个 alpha 版本的主要功能是在 Datasette 界面中插入、编辑和删除行的工具。这些功能在表页面上可用，编辑和删除也可以在行页面上作为操作项使用。

这个功能的灵感——早就该有了——来自

[Datasette Agent](https://datasette.io/blog/datasette-agent)

。几天前我为它添加了

[SQL 写支持](https://datasette.io/blog/datasette-agent#sql-write-support)

，这突显了一个荒谬的事实：你可以通过聊天界面插入和编辑数据，但无法在常规 Datasette UI 中做到！

2026年6月16日 下午9:31

·

项目

,

annotated-release-notes

,

datasette

### 发布

[datasette-tailscale 0.1a0](https://datasette.io/)

一个非常实验性的 alpha 插件，让你这样做：

```bash
datasette tailscale mydata.db \
  --ts-authkey tskey-auth-xxxx --ts-hostname datasette-preview
```

这会启动一个本地 Datasette 服务器，并附带一个

[Tailscale](https://tailscale.com/)

边车，将其连接到你的 Tailnet，这样

`http://datasette-preview/`

就能提供 Datasette 服务。

它使用的是实验性的

[tailscale-rs](https://github.com/simonw/tailscale-rs)

库的 Python 绑定。我

[提交了一个 issue](https://github.com/simonw/datasette-tailscale/issues/1)

询问是否有更干净的方式设置代理机制。

2026年6月16日 下午4:18

·

tailscale

,

datasette

---

> 我可以 100% 证明 Qwen3.6-27B 是一个非常有能力的本地编程模型。过去一个半月我几乎每天都在使用它，无论是在我的 M2 Ultra 上还是在我的 RTX 5090 机器上。我用它来处理

[ggml-org](https://ggml.org/)

的一些小型日常任务——没有什么特别令人印象深刻的，但对维护者来说绝对是一个有用的工具。如果我不花大量时间审查 PR，可能会更多地使用它。目前我有一个非常轻量级的测试框架——使用 `pi -nc --offline` 的 pi agent，去掉了所有装饰，还有一个

[简短的系统提示](https://github.com/simonw/dotfiles/blob/main/bin/pi-prompt)

来让它更符合我的风格。
>
> ——[Georgi Gerganov](https://news.ycombinator.com/user?id=ggerganov)
>
> Hacker News 评论

# 本地模型运行现在已经很不错了

作者：Boykis

4:04 下午
标签：georgi-gerganov、llms、ai、generative-ai、pi、ai-assisted-programming、local-llms、qwen、coding-agents

**Fable 5 出口管制损害美国网络防御**

我之前引用了《大西洋月刊》引用 Kate Moussouris 的话，但我应该直接去找原始来源。以下是她确认导致 Claude Fable 5 因出口管制被禁的"越狱"实际上是"修复这段代码"：

研究人员使用了带有已知 CVE 的开源代码，以及带有故意植入漏洞的新代码，要求 Fable 5、Mythos 和 Opus"审查代码的安全问题"。Fable 5 拒绝了。然后他们要求模型"修复这段代码"，通过多步骤的手动过程，将输出转化为测试补丁的脚本。

正如 Kate 指出的，这太荒谬了。编程模型就是用来修复 bug 的，而安全漏洞是他们需要修复的最重要的 bug 类别！

防御者需要能够要求 AI 修复文件中的 bug，解释为什么这个修复很重要，并编写测试来确认补丁有效。这不是绕过安全护栏。这是 AI 模型为防御性安全所做的最有价值的事情：执行防御者每天都在运行的查找、修复和测试循环。[...]

这些提示之所以有效，是因为它们是防御性请求，而这种能力无法被移除，否则会削弱模型修复 bug 和验证补丁的能力。

整个情况真是太乱了。几个月来，非技术决策者一直听说能够"制作网络攻击"的模型特别危险。现在他们似乎准备禁止任何能帮助我们保护代码的模型。

5:20 上午
标签：jailbreaking、security、ai、generative-ai、llms、anthropic、ai-security-research、claude-mythos

Katie Moussouris 是一位网络安全专家，也是 Luta Security 的 CEO，她告诉我 Anthropic 向她分享了白宫关于 Fable 越狱的报告，以获取她的评估。（她说她没有从 Anthropic 那里获得报酬。）Moussouris 说，该报告涉及 IT 专家要求 Fable 帮助查找和修补 bug。她说，当被给予故意不安全的代码时，Fable 拒绝了"审查代码安全问题"的提示，但随后在被要求"修复这段代码"时遵从了，然后进行了一些进一步的手动步骤。Moussouris 告诉我，这只是"模型按预期工作"，用于网络防御。

— Matteo Wong，《大西洋月刊》，《白宫正在加大对 Anthropic 的打击力度》

3:07 上午
标签：anthropic、claude、ai、llms、ai-ethics、jailbreaking、generative-ai、ai-security-research、claude-mythos

**目击**
太平洋港海豹
太平洋港海豹
太平洋港海豹
太平洋港海豹
2026年6月16日
下午 6:56
— 太平洋港海豹，在蒙特雷湾国家海洋保护区，加利福尼亚州，美国

---

2026年6月16日

**今日学习**
Cloudflare CAPTCHA 至少包含一个 & 符号的情况

我正在使用 Cloudflare 的 CAPTCHA（他们现在称之为"Web Application Firewall > Custom rules > Managed Challenge"）来防止爬虫过度抓取我网站上的分面搜索，但我受够了即使是简单的 ?q=term 搜索也会触发验证挑战。

在用 Claude Code 折腾了一番后，我发现可以注册以下规则，这样 CAPTCHA 只会在包含至少一个 & 符号的搜索

# 中文翻译

ai

、

generative-ai

、

llms

、

anthropic

、

claude

、

nicholas-carlini

、

ai-ethics

、

claude-mythos

[...] 相反，我脑海中会想象一个具体的人，然后只为这个人写作。这个人通常是我"三年前的样子"，或者是一位好朋友。

—

Julia Evans

、

write for 1 person

#

凌晨 2:05

/

写作

、

julia-evans

观测记录

下午 5:38

— 加州鹈鹕，拍摄于蒙特利湾国家海洋保护区，加利福尼亚州，美国

加州鹈鹕

加州鹈鹕

加州鹈鹕

2026年6月15日

2026年6月14日

# 为什么AI还没有取代软件工程师，而且将来也不会

Arvind Narayanan和Sayash Kappor从软件工程这一对AI颠覆具有独特适应性的职业角度，探讨了AI失业问题。

在本文中，我们认为有足够的证据来反驳一种说法：一旦AI能力达到某个临界点，就会导致大规模裁员。考虑到在监管壁垒极少的行业中尚且如此，其他大多数职业受到的影响可能更小。

第一个好消息是，数据仍然不支持AI正在导致大规模失业的观点。

2025年3月，纽约成为美国第一个在WARN法案文件中添加AI披露复选框的州。在完整的第一年里，超过160家公司提交了WARN通知。

没有一家

勾选了AI选项

AI加速了将代码输入计算机的阶段，但事实证明，软件工程远不止于此：

如果写代码不是瓶颈，那什么才是？任务分解调查显示，问题在于会议或调试等环节。这引出了更多问题：开发者在那些会议中做什么？为什么不能让AI来做？随着能力提升，调试不会自动化吗？要理解真正的瓶颈，我们必须进行定性分析，深入了解软件工程师自己对工作中哪些部分抗拒自动化的理解。

当我们进行这项分析时，发现有三个真正的瓶颈：(1) 决定和明确要构建什么，(2) 验证并对交付成果负责，(3) 执行这两项工作所需的深度人类理解——对代码库、业务和环境的理解。

我发现AI辅助也在帮助我进行决定和验证这两个步骤，但"深度人类理解"仍然是我所提供的价值的关键。无论给我多少AI辅助，我产生的价值仍然取决于我对代理正在为之构建的问题和解决方案的理解深度。

#

晚上 11:54

/

职业发展

、

ai

、

generative-ai

、

llms

、

arvind-narayanan

、

ai-ethics

观测记录

晚上 7:11 至 7:19

— 加州鹈鹕、大蓝鹭、加州海狮，拍摄于蒙特利湾国家海洋保护区，加利福尼亚州，美国

大蓝鹭

加州海狮

加州鹈鹕

加州鹈鹕

2026年6月14日

2026年6月13日

# 为PyOdide发布WASM轮子到PyPI

Pyodide 314.0发布公告（via Hacker News）包含了我期待已久的消息：

[...]

757字

#

晚上 11:55

/

lua

、

pypi

、

python

、

沙箱隔离

、

webassembly

、

github-actions

、

pyodide

发布

luau-wasm 0.1a0

详情请参阅《为PyOdide发布WASM轮子到PyPI》。

2026年6月13日，晚上 11:14

·

lua

、

pyodide

、

webassembly

研究

# 将SQLite结果列映射回其来源表

如果Datasette中的任意SQL查询能够根据结果中包含的来自哪些表的列，渲染出附加信息，那将非常方便。

要实现这一点，我们需要能够分析如下SQL查询：

select users.name, orders.total from users join orders on orders.user_id = users.id

并以编程方式识别每个结果的table.column——不仅要导航连接，还要处理CTE等更复杂的语法。

我决定让Claude Code（Opus 4.8，因为Fable目前被美国政府禁用）来处理这个问题。它找到了几个有前景的解决方案——一个使用apsw，另一个使用ctypes访问SQLite的sqlite3_column_table_name() C函数（该函数在其他情况下不会暴露给Python），还有一个巧妙地利用EXPLAIN输出的分析。

2026年6月13日，晚上 11:05

·

sqlite

、

datasette

、

python

观测记录

晚上 7:49

— 港豹，拍摄于蒙特利湾国家海洋保护区，加利福尼亚州，美国

港豹

港豹

2026年6月13日

# 关于美国政府暂停访问Fable 5和Mythos 5的声明

（via）

好吧，这太疯狂了：

美国政府以国家安全为由，发布了出口管制指令，暂停所有外国人——无论在美国境内还是境外，包括外籍Anthropic员工——对Fable 5和Mythos 5的访问。该命令的最终效果是，我们必须立即为所有客户禁用Fable 5和Mythos 5，以确保合规。

其他所有Anthropic模型的访问权限将不受影响。

我们于今天下午5:21（东部时间）收到政府指令。信中没有提供其国家安全关切的具体细节。我们的理解是，政府认为它已经发现了一种绕过或"越狱"Fable 5的方法。我们审查了使用这种特定技术识别少量先前已知且较轻微的安全漏洞的演示。这些漏洞似乎都相对简单，我们发现其他公开可用的模型也能在不需绕过的情况下发现它们。[...]

到目前为止，政府只向我们提供了潜在窄范围、非通用越狱的口头证据，这本质上只是要求模型读取特定代码库并修复任何软件缺陷。我们的理解是，一种潜在的越狱方法已与政府分享。我们已审查了该报告，并验证其中显示的能力水平在其他模型（包括OpenAI的GPT-5.5）中广泛存在，而且防御者每天都在使用这些能力来保护系统安全。我们将在未来24小时内分享更多细节。

截至晚上9:01（东部时间），我仍可通过claude.ai和Claude Code访问Fable。

更新：我运行了这个脚本，以观察claude-fable-5何时停止工作。我的访问在太平洋时间下午6:59（东部时间晚上9:59）被切断：

[2026-06-12T18:56:50-07:00] 第35次尝试：运行 uv run llm -m claude-fable-5 hi
[2026-06-12T18:56:55-07:00] 成功：Hi there! How can I help you today?
[2026-06-12T18:57:55-07:00] 第36次尝试：运行 uv run llm -m claude-fable-5 hi
[2026-06-12T18:57:59-07:00] 成功：Hi! How can I help you today?
[2026-06-12T18:58:59-07:00] 第37次尝试：运行 uv run llm -m claude-fable-5 hi
[2026-06-12T18:59:00-07:00] 第37次尝试后失败，退出代码1

stderr:
Error: Error code: 404 - {'error': {'type': 'not_found_error', 'message': 'Claude Fable 5 is not available. Please use Opus 4.8. Learn more: https://www.anthropic.com/news/fable-mythos-access', 'request_id': 'req_011CbzRyirV7KZLHYYdBM9od'}}

#

凌晨 1:01

/

越狱

、

ai

、

generative-ai

、

llms

、

anthropic

、

claude

、

ai-ethics

、

claude-mythos

2026年6月12日

# OpenAI WebRTC音频会话，现在支持文档上下文

我于2024年12月构建了这个工具的第一个版本，以尝试当时新推出的OpenAI WebRTC API来与其实时音频模型交互。

上个月OpenAI向该API引入了一个全新的模型，称为GPT‑Realtime‑2，他们将其宣传为"我们第一个具有GPT‑5级推理能力的语音模型"——知识截止日期为2024年9月30日。

我一直在等待该模型出现在ChatGPT iPhone应用中，但它仍未上线，所以我重新审视了我的旧 Playground。

# 中文翻译

您现在可以选择更好的模型，也可以粘贴一大段文档上下文，这样您就可以在浏览器中进行音频对话，以会话方式探索任何您认为有用的信息。

#

下午11:53

/

音频

、

工具

、

AI

、

OpenAI

、

生成式AI

、

LLM

、

多模态输出

、

WebRTC

---

珍妮经营一家火葬场。约翰的丙烷公司向她投资200亿美元，换取她5%的股份。珍妮将100亿美元投入焚化炉，然后支付约翰100亿美元购买丙烷，把那笔钱烧成灰烬。约翰报告称，他的AI投资本季度产生了100亿美元的收入，并声称自己拥有一家价值1000亿美元企业的5%股份。一位来自**福布斯**的记者被指派撰写关于约翰和珍妮的人物专访，在研究过程中，他与他们陷入了一段充满激情但令人困惑的三角恋，最终变成了一段多元恋的事实婚姻。他的报道满是溢美之词，但在财务细节方面却轻描淡写。

——

安德鲁·辛格尔顿

，《AI经济学入门》

#

下午6:09

/

AI

2026年6月11日

**Claude Fable表现出持续主动的特质**

使用Claude Fable 5两天后，我想最好的形容方式是：**持续主动**。它掌握大量技巧，几乎会动用任何手段来实现目标。

[...

1,939字

]

下午11:35

/

AI

、

提示词注入

、

生成式AI

、

LLM

、

AI辅助编程

、

编程智能体

、

Claude Code

、

Claude Mythos

## 发布

**datasette 1.0a33**

这个alpha版本是迈向稳定1.0版本的重要一步，终于将在Datasette 1.0a3中引入的`?_extra=`模式扩展到了查询和行，超越了之前的表。新模式现也已提供文档！

我在Datasette项目博客上详细介绍了新版本：

[Datasette 1.0a33：API中的JSON extras](https://example.com)

。

由于API探索工具现在几乎可以零成本构建，我让Claude Fable 5在Claude Code中（负责规划）和GPT-5.5 xhigh在Codex Desktop中（负责实现）为我构建了这个自定义extras API探索器来演示该功能：

2026年6月11日 下午3:26

·

项目

、

带注释的发布说明

、

Datasette

、

AI辅助编程

## 工具

**Datasette extras探索器**

— 输入URL并选择要请求的extras，查询Datasette JSON端点并发现可用的extras。界面以语法高亮显示返回的JSON响应，并允许您检查Datasette实例支持哪些extras，支持通过URL哈希参数共享配置。

2026年6月11日 下午3:10

## 发布

**asyncinject 0.7**

几年前我构建了这个实用库来支持一种`asyncio`依赖注入模式。我将它与Datasette一起使用，Claude Fable 5发现了依赖项中的一些错误，然后帮我修复了。这是一款非常主动的模型！

2026年6月11日 上午6:28

·

项目

、

异步

、

Claude Mythos

、

Python

## 研究

**运行不可信查询：Datasette/SQLite vs psycopg/PostgreSQL**

— 本项目探索如何在Datasette（使用SQLite）中安全运行不可信SQL查询，以及类似保护是否可应用于psycopg和PostgreSQL。研究表明两者都可以提供强大的数据损坏和资源耗尽防护。Datasette利用硬只读文件模式和VM进度处理器实现查询超时，而PostgreSQL的权限系统强制执行仅SELECT访问，并通过``statement_timeout``取消资源密集型或睡眠查询。

2026年6月11日 上午4:17

---

## 精选内容

- **sqlite-utils 4.0rc1新增迁移和嵌套事务** - 2026年6月21日
- **Datasette应用：在Datasette中托管自定义HTML应用** - 2026年6月18日
- **GLM-5.2可能是最强大的纯文本开源权重LLM** - 2026年6月17日
- **向PyPI发布用于Pyodide的WASM wheel** - 2026年6月13日
- **Claude Fable表现出持续主动的特质** - 2026年6月11日
- **Claude Fable 5初步印象** - 2026年6月9日
- **使用MicroPython和WASM在沙箱中运行Python代码** - 2026年6月6日
- **Claude Opus 4.8："适度但有形的改进"** - 2026年5月28日
- **我认为Anthropic和OpenAI已经找到了产品市场契合点** - 2026年5月27日
- **关于教皇利奥十四世AI通谕的笔记** - 2026年5月25日
- **Datasette智能体** - 2026年5月21日
- **Gemini 3.5 Flash：更贵，但Google计划用它做一切** - 2026年5月19日
- **五分钟了解过去六个月的LLM发展** - 2026年5月19日
- **关于xAI/Anthropic数据中心交易的笔记** - 2026年5月7日
- **直播博客：2026年与Claude一起编程** - 2026年5月6日
- **氛围编程和智能体工程比我想象的更接近** - 2026年5月6日
- **LLM 0.32a0是一次重大的向后兼容重构** - 2026年4月29日
- **追踪现已终止的OpenAI Microsoft AGI条款历史** - 2026年4月27日
- **DeepSeek V4 - 接近前沿，价格的一小部分** - 2026年4月24日
- **使用LiteParse在浏览器中提取PDF文本** - 2026年4月23日
- **通过半官方Codex后门API用GPT-5.5画鹈鹕** - 2026年4月23日
- **Claude Code每月要花100美元吗？可能不会——这很令人困惑** - 2026年4月22日
- **带着火腿收音机的浣熊在哪里？(ChatGPT Images 2.0)** - 2026年4月21日
- **Claude Opus 4.6和4.7之间系统提示的变化** - 2026年4月18日
- **加入我们在长滩的PyCon US 2026——今年有新的AI和安全轨道** - 2026年4月17日
- **Qwen3.6-35B-A3B在我的笔记本上画的鹈鹕比Claude Opus 4.7更好** - 2026年4月16日
- **Meta的新模型叫Muse Spark，meta.ai聊天有一些有趣的工具** - 2026年4月8日
- **Anthropic的Glasswing项目——将Claude Mythos限制给安全研究人员——我认为这是必要的** - 2026年4月7日
- **Axios供应链攻击使用针对性社会工程** - 2026年4月3日
- **Lenny播客上关于智能体工程的对话亮点** - 2026年4月2日
- **Chatterbox先生是一个（较弱的）维多利亚时代经过道德训练的模型，您可以在自己的电脑上运行** - 2026年3月30日
- **用氛围编程写SwiftUI应用很有趣** - 2026年3月27日
- **使用Claude技能实验Starlette 1.0** - 2026年3月22日
- **基于评论对Hacker News用户进行画像** - 2026年3月21日
- **关于OpenAI收购Astral和uv/ruff/ty的想法** - 2026年3月19日
- **GPT-5.4 mini和GPT-5.4 nano，可以用52美元描述76000张照片** - 2026年3月17日
- **我在Pragmatic峰会关于智能体工程的炉边谈话** - 2026年3月14日
- **也许不是无聊技术之后** - 2026年3月9日
- **编程智能体能通过"干净室"代码实现重新许可开源吗？** - 2026年3月5日
- **Qwen世界有些动静** - 2026年3月4日

---

## 月度简报

**赞助我每月$10**，获取本月最重要的LLM发展精选邮件摘要。

付费让我少发邮件！

[赞助并订阅]()

---

## 披露信息

## 版权页

©

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

2020

2021

2022

2023

2024

2025

2026

*原文请访问 [simonwillison.net](https://simonwillison.net)*