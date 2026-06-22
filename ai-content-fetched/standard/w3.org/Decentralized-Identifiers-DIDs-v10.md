---
title: 去中心化标识符（DID）v1.0
source: w3.org
url: https://www.w3.org/TR/did-core
date: 2026-06-22
category: standard/w3.org
translated: true
fetched_at: 2026-06-22T18:51:21.910840
---
# 去中心化标识符（DID）v1.0

**来源**: w3.org | **日期**: 2026-06-22

---

# 分布式标识符（DIDs）v1.0

## 核心架构、数据模型和表示形式

**W3C 推荐规范**

2022年7月19日

### 关于本文档的更多信息

**当前版本：**
https://www.w3.org/TR/2022/REC-did-core-20220719/

**最新发布版本：**
https://www.w3.org/TR/did-core/

**最新编辑草稿：**
https://w3c.github.io/did-core/

**历史版本：**
https://www.w3.org/standards/history/did-core

**提交历史**

**实现报告：**
https://w3c.github.io/did-test-suite/

### 编辑

**Manu Sporny**
（Digital Bazaar）

**Amy Guy**
（Digital Bazaar）

**Markus Sabadello**
（Danube Tech）

**Drummond Reed**
（Evernym/Avast）

### 作者

**Manu Sporny**
（Digital Bazaar）

**Dave Longley**
（Digital Bazaar）

**Markus Sabadello**
（Danube Tech）

**Drummond Reed**
（Evernym/Avast）

**Orie Steele**
（Transmute）

**Christopher Allen**
（Blockchain Commons）

### 反馈

GitHub w3c/did-core
（Pull Requests、新Issue、开放Issue）

public-did-wg@w3.org
邮件主题请注明
[did-core] … 消息主题 …
（存档）

### 勘误

存在勘误表。

### 相关文档

DID 用例与需求
DID 规范注册表
DID Core 实现报告

### 另见

翻译版本。

### 版权

© 2022 W3C®（MIT、ERCIM、Keio、Beihang）。适用W3C责任、商标和 permissive 文档许可规则。

---

## 摘要

**分布式标识符（Decentralized Identifiers，DIDs）**是一种新型标识符，能够实现可验证的、去中心化的数字身份。DID 可以指代任何主体（例如：个人、组织、事物、数据模型、抽象实体等），具体指代关系由 DID 的控制者决定。与典型的联邦式标识符不同，DID 的设计使其可以与中心化注册机构、身份提供商和证书颁发机构解耦。具体而言，尽管可能使用其他方来帮助发现与 DID 相关的信息，但 DID 的设计使得其控制者能够在无需任何其他方许可的情况下证明对该 DID 的控制权。

DID 是 URI，它将 DID 主体与 DID 文档相关联，从而实现与该主体相关的可信交互。每个 DID 文档可以表达加密材料、验证方法或服务，这些机制使得 DID 控制者能够证明对 DID 的控制权。服务实现了与 DID 主体相关的可信交互。如果 DID 主体是信息资源（如数据模型），DID 可能提供返回该 DID 主体本身的方式。

本规范规定了 DID 语法、通用数据模型、核心属性、序列化表示形式、DID 操作，以及将 DID 解析为其所代表资源的过程说明。

---

## 文档状态

本节描述本文档在发布时的状态。当前 W3C 出版物列表和技术报告的最新修订版可参见 W3C 技术报告索引，网址为 https://www.w3.org/TR/。

在发布时，已存在 103 个实验性 DID 方法规范、32 个实验性 DID 方法驱动实现、一个用于判断给定实现是否符合本规范的测试套件，以及 46 个提交至一致性测试套件的实现。读者应注意 DID Core 问题列表和 DID Core 测试套件问题列表，其中包含关注点和拟议变更的最新列表，这些内容可能导致对本规范的修改。在发布时，暂未预期有其他实质性问题、变更或修改。

欢迎对本文档提出意见。请直接在 GitHub 上提交问题，或发送至 public-did-wg@w3.org（订阅、存档）。

本文档由分布式标识符工作组作为推荐规范发布，采用推荐标准流程。

W3C 建议广泛部署本规范作为 Web 标准。

W3C 推荐规范是经过广泛共识建立后，由 W3C 及其成员认可并支持的规范，工作组成员承诺对其实现采用免许可费授权。

本文档由根据 W3C 专利政策运作的小组制作。

W3C 维护与该小组成果相关的专利披露公开列表；该页面还包含披露专利的说明。了解可能包含必要权利主张的专利的个人必须按照 W3C 专利政策第 6 条的规定披露相关信息。

本文档受 2021 年 11 月 2 日 W3C 流程文档的约束。

---

## 1. 引言

本节为非规范性内容。

作为个人和组织，我们中的许多人在各种情境中使用全球唯一标识符。这些标识符充当通信地址（电话号码、电子邮件地址、社交媒体用户名）、身份证件号码（护照、驾驶执照、税务编号、健康保险）以及产品标识符（序列号、条形码、射频识别标签）。URI（统一资源标识符）用于 Web 上的资源，您在浏览器中查看的每个网页都有一个全球唯一的 URL（统一资源定位符）。

这些全球唯一标识符中的绝大多数不受我们控制。它们由外部机构颁发，这些机构决定它们所指代的对象以及撤销的时间和条件。它们仅在特定情境中有用，且仅被并非我们自己选择的特定机构认可。它们可能随着组织的倒闭而消失或失效。它们可能不必要的泄露个人信息。在许多情况下，它们可以被恶意第三方欺诈性复制和声称，这就是通常所说的"身份盗窃"。

本规范定义的分布式标识符（DIDs）是一种新型的全球唯一标识符。它们旨在使个人和组织能够使用他们信任的系统生成自己的标识符。这些新标识符使实体能够通过使用数字签名等加密证明进行身份验证来证明对其的控制权。

由于分布式标识符的生成和声明是由实体控制的，每个实体可以根据需要拥有尽可能多的 DID，以保持其期望的身份、角色和交互的分离。这些标识符的使用可以根据不同情境适当限定范围。它们支持与其他需要实体识别自身或其控制事物的个人、机构或系统进行交互，同时提供对应该披露多少个人或隐私数据的控制，且无需依赖中心化权威机构来保证标识符的持续存在。这些理念在 DID 用例文档 [DID-USE-CASES] 中有详细探讨。

本规范不预设任何特定技术或加密方法来支撑 DID 的生成、持久化、解析或解释。例如，实现者可以基于联邦或集中式身份管理系统中注册的标识符创建分布式标识符。事实上，几乎所有类型的标识符系统都可以添加对 DID 的支持。这在集中式、联邦式和去中心化标识符的世界之间创建了互操作性桥梁。这也使实现者能够设计特定类型的 DID，以与其信任的计算基础设施（如分布式账本、去中心化文件系统、分布式数据库和点对点网络）配合工作。

本规范适用于：

- 任何想要理解作为分布式标识符基础的核心理构原则的人；

# 去中心化标识符（DID）规范文档（节选）中文翻译

## 目标读者

希望生成和使用去中心化标识符及其相关数据格式的软件开发者；

希望了解如何在软件和硬件系统中使用去中心化标识符的系统集成商；

希望创建符合本文档所述生态系统的全新DID基础设施（即DID方法）的新规范制定者。

除本规范外，读者可能还会发现《去中心化标识符用例与需求》[DID-USE-CASES]文档也很有帮助。

## 1.1 一个简单示例

本节为非规范性内容。

**DID**是一个简单的文本字符串，由三部分组成：1）`did` URI方案标识符，2）DID方法的标识符，以及3）DID方法特定的标识符。

**图1** 一个去中心化标识符（DID）的简单示例

上面的示例DID解析为一个**DID文档**。**DID文档**包含与DID关联的信息，例如对DID控制器进行加密**身份验证**的方式。

**示例1**：一个简单的DID文档

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:example:123456789abcdefghi",
  "authentication": [{
    // 用于身份验证为 did:...fghi
    "id": "did:example:123456789abcdefghi#keys-1",
    "type": "Ed25519VerificationKey2020",
    "controller": "did:example:123456789abcdefghi",
    "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
  }]
}
```

## 1.2 设计目标

本节为非规范性内容。

**去中心化标识符**是更大系统的组成部分，例如可验证凭证生态系统[VC-DATA-MODEL]，这些系统影响了本规范的设计目标。去中心化标识符的设计目标总结如下。

| 目标 | 描述 |
|------|------|
| **去中心化** | 消除对中心化权威机构或标识符管理中单点故障的需求，包括全局唯一标识符、公钥、**服务**和其他信息的注册。 |
| **控制权** | 赋予实体（包括人类和非人类）直接控制其数字标识符的权力，无需依赖外部权威机构。 |
| **隐私** | 使实体能够控制其信息的隐私，包括对属性或其他数据的最小化、选择性和渐进式披露。 |
| **安全性** | 为请求方提供足够的安全性，使其能够依赖**DID文档**达到所需的保障级别。 |
| **基于证明** | 使**DID控制器**能够在与其他实体交互时提供加密证明。 |
| **可发现性** | 使实体能够发现其他实体的**DID**，以便了解更多相关信息或与这些实体交互。 |
| **互操作性** | 使用可互操作的标准，使DID基础设施能够利用为实现互操作性而设计的现有工具和软件库。 |
| **可移植性** | 不依赖系统和网络，使实体能够在支持**DID**和**DID方法**的任何系统中使用其数字标识符。 |
| **简洁性** | 偏好减少的简单功能集，使技术更易于理解、实施和部署。 |
| **可扩展性** | 在可能的情况下启用可扩展性，只要不会严重阻碍互操作性、可移植性或简洁性。 |

## 1.3 架构概述

本节为非规范性内容。

本节提供去中心化标识符架构主要组件的基本概述。

**图2** DID架构概览及基本组件之间的关系。另请参阅：**叙述性描述**。

图中显示了六个内部带标签的形状，以及它们之间的带标签箭头，如下所示。图的中心是一个标有"DID URL"的矩形框，内含小打字文本"did:example:123/path/to/rsrc"。图的顶部中央是一个标有"DID"的矩形框，内含小打字文本"did:example:123"。图的左上角是一个椭圆，标有"DID Subject"（DID主体）。图的底部中央是一个标有"DID document"（DID文档）的矩形框。左下角是一个椭圆，标有"DID Controller"（DID控制器）。图的右侧中央是一个二维圆柱体渲染图，标有"Verifiable Data Registry"（可验证数据注册表）。

从"DID URL"矩形的顶部，一条标有"contains"（包含）的箭头向上延伸，指向"DID"矩形。从"DID URL"矩形的底部，一条标有"refers, and **dereferences**, to"（指代并解引用）的箭头向下延伸，指向"DID document"矩形。从"DID"矩形出发，一条标有"**resolves** to"（解析为）的箭头向下指向"DID document"矩形。从"DID"矩形出发，一条标有"refers to"（指代）的箭头向左指向"DID subject"椭圆。从"DID controller"椭圆出发，一条标有"controls"（控制）的箭头向右指向"DID document"矩形。从"DID"矩形出发，一条标有"recorded on"（记录于）的箭头向右下方指向"Verifiable Data Registry"圆柱体。从"DID document"矩形出发，一条标有"recorded on"（记录于）的箭头向右上方指向"Verifiable Data Registry"圆柱体。

### DIDs和DID URL

去中心化标识符（**DID**）是一个由三部分组成的**URI**：方案`did:`、方法标识符，以及由**DID方法**指定的唯一方法特定标识符。

**DID**可解析为**DID文档**。**DID URL**扩展了基本**DID**的语法，包含其他标准**URI**组件（如路径、查询和片段），以便定位特定**资源**——例如，**DID文档**内的加密公钥，或**DID文档**外部的**资源**。这些概念在**3.1 DID语法**和**3.2 DID URL语法**中有详细说明。

### DID主体

**DID**的主体，根据定义，即由DID标识的实体。**DID主体**也可能同时是**DID控制器**。任何事物都可以作为DID的主体：人、群体、组织、物品或概念。这在**5.1.1 DID主体**中有进一步定义。

### DID控制器

**DID**的**控制器**是指具有根据**DID方法**定义的能力对**DID文档**进行更改的实体（个人、组织或自主软件）。这种能力通常通过控制一组由代表控制器行事的软件使用的加密密钥来声明，但也可以通过其他机制声明。请注意，一个DID可能有多个控制器，**DID主体**可以是**DID控制器**或其中之一。这个概念在**5.1.2 DID控制器**中有文档记录。

### 可验证数据注册表

为了能够解析为**DID文档**，**DID**通常记录在某种底层系统或网络上。无论使用何种特定技术，任何支持记录**DID**并返回生成**DID文档**所需数据的系统都称为**可验证数据注册表**。示例包括**分布式账本**、去中心化文件系统、任何类型的数据库、点对点网络以及其他形式的可信数据存储。这个概念在**8.方法**中有进一步阐述。

### DID文档

**DID文档**包含与**DID**关联的信息。它们通常表达**验证方法**（如加密公钥）和与**DID主体**交互相关的**服务**。**DID文档**支持的一般属性在**5.核心属性**中有规定。**DID文档**可以序列化为字节流（参见**6.表示**）。**DID文档**中的属性可以根据**8.方法**中概述的适用操作进行更新。

### DID方法

**DID方法**是创建、解析、更新和停用特定类型**DID**及其关联**DID文档**的机制。**DID方法**使用单独的DID方法规范来定义，如**8.方法**中所述。

# DID解析器和DID解析

**DID解析器**是接收**DID**作为输入并生成符合规范的**DID文档**作为输出的系统组件。此过程称为**DID解析**。解析特定类型**DID**的步骤由相关的**DID方法**规范定义。**DID解析**的详细过程在第7节**解析**中有详细说明。

# DID URL解引用器和DID URL解引用

**DID URL解引用器**是接收**DID URL**作为输入并生成**资源**作为输出的系统组件。此过程称为**DID URL解引用**。**DID URL解引用**的详细过程在第7.2节**DID URL解引用**中有详细说明。

# 1.4 一致性

除了标记为非规范性的章节外，本规范中的所有编写指南、图表、示例和注释均为非规范性内容。本规范中的其他内容均为规范性内容。

本文档中的关键词**MAY**、**MUST**、**MUST NOT**、**OPTIONAL**、**RECOMMENDED**、**REQUIRED**、**SHOULD**和**SHOULD NOT**在出现且全部大写时（如本文所示），应按照**BCP 14** [**RFC2119**] [**RFC8174**]中的描述进行解释。

本文件包含JSON和JSON-LD内容的示例。其中一些示例包含无效字符，例如内联注释（**//**）和省略号（**...**）表示对示例价值不大的信息。实施者应注意，如果希望将这些信息用作有效的JSON或JSON-LD，则应删除这些内容。

某些示例包含未在本规范中定义的术语，包括属性名和属性值。这些术语用注释（**// external (property name|value)**）标示。当在**DID文档**中使用此类术语时，预期会在DID规范注册表 [**DID-SPEC-REGISTRIES**] 中注册，并链接到正式定义和JSON-LD上下文。

**DID**和**DID文档**实现的互操作性通过评估实现创建和解析符合本规范的**DID**和**DID文档**的能力来测试。通过确保**DID**和**DID文档**符合规范，为**DID**和**DID文档**的生产者和消费者提供互操作性。**DID方法**规范的互操作性由每个**DID方法**规范中的细节提供。应当理解，与Web浏览器不需要实现所有已知的**URI**方案的方式相同，与**DID**配合使用的符合性软件不需要实现所有已知的**DID方法**。然而，给定**DID方法**的所有实现预期在该方法上可互操作。

**符合规范的DID**是第3节**标识符**中指定规则的任何具体表达形式，且符合该节中相关的规范性陈述。

**符合规范的DID文档**是本规范中描述的数据模型的任何具体表达形式，且符合第4节**数据模型**和第5节**核心属性**中相关的规范性陈述。符合规范文档的序列化格式是确定的、双向的和无损的，如第6节**表示形式**中所述。

**符合规范的生产者**是实现为软件和/或硬件的任何算法，该算法生成**符合规范的DID**或**符合规范的DID文档**，并符合第6节**表示形式**中相关的规范性陈述。

**符合规范的消费者**是实现为软件和/或硬件的任何算法，该算法使用**符合规范的DID**或**符合规范的DID文档**，并符合第6节**表示形式**中相关的规范性陈述。

**符合规范的DID解析器**是实现为软件和/或硬件的任何算法，该算法符合第7.1节**DID解析**中相关的规范性陈述。

**符合规范的DID URL解引用器**是实现为软件和/或硬件的任何算法，该算法符合第7.2节**DID URL解引用**中相关的规范性陈述。

**符合规范的DID方法**是符合第8节**方法**中相关规范性陈述的任何规范。

# 2. 术语

本节是非规范性的。

本节定义本规范中使用的术语以及整个**去中心化标识符**基础设施中使用的术语。本规范中出现这些术语时会包含指向这些术语的链接。

**放大攻击**

攻击者通过向目标系统提供小型有效输入来耗尽其CPU、存储、网络或其他资源的一类攻击，这些输入产生的损害影响可能比输入本身的处理成本呈指数级增长。

**认证**

认证是实体证明其拥有特定属性或控制特定秘密的过程，使用一种或多种**验证方法**。对于**DID**，一个常见示例是证明控制与**DID文档**中发布的公钥关联的加密私钥。

**加密套件**

定义使用特定加密原语以实现特定安全目标的规范。这些文档通常用于指定**验证方法**、数字签名类型及其标识符以及其他相关属性。

**去中心化标识符**（DID）

全球唯一的持久标识符，不需要中心化注册机构，通常以加密方式生成和/或注册。**DID**的一般格式在第3.1节**DID语法**中定义。特定的**DID方案**在**DID方法**规范中定义。许多——但不是所有——DID方法使用**分布式账本技术**（DLT）或某种其他形式的去中心化网络。

**去中心化身份管理**

基于使用**去中心化标识符**的**身份管理**。去中心化身份管理将标识符生成、注册和分配权限扩展到传统的信任根（如**X.500目录服务**、**域名系统**和大多数国家身份证系统）之外。

**DID控制器**

具有对**DID文档**进行更改能力的实体。**DID**可能有一个或多个DID控制器。DID控制器可以由**DID文档**顶层的可选**controller**属性表示。请注意，DID控制器可能是**DID主体**。

**DID委托方**

**DID控制器**已授予使用与**DID**关联的**验证方法**权限的实体，通过**DID文档**进行。例如，控制孩子**DID文档**的父母可能允许孩子使用他们的个人设备进行**认证**。在这种情况下，孩子是**DID委托方**。孩子的个人设备将包含使孩子能够使用**DID**进行**认证**的加密私钥材料。但是，未经父母许可，孩子可能不被允许添加其他个人设备。

**DID文档**

描述**DID主体**的数据集合，包括**DID主体**或**DID委托方**可用于**认证**自身并证明其与**DID**关联的机制（如加密公钥）。**DID文档**可能有一种或多种不同的**表示形式**，如第6节**表示形式**或**W3C** DID规范注册表 [**DID-SPEC-REGISTRIES**] 中所定义。

**DID片段**

**DID URL**中跟在第一个哈希符（**#**）后面的部分。DID片段语法与URI片段语法相同。

**DID方法**

定义特定**DID方法方案**如何实现的规范。DID方法由DID方法规范定义，该规范指定了创建、解析、更新和停用**DID**和**DID文档**的精确操作。参见第8节**方法**。

**DID路径**

**DID URL**中从第一个正斜杠（**/**）字符开始并包含该字符的部分，结束于问号（**?**）字符、片段哈希符（**#**）或**DID URL**的末尾（以先到者为准）。

以下是对该技术文档的中文翻译：

）字符，
或结尾

DID URL

。DID 路径语法与 URI 路径语法相同。
参见

路径

。

DID 查询

DID URL 中从第一个问号字符（

?

）开始的部分（包括该问号）。DID 查询语法与 URI 查询语法相同。参见

查询

。

DID 解析

该过程以

DID

和一组解析选项作为输入，返回符合规范的

DID 文档

表示形式以及附加元数据。此过程依赖于相应

DID 方法

的"读取"操作。该过程的输入和输出在

7.1

DID 解析

中定义。

DID 解析器

DID 解析器是执行

DID 解析

功能的软件和/或硬件组件，以

DID

作为输入并输出符合规范的

DID 文档

。

DID 方案

去中心化标识符

的正式语法。通用 DID 方案以前缀

did:

开头，如

3.1

DID 语法

中所定义。每个

DID 方法

规范都定义了一个特定的 DID 方法方案，该方案与该特定

DID 方法

配合使用。在特定的 DID 方法方案中，DID 方法名称位于第一个冒号之后，以第二个冒号结束，例如

did:example:

。

DID 主体

由

DID

标识并由

DID 文档

描述的实体。任何事物都可以是 DID 主体：人、团体、组织、物理事物、数字事物、逻辑事物等。

DID URL

DID

加上任何符合

3.2

DID URL 语法

定义的附加语法组件。这包括可选的

DID 路径

（带有其前导的

/

字符）、可选的

DID 查询

（带有其前导的

?

字符）以及可选的

DID 片段

（带有其前导的

#

字符）。

DID URL 解引用

该过程以

DID URL

和一组输入元数据作为输入，并返回一个

资源

。该资源可能是

DID 文档

加上附加元数据、

DID 文档

内包含的二级资源，或是完全位于

DID 文档

外部的资源。该过程使用

DID 解析

来获取由

DID URL

中包含的

DID

所指示的

DID 文档

。然后解引用过程可以对

DID 文档

执行额外的处理，以返回由

DID URL

指示的解引用资源。该过程的输入和输出在

7.2

DID URL 解引用

中定义。

DID URL 解引用器

对给定的

DID URL

或

DID 文档

执行

DID URL 解引用

功能的软件和/或硬件系统。

分布式账本

（DLT）

用于记录事件的非中心化系统。这些系统为参与者建立了足够的信任，使它们能够依赖他人记录的数据来做出操作决策。它们通常使用分布式数据库，其中不同节点使用共识协议来确认加密签名交易的顺序。随着时间的推移，对数字签名交易的链接通常使账本历史变得不可篡改。

公钥描述

包含在

DID 文档

内部的数据对象，其中包含使用公钥或验证密钥所需的全部元数据。

资源

按照 [

RFC3986

] 的定义："...术语'资源'在广义上用于指代任何可以被 URI 标识的事物。"类似地，任何资源都可以作为由

DID

标识的

DID 主体

。

表示

按照 HTTP [

RFC7231

] 的定义："旨在反映给定资源的过去、当前或期望状态的信息，采用可以通过协议方便通信的格式，由一组表示元数据和潜在无界的表示数据流组成。"

DID 文档

是描述

DID 主体

的信息的表示。参见

6.

表示

。

表示特定条目

其含义特定于特定

表示

的

DID 文档

中的条目。在

4.

数据模型

和

6.

表示

中定义。例如，

JSON-LD 表示

中的

@context

是一个

表示特定条目

。

服务

与

DID 主体

或相关实体通信或交互的方式，通过一个或多个

服务端点

。示例包括发现服务、代理服务、社交网络服务、文件存储服务和可验证凭证存储库服务。

服务端点

作为

DID 主体

代表的

服务

运行的 网络地址，例如 HTTP URL。

统一资源标识符

（URI）

万维网上所有资源的标准标识符格式，如 [

RFC3986

] 所定义。

DID

是一种 URI 方案。

可验证凭证

用于密码学可验证的数字凭证的标准数据模型和表示格式，由

W3C

可验证凭证规范 [

VC-DATA-MODEL

] 定义。

可验证数据注册表

便于创建、验证、更新和/或停用

去中心化标识符

和

DID 文档

的系统。可验证数据注册表也可能用于其他密码学可验证的数据结构，例如

可验证凭证

。更多信息，请参阅

W3C

可验证凭证规范 [

VC-DATA-MODEL

]。

可验证时间戳

可验证时间戳使第三方能够验证数据对象在特定时刻存在，并且自该时刻以来未被修改或损坏。如果数据完整性在该时刻之后可能被合理地修改或损坏，则该时间戳不可验证。

验证方法

可用于与某个过程结合以独立验证证明的一组参数。例如，密码学公钥可以用作与数字签名相关的验证方法；在这种使用中，它验证签名者持有相关的密码学私钥。

此定义中的"验证"和"证明"旨在广泛适用。例如，密码学公钥可能在 Diffie-Hellman 密钥交换期间用于协商共享对称密钥以进行加密。这保证了密钥协商过程的完整性。因此，这是另一种类型的验证方法，即使过程的描述可能不使用"验证"或"证明"一词。

验证关系

DID 主体

与

验证方法

之间关系的表达。验证关系的一个示例是

5.3.1

身份验证

。

通用唯一标识符

（UUID）

按照 [

RFC4122

] 定义的全局唯一标识符类型。UUID 与 DID 类似，因为它们不需要集中式注册机构。UUID 与 DID 的不同之处在于它们不可解析或密码学可验证。

除了上述术语外，本规范还使用 [

INFRA

] 规范中的术语来正式定义

数据模型

。当使用 [

INFRA

] 术语时，如

字符串

、

集合

和

映射

，它们直接链接到该规范。

3.

标识符

本节描述

DID

和

DID URL

的正式语法。
术语"通用"用于区分此处定义的语法与

特定

DID 方法

在其各自规范中定义的语法。

DID

和

DID URL

的创建过程及其时间在

8.2

方法操作

和

B.2

DID 的创建

中描述。

3.1

DID 语法

通用

DID 方案

是符合 [

RFC3986

] 的 URI 方案。ABNF 定义如下，使用 [

RFC5234

] 中的语法以及

ALPHA

和

DIGIT

的相应定义。所有其他在以下 ABNF 中未定义的规则名称在 [

RFC3986

] 中定义。所有

DID

必须

符合 DID 语法 ABNF 规则。

DID 语法 ABNF 规则

以下是您提供内容的简体中文翻译。我已尽量保持技术术语的准确性（例如使用“必须”、“可选”等RFC标准词汇，以及保留ABNF语法的原始结构）。

```markdown
did                = "did:" method-name ":" method-specific-id
method-name        = 1*method-char
method-char        = %x61-7A / DIGIT
method-specific-id = *( *idchar ":" ) 1*idchar
idchar             = ALPHA / DIGIT / "." / "-" / "_" / pct-encoded
pct-encoded        = "%" HEXDIG HEXDIG

**3.1 DID 方法的要求**
关于 DID 方法与 DID 语法相关的要求，请参见第 8.1 节《方法语法》。

**3.2 DID URL 语法**

DID URL 是用于特定**资源**的网络位置标识符。它可用于检索 DID 主体、**验证方法**、**服务**、DID 文档的特定部分或其他资源的表示。

以下是基于 [RFC5234] 语法的 ABNF 定义。它基于第 3.1 节《DID 语法》中定义的 `did` 方案。`path-abempty`、`query` 和 `fragment` 组件在 [RFC3986] 中定义。所有 DID URL **必须**符合 DID URL 语法 ABNF 规则。

DID 方法可以进一步限制这些规则，如第 8.1 节《方法语法》所述。

DID URL 语法 ABNF 规则如下：

```
did-url = did path-abempty [ "?" query ] [ "#" fragment ]
```

**注**：分号字符保留供将来使用。

虽然分号（`;`）字符可以根据 DID URL 语法的规则使用，但本规范的未来版本可能会将其用作如 [MATRIX-URIS] 中所述的子分隔符（用于参数）。为避免将来的冲突，开发者应避免使用它。

**路径（Path）**

DID 路径与通用 URI 路径相同，并符合 RFC 3986 第 3.3 节中的 `path-abempty` ABNF 规则。与 URI 一样，路径语义可以由 DID 方法指定，而 DID 控制器又可以进一步专门化这些语义。

**示例 2**  
`did:example:123456/path`

**查询（Query）**

DID 查询与通用 URI 查询相同，并符合 RFC 3986 第 3.4 节中的 `query` ABNF 规则。此语法特性在第 3.2.1 节《DID 参数》中有详细说明。

**示例 3**  
`did:example:123456?versionId=1`

**片段（Fragment）**

DID 片段语法和语义与通用 URI 片段相同，并符合 RFC 3986 第 3.5 节中的 `fragment` ABNF 规则。

DID 片段用作对 DID 文档或外部**资源**的与方法无关的引用。以下是 DID 片段标识符的一些示例。

**示例 4**：DID 文档中的唯一验证方法  
`did:example:123#public-key-0`

**示例 5**：DID 文档中的唯一服务  
`did:example:123#agent`

**示例 6**：DID 文档外部的资源  
`did:example:123?service=agent&relativeRef=/credentials#degree`

**注**：跨表示的片段语义

为最大程度地提高互操作性，实现者应努力确保 **DID 片段** 在不同的**表示**（参见第 6 节《表示》）中被以相同方式解释。例如，虽然 JSON Pointer [RFC6901] 可以在 DID 片段中使用，但它在非 JSON 表示中不会被以相同方式解释。

有关与 JSON-LD 表示兼容并在其基础上添加的片段标识符的其他语义，请参见第 E.2 节《application/did+ld+json》。有关如何解引用 DID 片段的信息，请参见第 7.2 节《DID URL 解引用》。

**3.2.1 DID 参数**

DID URL 语法支持基于上一节《查询》中描述的 `query` 组件的简单参数格式。向 DID URL 添加 DID 参数意味着该参数成为**资源**标识符的一部分。

**示例 7**：带有 'versionTime' DID 参数的 DID URL  
`did:example:123?versionTime=2021-05-10T17:00:00Z`

**示例 8**：带有 'service' 和 'relativeRef' DID 参数的 DID URL  
`did:example:123?service=files&relativeRef=/resume.pdf`

某些 DID 参数完全独立于任何特定的 DID 方法，对所有 DID 的功能方式相同。其他 DID 参数并非所有 DID 方法都支持。对于支持可选参数的方法，这些参数应在其支持的所有 DID 方法中统一运行。下表提供了在所有 DID 方法中以相同方式运行的常见 DID 参数。对所有 DID 参数的支持是**可选的**。

**注**

通常期望 DID URL 解引用器实现会参考 [DID-RESOLUTION] 以获取更多实现细节。本规范的范围仅定义最常见查询参数的约定。

| 参数名称 | 描述 |
| :--- | :--- |
| **service** | 通过服务 ID 从 **DID 文档** 中标识服务。如果存在，关联值 **必须**是 **ASCII 字符串**。 |
| **relativeRef** | 根据 RFC3986 第 4.2 节定义的相对 URI 引用，用于标识 **服务端点** 上的**资源**，该服务端点通过使用 `service` 参数从 **DID 文档** 中选择。如果存在，关联值 **必须**是 **ASCII 字符串**，并且 **必须**按照 RFC3986 第 2.1 节的规定对某些字符使用百分号编码。 |
| **versionId** | 标识要解析的 **DID 文档** 的特定版本（版本 ID 可以是顺序的、UUID 或方法特定的）。如果存在，关联值 **必须**是 **ASCII 字符串**。 |
| **versionTime** | 标识要解析的 **DID 文档** 的某个版本时间戳。也就是说，是某个特定时间有效的 **DID 文档**。如果存在，关联值 **必须**是 **ASCII 字符串**，且是有效的 XML 日期时间值，定义于 **W3C** XML Schema Definition Language (XSD) 1.1 Part 2: Datatypes [XMLSCHEMA11-2] 第 3.3.7 节。该日期时间值 **必须**归一化为 UTC 00:00:00 且不带亚秒精度。例如：`2020-12-20T19:17:47Z`。 |
| **hl** | 添加完整性保护的 **DID 文档** 的资源哈希，如 [HASHLINK] 中所述。此参数是非规范性的。如果存在，关联值 **必须**是 **ASCII 字符串**。 |

实现者以及 DID 方法规范作者可能会使用此处未列出的其他 DID 参数。为获得最大的互操作性，**建议** DID 参数使用 DID 规范注册表机制 [DID-SPEC-REGISTRIES]，以避免与其他使用相同 DID 参数但具有不同语义的用法发生冲突。

如果存在明确的用例，其中参数需要成为引用**资源**的 **URL** 的一部分，并且比单独使用 DID 更精确，则可以使用 DID 参数。如果相同的功能可以通过向 DID 解析器传递输入元数据来表达，则**不应**使用 DID 参数。处理这些参数的其他注意事项在 [DID-RESOLUTION] 中讨论。

**注**：DID 参数与 DID 解析

**DID 解析**和 **DID URL 解引用**函数可以通过向 **DID 解析器**传递不属于 **DID URL** 一部分的输入元数据来受到影响（参见第 7.1.1 节《DID 解析选项》）。这与 HTTP 类似，某些参数可以包含在 HTTP URL 中，也可以作为 HTTP 标头在解引用过程中传递。重要的区别在于，作为 **DID URL** 一部分的 DID 参数应用于指定**正在标识的****资源**，而作为 **DID URL** 一部分的输入元数据应用于控制**如何**解析或解引用该**资源**。

**3.2.2 相对 DID URL**

相对 DID URL 是 DID 文档中不以 `did:<method-name>:<method-specific-id>` 开头的任何 URL 值。更具体地说，它是不以第 3.1 节《DID 语法》中定义的 ABNF 开头的任何 URL 值。该 URL 预期引用同一 **DID 文档** 中的**资源**。相对 DID URL **可以**包含相对路径组件、查询参数和片段标识符。

解析相对 DID URL 引用时，**必须**使用 RFC3986 第 5 节《引用解析》中规定的算法。
```

The user wants translation to Chinese, keep technical terms accurate. The text is long and includes technical documentation about DIDs (Decentralized Identifiers) and data model. Need to translate into Chinese, preserving technical terms (e.g., "DID", "DID subject", "base URI", "path", "query", "fragment", "verification method", "services", "DID Document", "representation", "data model", "property", "core properties", "extensibility", "W3C DID Specification Registries", etc.). The user provided text with some line breaks and formatting like "Example 9". The translation must be accurate.

We need to translate entire block. Let's ensure Chinese translation:

Paragraph 1: "be used. The base URI value is the DID that is associated with the DID subject, see 5.1.1 DID Subject. The scheme is did. The authority is a combination of <method-name>:<method-specific-id>, and the path, query, and fragment values are those defined in Path, Query, and Fragment, respectively."

Probably better: "要使用。基础URI值为与DID主体关联的DID，参见5.1.1 DID主体。scheme为did。authority是<method-name>:<method-specific-id>的组合，path、query和fragment的值分别遵循Path、Query和Fragment的定义。"

Paragraph 2: "Relative DID URLs are often used to reference verification methods and services in a DID Document without having to use absolute URLs. DID methods where storage size is a consideration might use relative URLs to reduce the storage size of DID documents."

Chinese: "相对DID URL经常用于在DID文档中引用验证方法和服务，而无需使用绝对URL。对于需要考虑存储大小的DID方法，可能会使用相对URL来减小DID文档的存储大小。"

Then Example 9: Provide JSON. Probably keep JSON as is, but translate comments. The comments are // external (property value), // a relative DID URL used to reference a verification method above. They need Chinese translation but maintain format.

Then "In the example above, the relative DID URL value will be transformed to an absolute DID URL value of did:example:123456789abcdefghi#key-1."

Chinese: "在上面的示例中，相对DID URL值将被转换为绝对DID URL值 did:example:123456789abcdefghi#key-1。"

Then "4. Data Model"

Translate "4. Data Model". Also "This specification defines a data model that can be used to express DID documents and DID document data structures, which can then be serialized into multiple concrete representations. This section provides a high-level description of the data model, descriptions of the ways different types of properties are expressed in the data model, and instructions for extending the data model."

Chinese: "本规范定义了一种数据模型，可用于表达DID文档和DID文档数据结构，这些结构随后可以序列化为多种具体的表示形式。本节提供数据模型的高级描述、不同属性类型在数据模型中的表达方式的说明，以及扩展数据模型的说明。"

Then "A DID document consists of a map of entries, where each entry consists of a key/value pair. The DID document data model contains at least two different classes of entries. The first class of entries is called properties, and is specified in section 5. Core Properties. The second class is made up of representation-specific entries, and is specified in section 6. Representations."

Chinese: "DID文档由一组条目（map）组成，每个条目由键/值对构成。DID文档数据模型至少包含两类条目。第一类条目称为属性（properties），在第5节“核心属性”中规定。第二类条目由表示特定条目（representation-specific entries）组成，在第6节“表示”中规定。"

Then "Figure 3 The entries in a DID document. See also: narrative description."

Probably keep "图3" and Chinese: "DID文档中的条目。另请参见：叙述性描述。"

Then "The diagram is titled, "Entries in the DID Document map". ..."

This description is quite detailed. We'll translate as a paragraph, but keep terms.

Chinese: "该图的标题为“ DID文档映射中的条目”。图中有一条水平的灰色虚线穿过中心。虚线上方的区域标记为“属性”，下方区域标记为“表示特定条目”。图中出现六个带标签的矩形，上方三个、下方三个。左侧四个矩形（上方左侧、上方中间、下方左侧、下方中间）被一个大绿色矩形包围，标题为“ DID规范注册表”。最左边的两个矩形（上方左侧和下方左侧）用蓝色边框和蓝色标签标记。上方左侧的矩形标记为“核心属性”，内部文字为“id, alsoKnownAs, controller, authentication, verificationMethod, service, serviceEndpoint, ...”。下方左侧的矩形标记为“核心表示特定条目”，内部文字为“@context”。右侧的四个矩形（上方中间、上方右侧、下方中间、下方右侧）用灰色边框和黑色标签标记。上方中间的矩形标记为“属性扩展”，内部文字为“ethereumAddress”。下方中间的矩形标记为“表示特定条目扩展”，内部没有其他文字。上方右侧的矩形标记为“未注册的属性扩展”，内部文字为“foo”。下方右侧的矩形标记为“未注册的表示特定条目扩展”，内部文字为“%YAML, xmlns”。"

Continue with "All entry keys in the DID document data model are strings. All entry values are expressed using one of the abstract data types in the table below, and each representation specifies the concrete serialization format of each data type."

Chinese: "DID文档数据模型中的所有条目键都是字符串。所有条目值使用下表中的抽象数据类型之一表示，每种表示形式都规定每种数据类型的具体序列化格式。"

Then the table of data types. Translate each Data Type with Chinese translation.

Data Type table:

map: A finite ordered sequence... -> "map（映射）：一个有限的键/值对有序序列..."

list: "list（列表）：..."

set: "set（集合）：..."

datetime: "datetime（日期时间）：..."

string: "string（字符串）：..."

integer: "integer（整数）：..."

double: "double（双精度浮点数）：..."

boolean: "boolean（布尔值）：..."

null: "null（空值）：..."

Then after table: "As a result of the data model being defined using terminology from [INFRA], property values which can contain more than one item, such as lists, maps and sets, are explicitly ordered. All list-like value structures in [INFRA] are ordered, whether or not that order is significant. For the purposes of this specification, unless otherwise stated, map and set ordering is not important and implementations are not expected to produce or consume deterministically ordered values."

Chinese: "由于数据模型使用[INFRA]的术语定义，包含多个项的属性值（如列表、映射和集合）被明确排序。[INFRA]中的所有类似列表的值结构都是有序的，无论该顺序是否重要。在本规范中，除非另有说明，映射和集合的顺序并不重要，实现不必生成或使用确定性的有序值。"

Then "4.1 Extensibility"

"4.1 可扩展性". Then translate.

"The data model supports two types of extensibility."

Chinese: "数据模型支持两种类型的可扩展性。"

"For maximum interoperability, it is RECOMMENDED that extensions use the W3C DID Specification Registries mechanism [DID-SPEC-REGISTRIES]. The use of this mechanism for new properties or other extensions is the only specified mechanism that ensures that two different representations will be able to work together."

Chinese: "为实现最大程度的互操作性，建议扩展使用 W3C DID 规范注册表机制 [DID-SPEC-REGISTRIES]。使用此机制来处理新属性或其他扩展是唯一明确规定的机制，可确保两种不同的表示形式能够协同工作。"

"Representations MAY define other extensibility mechanisms, including ones that do not require the use of the DID Specification Registries. Such extension mechanisms SHOULD support lossless conversion into any other conformant representation. Extension mechanisms for a representation SHOULD define a mapping of all properties and representation syntax into the data model and its type system."

Chinese: "表示形式可以定义其他可扩展性机制，包括不需要使用 DID 规范注册表的机制。此类扩展机制应支持无损转换为任何其他合规的表示形式。表示形式的扩展机制应定义所有属性和表示语法到数据模型及其类型系统的映射。"

Then note: "Note: Unregistered extensions are less reliable"

Chinese: "注：未注册的扩展可靠性较低"

Then the note text: "It is always possible for two specific implementations to agree out-of-band to use a mutually understood extension or representation that is not recorded in the DID Specification Registries [DID-SPEC-REGISTRIES]; interoperability between such implementations and the larger ecosystem will be less reliable."

Chinese: "两个特定实现总是可以在带外协商使用双方都理解的扩展或表示形式，而不将其记录在 DID 规范注册表 [DID-SPEC-REGISTRIES] 中；此类实现与更大生态系统之间的互操作性将不那么可靠。"

Then "5. Core Properties"

"5. 核心属性"

"A DID is associated with a DID document."

"DID 与 DID 文档关联。"

"DID documents are expressed using the data model and can be serialized into a representation."

"DID 文档使用数据模型表示，并可以序列化为一种表示形式。"

"The following sections define the properties in a DID document, including whether these properties are required or optional. These properties describe relationships between the DID subject and the value of the property."

"以下各节定义 DID 文档中的属性，包括这些属性是必需的还是可选的。这些属性描述 DID 主体与属性值之间的关系。"

"The following tables contain informative references for the core properties defined by this specification, with expected values, and whether or not they are required. The property names in the tables are linked to the normative definitions and more detailed descriptions of each property."

"下表提供了本规范定义的核心属性的参考信息，包括预期值以及是否为必需。表中属性名称链接到规范性定义和每个属性的更详细说明。"

"Note: Property names used in maps of different types"

"注：不同类型映射中使用的属性名称"

"The property names id, type, and controller can be present in maps of different types with possible differences in constraints."

"属性名称 id、type 和 controller 可以出现在不同类型的映射中，约束条件可能有所不同。"

Then "DID Document properties"

"DID 文档属性"

Then the table: "Property", "Required?", "Value constraints"

We'll translate that: "属性", "必需?", "值约束". Then entries: "id", "yes", "A string that conforms to the rules in 3.1 DID Syntax." "alsoKnownAs", "no", "A set of ..."

Thus we need to produce final Chinese translation preserving technical terms and formatting.

We'll need to keep code sections like JSON and comments unchanged except for translation of comments.

Make sure to keep JSON as is, but translate comments inside.

Now proceed.

But note the JSON example includes double quotes and commas and line breaks. We'll preserve it exactly as given, but add Chinese translations for comments.

Original JSON snippet:

{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ]
  "id": "did:example:123456789abcdefghi",
  "verificationMethod": [{
    "id": "did:example:123456789abcdefghi#key-1",
    "type": "Ed25519VerificationKey2020",

// external (property value)

"controller": "did:example:123456789abcdefghi",
    "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
  }, ...],
  "authentication": [

// a relative DID URL used to reference a verification method above

"
#key-1
"
  ]
}

The JSON is not perfectly formatted: missing comma after "]" of @context. But we will replicate as is. Usually we keep exactly same.

We need to translate comments: // external (property value) => // 外部（属性值）; // a relative DID URL used to reference a verification method above => // 用于引用上方验证方法的相对 DID URL.

Make sure to preserve comment style // and keep Chinese translation.

Then after JSON we have "In the example above, the relative DID URL value will be transformed to an absolute DID URL value of did:example:123456789abcdefghi#key-1." So we will translate that.

Now everything else.

Also need to ensure that we use Chinese punctuation appropriate.

We'll present translation as a continuous text.

Now let's go through the entire text again and mark each piece to translate.

Original text:

be used. The

base URI

value is the

DID

that is
associated with the

DID subject

, see

5.1.1

DID Subject

. The

scheme

is

did

. The

authority

is a
combination of

<method-name>:<method-specific-id>

, and the

path

,

query

, and

fragment

values are those defined in

Path

,

Query

, and

Fragment

, respectively.

Relative

DID URLs

are often used to reference

verification methods

and

services

in a

DID Document

without having to use absolute
URLs.

DID methods

where storage size is a consideration might use
relative URLs to reduce the storage size of

DID documents

.

Example

9

: An example of a relative DID URL

{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ]
  "id": "did:example:123456789abcdefghi",
  "verificationMethod": [{
    "id": "did:example:123456789abcdefghi#key-1",
    "type": "Ed25519VerificationKey2020",

// external (property value)

"controller": "did:example:123456789abcdefghi",
    "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
  }, ...],
  "authentication": [

// a relative DID URL used to reference a verification method above

"
#key-1
"
  ]
}

In the example above, the relative

DID URL

value will be transformed to
an absolute

DID URL

value of

did:example:123456789abcdefghi#key-1

.

4.

Data Model

This specification defines a data model that can be used to express

DID
documents

and DID document data structures, which can then be serialized
into multiple concrete

representations

. This section provides a
high-level description of the data model, descriptions of the ways different
types of properties are expressed in the data model, and instructions for
extending the data model.

A

DID document

consists of a

map

of

entries

, where each entry consists of a
key/value pair. The

DID document

data model contains at least two
different classes of entries. The first class of entries is called properties,
and is specified in section

5.

Core Properties

. The second class
is made up of

representation-specific entries

, and is specified in
section

6.

Representations

.

Figure

3

The entries in a DID document.
See also:

narrative description

.

The diagram is titled, "Entries in the DID Document map". A dotted grey line
runs horizontally through the center of the diagram. The space above the line
is labeled "Properties", and the space below it, "Representation-specific
entries". Six labeled rectangles appear in the diagram, three lying above the
dotted grey line and three below it. A large green rectangle, labeled "DID
Specification Registries", encloses the four leftmost rectangles (upper left,
upper center, lower left, and lower center). The two leftmost rectangles
(upper left and lower left) are outlined in blue and labeled in blue, as
follows. The upper left rectangle is labeled "Core Properties", and contains
text "id, alsoKnownAs, controller, authentication, verificationMethod, service,
serviceEndpoint, ...". The lower left rectangle is labeled "Core
Representation-specific Entries", and contains text "@context". The four
rightmost rectangles (upper center, upper right, lower center, and lower right)
are outlined in grey and labeled in black, as follows. The upper center
rectangle is labeled, "Property Extensions", and contains text
"ethereumAddress". The lower center rectangle is labeled,
"Representation-specific Entry Extensions", and contains no other text. The
upper right rectangle is labeled, "Unregistered Property Extensions", and
contains text "foo". The lower right rectangle is labeled "Unregistered
Representation-specific Entry Extensions", and contains text "%YAML, xmlns".

All entry keys in the

DID document

data model are

strings

. All entry values are expressed using one
of the abstract data types in the table below, and each

representation

specifies the concrete serialization format of each data type.

Data Type

Considerations

map

A finite ordered sequence of key/value pairs, with no key appearing twice as
specified in [

INFRA

]. A map is sometimes referred to as an

ordered map

in [

INFRA

].

list

A finite ordered sequence of items as specified in [

INFRA

].

set

A finite ordered sequence of items that does not contain the same item twice
as specified in [

INFRA

]. A set is sometimes referred to as an

ordered set

in [

INFRA

].

datetime

A date and time value that is capable of losslessly expressing all values
expressible by a

dateTime

as specified in
[

XMLSCHEMA11-2

].

string

A sequence of code units often used to represent human readable language
as specified in [

INFRA

].

integer

A real number without a fractional component as specified in
[

XMLSCHEMA11-2

]. To maximize
interoperability, implementers are urged to heed the advice regarding
integers in

RFC8259, Section 6: Numbers

.

double

A value that is often used to approximate arbitrary real numbers as specified
in [

XMLSCHEMA11-2

]. To maximize
interoperability, implementers are urged to heed the advice regarding
doubles in

RFC8259, Section 6: Numbers

.

boolean

A value that is either true or false as defined in [

INFRA

].

null

A value that is used to indicate the lack of a value as defined in [

INFRA

].

As a result of the

data model

being defined using
terminology from [

INFRA

], property values which can contain more than one
item, such as

lists

,

maps

and

sets

, are explicitly ordered. All list-like
value structures in [

INFRA

] are ordered, whether or not that order is
significant. For the purposes of this specification, unless otherwise stated,

map

and

set

ordering is not important and
implementations are not expected to produce

# 中文翻译

字符串

符合

[

RFC3986

] 中

URI

的规则。

控制器

否

符合

3.1

DID 语法

规则的

字符串

或

字符串集合

。

验证方法

否

符合

验证方法属性

规则的

验证方法映射

集合

。

身份验证

否

符合

验证方法属性

规则的

验证方法映射

集合

，或符合

3.2

DID URL 语法

规则的

字符串

集合

。

断言方法

否

密钥协商

否

能力调用

否

能力委托

否

服务

否

符合

服务属性

规则的

服务端点映射

集合

。

## 验证方法属性

| 属性 | 必需？ | 值约束 |
|------|--------|--------|
| id | 是 | 符合<br>3.2<br>DID URL 语法<br>规则的<br>字符串 |
| controller | 是 | 符合<br>3.1<br>DID 语法<br>规则的<br>字符串 |
| type | 是 | 字符串 |
| publicKeyJwk | 否 | 表示符合 [<br>RFC7517<br>] 的 JSON Web Key 的<br>映射 |
| publicKeyMultibase | 否 | 符合<br>[<br>MULTIBASE<br>] 编码公钥的<br>字符串 |

## 服务属性

| 属性 | 必需？ | 值约束 |
|------|--------|--------|
| id | 是 | 符合<br>[<br>RFC3986<br>]<br>中<br>URI<br>规则的<br>字符串 |
| type | 是 | 字符串<br>或<br>字符串集合 |
| serviceEndpoint | 是 | 符合<br>[<br>RFC3986<br>]<br>中<br>URI<br>规则的<br>字符串<br>、<br>映射<br>，或<br>由一个或多个符合<br>[<br>RFC3986<br>]<br>中<br>URI<br>规则的<br>字符串<br>和/或<br>映射<br>组成的<br>集合 |

## 5.1 标识符

本节描述

DID 文档

包含

DID 主体

和

DID 控制器

标识符的机制。

### 5.1.1 DID 主体

特定

DID 主体

的

DID

使用

DID 文档

中的

id

属性表示。

**id**

id

属性的值**必须**是符合

3.1

DID 语法

规则的**字符串**，并且**必须**存在于

DID 文档

的

数据模型

根

映射

中。

**示例 10**

```json
{
  "id": "did:example:123456789abcdefghijk"
}
```

当

id

属性出现在

DID 文档

的**顶层**映射中时，它仅表示

DID 主体

的

DID

。

**注意**：中间表示

DID 方法

规范可以创建不包含

id

属性的

DID 文档

的中间表示，例如当

DID 解析器

执行

DID 解析

时。然而，完全解析的

DID 文档

始终包含有效的

id

属性。

### 5.1.2 DID 控制器

DID 控制器

是授权对

DID 文档

进行更改的实体。授权

DID 控制器

的过程由

DID 方法

定义。

**controller**

controller

属性是**可选的**。如果存在，其值**必须**是符合

3.1

DID 语法

规则的**字符串**或**字符串集合**。对应的

DID 文档

**应当**包含明确允许将某些

验证方法

用于特定目的的

验证关系

。

当

controller

属性出现在

DID 文档

中时，其值表示一个或多个

DID

。那些

DID

对应的

DID 文档

中包含的任何

验证方法

**应当**被接受为权威的，使得满足这些

验证方法

的证明与

DID 主体

提供的证明等效。

**示例 11**：包含 controller 属性的 DID 文档

```json
{
  "@context": "https://www.w3.org/ns/did/v1",
  "id": "did:example:123456789abcdefghi",
  "controller": "did:example:bcehfew7h32f32h7af3"
}
```

**注意**：授权与身份验证

请注意，由

controller

的值提供的授权与

5.3.1

身份验证

中描述的身份验证是分开的。这对于加密密钥丢失时（

DID 主体

无法再访问其密钥）或密钥泄露时（

DID 控制器

的可信第三方需要阻止攻击者的恶意活动）的密钥恢复尤为重要。有关威胁模型和攻击向量的相关信息，请参见

9.

安全注意事项

。

### 5.1.3 又称为

DID 主体

可以出于不同目的或在不同时间拥有多个标识符。可以使用

alsoKnownAs

属性来声明两个或多个

DID

（或其他类型的

URI

）指向同一个

DID 主体

。

**alsoKnownAs**

alsoKnownAs

属性是**可选的**。如果存在，其值**必须**是一个**集合**，其中每个元素都是符合 [

RFC3986

] 的

URI

。

此关系表示此标识符的主体也被一个或多个其他标识符标识。

**注意**：等价性与 alsoKnownAs

如果

alsoKnownAs

关系在反向上被接受，应用程序可以选择将两个相关的标识符视为等价的。**最佳做法是**，在没有这种反向关系的情况下**不要**将它们视为等价的。换句话说，

alsoKnownAs

断言的存在并不能证明此断言是真实的。因此，强烈建议请求方获取对

alsoKnownAs

断言的独立验证。

鉴于

DID 主体

可能为不同目的使用不同的标识符，即使存在互惠关系，对两个标识符之间的强等价性或合并两个对应

DID 文档

的信息的期望也不一定是适当的。

## 5.2 验证方法

DID 文档

可以表达

验证方法

，例如可用于对

DID 主体

或相关方进行

身份验证

或授权交互的加密公钥。例如，加密公钥可用作与数字签名相关的

验证方法

；在这种使用中，它验证签名者可以使用关联的加密私钥。

验证方法

可能有许多参数。例如，一组五个加密密钥需要其中任意三个才能生成加密阈值签名。

**verificationMethod**

verificationMethod

属性是**可选的**。如果存在，其值**必须**是

验证方法

的**集合**，其中每个

验证方法

使用

映射

表示。

验证方法

映射

**必须**包含由

type

的值决定的

id

、

type

、

controller

以及特定的验证材料属性，这些属性在

5.2.1

验证材料

中定义。

验证方法

**可以**包含其他属性。

验证方法

**应当**在 DID 规范注册表 [

DID-SPEC-REGISTRIES

] 中注册。

**id**

验证方法

的

id

属性值**必须**是符合

3.2

DID URL 语法

规则的**字符串**。

**type**

type

属性值**必须**是引用恰好一个

验证方法

类型的**字符串**。为了最大化全局互操作性，

验证方法

类型

**应当**在 DID 规范注册表 [

DID-SPEC-REGISTRIES

] 中注册。

**controller**

controller

属性值**必须**是符合

3.1

DID 语法

规则的**字符串**。

**示例 12**：示例验证方法结构

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/jws-2020/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:example:123456789abcdefghi",
  ...
  "verificationMethod": [{
    "id": ...,
    "type": ...,
    "controller": ...,
    "publicKeyJwk": ...
  }, {
    "id": ...,
    "type": ...,
    "controller": ...,
    "publicKeyMultibase": ...
  }]
}
```

**注意**：验证方法控制器与 DID 控制器

当关系的主体是

DID 文档

时，

controller

属性的语义与当关系的主体是

验证方法

时的语义相同。

The user asks: "Translate to Chinese, keep technical terms accurate". They provide a large passage in English about DID documents, verification material, etc. The user wants the translation into Chinese, preserving technical terms. So we need to translate all text to Chinese, including technical terms like "cryptographic public key", "key controller", "DID document", "controller", "verification method", "verification material", "publicKeyJwk", "publicKeyMultibase", "cryptographic suite", "JSON Web Signature 2020", "Ed25519 Signature 2020", "DID Specification Registries", "verification relationships", "authentication", "keyAgreement", "DID subject", "verifier", etc. We need to maintain the formatting: sections numbers and headings, examples with code. Provide Chinese translation while preserving structure and code.

We need to translate the entire passage, including code block content (JSON) which is presumably code. Should we translate the code comments? The code includes comments like "// external (property value)" etc. In the original English, these comments are there. We might translate them to Chinese but keep technical terms like "external (property value)" perhaps? Probably better to translate comments into Chinese as they are explanatory. But user might want to keep code unchanged? The instruction says "keep technical terms accurate". So for code we could translate comments but not the JSON keys and values. The JSON keys like "publicKeyJwk", "publicKeyMultibase" must remain unchanged. So comments can be translated. The heading numbers like "5.2.1" remain same. The "Example 13", "Example 14", "Example 15" might remain as is or translate to Chinese, but probably keep them as Example 13 etc.

Thus we produce a Chinese translation with appropriate technical terms in Chinese, but ensure accurate translations of terms like "verification method" => "验证方法", "verification material" => "验证材料", "verification relationship" => "验证关系". "controller" => "控制器". "DID document" => "DID 文档". "DID controller" => "DID 控制器". "cryptographic public key" => "加密公钥". "cryptographic suite" => "加密套件". "publicKeyJwk" stays same. "publicKeyMultibase" stays same. "JSON Web Signature 2020" maybe "JSON Web Signature 2020". "Ed25519 Signature 2020" maybe "Ed25519 签名 2020". "DID Specification Registries" => "DID 规范注册表". "Verification Material" => "验证材料". "Verification Method" => "验证方法". "Verification Relationships" => "验证关系". "authentication" => "认证". "keyAgreement" => "密钥协商". "DID subject" => "DID 主体". "verifier" => "验证者". "map" => "映射". "set" => "集合". "string" => "字符串". "URL" => "URL". "dereferencing" => "解引用". "fragment identifier" => "片段标识符". "fingerprint" => "指纹". "non-normative" => "非规范性". "OPTIONAL" => "可选". "RECOMMENDED" => "推荐". "MUST" => "必须". "MUST NOT" => "禁止". "MAY" => "可以". "SHOULD" => "应当". Provide translation of these normative keywords accordingly.

We must be careful to maintain the normative style: e.g., "The publicKeyJwk property is OPTIONAL. If present, the value MUST be a map ...". In Chinese: "publicKeyJwk 属性是可选的。如果存在，其值必须是一个映射...". Use capitals? In Chinese normative language, we can keep the uppercase normative keywords (OPTIONAL, MUST) or translate them as "可选" and "必须". The user asked to keep technical terms accurate; normative keywords may be considered technical. We can keep them as uppercase English words, as they are common in spec. However we could also translate them to Chinese but maintain meaning. The original text uses uppercase normative words. We can preserve them: "publicKeyJwk 属性是 OPTIONAL。如果存在，值 MUST 为 ...". But that may be weird in Chinese. Usually Chinese translations keep them as English uppercase. The user didn't specify, but to keep technical terms accurate, normative keywords are often kept in uppercase. So we can preserve them in the Chinese translation.

Thus we will produce a Chinese translation with the sections, headings, normative terms as uppercase English, technical terms in Chinese translations, and preserve JSON code block.

Let's translate step by step.

Original text includes multiple paragraphs, sections. We'll produce Chinese translation accordingly.

First part: "such as a cryptographic public key. Since a key can't control itself, and the key controller cannot be inferred from the DID document, it is necessary to explicitly express the identity of the controller of the key. The difference is that the value of controller for a verification method is not necessarily a DID controller. DID controllers are expressed using the controller property at the highest level of the DID document (the topmost map in the data model); see 5.1.2 DID Controller."

We translate: "例如，加密公钥。由于密钥不能控制自身，且密钥控制器无法从 DID 文档中推断，因此必须显式表达密钥控制器的身份。区别在于，验证方法的 controller 属性的值不一定等同于 DID 控制器。DID 控制器通过在 DID 文档的最高层级（数据模型中的最外层映射）使用 controller 属性表示；请参见 5.1.2 DID 控制器。"

Then "5.2.1 Verification Material" => "5.2.1 验证材料".

Paragraph: "Verification material is any information that is used by a process that applies a verification method. The type of a verification method is expected to be used to determine its compatibility with such processes. Examples of verification material properties are publicKeyJwk or publicKeyMultibase. A cryptographic suite specification is responsible for specifying the verification method type and its associated verification material. For example, see JSON Web Signature 2020 and Ed25519 Signature 2020. For all registered verification method types and associated verification material available for DIDs, please see the DID Specification Registries [DID-SPEC-REGISTRIES]."

Translation: "验证材料是指在执行验证方法的过程中使用的任何信息。验证方法的 type 预期用于确定其与此类过程的兼容性。验证材料属性的示例包括 publicKeyJwk 或 publicKeyMultibase。加密套件规范负责指定验证方法的 type 及其关联的验证材料。例如，参见 JSON Web Signature 2020 和 Ed25519 Signature 2020。关于 DID 可用的所有已注册的验证方法类型及其关联的验证材料，请参阅 DID 规范注册表 [DID-SPEC-REGISTRIES]。"

Next: "To increase the likelihood of interoperable implementations, this specification limits the number of formats for expressing verification material in a DID document. The fewer formats that implementers have to implement, the more likely it will be that they will support all of them. This approach attempts to strike a delicate balance between ease of implementation and supporting formats that have historically had broad deployment. Two supported verification material properties are listed below:"

Translate: "为提高互操作实现的概率，本规范限制了 DID 文档中表达验证材料的格式数量。实现者需要实现的格式越少，他们支持所有格式的可能性就越大。此方法旨在实现易于实现与支持历史上已广泛部署的格式之间的微妙平衡。下面列出两种支持的验证材料属性："

Then "publicKeyJwk" paragraph.

"The publicKeyJwk property is OPTIONAL. If present, the value MUST be a map representing a JSON Web Key that conforms to [RFC7517]. The map MUST NOT contain "d", or any other members of the private information class as described in Registration Template. It is RECOMMENDED that verification methods that use JWKs [RFC7517] to represent their public keys use the value of kid as their fragment identifier. It is RECOMMENDED that JWK kid values are set to the public key fingerprint [RFC7638]. See the first key in Example 13 for an example of a public key with a compound key identifier."

Translate: "publicKeyJwk 属性是 OPTIONAL。如果存在，其值 MUST 为一个表示符合 [RFC7517] 的 JSON Web Key 的映射。该映射不得包含 "d"，亦不得包含 Registration Template 中所述的私有信息类的任何其他成员。推荐使用 JWK [RFC7517] 表示公钥的验证方法使用 kid 的值作为其片段标识符。推荐将 JWK kid 值设为公钥指纹 [RFC7638]。请参见示例 13 中的第一个密钥，了解具有复合密钥标识符的公钥示例。"

Then "publicKeyMultibase" paragraph.

"The publicKeyMultibase property is OPTIONAL. This feature is non-normative. If present, the value MUST be a string representation of a [MULTIBASE] encoded public key. Note that the [MULTIBASE] specification is not yet a standard and is subject to change. There might be some use cases for this data format where publicKeyMultibase is defined, to allow for expression of public keys, but privateKeyMultibase is not defined, to protect against accidental leakage of secret keys."

Translate: "publicKeyMultibase 属性是 OPTIONAL。此特性为非规范性。如果存在，其值 MUST 为 [MULTIBASE] 编码公钥的字符串表示。请注意，[MULTIBASE] 规范尚未成为标准，可能会有变化。在某些使用场景中，定义了 publicKeyMultibase 以允许表达公钥，但未定义 privateKeyMultibase，以防止意外泄露私钥。"

Then: "A verification method MUST NOT contain multiple verification material properties for the same material. For example, expressing key material in a verification method using both publicKeyJwk and publicKeyMultibase at the same time is prohibited."

Translate: "验证方法不得为同一材料包含多个验证材料属性。例如，在同一验证方法中同时使用 publicKeyJwk 和 publicKeyMultibase 表达密钥材料是被禁止的。"

Then: "An example of a DID document containing verification methods using both properties above is shown below. Example 13: Verification methods using publicKeyJwk and publicKeyMultibase"

Translate: "下面给出一个包含上述两种属性的验证方法的 DID 文档示例。示例 13：使用 publicKeyJwk 和 publicKeyMultibase 的验证方法"

Then the JSON code block. We must keep JSON unchanged except comments translated. The code currently includes comments: "// external (property value)" etc. We'll translate these to Chinese: maybe "// 外部（属性值）", "// 外部（属性名称）". So comments will become Chinese, but JSON key names remain. Also we need to preserve the backticks etc. Also "Example 13" and "Example 13" might remain as is. We'll translate "Example 13:" to "示例 13：" in Chinese.

The JSON:

{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/jws-2020/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ]
  "id": "did:example:123456789abcdefghi",

...

"verificationMethod": [{
    "id": "did:example:123#_Qq0UL2Fq651Q0Fjd6TvnYE-faHiOpRlPVQcY_-tA4A",
    "type": "JsonWebKey2020",

// external (property value)

"controller": "did:example:123",
    "publicKeyJwk": {
      "crv": "Ed25519",

// external (property name)

"x": "VCpo2LMLhn6iWku8MKvSLg2ZAoC-nlOyPVQaO3FxVeQ",

// external (property name)

"kty": "OKP",

// external (property name)

"kid": "_Qq0UL2Fq651Q0Fjd6TvnYE-faHiOpRlPVQcY_-tA4A"

// external (property name)

}
  }, {
    "id": "did:example:123456789abcdefghi#keys-1",
    "type": "Ed25519VerificationKey2020",

// external (property value)

"controller": "did:example:pqrstuvwxyz0987654321",
    "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
  }],

...

}

We'll translate comments accordingly.

Now next section: "5.2.2 Referring to Verification Methods". Translate: "5.2.2 引用验证方法". Then the paragraph:

"Verification methods can be embedded in or referenced from properties associated with various verification relationships as described in 5.3 Verification Relationships. Referencing verification methods allows them to be used by more than one verification relationship."

Translation: "验证方法可以嵌入到或从与各种验证关系关联的属性中引用，如 5.3 验证关系 中所述。引用验证方法使得它们可以被多个验证关系使用。"

Paragraph: "If the value of a verification method property is a map, the verification method has been embedded and its properties can be accessed directly. However, if the value is a URL string, the verification method has been included by reference and its properties will need to be retrieved from elsewhere in the DID document or from another DID document. This is done by dereferencing the URL and searching the resulting resource for a verification method map with an id property whose value matches the URL."

Translation: "如果验证方法属性的值是一个映射，则该验证方法已被嵌入，其属性可以直接访问。但是，如果该值是 URL 字符串，则该验证方法已被引用，其属性需要从 DID 文档的其他位置或从另一个 DID 文档中检索。这是通过解引用 URL 并在得到的资源中查找 id 属性值匹配该 URL 的验证方法映射来实现的。"

Then "Example 14: Embedding and referencing verification methods". Translate: "示例 14：嵌入和引用验证方法". Provide JSON code with comments translated.

The JSON:

{
  ...

"authentication": [
    // this key is referenced and might be used by
    // more than one verification relationship
    "did:example:123456789abcdefghi#keys-1",

    // this key is embedded and may *only* be used for authentication
    {
      "id": "did:example:123456789abcdefghi#keys-2",
      "type": "Ed25519VerificationKey2020",

// external (property value)

"controller": "did:example:123456789abcdefghi",
      "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
    }
  ],

...

}

We need to translate comments: // this key is referenced... => // 此密钥被引用，可能被多个验证关系使用； // this key is embedded... => // 此密钥已嵌入，仅可用于认证； // external (property value) => // 外部（属性值）.

Now next section: "5.3 Verification Relationships". Translate: "5.3 验证关系". Then paragraphs:

"A verification relationship expresses the relationship between the DID subject and a verification method. Different verification relationships enable the associated verification methods to be used for different purposes. It is up to a verifier to ascertain the validity of a verification attempt by checking that the verification method used is contained in the appropriate verification relationship property of the DID Document."

Translation: "验证关系表示 DID 主体与验证方法之间的关系。不同的验证关系使得关联的验证方法可以用于不同目的。验证者负责通过检查所使用的验证方法是否位于 DID 文档中相应的验证关系属性中，来确认验证尝试的有效性。"

Paragraph: "The verification relationship between the DID subject and the verification method is explicit in the DID document. Verification methods that are not associated with a particular verification relationship cannot be used for that verification relationship. For example, a verification method in the value of the authentication property cannot be used to engage in key agreement protocols with the DID subject — the value of the keyAgreement property needs to be used for that."

Translation: "验证关系在 DID 文档中明确表达。未与特定验证关系关联的验证方法不能用于该验证关系。例如，authentication 属性值中的验证方法不能用于与 DID 主体进行密钥协商协议——必须使用 keyAgreement 属性的值。"

Paragraph: "The DID document does not express revoked keys using a verification relationship. If a referenced verification method is not in the latest DID Document used to dereference it, then that verification method is considered invalid or revoked. Each DID method specification is expected to detail how revocation is performed and tracked."

Translation: "DID 文档不使用验证关系来表达已撤销的密钥。如果所引用的验证方法不在用于解引用的最新 DID 文档中，则该验证方法被视为无效或已撤销。每个 DID 方法规范预计会详细说明如何执行和跟踪撤销。"

Paragraph: "The following sections define several useful verification relationships. A DID document MAY include any of these, or other properties, to express a specific verification relationship. In order to maximize global interoperability, any such properties used SHOULD be registered in the DID Specification Registries [DID-SPEC-REGISTRIES]."

Translation: "以下章节定义了几种有用的验证关系。DID 文档可以包含这些属性中的任意一个或其他属性，以表达特定的验证关系。为最大程度提高全球互操作性，所使用的此类属性应当注册到 DID 规范注册表 [DID-SPEC-REGISTRIES]。"

Now "5.3.1 Authentication". Translate: "5.3.1 认证". Paragraph: "The authentication verification relationship is used to specify how the DID subject is expected to be authenticated, for purposes such as logging into a website or engaging in any sort of challenge-response protocol."

Translation: "authentication 验证关系用于指定 DID 主体预期的身份验证方式，例如登录网站或参与任何挑战-响应协议。"

Paragraph: "authentication The authentication property is OPTIONAL. If present, the associated value MUST be a set of one or more verification methods. Each verification method MAY be embedded or referenced."

Translate: "authentication 属性是 OPTIONAL。如果存在，关联的值 MUST 为一个包含一个或多个验证方法的集合。每个验证方法可以嵌入或引用。"

Paragraph: "Example 15: Authentication property containing three verification methods". Translate: "示例 15：包含三个验证方法的 authentication 属性". Provide code? Actually there is no code block for Example 15 in the given text; maybe they omitted. In the original, it says "Example 15: Authentication property containing three verification methods". We can just translate that line. The passage ends after "Example 15: Authentication property containing three verification methods". So we can leave that as a line.

Thus overall translation is ready.

Now format: The user wants translation to Chinese. Provide the Chinese translation with headings and code blocks. Possibly we can include the original headings and sections numbers. We'll keep "5.2.1 验证材料", "5.2.2 引用验证方法", "5.3 验证关系", "5.3.1 认证". Ensure technical terms accurate. Use uppercase normative terms. Ensure code comments in Chinese.

Now produce final answer. We'll wrap JSON in proper formatting.

We need to be careful about indentation. Provide Chinese translation for all paragraphs. Keep the JSON code unchanged except

The user wants translation to Chinese, keep technical terms accurate. The text is from a W3C DID spec. They provide a large chunk of JSON and explanatory text about verification relationships: authentication, assertion, key agreement, capability invocation, and capability delegation. They want a Chinese translation, preserving technical terms.

The translation must be accurate and maintain terminology consistency. The JSON includes "@context", "id", "authentication", etc. Chinese translations: "身份验证" for authentication, "断言方法" for assertionMethod, "密钥协商" for keyAgreement, "能力调用" for capabilityInvocation, "能力委托" for capabilityDelegation. But need to preserve original terms? In Chinese spec, these are often kept as English words in Chinese translations: "authentication" might remain "authentication" in Chinese contexts, but generally translation includes Chinese equivalents. For technical documents, it's often recommended to translate to Chinese while preserving the English terms in parentheses for clarity. The instruction says "keep technical terms accurate". So we need to keep the technical terms accurate. I think we should keep the English terms (e.g., DID, DID Document, verification method) unchanged, but translate explanatory text to Chinese. For JSON, the keys remain same; but the comments can be translated.

The JSON also includes comments (// comments). We need to translate the comments to Chinese, but preserve the code syntax.

Thus, we should produce the Chinese translation of the narrative paragraphs and the comments in JSON, while leaving the code lines unchanged (including key names and values). For the comments (which are not part of JSON but text in this sample), we translate them to Chinese. The JSON properties like "authentication", "assertionMethod", "keyAgreement", "capabilityInvocation", "capabilityDelegation" remain as keys.

The user gave a huge chunk. The final piece stops in the middle of 5.3.5 Capability Delegation (text cut off). The instruction: "Translate to Chinese, keep technical terms accurate". So we need to translate all provided text. Let's go through each part.

First block: JSON with authentication. The JSON code includes comments in // style. We'll translate comments.

We need to handle the ellipsis "..." placeholders. They can remain as "..." or translate as "...".

We need to handle the code indentation: we will preserve JSON formatting. The comments after // need to be Chinese. For each comment line, translate the English explanation into Chinese. For example:

// this method can be used to authenticate as did:...fghi => // 此方法可用于以 did:...fghi 进行身份验证

// this method is *only* approved for authentication, it may not

// be used for any other proof purpose, so its full description is

// embedded here rather than using only a reference => // 此方法*仅*被批准用于身份验证，不能用于其他证明目的，因此其完整描述在此嵌入，而不是仅使用引用

Then the JSON block for authentication keys.

The next block after the JSON is explanation paragraphs. Need to translate to Chinese.

Key points:

- Use Chinese punctuation? Usually Chinese uses full-width punctuation: "。" "，" etc.

- Keep technical terms like DID, DID Document, verification method, public key, etc. Should we keep English or Chinese? Usually we keep the English term in brackets.

We'll produce the translation.

We need to be careful with context: The Chinese translation of "authentication" is "身份验证", "assertionMethod" maybe "断言方法", "keyAgreement" maybe "密钥协商", "capabilityInvocation" maybe "能力调用", "capabilityDelegation" maybe "能力委托". But these are technical property names that remain unchanged in JSON. The Chinese text will refer to them accordingly.

We'll produce translation for each section: 5.3.1 Authentication, 5.3.2 Assertion, 5.3.3 Key Agreement, 5.3.4 Capability Invocation, 5.3.5 Capability Delegation (the snippet cut off, but we translate what's present).

We also need to translate the headings: "5.3.1 Authentication", "5.3.2 Assertion", etc. Should we keep them as English headings? Usually they are headings in spec; we can translate the text after them.

Now, the JSON examples for each section. Let's process each one.

First JSON example for authentication:

{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:example:123456789abcdefghi",

...

"authentication": [

// this method can be used to authenticate as did:...fghi

"did:example:123456789abcdefghi#keys-1",

// this method is *only* approved for authentication, it may not

// be used for any other proof purpose, so its full description is

// embedded here rather than using only a reference

{
      "id": "did:example:123456789abcdefghi#keys-2",
      "type": "Ed25519VerificationKey2020",
      "controller": "did:example:123456789abcdefghi",
      "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
    }
  ],

...

}

We translate comments to Chinese, preserve code.

Now explanation paragraphs: They discuss authentication, what is done after authentication check, etc. We'll translate.

"Note that the verification method indicated by the authentication property of a DID document can only be used to authenticate the DID subject. To authenticate a different DID controller, the entity associated with the value of controller, as defined in 5.1.2 DID Controller, needs to authenticate with its own DID document and associated authentication verification relationship."

Now go to 5.3.2 Assertion section. It defines assertionMethod property.

Now JSON example for assertionMethod: similar to authentication, with comments.

We translate comments.

Now 5.3.3 Key Agreement.

Now JSON example for keyAgreement.

Now 5.3.4 Capability Invocation.

Now JSON example.

Now 5.3.5 Capability Delegation. The user text ends with "5.3.5 Capability Delegation". We need to translate the heading and any explanation if present. The snippet cuts after "The". The next line is "The". It seems the next part would be the description. But it's cut off. The user didn't provide the rest. We can include the heading and maybe a placeholder for missing description: "（待补充）". But we can just provide translation for what we have: the heading "5.3.5 Capability Delegation". Possibly a short translation: "5.3.5 能力委托". Then maybe a placeholder for the description. But the instruction is to translate the given text. So we can translate heading only, and if there is any partial text after heading, we translate that.

Let's check the text: At the end: "5.3.5 Capability Delegation

The". There's no further content. So just heading.

Thus we produce translation for that heading: "5.3.5 能力委托". Possibly a newline.

Now, let's produce final output: The JSON sections with Chinese comments, the narrative sections in Chinese. Ensure we keep the code as is except comments.

Potential pitfalls: The code includes line breaks and indentation. We'll preserve them. We'll need to ensure we escape line breaks correctly? The output is plain text. We'll produce it as code block maybe. The user didn't specify format. We'll output as plain text.

We need to handle the placeholder "...". The ellipsis likely means omitted parts. We can keep them as "...". The comments referencing them may need translation: "此方法可用于以 did:...fghi 进行身份验证". But the comment includes "did:...fghi". We'll keep as is. So the comment will be: // 此方法可用于以 did:...fghi 进行身份验证

Now translation of paragraphs:

First paragraph after authentication JSON:

"If authentication is established, it is up to the DID method or other application to decide what to do with that information. A particular DID method could decide that authenticating as a DID controller is sufficient to, for example, update or delete the DID document. Another DID method could require different keys, or a different verification method entirely, to be presented in order to update or delete the DID document than that used to authenticate. In other words, what is done after the authentication check is out of scope for the data model; DID methods and applications are expected to define this themselves."

We translate to Chinese: "一旦身份验证建立，后续如何处理该信息取决于 DID 方法或其他应用程序。某个 DID 方法可以决定，作为 DID 控制器进行身份验证足以（例如）更新或删除 DID 文档。另一个 DID 方法可能要求使用不同的密钥，或者完全不同的验证方法来更新或删除 DID 文档，而不是用于身份验证的密钥。换言之，身份验证检查之后的行为不在数据模型的范围内；DID 方法和应用程序需要自行定义。"

Now next paragraph:

"This is useful to any authentication verifier that needs to check to see if an entity that is attempting to authenticate is, in fact, presenting a valid proof of authentication. When a verifier receives some data (in some protocol-specific format) that contains a proof that was made for the purpose of "authentication", and that says that an entity is identified by the DID, then that verifier checks to ensure that the proof can be verified using a verification method (e.g., public key) listed under authentication in the DID Document."

Translate: "这对于任何需要检查尝试进行身份验证的实体是否确实提供了有效身份验证证明的身份验证验证者都非常有用。当验证者收到包含为“身份验证”目的而生成的证明的某些数据（采用特定协议的格式）时，该证明表明某个实体由 DID 标识，此时验证者会检查该证明是否能够使用 DID 文档中列在 authentication 下的验证方法（如公钥）进行验证。"

Now note paragraph:

"Note that the verification method indicated by the authentication property of a DID document can only be used to authenticate the DID subject. To authenticate a different DID controller, the entity associated with the value of controller, as defined in 5.1.2 DID Controller, needs to authenticate with its own DID document and associated authentication verification relationship."

Translate: "请注意，DID 文档的 authentication 属性所指示的验证方法只能用于身份验证 DID 主体。若要身份验证其他 DID 控制器，需要由 controller 值所关联的实体（如 5.1.2 DID 控制器中所定义）使用其自己的 DID 文档以及相应的 authentication 验证关系进行身份验证。"

Now heading "5.3.2 Assertion".

We'll translate heading to Chinese: "5.3.2 断言".

Now paragraph: "The assertionMethod verification relationship is used to specify how the DID subject is expected to express claims, such as for the purposes of issuing a Verifiable Credential [VC-DATA-MODEL]."

Translate: "assertionMethod 验证关系用于指定 DID 主体如何表达声明，例如用于签发可验证凭证 [VC-DATA-MODEL]。"

Now property description: "The assertionMethod property is OPTIONAL. If present, the associated value MUST be a set of one or more verification methods. Each verification method MAY be embedded or referenced."

Translate: "assertionMethod 属性是可选的。如果存在，其关联值必须是一个包含一个或多个验证方法的集合。每个验证方法可以是嵌入的或引用的。"

Now paragraph: "This property is useful, for example, during the processing of a verifiable credential by a verifier. During verification, a verifier checks to see if a verifiable credential contains a proof created by the DID subject by checking that the verification method used to assert the proof is associated with the assertionMethod property in the corresponding DID document."

Translate: "此属性在验证者处理可验证凭证时非常有用。在验证过程中，验证者检查可验证凭证是否包含由 DID 主体创建的证明，具体做法是检查用于断言该证明的验证方法是否与相应 DID 文档中的 assertionMethod 属性关联。"

Now JSON example with comments.

We'll translate comments:

// this method can be used to assert statements as did:...fghi => // 此方法可用于以 did:...fghi 断言语句

// this method is *only* approved for assertion of statements, it is not

// used for any other verification relationship, so its full description is

// embedded here rather than using a reference => // 此方法*仅*被批准用于断言语句，不能用于其他验证关系，因此其完整描述在此嵌入，而不是使用引用

Now "5.3.3 Key Agreement".

Translate heading: "5.3.3 密钥协商".

Now paragraph: "The keyAgreement verification relationship is used to specify how an entity can generate encryption material in order to transmit confidential information intended for the DID subject, such as for the purposes of establishing a secure communication channel with the recipient."

Translate: "keyAgreement 验证关系用于指定实体如何生成加密材料，以便传输仅供 DID 主体使用的机密信息，例如用于与接收方建立安全通信通道。"

Now property description: "The keyAgreement property is OPTIONAL. If present, the associated value MUST be a set of one or more verification methods. Each verification method MAY be embedded or referenced."

Translate: "keyAgreement 属性是可选的。如果存在，其关联值必须是一个包含一个或多个验证方法的集合。每个验证方法可以是嵌入的或引用的。"

Now paragraph: "An example of when this property is useful is when encrypting a message intended for the DID subject. In this case, the counterparty uses the cryptographic public key information in the verification method to wrap a decryption key for the recipient."

Translate: "一个使用此属性的示例是在加密发送给 DID 主体的消息时。此时，对方使用验证方法中的加密公钥信息来包装接收者的解密密钥。"

Now JSON example with comments.

Translate comments:

// this method can be used to perform key agreement as did:...fghi => // 此方法可用于以 did:...fghi 执行密钥协商

// this method is *only* approved for key agreement usage, it will not

// be used for any other verification relationship, so its full description is

// embedded here rather than using only a reference => // 此方法*仅*被批准用于密钥协商，不能用于其他验证关系，因此其完整描述在此嵌入，而不是仅使用引用

Now heading "5.3.4 Capability Invocation".

Translate heading: "5.3.4 能力调用".

Now paragraph: "The capabilityInvocation verification relationship is used to specify a verification method that might be used by the DID subject to invoke a cryptographic capability, such as the authorization to update the DID Document."

Translate: "capabilityInvocation 验证关系用于指定 DID 主体可能用来调用加密能力的验证方法，例如用于更新 DID 文档的授权。"

Now property description: "The capabilityInvocation property is OPTIONAL. If present, the associated value MUST be a set of one or more verification methods. Each verification method MAY be embedded or referenced."

Translate: "capabilityInvocation 属性是可选的。如果存在，其关联值必须是一个包含一个或多个验证方法的集合。每个验证方法可以是嵌入的或引用的。"

Now paragraph: "An example of when this property is useful is when a DID subject needs to access a protected HTTP API that requires authorization in order to use it. In order to authorize when using the HTTP API, the DID subject uses a capability that is associated with a particular URL that is exposed via the HTTP API. The invocation of the capability could be expressed in a number of ways, e.g., as a digitally signed message that is placed into the HTTP Headers."

Translate: "一个使用此属性的示例是当 DID 主体需要访问需要授权的受保护 HTTP API 时。为了在使用 HTTP API 时进行授权，DID 主体使用与通过 HTTP API 公开的特定 URL 关联的能力。该能力的调用可以以多种方式表达，例如作为放入 HTTP Header 的数字签名消息。"

Now paragraph: "The server providing the HTTP API is the verifier of the capability and it would need to verify that the verification method referred to by the invoked capability exists in the capabilityInvocation property of the DID document. The verifier would also check to make sure that the action being performed is valid and the capability is appropriate for the resource being accessed. If the verification is successful, the server has cryptographically determined that the invoker is authorized to access the protected resource."

Translate: "提供 HTTP API 的服务器是该能力的验证者，它需要验证被调用能力所引用的验证方法是否存在于 DID 文档的 capabilityInvocation 属性中。验证者还会检查所执行的操作是否有效以及该能力是否适用于被访问的资源。如果验证成功，服务器在加密学上确定调用者已获得访问受保护资源的授权。"

Now JSON example with comments.

Translate comments:

// this method can be used to invoke capabilities as did:...fghi => // 此方法可用于以 did:...fghi 调用能力

// this method is *only* approved for capability invocation usage, it will not

// be used for any other verification relationship, so its full description is

// embedded here rather than using only a reference => // 此方法*仅*被批准用于能力调用，不能用于其他验证关系，因此其完整描述在此嵌入，而不是仅使用引用

Now heading "5.3.5 Capability Delegation".

Translate heading: "5.3.5 能力委托".

If there is any paragraph after heading, we would translate, but it's cut. We'll just include heading.

Now final output should include all translations. We need to keep code sections exactly as original except comments. Let's be careful about indentation and formatting. Use triple backticks for code blocks? The user didn't ask to wrap anything, but we can present the JSON examples in code blocks, with comments in Chinese. The narrative paragraphs can be plain text. Possibly separate sections.

We need to ensure that comments in JSON are not inside string values; they are separate lines. That's fine.

One nuance: In JSON, the key names remain unchanged. The comments after // are not part of JSON but in the example text. We'll keep them.

Now also need to translate "Example 16 : Assertion method property containing two verification methods". The user wrote "Example 16 : Assertion method property containing two verification methods". We'll translate it: "示例 16：断言方法属性包含两个验证方法". Similarly "Example 17 : Key agreement property containing two verification methods" => "示例 17：密钥协商属性包含两个验证方法". And "Example 18 : Capability invocation property containing two verification methods" => "示例 18：能力调用属性包含两个验证方法".

Now we need to translate "Example 16" may be part of the narrative, but it's preceded by "Example". We'll translate accordingly.

Now ensure we maintain the numbering: The heading numbers remain as they are, but the Chinese translation may add Chinese characters. For instance "5.3.1 Authentication" => "5.3.1 身份验证". Keep "5.3.1" unchanged.

Now we need to ensure we include all content. Let's go step by step.

Will produce final output.

We should separate sections clearly.

Potential translation choices:

- "DID method": "DID 方法"

- "DID Document": "DID 文档"

- "verification method": "验证方法"

- "public key": "公钥"

- "controller": "控制器"

- "authentication": "身份验证"

- "assertionMethod": "断言方法"

- "keyAgreement": "密钥协商"

- "capabilityInvocation": "能力调用"

- "capabilityDelegation": "能力委托

# 中文翻译

**能力委托（capabilityDelegation）**

验证关系用于指定一种机制，DID主体可能使用该机制将加密能力委托给另一方，例如将访问特定HTTP API的权限委托给下属。

**capabilityDelegation** 属性是**可选的（OPTIONAL）**。如果存在，关联值**必须（MUST）**是一个包含一个或多个**验证方法**的**集合**。每个**验证方法**可以是**内嵌的**或**引用的**。

此属性有用的一个示例场景是：当DID控制器选择将访问受保护HTTP API的能力委托给自身以外的另一方。为了委托该能力，DID主体将使用与**capabilityDelegation**验证关系关联的**验证方法**，以加密方式将能力签署给另一个DID主体。然后，代理人将以类似于5.3.4节**能力调用（Capability Invocation）**中描述的示例方式使用该能力。

**示例19：包含两个验证方法的能力委托属性**

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:example:123456789abcdefghi",

...

"capabilityDelegation": [

// 此方法可用于执行能力委托，如 did:...fghi

"did:example:123456789abcdefghi#keys-1",

// 此方法*仅*被批准用于授予能力；它不会用于任何其他验证关系，
// 因此此处完整描述该方法，而不是仅使用引用

{
    "id": "did:example:123456789abcdefghi#keys-2",
    "type": "Ed25519VerificationKey2020",

// 外部（属性值）

"controller": "did:example:123456789abcdefghi",
    "publicKeyMultibase": "zH3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
    }
  ],

...

}
```

---

**5.4 服务（Services）**

服务用于在DID文档中表达与DID主体或相关实体通信的方式。服务可以是DID主体希望广告的任何类型的服务，包括用于进一步发现、身份认证、授权或交互的去中心化身份管理服务。

出于隐私考虑，不鼓励通过服务公开披露社交媒体账户、个人网站和电子邮件地址等公共信息。更多关于隐私问题的探讨可参见10.1节**保护个人数据隐私**和10.6节**服务隐私**。与服务关联的信息通常是特定于服务的。例如，与加密消息服务关联的信息可以表达在消息开始之前如何建立加密链接。

服务使用**service**属性表达，具体描述如下：

---

**service（服务）属性**

**service**属性是**可选的（OPTIONAL）**。如果存在，关联值**必须（MUST）**是一个**服务集合**，其中每个服务由一个**映射（map）**描述。每个**服务映射**必须包含**id**、**type**和**serviceEndpoint**属性。每个服务扩展**可以（MAY）**包含额外属性，并**可以（MAY）**进一步限制与该扩展关联的属性。

**id**

**id**属性的值**必须（MUST）**是符合[RFC3986]的**URI**。**符合规范的生产者**不得（MUST NOT）生成具有相同id的多个服务条目。**符合规范的消费者**必须（MUST）在检测到具有相同id的多个服务条目时产生错误。

**type**

**type**属性的值**必须（MUST）**是一个**字符串**或一个**字符串集合**。为了最大化互操作性，服务类型及其关联属性**应当（SHOULD）**在DID规范注册表[DID-SPEC-REGISTRIES]中注册。

**serviceEndpoint**

**serviceEndpoint**属性的值**必须（MUST）**是一个**字符串**、一个**映射**，或由一个或多个**字符串**和/或**映射**组成的**集合**。所有**字符串**值**必须（MUST）**是符合[RFC3986]的有效**URI**，并根据RFC3986的**规范化与比较规则**以及其适用**URI**方案规范中的任何规范化规则进行规范化。

有关与服务相关的隐私和安全注意事项的更多信息，请参见10.6节**服务隐私**、10.1节**保护个人数据隐私**、10.3节**DID文档关联风险**以及9.3节**身份认证服务端点**。

**示例20：service属性的使用**

```json
{
  "service": [{
    "id":"did:example:123#linked-domain",
    "type": "LinkedDomains",

// 外部（属性值）

"serviceEndpoint": "https://bar.example.com"
  }]
}
```

---

**6. 表示（Representations）**

本规范中DID文档的具体序列化被称为**表示（representation）**。**表示**通过称为**生成（production）**的过程对**数据模型**进行序列化来创建。**表示**通过称为**消费（consumption）**的过程转换为**数据模型**。**生成**和**消费**过程使信息能够从一个**表示**转换到另一个表示。本规范为JSON和JSON-LD定义了**表示**，开发者可以使用任何其他能够表达**数据模型**的**表示**，如XML或YAML。以下各节定义了**生成**和**消费**的一般规则，以及JSON和JSON-LD的**表示**。

---

**6.1 生成与消费**

除了本规范中定义的**表示**外，实现者可以使用其他**表示**，前提是每个这样的**表示**都被正确指定（包括对DID规范注册表[DID-SPEC-REGISTRIES]中未列出的属性的可互操作处理规则）。更多信息请参见4.1节**可扩展性**。

所有**表示**的要求如下：

1. **表示**必须为第4节**数据模型**中指定的所有数据类型定义确定性的生成和消费规则。

2. **表示**必须与一个IANA注册的媒体类型唯一关联。

3. **表示**必须为其媒体类型定义符合第**片段（Fragment）**节中定义的片段处理规则的片段处理规则。

4. **表示**应当使用**数据模型**数据类型的词法表示。例如，JSON和JSON-LD使用XML Schema的dateTime词法序列化来表示**日期时间**。**表示**可以选择使用不同的词法序列化来序列化**数据模型**数据类型，只要**消费**过程回到**数据模型**是无损的即可。例如，某些基于CBOR的**表示**使用整数来表示自Unix纪元以来的秒数来表示**日期时间**值。

5. **表示**可以定义存储在**表示特定条目映射**中供**生成**和**消费**过程使用的**表示特定条目**。这些条目在消费或生成时用于帮助确保无损转换。

6. 为了最大化互操作性，**表示**规范作者**应当（SHOULD）**在DID规范注册表[DID-SPEC-REGISTRIES]中注册其**表示**。

所有**符合规范的生产者**的要求如下：

1. **符合规范的生产者**必须将**DID文档数据模型**和**表示特定条目映射**作为**生成**过程的输入。**符合规范的生产者****可以（MAY）**接受额外选项作为**生成**过程的输入。

2. **符合规范的生产者**必须序列化**DID文档数据模型**和**表示特定条目映射**中所有没有针对正在生成的**表示**的显式处理规则的条目，仅使用**表示**的数据类型处理规则，并在**生成**过程完成后返回序列化结果。

3. **符合规范的生产者**必须在**生成**过程完成后返回与**表示**关联的媒体类型字符串。

**符合规范的生产者**...

# 中文翻译

**禁止**

产生

不符合规范的

DID

或

DID

文档

。

所有

一致性消费者

的要求如下：

一个

一致性消费者

**必须**

将

一个表示

和

媒体类型

字符串

作为

消费

过程的输入。一个

一致性消费者

**可以**

接受

附加选项作为

消费

过程的输入。

一个

一致性消费者

**必须**

使用媒体类型输入字符串来确定

DID文档

的

表示

。

一个

一致性消费者

**必须**

检测所有已知

表示

中的

表示特定条目

，并将该条目放入

表示特定条目映射

中，该映射在

消费

过程完成后返回。所有已知

表示特定条目

的列表可在DID规范注册表 [

DID-SPEC-REGISTRIES

] 中获取。

一个

一致性消费者

**必须**

将所有

非表示特定条目

（对于正在被消费的

表示

没有显式处理规则的条目）仅使用该

表示

的数据类型处理规则添加到

DID文档

数据模型

中，并在

消费

过程完成后返回

DID文档

数据模型

。

一个

一致性消费者

**必须**

在消费不符合规范的

DID

或

DID文档

时产生错误。

**图4**

表示的生产和消费。另请参阅：

叙述性描述

。

图表的左上象限包含一个带灰色虚线轮廓的矩形，其中包含两个蓝色轮廓矩形，上下排列。上方的较大矩形用蓝色标注为"核心属性"，包含以下

INFRA

表示法：

«[

"id"

→

"example:123"

,

"verificationMethod"

→ « «[

"id"

:

"did:example:123#keys-1"

,

"controller"

:

"did:example:123"

,

"type"

:

"Ed25519VerificationKey2018"

,

"publicKeyBase58"

:

"H3C2AVvLMv6gmMNam3uVA"

]» »,

"authentication"

→ «

"did:example:123#keys-1"

»
]»

下方较小的矩形用蓝色标注为"核心表示特定条目 (JSON-LD)"，包含以下等宽

INFRA

表示法：

«

[

"@context"

→

"https://www.w3.org/ns/did/v1"

]

»

从灰色轮廓矩形延伸出三对箭头，分别指向三个黑色轮廓矩形：一个在图表的右上方，一个在右下方，一个在左下方。每一对箭头包括一条从灰色轮廓矩形指向相应黑色轮廓矩形的蓝色箭头，标注为"produce（生产）"，以及一条方向相反的红色箭头，标注为"consume（消费）"。右上方的黑色轮廓矩形标注为"application/did+cbor"，包含十六进制数据。左下方的矩形标注为"application/did+json"，包含以下JSON数据：

{
  "id": "did:example:123",
  "verificationMethod": [{
    "id": "did:example:123#keys-1",
    "controller": "did:example:123",
    "type": "Ed25519VerificationKey2018",
    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVA"
  }],
  "authentication": [
    "did:example:123#keys-1"
  ]
}

左下方的矩形标注为"application/did+ld+json"，包含以下JSON-LD数据：

{
  "@context": [
    "https://www.w3.org/ns/did/v1"
  ],
  "id": "did:example:123",
  "verificationMethod": [{
    "id": "did:example:123#keys-1",
    "controller": "did:example:123",
    "type": "Ed25519VerificationKey2018",
    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVA"
  }],
  "authentication": [
    "did:example:123#keys-1"
  ]
}

**注意**

：表示之间的转换

实现应通过使用源表示上的

消费

规则生成

数据模型

，然后使用

生产

规则将

数据模型

序列化为目标表示，或任何其他能产生相同目标表示的机制来完成表示之间的转换。

## 6.2 JSON

本节定义了JSON

表示

的

生产

和

消费

规则。

### 6.2.1 生产

DID文档

、DID文档数据结构以及

表示特定条目映射

**必须**

根据以下

生产

规则序列化为JSON

表示

：

| 数据类型 | JSON表示类型 |
|---------|-------------|
| map | **JSON对象**，其中每个条目被序列化为JSON对象的成员，条目键作为**JSON字符串**成员名，条目值根据其类型（见本表）进行序列化。 |
| list | **JSON数组**，其中列表的每个元素按顺序作为数组的值，根据其类型（见本表）进行序列化。 |
| set | **JSON数组**，其中集合的每个元素按顺序作为数组的值，根据其类型（见本表）进行序列化。 |
| datetime | **JSON字符串**，序列化为**XML日期时间**，归一化为UTC 00:00:00且不带亚秒精度。例如：`2020-12-20T19:17:47Z`。 |
| string | **JSON字符串**。 |
| integer | **JSON数字**，不带小数或分数部分。 |
| double | **JSON数字**，带小数和分数部分。 |
| boolean | **JSON布尔值**。 |
| null | **JSON null字面量**。 |

所有创建生成JSON

表示

的

一致性生产者

的实现者应确保其算法与[

INFRA

]规范中的

JSON序列化规则

以及JSON [

RFC8259

]规范中的

关于数字精度的建议

保持一致。

DID文档

的所有条目**必须**包含在根

JSON对象

中。条目**可以**包含附加的数据子结构，须遵循上表中值的表示规则。在序列化

DID文档

时，

一致性生产者

**必须**指定媒体类型为

application/did+json

，以便向下游应用（如7.1.2节

DID解析元数据

中所述）提供。

**示例21**：JSON表示中的DID文档示例

{
  "id": "did:example:123456789abcdefghi",
  "authentication": [{
    "id": "did:example:123456789abcdefghi#keys-1",
    "type": "Ed25519VerificationKey2018",
    "controller": "did:example:123456789abcdefghi",
    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVAjZpfkcJCwDwnZn6z3wXmqPV"
  }]
}

### 6.2.2 消费

DID文档

和DID文档数据结构的JSON

表示

**必须**

根据以下

消费

规则反序列化为

数据模型

：

| JSON表示类型 | 数据类型 |
|-------------|---------|
| JSON对象 | **map**，其中JSON对象的每个成员作为条目添加到映射中。每个条目键设置为JSON对象成员名。每个条目值通过根据本表定义的JSON表示类型转换JSON对象成员值来设置。由于JSON对象未指定顺序，因此不保证插入顺序。 |
| JSON数组，其中数据模型条目值是**list**或未知类型 | **list**，其中JSON数组的每个值按顺序添加到列表中，根据数组值的JSON表示类型（见本表）进行转换。 |
| JSON数组，其中数据模型条目值是**set** | **set**，其中JSON数组的每个值按顺序添加到集合中，根据数组值的JSON表示类型（见本表）进行转换。 |
| JSON字符串，其中数据模型条目值是**datetime** | **datetime**。 |
| JSON字符串，其中数据模型条目值类型是**string**或未知类型 | **string**。 |
| 不带小数或分数部分的JSON数字 | **integer**。 |
| 带小数和分数部分的JSON数字，或当条目值是**double**（无论是否包含分数部分）时 | **double**。 |
| JSON布尔值 | **boolean**。 |
| JSON null字面量 | **null**值。 |

所有创建消费JSON

表示

的

一致性消费者

的实现者应确保其算法与[

INFRA

]规范中的

JSON转换规则

以及JSON [

RFC8259

]规范中的

关于数字精度的建议

保持一致。

如果媒体类型信息对符合规范的消费者可用，且媒体类型值为 application/did+json，则正在消费的数据结构为 DID 文档，且根元素必须是 JSON 对象，其中该对象的所有成员均为 DID 文档的条目。对于消费 JSON 表示形式且正在消费根元素不是 JSON 对象的 DID 文档的符合规范消费者，必须报告错误。

6.3 JSON-LD

JSON-LD [JSON-LD11] 是一种基于 JSON 的格式，用于序列化链接数据。本节定义了 JSON-LD 表示形式的生成和消费规则。

JSON-LD 表示形式定义了以下表示特定条目：

@context

JSON-LD Context 是字符串或列表，包含字符串和/或有序映射的任意组合。

6.3.1 生成

DID 文档、DID 文档数据结构以及表示特定条目必须根据 6.2 JSON 中定义的 JSON 表示形式生成规则序列化为 JSON-LD 表示形式。

除了使用 JSON 表示形式生成规则外，JSON-LD 生成必须包含表示特定条目 @context。@context 的序列化值必须是 JSON 字符串 https://www.w3.org/ns/did/v1，或者是 JSON 数组，其中第一项是 JSON 字符串 https://www.w3.org/ns/did/v1，后续项根据 JSON 表示形式生成规则进行序列化。

示例 22：简单 @context 条目的有效序列化

{
  "@context": "https://www.w3.org/ns/did/v1",
  ...
}

示例 23：分层 @context 条目的有效序列化

{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://did-method-extension.example/v1"
  ],
  ...
}

所有创建生成 JSON-LD 表示形式的符合规范生产者的实现者，建议确保其算法生成有效的 JSON-LD [JSON-LD11] 文档。无效的 JSON-LD 文档将导致 JSON-LD 处理器停止并报告错误。

为了实现不同表示形式之间的互操作性，所有 JSON-LD Context 及其术语都应当在 DID 规范注册表 [DID-SPEC-REGISTRIES] 中注册。

生成 JSON-LD 表示形式的符合规范生产者不应生成包含未通过 @context 定义的术语的 DID 文档，因为符合规范消费者预期会移除未知术语。在序列化 DID 文档的 JSON-LD 表示形式时，符合规范生产者必须指定媒体类型为 application/did+ld+json，以供下游应用程序使用，如 7.1.2 DID 解析元数据中所述。

6.3.2 消费

DID 文档以及 JSON-LD 表示形式表示的任何 DID 文档数据结构必须根据 6.2 JSON 中定义的 JSON 表示形式消费规则反序列化为数据模型。

所有创建消费 JSON-LD 表示形式的符合规范消费者的实现者，建议确保其算法仅接受有效的 JSON-LD [JSON-LD11] 文档。无效的 JSON-LD 文档将导致 JSON-LD 处理器停止并报告错误。

处理 JSON-LD 表示形式的符合规范消费者应当丢弃 DID 文档中所有未通过 @context 定义的术语。

7. 解析

本节定义了 DID 解析和 DID URL 解引用的输入和输出。其确切实现不在本规范的范围内，但一些实现者注意事项在 [DID-RESOLUTION] 中讨论。

所有符合规范的 DID 解析器必须实现至少一个 DID 方法的 DID 解析功能，并且必须能够以至少一种符合规范的表示形式返回 DID 文档。

7.1 DID 解析

DID 解析函数通过使用适用 DID 方法的"读取"操作（参见 8.2 方法操作）将 DID 解析为 DID 文档。此过程如何完成的详细信息不在本规范范围内，但所有符合规范的 DID 解析器都实现以下函数，这些函数具有以下抽象形式：

resolve(did, resolutionOptions) →
   « didResolutionMetadata, didDocument, didDocumentMetadata »

resolveRepresentation(did, resolutionOptions) →
   « didResolutionMetadata, didDocumentStream, didDocumentMetadata »

resolve 函数以抽象形式（映射）返回 DID 文档。resolveRepresentation 函数返回以相应表示形式格式化的 DID 文档字节流。

图 5 函数 resolve() 和 resolveRepresentation()。另请参阅：叙述性描述。

该图的上中部分包含一个带灰色虚线轮廓的矩形，其中包含两个蓝色轮廓的矩形，一个在上，一个在下。上面较大的矩形用蓝色标注为"核心属性"，包含以下 INFRA 表示法：

«[
  "id" → "example:123",
  "verificationMethod" → « «[
    "id": "did:example:123#keys-1",
    "controller": "did:example:123",
    "type": "Ed25519VerificationKey2018",
    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVA"
  ]» »,
  "authentication" → « "did:example:123#keys-1" »
]»

下面较小的矩形用蓝色标注为"核心表示特定条目（JSON-LD）"，包含以下等宽 INFRA 表示法：

«[
  "@context" → "https://www.w3.org/ns/did/v1"
]»

从灰色轮廓矩形延伸出三对箭头，指向底部并排水平排列的三个黑色轮廓矩形。每一对箭头包括一条蓝色箭头，从灰色轮廓矩形指向相应的黑色轮廓矩形，标注为"produce"，以及一条红色箭头沿相反方向延伸，标注为"consume"。该行中第一个黑色轮廓矩形标注为"application/did+ld+json"，包含以下 JSON-LD 数据：

{
  "@context": ["https://www.w3.org/ns/did/v1"],
  "id": "did:example:123",
  "verificationMethod": [{
    "id": "did:example:123#keys-1",
    "controller": "did:example:123",
    "type": "Ed25519VerificationKey2018",
    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVA"
  }],
  "authentication": ["did:example:123#keys-1"]
}

该行中第二个矩形标注为"application/did+json"，包含以下 JSON 数据：

{
  "id": "did:example:123",
  "verificationMethod": [{
    "id": "did:example:123#keys-1",
    "controller": "did:example:123",
    "type": "Ed25519VerificationKey2018",
    "publicKeyBase58": "H3C2AVvLMv6gmMNam3uVA"
  }],
  "authentication": ["did:example:123#keys-1"]
}

第三个矩形标注为"application/did+cbor"，包含十六进制数据。

在该图的左侧中间，有一个带黑色轮廓和浅灰色背景的框。该框标注为"可验证数据注册表"，包含一个表示带有节点和弧线的图形符号。从该框延伸出一条标注为"resolve()"的箭头，指向上方灰色轮廓矩形所在的上半部分。另一条标注为"resolveRepresentation()"的箭头向下延伸，指向下方三列黑色轮廓矩形所在的下半部分。

resolve 和 resolveRepresentation 函数的输入变量如下：

did

这是要解析的 DID。此输入是必需的，且值必须是 3.1 DID 语法中定义的可符合规范的 DID。

resolutionOptions

# 中文翻译

元数据结构，包含在 7.1.1 "DID 解析选项" 中定义的属性。此输入是**必需**的，但该结构**可以**为空。

这些函数各自返回多个值，对于这些值如何一起返回没有限制。**resolve** 的返回值是 **didResolutionMetadata**、**didDocument** 和 **didDocumentMetadata**。**resolveRepresentation** 的返回值是 **didResolutionMetadata**、**didDocumentStream** 和 **didDocumentMetadata**。这些值的说明如下：

**didResolutionMetadata**

一个由与 **DID 解析** 过程结果相关的值组成的**元数据结构**，这些值通常在调用 **resolve** 和 **resolveRepresentation** 函数之间发生变化，因为它表示的是关于解析过程本身的数据。此结构是**必需**的，且在解析过程发生错误时，此结构**不得**为空。此元数据在 7.1.2 "DID 解析元数据" 中定义。如果调用了 **resolveRepresentation**，则此结构**必须**包含一个 **contentType** 属性，其中包含 **didDocumentStream** 中所找到的表示的媒体类型（Media Type）。如果解析不成功，则此结构**必须**包含一个描述错误的 **error** 属性。

**didDocument**

如果解析成功且调用了 **resolve** 函数，则此值**必须**是第 4 章"数据模型"中所述的 **DID 文档**抽象数据模型（一个 **map**），该模型能够使用表示所指定的生产规则转换为合规的 DID 文档（表示）。解析后的 **DID 文档** 中的 **id** 值**必须**与被解析的 **DID** 相匹配。如果解析不成功，则此值**必须**为空。

**didDocumentStream**

如果解析成功且调用了 **resolveRepresentation** 函数，则此值**必须**是所解析的 **DID 文档** 以某种合规**表示**形式的字节流。然后 **resolveRepresentation** 函数的调用者可以将该字节流解析为**数据模型**，进而进行验证和处理。如果解析不成功，则此值**必须**为空流。

**didDocumentMetadata**

如果解析成功，则此值**必须**是一个**元数据结构**。此结构包含关于 **didDocument** 属性中所含 **DID 文档**的元数据。此元数据通常在调用 **resolve** 和 **resolveRepresentation** 函数之间不会发生变化，除非 **DID 文档**发生了变化，因为它表示的是关于 **DID 文档**的元数据。如果解析不成功，则此输出**必须**是一个空的**元数据结构**。此规范所定义的属性在 7.1.3 "DID 文档元数据" 中。

合规的 **DID 解析器**实现不得以任何方式更改这些函数的签名。

**DID 解析器**实现可以将 **resolve** 和 **resolveRepresentation** 函数映射到特定方法的内部函数以执行实际的 **DID 解析**过程。

**DID 解析器**实现除了此处指定的 **resolve** 和 **resolveRepresentation** 函数外，还可以实现和暴露具有不同签名的其他函数。

## 7.1.1 DID 解析选项

此结构中可能的属性及其可能的值注册在 DID 规范注册表 [DID-SPEC-REGISTRIES] 中。本规范定义以下通用属性。

**accept**

调用者所期望的 **DID 文档****表示**的媒体类型。媒体类型**必须**表示为 **ASCII 字符串**。如果支持并可用，则 **DID 解析器**实现**应该**使用此值来确定返回的 **didDocumentStream** 中所含的**表示**。对于 **resolveRepresentation** 函数，此属性是**可选**的；对于 **resolve** 函数，**不得**使用此属性。

## 7.1.2 DID 解析元数据

此结构中可能的属性及其可能的值注册在 DID 规范注册表 [DID-SPEC-REGISTRIES] 中。本规范定义以下 DID 解析元数据属性：

**contentType**

返回的 **didDocumentStream** 的媒体类型。如果解析成功且调用了 **resolveRepresentation** 函数，则此属性是**必需**的。如果调用了 **resolve** 函数，则**不得**出现此属性。此属性的值**必须**是合规**表示**的媒体类型的 **ASCII 字符串**。**resolveRepresentation** 函数的调用者在确定如何将由此函数返回的 **didDocumentStream** 解析和处理为**数据模型**时，**必须**使用此值。

**error**

解析过程中的错误代码。当解析过程发生错误时，此属性是**必需**的。此属性的值**必须**是单个关键字 **ASCII 字符串**。此字段的可能属性值**应该**注册在 DID 规范注册表 [DID-SPEC-REGISTRIES] 中。本规范定义以下常见错误值：

**invalidDid**

传递给 **DID 解析**函数的 **DID** 不符合有效语法。（参见 3.1 "DID 语法"。）

**notFound**

**DID 解析器**无法找到此次解析请求产生的 **DID 文档**。

**representationNotSupported**

如果通过 **accept** 输入元数据属性请求的**表示**不被 **DID 方法**和/或 **DID 解析器**实现支持，则返回此错误代码。

## 7.1.3 DID 文档元数据

此结构中可能的属性及其可能的值**应该**注册在 DID 规范注册表 [DID-SPEC-REGISTRIES] 中。本规范定义以下常见属性：

**created**

**DID 文档**元数据**应该**包含一个 **created** 属性，以指示**创建操作**的时间戳。此属性的值**必须**是一个格式化为 **XML 日期时间**的字符串，归一化为 UTC 00:00:00 且不带亚秒级小数精度。例如：2020-12-20T19:17:47Z。

**updated**

**DID 文档**元数据**应该**包含一个 **updated** 属性，以指示所解析的文档版本的最后一次**更新操作**的时间戳。此属性的值**必须**遵循与 **created** 属性相同的格式规则。如果从未对 **DID 文档**执行过更新操作，则省略 **updated** 属性。如果存在 **updated** 属性，当两个时间戳之间的差异小于一秒时，它可能与 **created** 属性值相同。

**deactivated**

如果 DID 已被**停用**，则 **DID 文档**元数据**必须**包含此属性，值为布尔值 **true**。如果 DID 未被停用，则此属性是**可选**的，但如果包含，**必须**具有布尔值 **false**。

**nextUpdate**

如果所解析的文档版本不是文档的最新版本，则 **DID 文档**元数据**可以**包含 **nextUpdate** 属性。它指示下一次**更新操作**的时间戳。此属性的值**必须**遵循与 **created** 属性相同的格式规则。

**versionId**

**DID 文档**元数据**应该**包含一个 **versionId** 属性，以指示所解析的文档版本的最后一次**更新操作**的版本。此属性的值**必须**是 **ASCII 字符串**。

**nextVersionId**

如果所解析的文档版本不是文档的最新版本，则 **DID 文档**元数据**可以**包含 **nextVersionId** 属性。它指示下一次**更新操作**的版本。此属性的值**必须**是 **ASCII 字符串**。

**equivalentId**

**DID 方法**可以定义逻辑上等效的 **DID** 的不同形式。一个例子是 **DID** 在可验证数据注册表中注册前和注册后采用不同形式。

**中文翻译（保持技术术语准确）**

以及在注册之后的另一种形式。在这种情况下，DID 方法规范可能需要将一个或多个在逻辑上等同于已解析 DID 的 DID 表示为 DID 文档的属性。这就是 **equivalentId** 属性的目的。

DID 文档元数据 **可能** 包含 **equivalentId** 属性。  
如果存在，其值 **必须** 是 一个集合，其中每个元素都是符合 3.1 节 **DID 语法** 规则的字符串。该关系说明每个 **equivalentId** 值在逻辑上等同于 **id** 属性值，因此指向同一个 **DID 主体**。  

每个 **equivalentId** DID 值 **必须** 由 与 **id** 属性值相同的 **DID 方法** 生成，并且是该方法的一种形式。（例如，`did:example:abc` == `did:example:ABC`）  

符合规范的 **DID 方法** 规范 **必须** 保证每个 **equivalentId** 值在逻辑上等同于 **id** 属性值。  

请求方应保留 **id** 和 **equivalentId** 属性的值，以确保后续对其中任何值的交互都被正确处理为逻辑等效（例如，在数据库中保留所有变体，以便对任何一个值的交互都映射到相同的底层账户）。  

> **注意**：更强的等价性  
> **equivalentId** 是一种比 **alsoKnownAs** 更强的等价形式，因为等价性 **必须** 由所属的 **DID 方法** 保证。  
> **equivalentId** 表示完整的图合并，因为同一个 **DID 文档** 描述了 **equivalentId** DID 和 **id** 属性 DID。  

如果请求方不保留 **id** 和 **equivalentId** 属性的值，也不确保后续对其中任何值的交互都被正确处理为逻辑等效，则可能会出现负面或意外的问题。强烈建议实现者遵守与该元数据属性相关的指令。  

---

### canonicalId

**canonicalId** 属性 与 **equivalentId** 属性相同，不同之处在于：  
a) 它与单个值关联而不是集合，且  
b) 该 DID 被定义为包含它的 **DID 文档** 范围内该 **DID 主体** 的规范 ID。  

DID 文档元数据 **可能** 包含 **canonicalId** 属性。  
如果存在，其值 **必须** 是 符合 3.1 节 **DID 语法** 规则的字符串。该关系说明 **canonicalId** 值在逻辑上等同于 **id** 属性值，且该 **canonicalId** 值由 **DID 方法** 定义为包含它的 **DID 文档** 范围内该 **DID 主体** 的规范 ID。**canonicalId** 值 **必须** 由 与 **id** 属性值相同的 **DID 方法** 生成，并且是该方法的一种形式。（例如，`did:example:abc` == `did:example:ABC`）。  

符合规范的 **DID 方法** 规范 **必须** 保证 **canonicalId** 值在逻辑上等同于 **id** 属性值。  

请求方应使用 **canonicalId** 值作为其对 **DID 主体** 的主要 ID 值，并将所有其他等效值视为次要别名（例如，在其系统中更新相应的主引用，以反映新的规范 ID 指令）。  

> **注意**：规范等价性  
> **canonicalId** 与 **equivalentId** 的等价性声明相同，只是它被限制为单个值，且该值被定义为该 **DID 文档** 范围内该 **DID 主体** 的规范 ID。与 **equivalentId** 一样，**canonicalId** 表示完整的图合并，因为同一个 **DID 文档** 描述了 **canonicalId** DID 和 **id** 属性 DID。  

如果解析方不使用 **canonicalId** 值作为其对 **DID 主体** 的主要 ID 值，也不将所有其他等效值视为次要别名，则可能会出现与用户体验相关的负面或意外问题。强烈建议实现者遵守与该元数据属性相关的指令。  

---

## 7.2 DID URL 解引用  

**DID URL 解引用** 函数将 **DID URL** 解除引用为 **资源**，其内容取决于 **DID URL** 的组成部分，包括 **DID 方法**、方法特定标识符、路径、查询和片段。此过程依赖于对 **DID URL** 中包含的 **DID** 的 **DID 解析**。  

**DID URL 解引用** 可能涉及多个步骤（例如，当被解除引用的 **DID URL** 包含片段时），该函数被定义为在所有步骤完成后返回最终资源。如何完成此过程的细节不在本规范的范围之内。下图描述了上述关系。  

**图 6 – DID URL 解引用概述**  
另见：叙述性描述。  

- 图示左上部分包含一个带黑色轮廓的矩形，标记为 **"DID"**。  
- 图示左下部分包含一个带黑色轮廓的矩形，标记为 **"DID URL"**。该矩形内部有四个较小的黑色轮廓矩形，横向相邻排列，分别标记为 **"DID"**、**"path"**、**"query"** 和 **"fragment"**。  
- 图示右上部分包含一个带黑色轮廓的矩形，标记为 **"DID document"**。该矩形内部有三个较小的黑色轮廓矩形，分别标记为 **"id"**、**"(property X)"** 和 **"(property Y)"**，周围有多组三点（省略号）。一条弯曲的黑色箭头，标记为 **"DID document - relative fragment dereference"**，从标记为 **"(property X)"** 的矩形延伸，指向标记为 **"(property Y)"** 的矩形。  
- 图示右下部分包含一个带黑色轮廓的椭圆形，标记为 **"Resource"**。  

- 一条黑色箭头，标记为 **"resolves to a DID document"**，从左上部分的 **"DID"** 矩形延伸，指向右上部分的 **"DID document"** 矩形。  
- 一条黑色箭头，标记为 **"refers to"**，从右上部分的 **"DID document"** 矩形延伸，指向右下部分的 **"Resource"** 椭圆形。  
- 一条黑色箭头，标记为 **"contains"**，从 **"DID URL"** 矩形内部标记为 **"DID"** 的小矩形延伸，指向左上部分的 **"DID"** 矩形。  
- 一条黑色箭头，标记为 **"dereferences to a DID document"**，从左下部分的 **"DID URL"** 矩形延伸，指向右上部分的 **"DID document"** 矩形。  
- 一条黑色箭头，标记为 **"dereferences to a resource"**，从左下部分的 **"DID URL"** 矩形延伸，指向右下部分的 **"Resource"** 椭圆形。  

所有符合规范的 **DID 解析器** 必须实现以下函数，该函数具有以下抽象形式：

```
dereference(didUrl, dereferenceOptions) → « dereferencingMetadata, contentStream, contentMetadata »
```

**dereference** 函数的输入变量如下：

- **didUrl**  
  一个符合规范的 **DID URL**，作为单个字符串。这是 要解除引用的 **DID URL**。要解除引用 **DID 片段**，必须使用完整的 **DID URL**，包括 **DID 片段**。此输入为 **必需**。  

  > **注意**：DID URL 解引用器模式  
 

# 中文翻译

其自身。本规范定义的属性在

7.2.1

DID URL 解引用选项

中。此输入是

必需的

，但结构

可以

为空。

此函数返回多个值，且对如何一起返回这些值没有限制。

解引用

的返回值包括

dereferencingMetadata

、

contentStream

和

contentMetadata

：

dereferencingMetadata

一个

元数据结构

，包含与

DID URL 解引用

过程结果相关的值。此结构是

必需的

，如果在解引用过程中发生错误，则此结构

不得

为空。本规范定义的属性在

7.2.2

DID URL 解引用元数据

中。如果解引用不成功，此结构

必须

包含一个描述错误的

error

属性。

contentStream

如果

解引用

函数被调用且成功，则此

必须

包含一个对应于

DID URL

的

资源

。

contentStream

可以

是一种

资源

，例如可以以一种符合规范的

表示

方式序列化的

DID 文档

、

验证方法

、

服务

，或任何其他可以通过媒体类型识别并通过解析过程获取的资源格式。如果解引用不成功，此值

必须

为空。

contentMetadata

如果解引用成功，则此

必须

是一个

元数据结构

，但该结构

可以

为空。此结构包含关于

contentStream

的元数据。如果

contentStream

是一个

DID 文档

，则此

必须

是一个如

DID 解析

中所述的

didDocumentMetadata

结构。如果解引用不成功，此输出

必须

是一个空的

元数据结构

。

符合规范的

DID URL 解引用

实现不得以任何方式更改这些函数的签名。

DID URL 解引用

实现可能会将

解引用

函数映射到特定于方法的内部函数以执行实际的

DID URL 解引用

过程。

DID URL 解引用

实现可能除了此处指定的

解引用

函数外，还会实现和暴露具有不同签名的其他函数。

7.2.1 DID URL 解引用选项

此结构中的可能属性及其可能值

应当

在 DID 规范注册表 [

DID-SPEC-REGISTRIES

] 中注册。本规范为解引用选项定义以下常见属性：

accept

调用方为

contentStream

首选的媒体类型。媒体类型

必须

表示为

ASCII 字符串

。

DID URL 解引用

实现

应当

使用此值来确定返回结果中包含的

表示

的

contentType

（如果该

表示

受支持且可用）。

7.2.2 DID URL 解引用元数据

此结构中的可能属性及其可能值在 DID 规范注册表 [

DID-SPEC-REGISTRIES

] 中注册。本规范定义以下常见属性。

contentType

如果解引用成功，则

应当

使用此属性表示返回的

contentStream

的媒体类型。媒体类型值

必须

表示为

ASCII 字符串

。

error

解引用过程中的错误代码。当解引用过程中发生错误时，此属性是

必需的

。此属性的值

必须

是表示为

ASCII 字符串

的单个关键字。此字段的可能属性值

应当

在 DID 规范注册表 [

DID-SPEC-REGISTRIES

] 中注册。本规范定义以下常见错误值：

invalidDidUrl

提供给

DID URL 解引用

函数的

DID URL

不符合有效语法。（参见

3.2 DID URL 语法

。）

notFound

DID URL 解引用器

无法找到此次解引用请求产生的

contentStream

。

7.3 元数据结构

在

DID 解析

、

DID URL 解引用

以及其他与 DID 相关的过程中经常涉及输入和输出元数据。用于传递此元数据的结构

必须

是一个属性

映射

。每个属性名

必须

是一个

字符串

。每个属性值

必须

是

字符串

、

映射

、

列表

、

集合

、

布尔值

或

空值

。任何复杂数据结构（如映射和列表）中的值

必须

也是这些数据类型之一。在 DID 规范注册表 [

DID-SPEC-REGISTRIES

] 中注册的所有元数据属性定义

必须

定义值类型，包括对该值的任何额外格式或限制（例如，格式化为日期或十进制整数的字符串）。建议属性定义使用字符串作为值。整个元数据结构

必须

可以根据 [

INFRA

] 规范中的

JSON 序列化规则

进行序列化。实现

可以

将元数据结构序列化为其他数据格式。

所有使用元数据结构作为输入或输出的函数实现都能够以确定性方式完整表示此处描述的所有数据类型。由于使用元数据结构的输入和输出是根据数据类型而非其序列化定义的，因此

表示

方法是函数的内部实现细节，不在本规范的范围内。

以下示例演示了一个 JSON 编码的元数据结构，该结构可用作

DID 解析输入元数据

。

示例 24

：JSON 编码的 DID 解析输入元数据示例

{

"accept"

：

"application/did+ld+json"

}

此示例对应于以下格式的元数据结构：

示例 25

：DID 解析输入元数据示例

«[

"accept"

→

"application/did+ld+json"

]»

下一个示例演示了一个 JSON 编码的元数据结构，如果未找到

DID

，则该结构可用作

DID 解析元数据

。

示例 26

：JSON 编码的 DID 解析元数据示例

{

"error"

：

"notFound"

}

此示例对应于以下格式的元数据结构：

示例 27

：DID 解析元数据示例

«[

"error"

→

"notFound"

]»

下一个示例演示了一个 JSON 编码的元数据结构，该结构可用作

DID 文档元数据

，以描述与

DID 文档

关联的时间戳。

示例 28

：JSON 编码的 DID 文档元数据示例

{

"created"

：

"2019-03-23T06:35:22Z"

，

"updated"

：

"2023-08-10T13:40:06Z"

}

此示例对应于以下格式的元数据结构：

示例 29

：DID 文档元数据示例

«[

"created"

→

"2019-03-23T06:35:22Z"

，

"updated"

→

"2023-08-10T13:40:06Z"

]»

8. 方法

DID 方法

定义了实现者如何实现本规范描述的功能。

DID 方法

通常与特定的

可验证数据注册表

相关联。新的

DID 方法

在其自己的规范中定义，以实现同一

DID 方法

的不同实现之间的互操作性。

从概念上讲，本规范与

DID 方法

规范之间的关系类似于 IETF 通用

URI

规范 [

RFC3986

] 与特定

URI

方案 [

IANA-URI-SCHEMES

]（如

http

方案 [

RFC7230

]）之间的关系。除了定义特定的

DID 方案

外，

DID 方法

规范还定义了在使用特定类型的

可验证数据注册表

创建、解析、更新和停用

DID

及

DID 文档

的机制。它还记录了与

DID

相关的所有实现注意事项以及安全和隐私注意事项。

本节规定了编写

DID 方法

规范的要求。

8.1 方法语法

定义方法特定的 DID 语法时，所有

DID 方法

规范的要求如下：

DID 方法

规范

必须

正好定义一个方法特定的

DID 方案

以下是该技术文档的中文翻译：

通过3.1节DID语法中规定的method-name规则，以唯一方法名称进行标识的方法规范。

DID方法规范**必须**指定如何生成DID的method-specific-id组件。

DID方法规范**必须**定义method-specific-id值的敏感性和规范化处理。

method-specific-id值在同一DID方法内**必须**唯一。method-specific-id值本身可能是全局唯一的。

由DID方法生成的任何DID**必须**是全局唯一的。

为降低method-name冲突的可能性，DID方法规范**应该**在DID规范注册表[DID-SPEC-REGISTRIES]中注册。

DID方法**可以**定义多种method-specific-id格式。

method-specific-id格式**可以**包含冒号。冒号的使用**必须**在语法上符合method-specific-id的ABNF规则。

DID方法规范**可以**为DID路径指定比本节通用规则更严格的ABNF规则。

DID方法规范**可以**为DID查询指定比本节通用规则更严格的ABNF规则。

DID方法规范**可以**为DID片段指定比本节通用规则更严格的ABNF规则。

注意：method-specific-id中的冒号

method-specific-id中冒号的含义完全取决于具体方法。冒号可能被DID方法用于建立层次分区命名空间、标识可验证数据注册表的特定实例或部分，或用于其他目的。建议实现者避免对冒号做出任何对所有DID方法普遍适用的假设或行为。

## 8.2 方法操作

定义方法操作时所有DID方法规范的要求如下：

DID方法规范**必须**定义如何执行授权以完成所有操作，包括任何必要的加密过程。

DID方法规范**必须**指定DID控制器如何创建DID及其关联的DID文档。

DID方法规范**必须**指定DID解析器如何使用DID解析DID文档，包括DID解析器如何验证响应的真实性。

DID方法规范**必须**指定什么构成DID文档的更新，以及DID控制器如何更新DID文档，或说明更新是不可能的。

DID方法规范**必须**指定DID控制器如何停用DID，或说明停用是不可能的。

执行操作授权的一方权限特定于DID方法。例如，DID方法可能——

- 利用controller属性。
- 使用authentication下列出的验证方法。
- 使用DID文档中的其他构造，如通过capabilityInvocation验证关系指定的验证方法。
- 完全不使用DID文档进行此决策，而是依赖带外机制。

## 8.3 安全要求

编写安全注意事项章节时所有DID方法规范的要求如下：

DID方法规范**必须**遵循RFC3552：编写安全注意事项章节中提供的所有指南和规范语言，用于DID方法规范中定义的DID操作。

安全注意事项章节**必须**为DID方法规范中定义的DID操作记录以下攻击形式：窃听、重放、消息插入、删除、修改、拒绝服务、放大和中间人攻击。其他已知的攻击形式**应该**也要记录。

安全注意事项章节**必须**讨论残余风险，例如相关协议中妥协的风险、错误实现的风险，或在威胁缓解措施部署后密码算法的风险。

安全注意事项章节**必须**为第8.2节方法操作所需的所有操作提供完整性保护和更新身份验证。

如果涉及身份验证，特别是用户-主机身份验证，**必须**清楚地记录身份验证方法的安全特性。

安全注意事项章节**必须**讨论证明DID被唯一分配的政策机制。

**必须**讨论特定于方法的端点身份验证。如果DID方法使用具有不同网络拓扑的DLT（有时以轻节点或瘦客户端实现的形式提供，以减少所需的计算资源），则**必须**讨论DID方法实现可用的拓扑的安全假设。

如果协议包含密码保护机制，DID方法规范**必须**清楚指出数据的哪些部分受到保护以及受到何种保护，**并且应该**给出密码保护易受攻击类型的一些指示。例如完整性保护、机密性和端点身份验证。

要保密的数据（密钥材料、随机种子等）**应该**被明确标记。

DID方法规范**应该**解释并指定DID文档上的签名实现（如果适用）。

在DID方法使用点对点计算资源（如所有已知的DLT）的情况下，这些资源的预期负担**应该**在与拒绝服务的关系中讨论。

引入新身份验证服务类型（如5.4节服务中所述）的DID方法**应该**考虑所支持身份验证协议的安全要求。

## 8.4 隐私要求

编写隐私注意事项章节时所有DID方法规范的要求如下：

DID方法规范的隐私注意事项章节**必须**讨论RFC6973第5节的任何可能以特定于方法的方式适用的小节。需要考虑的小节包括：监控、存储数据泄露、未经请求的流量、错误归属、关联、识别、二次使用、披露和排除。

## 9. 安全注意事项

本节是非规范性的。

本节包含多种安全注意事项，建议人们在生产环境中部署去中心化标识符技术之前考虑这些注意事项。

DID被设计为在许多IETF标准使用的威胁模型下运行，并在RFC3552中记录。本节详细阐述了RFC3552中的多项注意事项，以及DID架构特有的其他注意事项。

### 9.1 选择DID解析器

DID规范注册表[DID-SPEC-REGISTRIES]包含DID方法名称及其对应DID方法规范的信息列表。实现者需要记住，没有中央机构强制要求特定DID方法名称使用哪个DID方法规范。如果对特定DID解析器是否正确实现了DID方法存在疑问，可以使用DID规范注册表查找已注册的规范，就使用哪个DID解析器实现做出知情决定。

### 9.2 证明控制权和绑定

将数字世界或物理世界中的实体绑定到DID、DID文档或密码材料，需要使用本规范所设想的的安全协议。以下小节描述了一些可能的场景，以及实体如何证明对DID或DID文档的控制权，用于身份验证或授权目的。

证明DID和/或DID文档的控制权

# 中文翻译

证明对 **DID** 和/或 **DID 文档** 的控制权，在**可验证数据注册表**中更新它们或与远程系统进行身份验证时非常有用。加密数字签名和**可验证时间戳**使与 **DID 文档** 相关的某些安全协议能够通过加密方式进行验证。为此，本规范在 **5.3.1 认证** 和 **5.3.4 能力调用** 中定义了有用的**验证关系**。与**验证方法**关联的加密密钥材料可用于生成加密数字签名，作为身份验证或授权安全协议的一部分。

> **注意**
>
> 签署的 DID 文档
>
> 某些 **DID 方法** 允许将数字签名和其他证明包含在 **DID 文档** 或 **7.3 元数据结构** 中。但是，此类证明本身不一定能证明对 **DID** 的控制权，也不能保证 **DID 文档** 是该 **DID** 的正确文档。为了获取正确的 **DID 文档** 并验证对 **DID** 的控制权，有必要执行 **DID 方法** 定义的 **DID 解析** 过程。

## 与物理身份的绑定

**DID** 和 **DID 文档** 本身不固有地携带任何**个人数据**，强烈建议非公开实体不要在 **DID 文档** 中发布个人数据。

将 **DID** 以可由可信权威机构（如政府）证明的方式绑定到个人或组织的物理身份可能是有用的。本规范为此目的提供了 **5.3.2 断言** 验证关系。此功能可以实现私密交互，并可被视为在某些管辖区具有法律约束力；建立此类绑定需要与隐私考虑事项谨慎平衡（参见 **10. 隐私注意事项**）。

将 **DID** 绑定到物理世界中某个事物（如个人或组织）的过程——例如，通过使用与该 **DID** 具有相同主题的**可验证凭证**——是本规范考虑的内容，并在可验证凭证数据模型 [VC-DATA-MODEL] 中进一步定义。

## 9.3 认证服务端点

如果 **DID 文档** 发布了用于 **DID 主题** 身份验证或授权的**服务**（参见第 **5.4 节 服务**），则**服务端点**提供者、主题或请求方有责任遵守该**服务端点**所支持的身份验证协议的要求。

## 9.4 不可否认性

如果满足以下条件，则支持对 **DID** 和 **DID 文档** 更新的不可否认性：

- **可验证数据注册表** 支持**可验证时间戳**。有关 **DID 解析** 过程中可用的有用时间戳的更多信息，请参见 **7.1.3 DID 文档元数据**。
- 主题正在监控未经授权的更新，如 **9.5 DID 文档变更通知** 中详述。
- 主题已根据 **DID 方法** 的授权机制有充分机会回滚恶意更新。

## 9.5 DID 文档变更通知

针对 **DID 文档** 未经授权的变更，一种缓解措施是监控并在发生变更时主动通知 **DID 主题**。这类似于通过向档案中的电子邮件地址发送密码重置通知来帮助防止传统用户名/密码账户被接管。

在 **DID** 的情况下，没有中介注册机构或账户提供者来生成此类通知。但是，如果注册 **DID** 的**可验证数据注册表**直接支持变更通知，则可以向 **DID 控制器** 提供订阅服务。通知可以直接发送到现有 **DID** 中列出的相关**服务端点**。

如果 **DID 控制器** 选择依赖第三方监控服务（而不是**可验证数据注册表**本身），则会引入另一种攻击向量。

## 9.6 密钥和签名过期

在**去中心化标识符**架构中，可能没有集中式机构来强制执行加密材料或加密数字签名过期策略。因此，需要由 **DID 解析器** 和验证库等支持软件来验证加密材料在使用时未过期。请求方可能会在其验证过程中加入自己的过期策略。例如，某些请求方可能接受五分钟前的身份验证，而其他可访问高精度时间源的请求方可能要求身份验证的时间戳在最近 500 毫秒内。

某些请求方有合法需要延长已过期加密材料的使用，例如验证遗留加密数字签名。在这些场景中，请求方可能指示其验证软件忽略加密密钥材料过期，或确定加密密钥材料在使用时是否已过期。

## 9.7 验证方法轮换

轮换是一种管理过程，使现有**验证方法**关联的加密密钥材料在新的**验证方法**添加到 **DID 文档** 后可以被停用或销毁。今后，**控制器**使用旧加密密钥材料生成的任何新证明现在可以改用新加密密钥材料生成，并可以使用新**验证方法**进行验证。

轮换是一种有用的机制，用于防止验证方法被破解，因为控制器频繁轮换验证方法会降低单个被破解验证方法对攻击者的价值。在轮换后立即执行撤销对于控制器指定用于短期验证的验证方法非常有用，例如涉及加密消息和身份验证的那些验证方法。

在考虑使用**验证方法**轮换时，以下注意事项可能有用：

- **验证方法**轮换是一种主动安全措施。
- 通常认为执行**验证方法**轮换是一种最佳实践。
- 安全要求更高的环境倾向于采用更频繁的**验证方法**轮换。
- **验证方法**轮换仅表现为对 **DID 文档** 当前版本或最新版本的变更。
- 当**验证方法**已活跃较长时间或用于许多操作时，控制器可能希望执行轮换。
- 频繁轮换**验证方法**可能会令被迫不断续期或刷新相关凭证的各方感到沮丧。
- 依赖不在 **DID 文档** 最新版本中的**验证方法**的证明或签名不受轮换影响。在这些情况下，验证软件可能需要额外信息，例如特定**验证方法**的预期有效期以及访问包含历史记录的**可验证数据注册表**，以确定证明或签名的有效性。此选项并非所有 **DID 方法** 都可用。
- **DID 方法操作**部分规定了 **DID 方法**规范需要支持的 **DID** 操作，包括预期用于执行**验证方法**轮换的**更新**操作。
- **控制器**在添加新的**验证方法**后一段时间后替换现有**验证方法**时执行轮换。
- 并非所有 **DID 方法** 都支持**验证方法**轮换。

## 9.8 验证方法撤销

撤销是一种管理过程，使现有

以下是中文翻译：

---

验证方法

被**停用**，使其不再成为创建新的数字签名证明的有效形式。

撤销是应对验证方法泄露的有用机制。在轮换之后立即执行撤销，对于控制器指定用于短期验证的验证方法非常有用，例如涉及消息加密和认证的验证方法。

与验证方法相关联的密钥的泄露，允许攻击者根据控制器在DID文档中表达的验证关系来使用它们，例如用于认证。攻击者对这些密钥的使用，从验证方法被注册之时起，到其被撤销之时止，可能无法与合法控制器的使用区分开来。

以下考虑因素在考虑使用验证方法撤销时可能有用：

- 验证方法撤销是一种反应式安全措施。
- 支持密钥撤销被认为是最佳实践。
- 控制器应立即撤销任何已知已泄露的验证方法。
- 验证方法撤销只能体现在DID文档的最新版本中；它无法追溯性地调整以前的版本。
- 如5.2.1节验证材料中所述，验证方法的缺失是适用于所有支持撤销的DID方法的唯一撤销形式。
- 如果验证方法不再仅由控制器或受信任代表控制器行事的各方访问，则应立即撤销它，以降低伪装、盗窃和欺诈等泄露风险。
- 撤销应被理解为控制器表示，与已撤销验证方法相关联的、在其撤销之后创建的证明或签名应被视为无效。它也可能暗示现有证明或签名可能由攻击者创建，但这不一定是事实。然而，验证者仍可自行决定接受或拒绝任何此类证明或签名。

DID方法操作一节规定了DID方法规范需要支持的DID操作，包括更新和停用，这些操作可用于从DID文档中移除验证方法。

并非所有DID方法都支持验证方法撤销。

即使验证方法出现在DID文档中，附加信息（如公钥撤销证书或外部允许/拒绝列表）也可用于确定验证方法是否已被撤销。

依赖已泄露验证方法的任何软件（如个人的操作系统、防病毒软件或端点保护软件）的日常操作，在验证方法被公开撤销时可能会受到影响。

**撤销语义**

尽管验证者可能选择不接受来自已撤销验证方法的证明或签名，但知道验证是否使用了已撤销的验证方法比看起来要复杂得多。一些DID方法提供了回溯查看DID在某个时间点的状态或DID文档特定版本的能力。当此功能与可靠地确定加密可验证声明做出时的DID版本或时间的方法相结合时，撤销不会撤销该声明。这可以作为使用DID做出有约束力承诺的基础；例如，用于签署抵押贷款。

如果满足这些条件，撤销不是追溯性的；它只会使该方法将来无法使用。

然而，为了使这种语义安全，第二个条件——了解断言做出时DID文档的状态——预计是适用的。没有这种保证，攻击者可能会发现已撤销的密钥，并用它来制作带有模拟过去日期的加密可验证声明。

一些DID方法仅允许检索DID的当前状态。当这是事实时，或者当加密可验证声明做出时的DID状态无法可靠确定时，唯一安全的做法是禁止考虑DID状态与时间的关系（除当前时刻外）。

采用这种方法的DID生态系统实质上将加密可验证声明作为临时令牌提供，控制器可以随时使其失效。

**无需信任系统中的撤销**

无需信任系统是指所有信任都来自加密可证明断言的系统，更具体地说，是没有外部元数据被纳入系统信任确定的系统。要在无需信任系统中验证已撤销验证方法的签名或证明，DID方法需要支持versionId或versionTime中的任一个或两者，以及DID文档元数据的updated和nextUpdate属性。验证者仅当以下所有条件都为真时，才能验证已撤销密钥的签名或证明：

1. 证明或签名包含创建签名或证明时使用的DID文档的versionId或versionTime。
2. 验证者可以确定签名或证明做出的时间点；例如，它被锚定在区块链上。
3. 对于解析后的DID文档元数据，updated时间戳早于签名或证明做出的时间点，nextUpdate时间戳晚于该时间点。

在愿意接受除构成加密输入之外的元数据的系统中，可以实现类似的信任——但始终基于以下基础：仔细判断签署事件发生时DID文档的内容是否包含预期内容。

**9.9 DID恢复**

恢复是一种反应式安全措施，通过该措施，失去执行DID操作能力（如因设备丢失）的控制器能够重新获得执行DID操作的能力。

以下考虑因素在考虑使用DID恢复时可能有用：

- 主动地以不频繁但定期的方式执行恢复，有助于确保控制权未丢失。
- 永不将恢复相关的加密材料重复用于任何其他目的，被认为是最佳实践。
- 恢复通常与验证方法轮换和验证方法撤销结合执行。
- 建议在控制器或受信任代表其行事的服务不再拥有执行DID操作（如同8.2节方法操作中所述）的排他能力时进行恢复。
- DID方法规范可能选择启用受信任方仲裁以促进恢复。实现此目的的一些设施在5.1.2节DID控制器中有所建议。
- 并非所有DID方法规范都会认可使用其他DID方法注册的DID的控制权，它们可能将第三方控制限制为使用相同方法的DID。
- DID方法规范中的访问控制和恢复也可以包括时间锁定功能，以通过维护恢复控制的第二条路径来防止密钥泄露。
- 目前没有适用于所有DID方法的通用恢复机制。

**9.10 人类友好标识符的作用**

DID无需中央注册机构即可实现全局唯一性。这以人类记忆性为代价。能够生成全局无歧义标识符的算法会产生随机字符串，这些字符串对人类没有意义。这种权衡通常被称为**Zooko三角**。

# 中文翻译

在某些用例中，从人类友好的标识符发现DID是理想的选择。例如，自然语言名称、域名或DID控制者的传统地址（如手机号码、电子邮件地址、社交媒体用户名或博客URL）。然而，将人类友好的标识符映射到DID，并以可验证和可信的方式实现此映射的问题，不在本规范的范围内。

此问题的解决方案在引用本规范的单独规范中定义，例如[DNS-DID]。强烈建议此类规范仔细考虑以下因素：

- 基于欺骗用户关于目标实体的真实人类友好标识符的众多安全攻击。

- 使用本质上可关联的人类友好标识符的隐私后果，特别是在它们具有全局唯一性的情况下。

## 9.11 DID作为增强型URN

如果DID控制者需要，DID或DID URL能够充当持久的、位置无关的资源标识符。这类标识符被归类为统一资源名称（URN），并在[RFC8141]中定义。

DID是一种增强型URN，它为数字资源提供加密安全的、位置无关的标识符，同时还提供支持检索的元数据。由于DID文档与DID本身之间存在间接关系，DID控制者可以调整资源的实际位置——甚至直接提供资源——而无需调整DID。

此类DID可以明确验证检索到的资源实际上就是所标识的资源。

打算将DID用于此目的的DID控制者被建议遵循[RFC8141]中的安全注意事项。具体而言：

- DID控制者应选择支持控制者持久性需求的DID方法。去中心化特性评分[ DID-RUBRIC ]是可供实施者决定最合适DID方法的工具之一。

- DID控制者应发布其操作策略，以便请求方能够确定他们可以依赖该DID控制者控制的DID的持久性程度。在没有此类策略的情况下，不期望请求方对DID是否为同一DID主题的持久标识符做出任何假设。

## 9.12 不可变性

许多网络安全滥用依赖于利用现实与理性、善意行为者假设之间的差距。DID文档的不可变性可以提供一些安全优势。各个DID方法应考虑消除其不需要的行为或语义的约束。DID方法在提供相同功能集的同时越"锁定"，就越不容易被恶意行为者操纵。

举个例子，对DID文档的单一编辑可以更改除文档根id属性之外的任何内容。但是，服务在定义后更改其类型实际上可取吗？或者密钥更改其值？还是在对象的某些基本属性更改时要求使用新的id会更好？网站的恶意接管通常旨在实现网站保留其主机名标识符，但底层被微妙改变的结果。如果规范的某些网站属性（如与其IP地址关联的ASN）被要求是不可变的，异常检测将更容易，攻击将更难且更昂贵实施。

对于与全局真实来源绑定的DID方法，可以直接实时查找DID文档的最新版本。然而，似乎缓存层最终可能位于DID解析器和该真实来源之间。如果是这样，假设DID文档中对象的属性处于给定状态，而实际上它们微妙地不同，可能会导致漏洞利用。如果某些查找是完整的DID文档，而其他查找是部分数据（其中假定存在更大的上下文），则尤其如此。

## 9.13 DID文档中的加密数据

加密算法由于密码学和计算能力的进步而失效。实施者被建议假设DID文档中放置的任何加密数据最终可能会以明文形式向与加密数据相同的受众提供。如果DID文档是公开的，这一点尤其重要。

加密DID文档的全部或部分内容并不是保护长期数据的适当手段。同样，在DID文档中放置加密数据也不是保护个人数据的适当手段。

鉴于上述注意事项，如果加密数据包含在DID文档中，实施者被建议不要关联任何可用于推断加密数据与相关方之间关系的可关联信息。可关联信息的示例包括接收方的公钥、已知在接收方控制下的数字资产的标识符，或接收方的人类可读描述。

## 9.14 等效属性

鉴于equivalentId和canonicalId属性由DID方法本身生成，适用于解析的DID（在DID文档的id字段中存在）的相同安全和准确性保证也适用于这些属性。alsoKnownAs属性不能保证是等效的准确声明，在执行超出DID文档解析的验证步骤之前，不应依赖它。

equivalentId和canonicalId属性表达对由同一DID方法生成的单个DID变体的等效断言，可以信任的程度取决于请求方信任DID方法以及符合规范的生产者和解析器的程度。

alsoKnownAs属性允许对不由同一DID方法管辖的URI进行等效断言，如果不执行治理DID方法之外的验证步骤，则无法信任。参见5.1.3节"也称为"中的其他指导。

与DID文档中的任何其他安全相关属性一样，依赖DID文档中任何等效声明的各方应防范这些属性值在正确验证完成后被攻击者替换。在验证完成后对存储在内存或磁盘中的DID文档的任何写访问都是可能绕过验证的攻击向量，除非重新验证DID文档。

## 9.15 内容完整性保护

包含指向外部机器可读内容（如图像、网页或模式）的链接的DID文档容易受到篡改。强烈建议使用哈希链接[HASHLINK]等解决方案对外部链接进行完整性保护。如果无法对外部链接进行完整性保护且DID文档的完整性依赖于外部链接，则应避免使用外部链接。

外部链接影响DID文档本身完整性的一个示例是JSON-LD上下文[JSON-LD11]。为了防止泄露，建议DID文档消费者缓存JSON-LD上下文的本地静态副本，和/或根据与外部JSON-LD上下文的安全版本关联的加密哈希验证外部上下文的完整性。

## 9.16 持久性

DID被设计为持久性的，使得控制者无需依赖单一可信第三方或管理员来维护其标识符。在理想情况下，没有管理员可以从控制者手中夺取控制权。

以下是该技术文档的中文翻译：

---

，同样地，管理员也无法阻止其标识符被用于任何特定目的（如身份验证、授权和证明）。

任何第三方未经**控制器**同意，不得代**控制器**行事，移除或使实体的标识符失效。

然而，需要注意的是，在所有支持加密控制证明的**DID方法**中，控制证明的手段始终可以通过转移秘密加密材料而转移给另一方。因此，依赖标识符在时间上持续存在的系统，务必定期检查以确保该标识符实际上仍由预期方控制。

遗憾的是，仅从密码学角度无法确定与给定**验证方法**关联的秘密加密材料是否已被泄露。很可能出现这样的情况：预期的**控制器**仍然可以访问秘密加密材料——因此可以在验证过程中执行控制证明——同时，恶意行为者也拥有对这些密钥或其副本的访问权限。

因此，加密控制证明预计仅作为评估高风险场景所需身份保障级别的一个因素来使用。

基于**DID**的身份验证比用户名和密码提供了更大的保障，这得益于无需在系统间传输秘密即可确定对加密密钥控制权的能力。然而，这并非万无一失。涉及敏感、高价值或生命关键操作的场景预计将根据需要使用额外的认证因素。

除了不同**控制器**使用可能带来的歧义外，一般而言，无法保证给定的**DID**在任何特定时间点都是指代同一主体。控制器将一个**DID**重复用于不同主体在技术上是可行的，更微妙的是，主体的精确定义也可能随时间变化或被误解。

例如，考虑一个用于独资企业、接收用于金融交易的各种凭证的**DID**。对**控制器**而言，该标识符指的是该企业。随着企业的发展，最终注册成立为有限责任公司。**控制器**继续使用同一个**DID**，因为对他们来说，**DID**指的是该企业。然而，对州政府、税务机关和当地市政当局而言，该**DID**不再指代同一实体。信贷提供商或供应商是否在乎这种意义上的微妙转变，必然由他们自己决定。在许多情况下，只要账单能够支付且可以执行收款，这种转变就无关紧要。

由于这些潜在的歧义，**DID**应被视为在**上下文**中有效，而非绝对有效。它们的持续存在并不意味着它们指代完全相同的主体，也不意味着它们处于同一**控制器**的控制之下。相反，人们需要了解**DID**创建的上下文、使用方式，并考虑其含义可能发生的变化，同时采用程序和政策来应对潜在和不可避免的语义漂移。

### 9.17 保障级别

出于合规原因，通常需要对身份验证事件的安全上下文提供额外信息，特别是在金融和公共部门等受监管领域。这些信息通常被称为保障级别（LOA）。示例包括对秘密加密材料的保护、身份验证流程以及认证器的形式因素。

**支付服务指令（PSD 2）**和**eIDAS**将此类要求引入安全上下文。保障级别框架由法规和标准（如**eIDAS**、**NIST 800-63-3**和**ISO/IEC 29115:2013**）进行分类和定义，包括对安全上下文的要求，并就如何实现这些要求提供建议。这可能包括强用户身份验证，其中**FIDO2**/**WebAuthn**可以满足要求。

某些受监管场景需要实施特定的保障级别。由于**验证关系**（如**assertionMethod**和**authentication**）可能在某些此类场景中使用，关于所应用安全上下文的信息可能需要被表达并提供给**验证者**。是否以及如何在**DID文档**数据模型中编码此信息不在本规范的范围内。有兴趣的读者可能会注意到：1）可以使用可验证凭证[**VC-DATA-MODEL**]传输此信息；2）**DID文档**数据模型可以按照**4.1 可扩展性**中的描述进行扩展以包含此信息，其中**10. 隐私注意事项**适用于此类扩展。

### 10. 隐私注意事项

本节为非规范性内容。

由于**DID**和**DID文档**设计为由**DID控制器**直接管理，因此将**隐私设计**[**PRIVACY-BY-DESIGN**]原则应用于**去中心化标识符**架构的各个方面至关重要。这七项原则均已在本规范的整个开发过程中得到应用。本规范中使用的设计不假设存在注册商、托管公司或其他中介服务提供商来推荐或应用额外的隐私保护措施。本规范中的隐私是预防性的，而非补救性的，是一种嵌入式默认值。以下各节涵盖了构建使用**去中心化标识符**系统的实施者可能觉得有用的隐私注意事项。

#### 10.1 保持个人数据私密

如果为公共-facing的**可验证数据注册表**编写了**DID方法**规范，其中相应的**DID**和**DID文档**可能会被公开提供，则**关键**的是这些**DID文档**不包含任何个人数据。个人数据可以通过其他方式传输，例如：1）可验证凭证[**VC-DATA-MODEL**]，或2）由**DID主体**或**DID控制器**控制的**服务端点**。

预期将对**服务端点**中URL的使用进行尽职调查，以防止个人数据泄露或在**服务端点**的URL中进行关联。例如，包含用户名的URL危险地包含在**DID文档**中，因为用户名很可能具有人类可理解的意义，可能会泄露**DID主体**未同意共享的信息。通过本规范建议的隐私架构，个人数据可以使用由**DID文档**中的**验证方法**识别和保护的通信通道，以私密、对等的方式交换。这也使**DID主体**和请求方能够实现**GDPR**的被遗忘权，因为没有任何个人数据被写入不可变的**分布式账本**。

#### 10.2 DID关联风险

与任何类型的全局唯一标识符一样，**DID**可能被用于关联。

**DID控制器**可以通过使用配对**DID**来缓解此隐私风险，这些**DID**对每个关系都是唯一的；实际上，每个**DID**都充当一个假名。配对**DID**仅在明确需要关联时才需要与多个方共享。如果配对**DID**是默认设置，那么公开发布**DID**或与多方共享**DID**的唯一需要是当**DID控制器**和/或**DID主体**明确需要公共标识和关联时。

#### 10.3 DID文档关联风险

如果相应**DID文档**中的数据可以被关联，则配对**DID**的反关联保护很容易被击败。例如，在多个**DID文档**中使用相同的**验证方法**或定制的**服务端点**...

# 中文翻译

可以提供与使用相同 **DID** 同样多的关联信息。因此，用于配对 **DID** 的 **DID 文档** 也需要使用配对唯一信息，例如确保**验证方法**对于该配对关系是唯一的。

看似自然地也可以在用于配对 **DID** 的 **DID 文档** 中使用配对唯一的**服务端点**。然而，唯一端点允许两个 **DID** 之间的所有流量被完美隔离到唯一桶中，此时时序关联及类似分析变得容易。因此，对于端点隐私而言，更好的策略是在大量由不同主体控制的 **DID** 之间共享一个端点（参见 10.5 **群体隐私**）。

## 10.4 DID 主体分类

向 **DID 文档** 添加可用于明确指示或通过推断表明 **DID 主体** 是什么**类型**或性质的属性是危险的，特别是当 **DID 主体** 是一个人的时候。

这些属性不仅可能导致个人数据（参见 10.1 **保护个人数据隐私**）或可关联数据（参见 10.2 **DID 关联风险** 和 10.3 **DID 文档关联风险**）存在于 **DID 文档** 中，还可用于对特定 **DID** 进行分组，从而将其包含在或排除在某些操作或功能之外。

在 **DID 文档** 中包含**类型**信息可能导致即使是 **DID 主体** 为非人物实体（如物联网设备）的个人隐私伤害。在 **DID 控制器** 周围聚合此类信息可能构成一种数字指纹形式，这最好予以避免。

为最大程度降低这些风险，**DID 文档** 中的所有属性都应仅用于表达与使用 **DID** 相关的加密材料、端点或**验证方法**。

## 10.5 群体隐私

当一个 **DID 主体** 与群体中的其他个体无法区分时，隐私便可获得。当与另一方私下交往的行为本身就是一个可识别的标志时，隐私将大大降低。

**DID** 和 **DID 方法** 需要努力改善群体隐私，特别是对于那些最需要隐私的人。选择默认保护匿名性和假名性的技术和用户界面。为减少**数字指纹**，在请求方实现之间共享常见设置，将有线协议上的协商选项保持在最少，使用加密传输层，并将消息填充到标准长度。

## 10.6 服务隐私

允许**控制器**选择在 **DID 文档** 中表达至少一个**服务端点**的能力增加了其控制力和能动性。**DID 文档** 中的每个附加端点都会增加隐私风险，或者由于关联（如跨端点描述），或者因为**服务**未受授权机制保护，或两者兼有。

**DID 文档** 通常是公开的，而且由于其标准化性质，将被其基于标准的天性高效地存储和索引。如果 **DID 文档** 发布到不可变的**可验证数据注册表**，此风险会更大。访问与 **DID** 引用的 **DID 文档** 的历史记录代表了一种通过使用标准而变得更加高效的流量分析形式。

在单个 **DID 文档** 中使用多个**服务端点**所导致的额外隐私风险程度可能难以估计。隐私伤害通常是意外后果。

**DID** 可以引用文档、**服务**、模式和其他可能与个人、家庭、俱乐部和雇主相关联的事物——而其**服务端点**的关联可能成为一种强大的监控和推断工具。当使用多个常见的国家级顶级域名（如 `https://example.co.uk`）时，可能会以更高的概率被用来推断 **DID 主体** 的大致位置，这可以作为一个潜在伤害的例子。

### 维护群体隐私

多种可能的端点使得维护群体隐私变得特别具有挑战性，即 **DID 主体** 的任何信息都不会被泄露（参见 10.5 **群体隐私**）。

首先，因为服务端点可能被指定为 **URI**，它们可能因服务架构而无意中泄露个人信息。例如，`http://example.com/MyFirstName` 这样的服务端点正在向所有可以访问 **DID 文档** 的人泄露 "MyFirstName" 这个术语。在链接到遗留系统时，这是一个不可避免的风险，在这种情况下需要格外小心。本规范鼓励新的、**DID** 感知的端点仅使用 **DID** 本身进行任何必要的标识。例如，如果服务描述包含 `http://example.com/did%3Aexample%3Aabc123`，则不会造成伤害，因为 `did:example:abc123` 已在 DID 文档中暴露；它不会泄露额外信息。

其次，因为 **DID 文档** 可以列出多个服务端点，可能使在没有任何其他上下文中关联的服务产生不可逆的关联。这种关联本身可能通过揭示有关 **DID 主体** 的信息而导致隐私伤害，即使所使用的 **URI** 不包含任何敏感信息。

第三，因为某些类型的 **DID 主体** 可能或多或少倾向于列出特定端点，给定服务的列出本身就可以泄露可用于推断有关 **DID 主体** 某些信息。例如，汽车的 **DID** 可能包含指向交通管理局的公共所有权记录的指针，而个人的 **DID** 则不会包含该信息。

群体隐私的目标是确保特定 **DID 主体** 的性质被整个人群所掩盖。为最大化群体隐私，实现者需要依赖一个——且仅一个——服务端点，该端点提供代理或中介服务，控制器愿意依靠它来保护此类关联并隐藏对最终服务的请求。

### 服务端点替代方案

鉴于上一节中的担忧，强烈建议实现者考虑以下任何服务端点方法：

**协商者端点** — 用于协商双方同意的通信渠道的服务，优选使用私有集合交集。协商的输出是通信渠道以及访问该渠道所需的任何凭证。

**Tor 端点**（**Tor 洋葱路由器**）— 提供一个尊重隐私的地址以访问服务端点。任何可以在线提供的服务都可以通过 Tor 提供以增加隐私。

**调解人端点** — **调解人** 为多方提供一个通用端点，代表这些方接收加密消息，并将其转发给预期接收者。这避免了需要每个主体一个特定端点的情况，这可能造成关联风险。这种方法也称为代理。

**机密存储** — 专有或机密个人信息可能需要保持在**可验证数据注册表**之外，以提供额外的隐私和/或安全保证，特别是对于那些 **DID 文档** 发布在公共账本上的 **DID 方法**。指向外部资源服务提供了授权检查和删除的手段。

**多态代理** — 一个可以充当任意数量服务的代理端点，取决于如何调用它。例如，同一 URL 可用于协商者和调解人功能，取决于重新路由机制。

这些服务端点类型继续是一个创新和探索领域。

## A. 示例

### A.1 DID 文档

本节是非规范性的。

有关可选扩展和其他验证方法类型，请参阅**验证方法类型** [**DID-SPEC-REGISTRIES**]。

**注意**

**译文（中文）**  

这些示例仅供参考，**最佳实践**是避免将同一个 **验证方法（verification method）** 用于多个目的。  

---

### 示例 30：DID 文档，包含 1 种验证方法类型  

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2020/v1"
  ],
  "id": "did:example:123",
  "authentication": [
    {
      "id": "did:example:123#z6MkecaLyHuYWkayBDLw5ihndj3T1m6zKTGqau3A51G7RBf3",
      "type": "Ed25519VerificationKey2020",
      // 外部（属性值）
      "controller": "did:example:123",
      "publicKeyMultibase": "zAKJP3f7BD6W4iWEQ9jwndVTCBq8ua2Utt8EEjJ6Vxsf"
    }
  ],
  "capabilityInvocation": [
    {
      "id": "did:example:123#z6MkhdmzFu659ZJ4XKj31vtEDmjvsi5yDZG5L7Caz63oP39k",
      "type": "Ed25519VerificationKey2020",
      // 外部（属性值）
      "controller": "did:example:123",
      "publicKeyMultibase": "z4BWwfeqdp1obQptLLMvPNgBw48p7og1ie6Hf9p5nTpNN"
    }
  ],
  "capabilityDelegation": [
    {
      "id": "did:example:123#z6Mkw94ByR26zMSkNdCUi6FNRsWnc2DFEeDXyBGJ5KTzSWyi",
      "type": "Ed25519VerificationKey2020",
      // 外部（属性值）
      "controller": "did:example:123",
      "publicKeyMultibase": "zHgo9PAmfeoxHG8Mn2XHXamxnnSwPpkyBHAMNF3VyXJCL"
    }
  ],
  "assertionMethod": [
    {
      "id": "did:example:123#z6MkiukuAuQAE8ozxvmahnQGzApvtW7KT5XXKfojjwbdEomY",
      "type": "Ed25519VerificationKey2020",
      // 外部（属性值）
      "controller": "did:example:123",
      "publicKeyMultibase": "z5TVraf9itbKXrRvt2DSS95Gw4vqU3CHAdetoufdcKazA"
    }
  ]
}
```

---

### 示例 31：DID 文档，包含多种不同密钥类型  

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/jws-2020/v1"
  ],
  "verificationMethod": [
    {
      "id": "did:example:123#key-0",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "OKP",
        // 外部（属性名）
        "crv": "Ed25519",
        // 外部（属性名）
        "x": "VCpo2LMLhn6iWku8MKvSLg2ZAoC-nlOyPVQaO3FxVeQ"
        // 外部（属性名）
      }
    },
    {
      "id": "did:example:123#key-1",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "OKP",
        // 外部（属性名）
        "crv": "X25519",
        // 外部（属性名）
        "x": "pE_mG098rdQjY3MKK2D5SUQ6ZOEW3a6Z6T7Z4SgnzCE"
        // 外部（属性名）
      }
    },
    {
      "id": "did:example:123#key-2",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "EC",
        // 外部（属性名）
        "crv": "secp256k1",
        // 外部（属性名）
        "x": "Z4Y3NNOxv0J6tCgqOBFnHnaZhJF6LdulT7z8A-2D5_8",
        // 外部（属性名）
        "y": "i5a2NtJoUKXkLm6q8nOEu9WOkso1Ag6FTUT6k_LMnGk"
        // 外部（属性名）
      }
    },
    {
      "id": "did:example:123#key-3",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "EC",
        // 外部（属性名）
        "crv": "secp256k1",
        // 外部（属性名）
        "x": "U1V4TVZVMUpUa0ZVU1NBcU9CRm5IbmFaaEpGNkxkdWx",
        // 外部（属性名）
        "y": "i5a2NtJoUKXkLm6q8nOEu9WOkso1Ag6FTUT6k_LMnGk"
        // 外部（属性名）
      }
    },
    {
      "id": "did:example:123#key-4",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "EC",
        // 外部（属性名）
        "crv": "P-256",
        // 外部（属性名）
        "x": "Ums5WVgwRkRTVVFnU3k5c2xvZllMbEcwM3NPRW91ZzN",
        // 外部（属性名）
        "y": "nDQW6XZ7b_u2Sy9slofYLlG03sOEoug3I0aAPQ0exs4"
        // 外部（属性名）
      }
    },
    {
      "id": "did:example:123#key-5",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "EC",
        // 外部（属性名）
        "crv": "P-384",
        // 外部（属性名）
        "x": "VUZKSlUwMGdpSXplekRwODhzX2N4U1BYdHVYWUZsaXVDR25kZ1U0UXA4bDkxeHpE",
        // 外部（属性名）
        "y": "jq4QoAHKiIzezDp88s_cxSPXtuXYFliuCGndgU4Qp8l91xzD1spCmFIzQgVjqvcP"
        // 外部（属性名）
      }
    },
    {
      "id": "did:example:123#key-6",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "EC",
        // 外部（属性名）
        "crv": "P-521",
        // 外部（属性名）
        "x": "VTI5c1lYSmZWMmx1WkhNZ0dQTXhaYkhtSnBEU3UtSXZwdUtpZ0VOMnB6Z1d0U28tLVJ3ZC1uNzhuclduWnplRGMx",
        // 外部（属性名）
        "y": "UW5WNVgwSnBkR052YVc0Z1VqY1B6LVpoZWNaRnliT3FMSUpqVk9sTEVUSDd1UGx5RzBnRW9NV25JWlhoUVZ5cFB5"
        // 外部（属性名）
      }
    },
    {
      "id": "did:example:123#key-7",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "RSA",
        // 外部（属性名）
        "e": "AQAB",
        // 外部（属性名）
        "n": "UkhWaGJGOUZRMTlFVWtKSElBdENGV2hlU1F2djFNRXh1NVJMQ01UNGpWazlraEpLdjhKZU1YV2UzYldIYXRqUHNrZGYyZGxhR2tXNVFqdE9uVUtMNzQybXZyNHRDbGRLUzNVTElhVDFoSkluTUhIeGoyZ2N1Yk82ZUVlZ0FDUTRRU3U5TE8wSC1MTV9MM0RzUkFCQjdRamE4SGVjcHl1c3BXMVR1X0RicXhjU253ZW5kYW13TDUyVjE3ZUtobE80dVh3djJIRmx4dWZGSE0wS21DSnVqSUt5QXhqRF9tM3FfX0lpSFVWSEQxdERJRXZMUGhHOUF6c24zajk1ZC1zYU"
        // 外部（属性名）
      }
    }
  ]
}
```

---

### 示例 32：DID 文档，包含不同验证方法类型  

```json
{
  "@context": [
    "https://www.w3.org/ns/did/v1",
    "https://w3id.org/security/suites/ed25519-2018/v1",
    "https://w3id.org/security/suites/x25519-2019/v1",
    "https://w3id.org/security/suites/secp256k1-2019/v1",
    "https://w3id.org/security/suites/jws-2020/v1"
  ],
  "verificationMethod": [
    {
      "id": "did:example:123#key-0",
      "type": "Ed25519VerificationKey2018",
      "controller": "did:example:123",
      "publicKeyBase58": "3M5RCDjPTWPkKSN3sxUmmMqHbmRPegYP1tjcKyrDbt9J"
      // 外部（属性名）
    },
    {
      "id": "did:example:123#key-1",
      "type": "X25519KeyAgreementKey2019",
      "controller": "did:example:123",
      "publicKeyBase58": "FbQWLPRhTH95MCkQUeFYdiSoQt8zMwetqfWoxqPgaq7x"
      // 外部（属性名）
    },
    {
      "id": "did:example:123#key-2",
      "type": "EcdsaSecp256k1VerificationKey2019",
      "controller": "did:example:123",
      "publicKeyBase58": "ns2aFDq25fEV1NUd3wZ65sgj5QjFW8JCAHdUJfLwfodt"
      // 外部（属性名）
    },
    {
      "id": "did:example:123#key-3",
      "type": "JsonWebKey2020",
      "controller": "did:example:123",
      "publicKeyJwk": {
        "kty": "EC",
        // 外部（属性名）
        "crv": "P-256",
        // 外部（属性名）
        "x": "Er6KSSnAjI70ObRWhlaMgqyIOQYrDJTE94ej5hybQ2M",
        // 外部（属性名）
        "y": "pPVzCOTJwgikPjuUE6UebfZySqEJ0ZtsWFpj7YSPGEk"
        // 外部（属性名）
      }
    }
  ]
}
```

---

## A.2 证明  

> **注意**  
> 这些示例仅供参考。请参阅 **W3C 可验证凭证数据模型（Verifiable Credentials Data Model）** 以获取更多示例。

### 示例 33：可验证凭证，关联到 Ed25519VerificationKey2020 类型的验证方法  

```json
{
  // 本示例中所有术语均为外部（外部）
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3id.org/citizenship/v1"
  ],
  "type": [
    "VerifiableCredential",
    "PermanentResidentCard"
  ],
  "credentialSubject": {
    "id": "did:example:123",
    "type": [
      "PermanentResident",
      "Person"
    ],
    "givenName": "JOHN",
    "familyName": "SMITH",
    "gender": "Male",
    "image": "data:image/png;base64,iVBORw0KGgo...kJggg==",
    "residentSince": "2015-01-01",
    "lprCategory": "C09",
    "lprNumber": "000-000-204",
    "commuterClassification": "C1",
    "birthCountry": "Bahamas",
    "birthDate": "1958-08-17"
  },
  "issuer": "did:example:456",
  "issuanceDate": "2020-04-22T10:37:22Z",
  "identifier": "83627465",
  "name": "Permanent Resident Card",
  "description": "Government of Example Permanent Resident Card.",
  "proof": {
    "type": "Ed25519VerificationKey2020",
    // 验证方法的标识符
    "verificationMethod": "did:example:456#z6MkecaLyHuYWkayBDLw5ihndj3T1m6zKTGqau3A51G7RBf3",
    // 签名（signature）示例（此处为占位符）
    "jws": "eyJhbGciOiJFZERTQSJ9....."
  }
}
```

> **说明**  
> 上述 JSON 中的 `proof` 对象展示了如何引用一个 **Ed25519VerificationKey2020** 类型的验证方法，并提供对应的签名值（在实际使用中会被替换为真实签名）。  



**示例 33：使用 Ed25519Signature2018 的可验证凭证**  

```json
{
  // 外部（本示例中所有术语）
  "type": "Ed25519Signature2018",
  "created": "2020-04-22T10:37:22Z",
  "proofPurpose": "assertionMethod",
  "verificationMethod": "did:example:456#key-1",
  "jws": "eyJjcml0IjpbImI2NCJdLCJiNjQiOmZhbHNlLCJhbGciOiJFZERTQSJ9..BhWew0x-txcroGjgdtK-yBCqoetg9DD9SgV4245TmXJi-PmqFzux6Cwaph0r-mbqzlE17yLebjfqbRT275U1AA"
}
```

---

**示例 34：可验证凭证链接到类型为 JsonWebKey2020 的验证方法**  

```json
{
  // 外部（本示例中所有术语）
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://www.w3.org/2018/credentials/examples/v1"
  ],
  "id": "http://example.gov/credentials/3732",
  "type": [
    "VerifiableCredential",
    "UniversityDegreeCredential"
  ],
  "issuer": {
    "id": "did:example:123"
  },
  "issuanceDate": "2020-03-10T04:24:12.164Z",
  "credentialSubject": {
    "id": "did:example:456",
    "degree": {
      "type": "BachelorDegree",
      "name": "Bachelor of Science and Arts"
    }
  },
  "proof": {
    "type": "JsonWebSignature2020",
    "created": "2020-02-15T17:13:18Z",
    "verificationMethod": "did:example:123#_Qq0UL2Fq651Q0Fjd6TvnYE-faHiOpRlPVQcY_-tA4A",
    "proofPurpose": "assertionMethod",
    "jws": "eyJiNjQiOmZhbHNlLCJjcml0IjpbImI2NCJdLCJhbGciOiJFZERTQSJ9..Y0KqovWCPAeeFhkJxfQ22pbVl43Z7UI-X-1JX32CA9MkFHkmNprcNj9Da4Q4QOl0cY3obF8cdDRdnKr0IwNrAw"
  }
}
```

---

**示例 35：可验证凭证链接到 bls12381 验证方法**  

```json
{
  // 外部（本示例中所有术语）
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3id.org/security/bbs/v1",
    {
      "name": "https://schema.org/name",
      "birthDate": "https://schema.org/birthDate"
    }
  ],
  "id": "urn:uuid:c499e122-3ba9-4e95-8d4d-c0ebfcf8c51a",
  "type": [
    "VerifiableCredential"
  ],
  "issuanceDate": "2021-02-07T16:02:08.571Z",
  "issuer": {
    "id": "did:example:123"
  },
  "credentialSubject": {
    "id": "did:example:456",
    "name": "John Smith",
    "birthDate": "2021-02-07"
  },
  "proof": {
    "type": "BbsBlsSignature2020",
    "created": "2021-02-07T16:02:10Z",
    "proofPurpose": "assertionMethod",
    "proofValue": "o7zD2eNTp657YzkJLub+IO4Zqy/R3Lv/AWmtSA/kUlEAOa73BNyP1vOeoow35jkABolx4kYMKkp/ZsFDweuKwe/p9vxv9wrMJ9GpiOZjHcpjelDRRJLBiccg9Yv7608mHgH0N1Qrj14PZ2saUlfhpQ==",
    "verificationMethod": "did:example:123#bls12381-g2-key"
  }
}
```

---

**示例 36：可验证凭证选择性披露零知识证明链接到 bls12381 验证方法**  

```json
{
  // 外部（本示例中所有术语）
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://w3id.org/security/bbs/v1",
    {
      "name": "https://schema.org/name",
      "birthDate": "https://schema.org/birthDate"
    }
  ],
  "id": "urn:uuid:c499e122-3ba9-4e95-8d4d-c0ebfcf8c51a",
  "type": "VerifiableCredential",
  "issuanceDate": "2021-02-07T16:02:08.571Z",
  "issuer": {
    "id": "did:example:123"
  },
  "credentialSubject": {
    "id": "did:example:456",
    "birthDate": "2021-02-07"
  },
  "proof": {
    "type": "BbsBlsSignatureProof2020",
    "created": "2021-02-07T16:02:10Z",
    "nonce": "OqZHsV/aunS34BhLaSoxiHWK+SUaG4iozM3V+1jO06zRRNcDWID+I0uwtPJJ767Yo8Q=",
    "proofPurpose": "assertionMethod",
    "proofValue": "AAsH34lcKsqaqPaLQWcnLMe3mDM+K7fZM0t4Iesfj7BhD//HBtuWCmZE946BqW7OHYU106MP8mLntutqB8FyGwS7AOyK+5/7iW6JwLNVCvh4Nt3IaF3AN47fqVs2VikD9DiCsaFAUU6ISj5pbad8O+6jiT9Yw6ug8t8vJn3XHvMUhCPnDZJeBEdKD1qo4Z0LOq3L8QAAAHSEgtC9BoZL2MLjz4QuPxpwbhTTRC08MIUjdJnP4JUtz6163Lsl3rpadGu2d3Te7loAAAACZBD4YWOgV0xpPoYZ5vywNA5/NTeDHDbX36gvoV5RDJtY1SLU2LN/IDPZGrfhEiASbD1/QXqj8dod6FbjBs9m/LchBcy7z4yDBv/8DnBzDJ9dEaM4bDjpwmqtgJqha2kwtlyNog67xG9tNjnp5rrbIgAAAANMVanwWmlkg5I/f1M2QJ5GRvQiBL4lyL5sttxwIOalbTZP8VqWtFJI54xMNjTiK71aFWWN8SlNEwfVIX34HO5zBIb6fvc+Or21ubYllT9eXv1epl2o2CojuieCZyxE8/Q=",
    "verificationMethod": "did:example:123#bls12381-g2-key"
  }
}
```

---

**示例 37：可验证凭证（解码后的 JWT）**  

```json
{
  // 外部（本示例中所有术语）
  "protected": {
    "kid": "did:example:123#_Qq0UL2Fq651Q0Fjd6TvnYE-faHiOpRlPVQcY_-tA4A",
    "alg": "EdDSA"
  },
  "payload": {
    "iss": "did:example:123",
    "sub": "did:example:456",
    "vc": {
      "@context": [
        "https://www.w3.org/2018/credentials/v1",
        "https://www.w3.org/2018/credentials/examples/v1"
      ],
      "id": "http://example.gov/credentials/3732",
      "type": [
        "VerifiableCredential",
        "UniversityDegreeCredential"
      ],
      "issuer": {
        "id": "did:example:123"
      },
      "issuanceDate": "2020-03-10T04:24:12.164Z",
      "credentialSubject": {
        "id": "did:example:456",
        "degree": {
          "type": "BachelorDegree",
          "name": "Bachelor of Science and Arts"
        }
      }
    },
    "jti": "http://example.gov/credentials/3732",
    "nbf": 1583814252
  },
  "signature": "qSv6dpZJGFybtcifLwGf4ujzlEu-fam_M7HPxinCbVhz9iIJCg70UMeQbPa1ex6BmQ2tnSS7F11FHnMB2bJRAw"
}
```

---

## A.3 加密  

本节为非规范性说明。

> **注意**：以下示例仅供参考，避免在 JWE 头中泄露不必要的信息被视为最佳实践。

**示例 38：通过 kid 链接到验证方法的 JWE**  

```json
{
  // 外部（本示例中所有术语）
  "ciphertext": "3SHQQJajNH6q0fyAHmw...",
  "iv": "QldSPLVnFf2-VXcNLza6mbylYwphW57Q",
  "protected": "eyJlbmMiOiJYQzIwUCJ9",
  "recipients": [
    {
      "encrypted_key": "BMJ19zK12YHftJ4sr6Pz1rX1HtYni_L9DZvO1cEZfRWDN2vXeOYlwA",
      "header": {
        "alg":

# 中文翻译

例如，允许DID主体变更的DID方法可用于为特定角色（如公司CEO）的当前担任者生成DID——实际担任该角色的人可能因DID被解析的时间不同而有所差异。

## B.4 引用DID文档

DID指向DID主体，并通过遵循DID方法指定的协议来解析到DID文档。DID文档并非独立于DID主体的单独资源，也不存在独立于DID的URI。相反，DID文档是DID解析的可控产物，由DID控制者控制，用以描述DID主体。

这一区别如下图所示的图形模型加以说明。

**图8**

DID是由DID控制者分配的标识符，用于引用DID主体并解析到描述该DID主体的DID文档。DID文档是DID解析的产物，而非独立于DID主体的单独资源。另请参阅：[叙述性描述](#narrative-description)。

图中上方有两个黑色实心圆，左侧标注为"DID控制者"，右侧标注为"DID主体"。下方有一个矩形，其右下角向内折成一个小三角形，内含标签"DID文档"。这三个元素之间有箭头连接，具体如下。一条红色实线箭头直接从DID控制者圆指向右侧的DID主体圆，上方标注大字"DID"，下方用小斜体标注"标识"。其他箭头的标签也使用小斜体。一条红色虚线箭头标注"解析到"，从DID控制者发出，与第一条箭头在同一位置，然后向下弯曲指向DID文档矩形。一条绿色箭头标注"控制"，直接从DID控制者指向DID文档。另一条绿色箭头标注"控制者"，从DID文档指向DID控制者，在图的左侧向外弯曲形成弧线。一条蓝色箭头标注"描述"，直接从DID文档指向DID主体。

## B.5 DID文档中的声明

DID文档中的每个属性都是DID控制者的一条声明，用于描述：

- 定义DID主体标识符的字符序列（例如`id`和`alsoKnownAs`属性）
- 如何与DID主体交互（例如`verificationMethod`和`service`属性）
- 如何解释DID文档的特定表示形式（例如JSON-LD表示的`@context`属性）

DID文档中唯一必需的属性是`id`，因此这是保证出现在DID文档中的唯一声明。该声明在**图8**中以DID和DID主体之间的直接链接来说明。

## B.6 发现关于DID主体的更多信息

发现DID主体更多信息的选项取决于DID文档中存在的属性。如果存在`service`属性，则可以从服务端点请求更多信息。例如，通过查询支持可验证凭证的服务端点来获取描述DID主体的一个或多个声明（属性）。

另一个选项是使用`alsoKnownAs`属性（如果它存在于DID文档中）。DID控制者可以使用它来提供引用同一DID主体的其他URI列表（包括其他DID）。解析或解引用这些URI可能会产生DID主体的其他描述或表示，如下图所示。

**图9**

DID文档可以使用alsoKnownAs属性来声明另一个URI（包括但不限于另一个DID）引用同一DID主体。另请参阅：[叙述性描述](#narrative-description)。

该图包含三个黑色实心小圆、两个带折角的矩形、它们之间的箭头和标签，具体如下。左上方是一个标注为"DID控制者"的圆。右上方是一个标注为"DID主体"的圆。右下偏中是一个无标签的圆。右下是一个标注为"描述"的矩形。图的中心是一个标注为"DID文档"的矩形。在DID文档矩形内部，标签下方有两行代码：`alsoKnownAs: [`和`URI]`。一条黑色箭头从第二行向右延伸，穿过矩形边框，指向图右侧的无标签圆。该箭头在上方用大字标注"URI"，下方用斜体标注"标识"。一条黑色箭头从无标签圆向下指向描述矩形，标注为"解引用到"。一条蓝色箭头标注"描述"，从描述向右弯曲指向上方的DID主体。一条蓝色箭头同样标注"描述"，直接从图中部的标注为"DID文档"的矩形向右上方指向DID主体圆。一条红色箭头标注"alsoKnownAs"，从DID主体向下指向无标签圆。一条红色箭头在上方用大字标注"DID"，下方用斜体标注"标识"，位于图的顶部，从DID控制者指向DID主体。一条红色虚线从同一位置出发但分叉并向下弯曲指向图中心的DID文档矩形。一条绿色箭头标注"控制"，直接从DID控制者指向DID文档。另一条绿色箭头标注"控制者"，从DID文档指向DID控制者，在图的左侧向外弯曲。

## B.7 提供DID主体的表示

如果DID主体是可以从互联网检索的数字资源，DID方法可以选择构造一个返回DID主体本身的表示的DID URL。例如，需要持久且密码学可验证的标识符的数据模式可以被分配一个DID，传递指定的DID参数（参见3.2.1 DID参数）可用作检索该模式表示的标准方式。

类似地，如果适用的DID方法支持此功能，DID可以用于引用可从可验证数据注册表直接返回的数字资源（如图像）。

## B.8 为现有Web资源分配DID

如果网页或任何其他Web资源的控制者想为其分配持久且密码学可验证的标识符，控制者可以为其分配一个DID。例如，托管在博客托管公司域名下的博客作者可以为该博客创建一个DID。在DID文档中，作者可以包含`alsoKnownAs`属性指向博客的当前URL，例如：

```json
"alsoKnownAs": ["https://myblog.blogging-host.example/home"]
```

如果作者随后将博客迁移到另一家托管公司（或作者自己的域名），作者可以更新DID文档以指向博客的新URL，例如：

```json
"alsoKnownAs": ["https://myblog.example/"]
```

DID有效地为博客URL添加了一层间接层。这层间接寻址由作者控制，而非由博客托管公司等外部管理机构控制。这就是DID可以有效地充当增强型URN（统一资源名称）的方式——即信息资源的持久标识符，其网络位置可能随时间变化。

## B.9 DID控制者与DID主体之间的关系

为避免混淆，根据DID主体与DID控制者的关系，将其分为两个不相交的集合是有帮助的。

### B.9.1 集合#1：DID主体是DID控制者

第一种情况（如**图10**所示）是DID主体是DID控制者的常见场景。

The user wants to translate a large passage from English to Chinese, keeping technical terms accurate. The text includes multiple sections (B.9.2, B.10, B.10.1, B.10.2, B.11, B.12, C). The user says "Translate to Chinese, keep technical terms accurate: is also the ..."

The text appears to be part of a specification, maybe W3C DID (Decentralized Identifiers) specification.

The user gave a text block, which includes some figure descriptions and references. The user wants a translation to Chinese, keeping technical terms accurate.

Thus I need to translate the whole given text into Chinese, presumably maintaining formatting. However, the user input includes "is also the" at the top, which seems incomplete. It may be a leftover. The original block:

```
is also the

DID
controller

. This is the case when an individual or organization creates a

DID

to self-identify.

Figure

10

The

DID subject

is the same entity as the

DID controller

. See
also:

narrative description

.

Two small black circles appear in the diagram, one on the upper left, labeled,
"DID Controller", and one on the upper right, labeled "DID Subject". A solid red
arrow extends from the DID Controller circle to the DID Subject circle, labeled
"DID" in large bold text above the arrow, and "Identifies" in small italic text
beneath the arrow. A dotted red double-ended arrow, labeled "Equivalence",
extends between the two circles, forming an arc in the space between and above
them. In the lower part of the diagram is a rectangle with bent corner, outlined
in black, containing the label "DID Document". Arrows point between this DID
Document rectangle and the small black circles for DID Controller and DID
Subject, with italic labels, as follows. A blue arrow points from the DID
Document to the DID Subject, labeled, "Describes". A green arrow points from the
DID Controller to the DID Document, labeled "Controls". A green arrow points
from the DID Document to the DID Controller, in an outward arc, labeled,
"Controller". A dotted red arrow, labeled "Resolves to", extends from the DID
controller starting to the right, branching off from the arrow to the DID
Subject, then curving downward to point to the DID Document.

From a graph model perspective, even though the nodes identified as the

DID controller

and

DID subject

in

Figure

10

are distinct, there is a
logical arc connecting them to express a semantic equivalence relationship.

B.9.2

Set #2: The DID subject is

not

the DID controller

The second case is when the

DID subject

is a separate entity from the

DID controller

. This is the case when, for example, a parent creates
and maintains control of a

DID

for a child; a corporation creates and
maintains control of a

DID

for a subsidiary; or a manufacturer
creates and maintains control of a

DID

for a product, an IoT device,
or a digital file.

From a graph model perspective, the only difference from Set 1 that there is
no equivalence arc relationship between the

DID subject

and

DID controller

nodes.

B.10

Multiple DID controllers

A

DID document

might have more than one

DID controller

. This can
happen in one of two ways.

B.10.1

Independent Control

In this case, each of the

DID controllers

might act on its own, i.e.,
each one has full power to update the

DID document

independently. From
a graph model perspective, in this configuration:

Each additional

DID controller

is another distinct graph node
(which might be identified by its own

DID

).

The same arcs ("controls" and "controller") exist between each

DID controller

and the

DID document

.

Figure

11

Multiple independent

DID controllers

that can each act independently. See
also:

Text
Description

Three black circles appear on the left, vertically, each labeled "DID
Controller". From each of these circles, a pair of green arrows extends towards
the center of the diagram, to a single rectangle, labeled "DID Document". The
rectangle has the lower right corner cut and bent inward to form a small
triangle, as if to represent a physical piece of paper with curled corner. Each
pair of green arrows consists of one arrow pointing from the black circle to the
rectangle, labeled "Controls", and one pointing in the opposite direction, from
the rectangle to the black circle, labeled "Controller". From the right of the
rectangle extends a blue arrow, labeled, "Describes", pointing to a black circle
labeled, "DID Subject".

B.10.2

Group Control

In the case of group control, the

DID controllers

are expected to act
together in some fashion, such as when using a cryptographic algorithm that
requires multiple digital signatures ("multi-sig") or a threshold number of
digital signatures ("m-of-n"). From a functional standpoint, this option is
similar to a single

DID controller

because, although each of the

DID controllers

in the

DID controller

group has its own graph
node, the actual control collapses into a single logical graph node
representing the

DID controller

group as shown in

Figure

12

.

Figure

12

Multiple

DID controllers

who are expected to act together as a

DID
controller

group. See also:

narrative description

.

On the left are three black filled circles, labeled "DID Controller Group" by a
brace on the left. From each of these three circles, a green arrow extends to
the center right. These three arrows converge towards a single filled white
circle. A pair of horizontal green arrows connects this white circle on its
right to a rectangle shaped like a page with a curled corner, labeled "DID
Document". The upper arrow points right, from the white circle to the
rectangle, and is labeled "Controls". The lower arrow points left, from the
rectangle to the white circle, and is labeled "Controller". From the right of
the rectangle extends a blue arrow, labeled "Describes", pointing to a black
circle, labeled "DID Subject".

This configuration will often apply when the

DID subject

is an
organization, corporation, government agency, community, or other group
that is not controlled by a single individual.

B.11

Changing the DID subject

A

DID document

has exactly one

DID

which refers to
the

DID subject

. The

DID

is expressed as the value of the

id

property. This property value is immutable for
the lifetime of the

DID document

.

However, it is possible that the resource

identified

by the

DID

,
the

DID subject

, may change over time. This is under the exclusive
authority of the

DID controller

. For more details, see section

9.16

Persistence

.

B.12

Changing the DID controller

The

DID controller

for a

DID document

might change over time.
However, depending on how it is implemented, a change in the

DID
controller

might not be made apparent by changes to the

DID document

itself. For example, if the change is implemented through a shift in ownership
of the underlying cryptographic keys or other controls used for one or more of
the

verification methods

in the

DID document

, it might be
indistinguishable from a standard key rotation.

On the other hand, if the change is implemented by changing the value of the

controller

property, it will be transparent.

If it is important to verify a change of

DID controller

, implementers are
advised to

authenticate

the new

DID controller

against the

verification methods

in the revised

DID document

.

C.

Revision History

This section contains the changes that have been made since the publication of
this specification as a

W3C

First Public Working Draft.

Changes since the

Second Candidate
Recommendation

include:

Non-normatively refer to the DID Resolution specification to guide implementers
toward common DID URL implementation patterns.

Elaborate upon when DID Documents are understood to start existing.

Convert PNG diagrams to SVG diagrams.

Rearrange order of Appendices to improve readability.

Update the IANA guidance as a result of the IETF Media Type Maintenance
Working Group efforts.

Add links to use cases document.

Add warning related to [

MULTIBASE

] and

publicKeyMultibase

.

Remove at risk issue markers for features that gained enough implementation
experience.

Finalize the Editors, Authors, and Acknowledgements information.

Changes since the

First Candidate
Recommendation

include:

Addition of at risk markers to most of the DID Parameters, the data model
datatypes that are expected to not be implemented, and the
application/did+ld+json media type. This change resulted from the DID WG's
decision to perform a second Candidate Recommendation phase. All other
changes were either editorial or predicted in "at risk" issue markers.

Removal of the at risk issue marker for the

method-specific-id

ABNF rule
and for

nextUpdate

and

```

Thus we need to translate to Chinese, preserving technical terms like DID, DID controller, DID subject, DID document, graph model, arcs, nodes, verification methods, cryptographic algorithm, multi-sig, m-of-n, etc. Also terms like "W3C", "IANA", "IETF". Keep Chinese formatting.

We should produce a Chinese translation, with proper Chinese punctuation. Keep terms like "DID", "DID controller", "DID subject", "DID Document" in English or maybe Chinese transliteration? Typically in Chinese translation of technical specs, they keep English terms for clarity. But we can also translate "controller" to "控制器", "subject" to "主题", "document" to "文档". But for technical terms, many specs keep "DID" as is and "DID controller" as "DID 控制器". For clarity, we could do "DID 控制器", "DID 主体", "DID 文档". But need to be consistent.

The user wants "keep technical terms accurate". So we should translate all English terms to Chinese but keep acronyms and proper nouns like "W3C", "IANA", "IETF", "DID", "URL", "PNG", "SVG", "IoT", "multi-sig", "m-of-n". Keep them as English. Also "Figure" could be translated as "图". "Set #2" maybe "集合 #2". The figure descriptions are long, we need to translate them, preserving the sense.

We need to handle line breaks and formatting: The original text has blank lines separating sections, etc. The translation should preserve the structure: like "B.9.2", "B.10", "B.10.1", etc.

Thus we produce Chinese translation.

Given the length, we need to produce a full translation.

We'll start from the beginning.

First line: "is also the

DID
controller

." That seems incomplete; maybe it's part of a sentence from previous text. The translation can start "也是 DID 控制器". Then "This is the case when an individual or organization creates a DID to self-identify." -> "在个人或组织创建 DID 以进行自我标识时，就是这种情况。"

Then "Figure 10" -> "图 10". Then "The DID subject is the same entity as the DID controller." -> "DID 主体 与 DID 控制器 为同一实体。". Then "See also: narrative description." -> "另请参阅：叙述性描述。"

Then the description of figure 10.

We must translate the diagram description.

Original: "Two small black circles appear in the diagram, one on the upper left, labeled, "DID Controller", and one on the upper right, labeled "DID Subject". A solid red arrow extends from the DID Controller circle to the DID Subject circle, labeled "DID" in large bold text above the arrow, and "Identifies" in small italic text beneath the arrow. A dotted red double-ended arrow, labeled "Equivalence", extends between the two circles, forming an arc in the space between and above them. In the lower part of the diagram is a rectangle with bent corner, outlined in black, containing the label "DID Document". Arrows point between this DID Document rectangle and the small black circles for DID Controller and DID Subject, with italic labels, as follows. A blue arrow points from the DID Document to the DID Subject, labeled, "Describes". A green arrow points from the DID Controller to the DID Document, labeled "Controls". A green arrow points from the DID Document to the DID Controller, in an outward arc, labeled, "Controller". A dotted red arrow, labeled "Resolves to", extends from the DID controller starting to the right, branching off from the arrow to the DID Subject, then curving downward to point to the DID Document."

We translate each piece.

"Two small black circles appear in the diagram, one on the upper left, labeled, "DID Controller", and one on the upper right, labeled "DID Subject"." -> "图中出现两个小黑圆圈，左上方的标记为 “DID Controller”，右上方的标记为 “DID Subject”。"

"A solid red arrow extends from the DID Controller circle to the DID Subject circle, labeled "DID" in large bold text above the arrow, and "Identifies" in small italic text beneath the arrow." -> "一条实心红色箭头从 DID Controller 圆圈指向 DID Subject 圆圈，箭头上方用大号粗体文字标记为 “DID”，下方用小号斜体文字标记为 “Identifies”。"

"A dotted red double-ended arrow, labeled "Equivalence", extends between the two circles, forming an arc in the space between and above them." -> "一条红色虚线双头箭头（标记为 “Equivalence”）在两个圆圈之间延伸，在它们之间的空间形成一条弧线。"

"In the lower part of the diagram is a rectangle with bent corner, outlined in black, containing the label "DID Document"." -> "在图的下方，有一个带折角的矩形，黑色轮廓，内部包含标签 “DID Document”。"

"Arrows point between this DID Document rectangle and the small black circles for DID Controller and DID Subject, with italic labels, as follows." -> "箭头在该 DID Document 矩形与 DID Controller 和 DID Subject 的小黑圆圈之间相连，带有斜体标签，具体如下。"

"A blue arrow points from the DID Document to the DID Subject, labeled, "Describes"." -> "一条蓝色箭头从 DID Document 指向 DID Subject，标记为 “Describes”。"

"A green arrow points from the DID Controller to the DID Document, labeled "Controls"." -> "一条绿色箭头从 DID Controller 指向 DID Document，标记为 “Controls”。"

"A green arrow points from the DID Document to the DID Controller, in an outward arc, labeled, "Controller"." -> "一条绿色箭头从 DID Document 指向 DID Controller，沿外部弧线，标记为 “Controller”。"

"A dotted red arrow, labeled "Resolves to", extends from the DID controller starting to the right, branching off from the arrow to the DID Subject, then curving downward to point to the DID Document." -> "一条红色虚线箭头（标记为 “Resolves to”）从 DID Controller 向右延伸，从指向 DID Subject 的箭头分叉出来，然后向下弯曲指向 DID Document。"

Then "From a graph model perspective, even though the nodes identified as the DID controller and DID subject in Figure 10 are distinct, there is a logical arc connecting them to express a semantic equivalence relationship." -> "从图模型的角度来看，尽管在图 10 中标识为 DID controller 和 DID subject 的节点是不同的，但存在一条逻辑弧将它们连接起来，以表达语义等价关系。"

Now "B.9.2 Set #2: The DID subject is not the DID controller" -> "B.9.2 集合 #2：DID 主体 不是 DID 控制器". Actually "Set #2:" maybe "集合 #2：". Could also be "场景 #2：". Use "集合 #2".

"The second case is when the DID subject is a separate entity from the DID controller." -> "第二种情况是 DID 主体 与 DID 控制器 为不同的实体。"

"This is the case when, for example, a parent creates and maintains control of a DID for a child; a corporation creates and maintains control of a DID for a subsidiary; or a manufacturer creates and maintains control of a DID for a product, an IoT device, or a digital file." -> "例如，父母为孩子创建并维护 DID 的控制权；公司为子公司创建并维护 DID 的控制权；或制造商为产品、物联网设备或数字文件创建并维护 DID 的控制权。"

"From a graph model perspective, the only difference from Set 1 that there is no equivalence arc relationship between the DID subject and DID controller nodes." -> "从图模型的角度来看，与集合 1 唯一的区别是 DID 主体 和 DID 控制器 节点之间没有等价弧关系。"

"B.10 Multiple DID controllers" -> "B.10 多个 DID 控制器". Keep as "多个 DID 控制器".

"A DID document might have more than one DID controller. This can happen in one of two ways." -> "DID 文档可能拥有多个 DID 控制器。这可以通过以下两种方式之一实现。"

"B.10.1 Independent Control" -> "B.10.1 独立控制". "In this case, each of the DID controllers might act on its own, i.e., each one has full power to update the DID document independently." -> "在这种情况下，每个 DID 控制器都可以独立行动，即每个控制器都有完整权限独立更新 DID 文档。"

"From a graph model perspective, in this configuration:" -> "从图模型的角度来看，在此配置中："

"Each additional DID controller is another distinct graph node (which might be identified by its own DID)." -> "每个额外的 DID 控制器都是另一个独立的图节点（可能由其自己的 DID 标识）。"

"The same arcs ("controls" and "controller") exist between each DID controller and the DID document." -> "每个 DID 控制器与 DID 文档之间都存在相同的弧（“controls”和“controller”）。"

"Figure 11 Multiple independent DID controllers that can each act independently. See also: Text Description" -> "图 11 多个独立的 DID 控制器，每个都可以独立行动。另请参阅：文本说明。"

Then figure description: "Three black circles appear on the left, vertically, each labeled "DID Controller". From each of these circles, a pair of green arrows extends towards the center of the diagram, to a single rectangle, labeled "DID Document". The rectangle has the lower right corner cut and bent inward to form a small triangle, as if to represent a physical piece of paper with curled corner. Each pair of green arrows consists of one arrow pointing from the black circle to the rectangle, labeled "Controls", and one pointing in the opposite direction, from the rectangle to the black circle, labeled "Controller". From the right of the

# 中文翻译

**nextVersionId**

**。**

**明确说明**

**equivalentId**

**和**

**canonicalId**

**是可选的。**

**新增"放大攻击"和"密码套件"的定义。**

**将**

**publicKeyBase58**

**替换为**

**publicKeyMultibase**

**。**

**更新了 DID 文档示例章节。**

**对"安全注意事项"章节进行了大量编辑整理。**

**自首个公开工作草案以来的变更包括：**

**引入了一种抽象数据模型，可序列化为多种表示形式，包括 JSON 和 JSON-LD。**

**引入了 DID 规范注册表，用于注册扩展属性、表示、DID 解析输入元数据和输出元数据、DID 文档元数据、DID 参数和 DID 方法。**

**将 DID 文档元数据（如创建时间和更新时间）与 DID 文档属性分离。**

**移除了 DID 文档中的嵌入式证明。**

**新增验证关系，用于身份验证、断言、密钥协商、能力调用和能力委托。**

**支持将多个标识符与 DID 文档关联，如 DID 控制器（也称为等价 ID 和规范 ID）。**

**通过减少 DID 文档中可能包含个人身份信息的内容来增强隐私保护。**

**新增了关于安全注意事项和隐私注意事项的大篇幅章节。**

**新增了"表示"章节，详细说明了抽象数据模型如何以多种不同格式生成和消费，以及所有表示形式、生产者和消费者的通用规则。**

**新增章节详细说明了所有 DID 解析器需要公开的 DID 解析和 DID URL 解引用接口定义，以及这些过程的输入和输出。**

**附录中的 DID 文档示例提供了更复杂的 DID 文档序列化示例。**

**针对 DID Core 中指定的多种表示形式的 IANA 注意事项。**

**移除了"未来工作"章节，因为大部分工作现已完成。**

**新增致谢章节。**

**D. 致谢**

**工作组对主席 Brent Zundel 和 Dan Burnett，以及 W3C 工作人员联系人 Ivan Herman 致以深切的感谢和衷心的谢意，感谢他们不懈努力推动工作组朝着富有成效的方向前进，并引领我们穿越标准制定过程中深邃而危险的水域。**

**工作组衷心感谢为创建本规范所做的工作，并向那些在深刻影响我们工作的技术和规范方面付出努力的的个人致以诚挚的谢意。特别是要感谢 Phil Zimmerman、Jon Callas、Lutz Donnerhacke、Hal Finney、David Shaw 和 Rodney Thayer 在 20 世纪 90 年代和 2000 年代对优良保密协议（PGP）所做的工作。**

**在 2010 年代中期，去中心化标识符的初步实现是与 Jeremie Miller 的 Telehash 项目以及由 Dave Longley 和 Manu Sporny 领导的 W3C 网络支付社区组的工作合作构建的。大约一年后，XDI.org 注册表工作组开始探索用于替换其现有标识符注册表的去中心化技术。一些最早探索去中心化标识符概念的学术论文可以追溯到 Christopher Allen 召集的前几次"重启网络信任"研讨会。这项工作促成了 Christopher Allen、Drummond Reed、Les Chasen、Manu Sporny 和 Anil John 之间的重要合作。Anil 看到了这项技术的潜力，并分配了首批政府资金来探索这一领域。如果没有 Anil John 多年的支持和指导，去中心化标识符不太可能达到今天的成就。在"重启网络信任"研讨会上进一步完善的成果产生了首个实现者文档，由 Drummond Reed、Les Chasen、Christopher Allen 和 Ryan Grant 编辑。贡献者包括 Manu Sporny、Dave Longley、Jason Law、Daniel Hardman、Markus Sabadello、Christian Lundkvist 和 Jonathan Endersby。这项初始工作随后合并到 W3C 凭证社区组，进一步孵化，然后过渡到 W3C 去中心化标识符工作组进行全球标准化。**

**本规范部分工作由美国国土安全部（DHS）科学技术理事会根据合同 HSHQDC-16-R00012-H-SB2016-1-002 和 HSHQDC-17-C-00019，以及美国国土安全部硅谷创新计划根据合同 70RSAT20T00000010、70RSAT20T00000029、70RSAT20T00000030、70RSAT20T00000045、70RSAT20T00000003 和 70RSAT20T00000033 提供资助。本规范的内容不一定反映美国政府的立场或政策，不应从中推断任何官方认可。**

**本规范的部分工作还由欧盟 StandICT.eu 计划根据分包受助合同编号 CALL05/19 提供资助。本规范的内容不一定反映欧盟的立场或政策，不应从中推断任何官方认可。**

**本规范的工作也得到了"重启网络信任"社区的支持，该社区由 Christopher Allen、Shannon Appelcline、Kiara Robles、Brian Weller、Betty Dhamers、Kaliya Young、Kim Hamilton Duffy、Manu Sporny、Drummond Reed、Joe Andrieu 和 Heather Vescent 推动。本规范的开发也得到了 W3C 凭证社区组的支持，该社区组由 Kim Hamilton Duffy、Joe Andrieu、Christopher Allen、Heather Vescent 和 Wayne Chang 担任主席。互联网身份 Workshop 的参与者由 Phil Windley、Kaliya Young、Doc Searls 和 Heidi Nobantu Saul 推动，也通过无数次工作会议支持了这项工作，这些会议旨在讨论、改进和向参与者宣传本规范。**

**工作组感谢以下个人对本规范的贡献（按字母顺序排列，GitHub 用户名以 @ 开头，按姓排序）：Denis Ah-Kang、Nacho Alamillo、Christopher Allen、Joe Andrieu、Antonio、Phil Archer、George Aristy、Baha、Juan Benet、BigBlueHat、Dan Bolser、Chris Boscolo、Pelle Braendgaard、Daniel Buchner、Daniel Burnett、Juan Caballero、@cabo、Tim Cappalli、Melvin Carvalho、David Chadwick、Wayne Chang、Sam Curren、Hai Dang、Tim Daubenschütz、Oskar van Deventer、Kim Hamilton Duffy、Arnaud Durand、Ken Ebert、Veikko Eeva、@ewagner70、Carson Farmer、Nikos Fotiou、Gabe、Gayan、@gimly-jack、@gjgd、Ryan Grant、Peter Grassberger、Adrian Gropper、Amy Guy、Daniel Hardman、Kyle Den Hartog、Philippe Le Hegaret、Ivan Herman、Michael Herman、Alen Horvat、Dave Huseby、Marcel Jackisch、Mike Jones、Andrew Jones、Tom Jones、jonnycrunch、Gregg Kellogg、Michael Klein、@kdenhartog-sybil1、Paul Knowles、@ktobich、David I. Lehn、Charles E. Lehner、Michael Lodder、@mooreT1881、Dave Longley、Tobias Looker、Wolf McNally、Robert Mitwicki、Mircea Nistor、Grant Noble、Mark Nottingham、@oare、Darrell O'Donnell、Vinod Panicker、Dirk Porsche、Praveen、Mike Prorock、@pukkamustard、Drummond Reed、Julian Reschke、Yancy Ribbens、Justin Richer、Rieks、@rknobloch、Mikeal Rogers、Evstifeev Roman、Troy Ronda、Leonard Rosenthol、Michael Ruminer、Markus Sabadello、Cihan Saglam、Samu、Rob Sanderson、Wendy Seltzer、Mehran Shakeri、Jaehoon (Ace) Shim、Samuel Smith、James M Snell、SondreB、Manu Sporny、@ssstolk、Orie Steele、Shigeya Suzuki、Sammotic Switchyard、@tahpot、Oliver Terbu、Ted Thibodeau Jr.、Joel Thorstensson、Tralcan、Henry Tsai、Rod Vagg、Mike Varley、Kaliya "Identity Woman" Young、Eric Welton、Fuqiao Xue、@Yue、Dmitri Zagidulin、@zhanb 和 Brent Zundel。**

**E. IANA 注意事项**

**本节将在本规范成为 W3C 提议推荐后，提交给互联网工程指导小组（IESG）进行审查、批准，并向 IANA 注册。**  

---

### E.1 application/did+json  

**类型名称：** application  
**子类型名称：** did+json  

**必需参数：** 无  

**可选参数：** 无  

**编码注意事项：** 见 RFC 8259 第 11 节。  

**安全注意事项：** 见 RFC 8259 第 12 节 [RFC8259]。  

**互操作性注意事项：** 不适用  

**发布的规范：** https://www.w3.org/TR/did-core/  

**使用此媒体类型的应用：** 任何需要去中心化、持久、密码可验证且可解析的标识符的应用程序。典型的应用包括加密身份系统、去中心化设备网络以及发行或验证 W3C 可验证凭证的网站。  

**附加信息：**  

- **魔术数字（Magic number(s)）：** 不适用  
- **文件扩展名：** .didjson  
- **Macintosh 文件类型代码：** TEXT  

**联系人和电子邮件地址：** Ivan Herman <ivan@w3.org>  

**预期用途：** 通用  

**使用限制：** 无  

**作者：** Drummond Reed, Manu Sporny, Markus Sabadello, Dave Longley, Christopher Allen  

**变更控制器：** W3C  

**与 application/did+json 一起使用的片段标识符** 按照 **Fragment（片段）** 章节中定义的规则处理。  

---

### E.2 application/did+ld+json  

**注：IETF 结构化媒体类型**  

本规范的候选推荐阶段收到了大量针对 **application/did+ld+json** 媒体类型的实现。**application/did+ld+json** 媒体类型在 IANA 的注册正等待 **Media Types with Multiple Suffixes** 问题的解决。预计将在 **IETF Media Type Maintenance Working Group** 继续工作，并在 **Media Types with Multiple Suffixes** RFC 发布后不久，由 **W3C** 完成 **application/did+ld+json** 媒体类型的注册。  

**类型名称：** application  
**子类型名称：** did+ld+json  

**必需参数：** 无  

**可选参数：** 无  

**编码注意事项：** 见 RFC 8259 第 11 节。  

**安全注意事项：** 见 JSON‑LD 1.1 安全注意事项 [JSON‑LD11]。  

**互操作性注意事项：** 不适用  

**发布的规范：** https://www.w3.org/TR/did-core/  

**使用此媒体类型的应用：** 任何需要去中心化、持久、密码可验证且可解析的标识符的应用程序。典型的应用包括加密身份系统、去中心化设备网络以及发行或验证 W3C 可验证凭证的网站。  

**附加信息：**  

- **魔术数字（Magic number(s)）：** 不适用  
- **文件扩展名：** .didjsonld  
- **Macintosh 文件类型代码：** TEXT  

**联系人和电子邮件地址：** Ivan Herman <ivan@w3.org>  

**预期用途：** 通用  

**使用限制：** 无  

**作者：** Drummond Reed, Manu Sporny, Markus Sabadello, Dave Longley, Christopher Allen  

**变更控制器：** W3C  

**与 application/did+ld+json 一起使用的片段标识符** 按照 **JSON‑LD 1.1: application/ld+json** 媒体类型的相关规则处理 [JSON‑LD11]。  

---

## F. 参考文献  

### F.1 规范性引用  

[INFRA] Infra 标准。Anne van Kesteren; Domenic Denicola. WHATWG. Living Standard. URL: https://infra.spec.whatwg.org/  

[JSON‑LD11] JSON‑LD 1.1。Gregg Kellogg; Pierre‑Antoine Champin; Dave Longley. W3C. 2020‑07‑16. W3C 建议。URL: https://www.w3.org/TR/json-ld11/  

[RFC2119] RFC 中用于表示需求级别的关键词。S. Bradner. IETF. 1997‑03. 最佳当前实践。URL: https://www.rfc-editor.org/rfc/rfc2119  

[RFC3552] 编写安全考虑 RFC 文本的指南。E. Rescorla; B. Korver. IETF. 2003‑07. 最佳当前实践。URL: https://www.rfc-editor.org/rfc/rfc3552  

[RFC3986] 统一资源标识符（URI）：通用语法。T. Berners‑Lee; R. Fielding; L. Masinter. IETF. 2005‑01. 互联网标准。URL: https://www.rfc-editor.org/rfc/rfc3986  

[RFC5234] 语法规范的扩展 BNF：ABNF。D. Crocker (编辑); P. Overell. IETF. 2008‑01. 互联网标准。URL: https://www.rfc-editor.org/rfc/rfc5234  

[RFC7517] JSON Web Key (JWK)。M. Jones. IETF. 2015‑05. 提议标准。URL: https://www.rfc-editor.org/rfc/rfc7517  

[RFC7638] JSON Web Key (JWK) 指纹。M. Jones; N. Sakimura. IETF. 2015‑09. 提议标准。URL: https://www.rfc-editor.org/rfc/rfc7638  

[RFC8174] RFC 2119 关键词中大写与小写的歧义。B. Leiba. IETF. 2017‑05. 最佳当前实践。URL: https://www.rfc-editor.org/rfc/rfc8174  

[RFC8259] JavaScript 对象表示法（JSON）数据交换格式。T. Bray (编辑). IETF. 2017‑12. 互联网标准。URL: https://www.rfc-editor.org/rfc/rfc8259  

[url] URL 标准。Anne van Kesteren. WHATWG. Living Standard. URL: https://url.spec.whatwg.org/  

[XMLSCHEMA11-2] W3C XML Schema 定义语言（XSD）1.1 第 2 部分：数据类型。David Peterson; Sandy Gao; Ashok Malhotra; Michael Sperberg‑McQueen; Henry Thompson; Paul V. Biron 等。W3C. 2012‑04‑05. W3C 建议。URL: https://www.w3.org/TR/xmlschema11-2/  

### F.2 信息性引用  

[DID‑RESOLUTION] 去中心化标识符解析。Markus Sabadello; Dmitri Zagidulin. Credentials Community Group. 草案社区组报告。URL: https://w3c-ccg.github.io/did-resolution/  

[DID‑RUBRIC] 去中心化特征评估 v1.0。Joe Andrieu. Credentials Community Group. 草案社区组报告。URL: https://w3c.github.io/did-rubric/  

[DID‑SPEC‑REGISTRIES] DID 规范注册表。Orie Steele; Manu Sporny; Michael Prorock. W3C. 2022‑06‑28. W3C 工作组说明。URL: https://www.w3.org/TR/did-spec-registries/  

[DID‑USE‑CASES] 去中心化标识符的用例与需求。Joe Andrieu; Phil Archer; Kim Duffy; Ryan Grant; Adrian Gropper. W3C. 2021‑03‑17. W3C 工作组说明。URL: https://www.w3.org/TR/did-use-cases/  

[DNS‑DID] DNS 中的去中心化标识符（DID）。Alexander Mayrhofer; Dimitrij Klesev; Markus Sabadello. 2019‑02. 互联网草案。URL: https://datatracker.ietf.org/doc/draft-mayrhofer-did-dns/  

[HASHLINK] 密码学超链接。Manu Sporny. IETF. 2018‑12. 互联网草案。URL: https://tools.ietf.org/html/draft-sporny-hashlink-05  

[IANA‑URI‑SCHEMES] 统一资源标识符（URI）方案。IANA. URL: https://www.iana.org/assignments/uri-schemes/uri-schemes.xhtml  

[MATRIX‑URIS] Matrix URI —— 关于 Web 架构的想法。Tim Berners‑Lee. 1996‑12. 个人视图。URL: https://www.w3.org/DesignIssues/MatrixURIs.html  

[MULT

The user asks: "Translate to Chinese, keep technical terms accurate". Then they provide a big chunk of text that seems like a references/bibliography or footnotes from a specification. This appears to be from the DID (Decentralized Identifier) spec, maybe the W3C DID spec. They include references to RFCs (HTTP, URN), a W3C Verifiable Credentials Data Model, and many section references with permalinks, "Referenced in:" sections, etc.

The user likely wants the entire text translated into Chinese while preserving technical terms. So the output should be a Chinese translation of the entire block.

We need to keep the formatting: The original text includes references and permalink markers. We need to preserve the structural layout: The references with brackets, titles, authors, organization, date, type, URL, and "Permalink" lines with references. Also there is a section "Referenced in:" with many bullet points and numbers. We need to translate each piece to Chinese while preserving the technical terms and formatting.

Potential issues: The references include abbreviations like "RFC7231", "RFC8141", "VC-DATA-MODEL". Should we translate them? Usually we keep the references as is but translate the description. For example: "[RFC7231] Uniform Resource Names (URNs)" actually the first reference is "[RFC7231]" about HTTP. Wait the first entry:

[RFC7231]

Uniform Resource Names (URNs) ??? Actually the original text:

[RFC7231]

Uniform Resource Names (URNs)

. R. Fielding, Ed.; J. Reschke, Ed..  IETF. June 2014. Proposed Standard. URL:

https://httpwg.org/specs/rfc7231.html

Hold on: The original text appears to be mis-formatted. It says:

[RFC7231]

Uniform Resource Names (URNs)

. R. Fielding, Ed.; J. Reschke, Ed..  IETF. June 2014. Proposed Standard. URL:

https://httpwg.org/specs/rfc7231.html

But that's wrong: RFC 7231 is "Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content". The "Uniform Resource Names (URNs)" is RFC 8141. So the text has a mistake: It shows "[RFC8141] Uniform Resource Names (URNs)" but then the second entry.

Wait, the text is:

[RFC8141]

Uniform Resource Names (URNs)

. P. Saint-Andre; J. Klensin.  IETF. April 2017. Proposed Standard. URL:

https://www.rfc-editor.org/rfc/rfc8141

[VC-DATA-MODEL]

Verifiable Credentials Data Model v1.1

...

So the first entry is [RFC7231] maybe incorrectly paired with "Uniform Resource Names (URNs)"? Actually the text shows:

Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content

. R. Fielding, Ed.; J. Reschke, Ed..  IETF. June 2014. Proposed Standard. URL:

https://httpwg.org/specs/rfc7231.html

[RFC8141]

Uniform Resource Names (URNs)

. P. Saint-Andre; J. Klensin.  IETF. April 2017. Proposed Standard. URL:

https://www.rfc-editor.org/rfc/rfc8141

[VC-DATA-MODEL]

Verifiable Credentials Data Model v1.1

...

Thus the first entry is "[RFC7231]" is the title line above: "Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content". But the original text lumps them together? Actually the original text includes:

Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content

. R. Fielding, Ed.; J. Reschke, Ed..  IETF. June 2014. Proposed Standard. URL:

https://httpwg.org/specs/rfc7231.html

[RFC8141]

Uniform Resource Names (URNs)

...

Thus we need to translate that as well. But the text is somewhat broken, with a missing [RFC7231] tag at the beginning. But we need to produce translation accordingly.

Thus we need to translate:

- Title: "Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content"
- Author(s): "R. Fielding, Ed.; J. Reschke, Ed."
- Organization: "IETF"
- Date: "June 2014"
- Type: "Proposed Standard"
- URL: "https://httpwg.org/specs/rfc7231.html"

Then [RFC8141] entry:

- Title: "Uniform Resource Names (URNs)"
- Author(s): "P. Saint-Andre; J. Klensin."
- Organization: "IETF"
- Date: "April 2017"
- Type: "Proposed Standard"
- URL: "https://www.rfc-editor.org/rfc/rfc8141"

Then [VC-DATA-MODEL] entry:

- Title: "Verifiable Credentials Data Model v1.1"
- Authors: "Manu Sporny; Grant Noble; Dave Longley; Daniel Burnett; Brent Zundel; Kyle Den Hartog."
- Organization: "W3C"
- Date: "3 March 2022"
- Type: "W3C Recommendation"
- URL: "https://www.w3.org/TR/vc-data-model/"

After that, the rest is a long list of "Permalink" and "Referenced in:" sections, referencing sections of the DID spec.

We need to translate that to Chinese. For each "Permalink", we need to translate "Permalink" maybe as "永久链接". For each "Referenced in:" we translate to "引用章节：" or "被引用章节：" perhaps. The section numbers and titles need translation? Possibly we can keep the section numbers (like § 1.4 Conformance) unchanged, but translate the heading text: "Conformance" -> "一致性". The heading of sections may be Chinese translations.

But the instruction: "Translate to Chinese, keep technical terms accurate". So for the text that is English headings, we should translate them to Chinese but keep technical terms like "DID", "URI", "URL", "URN", "W3C", "IETF", "RFC", "VC", "Data Model", "Verifiable Credentials", etc. The phrase "Referenced in:" maybe "引用章节：" is fine. "Permalink" -> "永久链接". The "↑" arrow maybe keep as is or translate as "返回"? But we can keep "↑".

We need to preserve the structure: bracket references [RFC7231], [RFC8141], [VC-DATA-MODEL] remain unchanged. The titles and descriptions are translated. For the many references to sections, we need to translate the titles. For example:

Referenced in:

§ 1.4 Conformance

(2)

Should become something like:

引用章节：

§1.4 一致性

(2)

But also the numbers like (2) refer to footnote or citation count. Keep them.

Thus we need to output a Chinese translation of the whole block, preserving line breaks and bullet-like formatting. The user didn't specify a particular style, just "translate to Chinese, keep technical terms accurate". So we can provide a translation line by line.

Now let's analyze the original text more thoroughly.

Original:

```
Hypertext Transfer Protocol (HTTP/1.1): Semantics and Content

. R. Fielding, Ed.; J. Reschke, Ed..  IETF. June 2014. Proposed Standard. URL:

https://httpwg.org/specs/rfc7231.html

[RFC8141]

Uniform Resource Names (URNs)

. P. Saint-Andre; J. Klensin.  IETF. April 2017. Proposed Standard. URL:

https://www.rfc-editor.org/rfc/rfc8141

[VC-DATA-MODEL]

Verifiable Credentials Data Model v1.1

. Manu Sporny; Grant Noble; Dave Longley; Daniel Burnett; Brent Zundel; Kyle Den Hartog.  W3C. 3 March 2022. W3C Recommendation. URL:

https://www.w3.org/TR/vc-data-model/

↑

Permalink

Referenced in:

§ 1.4 Conformance

(2)

Permalink

Referenced in:

§ 1.4 Conformance

(2)

§ 7.1 DID Resolution

Permalink

Referenced in:

§ 5.4 Services

§ 6.1 Production and Consumption

(2)

(3)

(4)

(5)

§ 6.2.1 Production

(2)

§ 6.3.1 Production

(2)

(3)

Permalink

Referenced in:

§ 5.4 Services

§ 6.1 Production and Consumption

(2)

(3)

(4)

(5)

(6)

§ 6.2.2 Consumption

(2)

(3)

§ 6.3.1 Production

§ 6.3.2 Consumption

(2)

Permalink

Referenced in:

§ 8.3 Security Requirements

Permalink

Referenced in:

§ 1.1 A Simple Example

§ 2. Terminology

(2)

(3)

§ 5.2 Verification Methods

§ 5.3.1 Authentication

(2)

(3)

(4)

(5)

(6)

§ B.12 Changing the DID controller

Permalink

Referenced in:

§ 5.2.1 Verification Material

Permalink

Referenced in:

§ Abstract

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

§ 1.1 A Simple Example

(2)

(3)

§ 1.2 Design Goals

(2)

(3)

(4)

§ 1.3 Architecture Overview

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

(13)

(14)

§ 1.4 Conformance

(2)

(3)

(4)

(5)

§ 2. Terminology

(2)

(3)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

(13)

(14)

(15)

(16)

(17)

(18)

§ 3. Identifier

(2)

§ 3.1 DID Syntax

(2)

§ 3.2.1 DID Parameters

(2)

(3)

§ 3.2.2 Relative DID URLs

§ 5. Core Properties

§ 5.1.1 DID Subject

(2)

§ 5.1.2 DID Controller

(2)

§ 5.1.3 Also Known As

§ 5.2.1 Verification Material

§ 5.3.1 Authentication

§ 6.1 Production and Consumption

(2)

§ 7.1 DID Resolution

(2)

(3)

(4)

§ 7.1.2 DID Resolution Metadata

§ 7.1.3 DID Document Metadata

(2)

(3)

(4)

(5)

(6)

(7)

(8)

§ 7.2 DID URL Dereferencing

§ 7.3 Metadata Structure

§ 8. Methods

(2)

§ 8.1 Method Syntax

(2)

§ 8.2 Method Operations

(2)

(3)

§ 8.3 Security Requirements

(2)

(3)

§ 9. Security Considerations

(2)

§ 9.2 Proving Control and Binding

(2)

§ Proving Control of a DID and/or DID Document

(2)

(3)

(4)

§ Binding to Physical Identity

(2)

(3)

(4)

§ 9.4 Non-Repudiation

§ 9.5 Notification of DID Document Changes

(2)

(3)

§ 9.6 Key and Signature Expiration

§ 9.7 Verification Method Rotation

§ 9.8 Verification Method Revocation

§ Revocation Semantics

(2)

(3)

(4)

(5)

(6)

§ 9.9 DID Recovery

(2)

(3)

§ 9.10 The Role of Human-Friendly Identifiers

(2)

(3)

§ 9.11 DIDs as Enhanced URNs

(2)

(3)

(4)

(5)

(6)

(7)

(8)

§ 9.14 Equivalence Properties

(2)

§ 9.16 Persistence

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

§ 10. Privacy Considerations

(2)

(3)

§ 10.1 Keep Personal Data Private

§ 10.2 DID Correlation Risks

(2)

(3)

(4)

(5)

(6)

§ 10.3 DID Document Correlation Risks

(2)

(3)

(4)

(5)

(6)

§ 10.4 DID Subject Classification

(2)

§ 10.5 Herd Privacy

§ 10.6 Service Privacy

(2)

§ Maintaining Herd Privacy

(2)

(3)

(4)

§ B.2 Creation of a DID

(2)

(3)

§ B.3 Determining the DID subject

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

(13)

(14)

§ B.4 Referring to the DID document

(2)

(3)

§ B.5 Statements in the DID document

§ B.6 Discovering more information about the DID subject

(2)

§ B.7 Serving a representation of the DID subject

(2)

§ B.8 Assigning DIDs to existing web resources

(2)

(3)

(4)

§ B.9.1 Set #1: The DID subject is the DID controller

§ B.9.2 Set #2: The DID subject is not the DID controller

(2)

(3)

§ B.10.1 Independent Control

§ B.11 Changing the DID subject

(2)

(3)

Permalink

Referenced in:

§ 5.4 Services

Permalink

Referenced in:

§ Abstract

§ 1.1 A Simple Example

§ 1.2 Design Goals

§ 1.3 Architecture Overview

(2)

§ 2. Terminology

§ Path

§ 5.1 Identifiers

§ 5.1.2 DID Controller

(2)

(3)

§ 5.2 Verification Methods

(2)

§ 5.3.1 Authentication

(2)

§ 5.3.5 Capability Delegation

§ 8.2 Method Operations

(2)

(3)

§ 9.5 Notification of DID Document Changes

(2)

§ Revocation Semantics

§ 9.10 The Role of Human-Friendly Identifiers

§ 9.11 DIDs as Enhanced URNs

(2)

(3)

(4)

(5)

(6)

§ 10. Privacy Considerations

§ 10.1 Keep Personal Data Private

§ 10.2 DID Correlation Risks

(2)

§ 10.4 DID Subject Classification

§ B.3 Determining the DID subject

§ B.4 Referring to the DID document

(2)

§ B.5 Statements in the DID document

§ B.6 Discovering more information about the DID subject

§ B.9 The relationship between DID controllers and DID subjects

§ B.9.1 Set #1: The DID subject is the DID controller

(2)

(3)

§ B.9.2 Set #2: The DID subject is not the DID controller

(2)

§ B.10 Multiple DID controllers

§ B.10.1 Independent Control

(2)

(3)

(4)

§ B.10.2 Group Control

(2)

(3)

(4)

(5)

(6)

(7)

§ B.11 Changing the DID subject

§ B.12 Changing the DID controller

(2)

(3)

(4)

Permalink

Referenced in:

§ 2. Terminology

(2)

Permalink

Referenced in:

§ Abstract

(2)

§ 1.1 A Simple Example

(2)

§ 1.2 Design Goals

§ 1.3 Architecture Overview

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

§ 1.4 Conformance

(2)

(3)

(4)

(5)

§ 2. Terminology

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

(13)

(14)

(15)

(16)

(17)

(18)

(19)

(20)

§ 3.2 DID URL Syntax

§ Fragment

§ 3.2.1 DID Parameters

(2)

(3)

(4)

(5)

(6)

§ 3.2.2 Relative DID URLs

(2)

(3)

(4)

§ 4. Data Model

(2)

(3)

(4)

§ 5. Core Properties

(2)

(3)

§ 5.1 Identifiers

§ 5.1.1 DID Subject

(2)

(3)

(4)

(5)

§ 5.1.2 DID Controller

(2)

(3)

(4)

§ 5.1.3 Also Known As

§ 5.2 Verification Methods

(2)

(3)

(4)

§ 5.2.1 Verification Material

(2)

§ 5.2.2 Referring to Verification Methods

(2)

§ 5.3 Verification Relationships

(2)

(3)

(4)

(5)

§ 5.3.1 Authentication

(2)

(3)

(4)

(5)

§ 5.3.2 Assertion

§ 5.3.4 Capability Invocation

(2)

§ 5.4 Services

§ 6. Representations

§ 6.1 Production and Consumption

(2)

(3)

(4)

(5)

(6)

(7)

§ 6.2.1 Production

(2)

(3)

§ 6.2.2 Consumption

(2)

(3)

(4)

§ 6.3.1 Production

(2)

(3)

§ 6.3.2 Consumption

(2)

§ 7. Resolution

§ 7.1 DID Resolution

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

§ 7.1.1 DID Resolution Options

§ 7.1.2 DID Resolution Metadata

§ 7.1.3 DID Document Metadata

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

(13)

(14)

(15)

§ 7.2 DID URL Dereferencing

(2)

§ 7.3

The user wants translation to Chinese, keep technical terms accurate. They gave a huge list of headings and subheadings. They likely want a translation of those headings. The content is basically a structured list of headings from the DID (Decentralized Identifiers) spec, presumably. The user wants the translation of the headings, maybe also any bullet numbers. They provided some items with (2), (3) etc which likely refer to footnotes or sub-points. The instruction: "Translate to Chinese, keep technical terms accurate". So we need to translate each heading into Chinese while preserving technical terms like DID, DID URL, DID Document, Decentralized Identifiers, method syntax, etc. We must keep technical terms as they are or translate them appropriately, but maintain accuracy. Usually "DID" is left as "DID" (or "去中心化标识符" could be used, but in the spec they often keep "DID"). The translation can use "去中心化标识符 (DID)" for the first mention. We can decide to keep "DID" as is.

We need to produce a list of Chinese translations for each entry. The user gave the headings and subheadings separated by line breaks, some duplicates (like multiple "Permalink" entries). The headings have parentheses "(2)", "(3)" etc, indicating maybe footnotes or "see also". The user wants them translated; the numbering remains. It might be better to keep the "(2)" etc as is. Possibly they want each line's translation.

We should also keep the structure (like "§ B.6 Discovering more information about the DID subject") and "Referenced in:" lines.

Thus we should output Chinese translations of each line, preserving the formatting.

Thus final answer: a Chinese translation of all headings. Let's do that.

We'll produce a Chinese translation for each heading: "§ B.6 发现更多关于 DID 主体的信息", "§ B.8 为现有 Web 资源分配 DID", etc. For "Permalink" maybe just "永久链接". For "Referenced in:" we can translate "被引用章节：" or "引用位置：". Usually "Referenced in:" is "被引用章节：" or "引用来源". The spec uses "Referenced in:" to list sections referencing the current section. So translate "被引用章节：" maybe.

We must ensure that "DID subject" is "DID 主体". "DID controller" is "DID 控制器". "DID Document" is "DID 文档". "DID URL Dereferencing" is "DID URL 解引用". "Method Syntax" is "方法语法". "Method operations" is "方法操作". "Security Requirements" is "安全要求". "Privacy Requirements" is "隐私要求". "Choosing DID Resolvers" is "选择 DID 解析器". "Proving Control of a DID and/or DID Document" is "证明对 DID 和/或 DID 文档的控制". "Non-Repudiation" is "不可否认性". "Verification Method Rotation" is "验证方法轮换". "Verification Method Revocation" is "验证方法撤销". "Revocation Semantics" is "撤销语义". "Revocation in Trustless Systems" is "无信任系统中的撤销". "DID Recovery" is "DID 恢复". "DIDs as Enhanced URNs" is "DID 作为增强的 URN". "Immutability" is "不可变性". "Equivalence Properties" is "等价属性". "Persistence" is "持久性". "Keep Personal Data Private" is "保护个人数据隐私". "Herd Privacy" is "群体隐私". "Service Endpoint Alternatives" is "服务端点替代方案". "Creation of a DID" is "DID 的创建". "Determining the DID subject" is "确定 DID 主体". "Referring to the DID document" is "引用 DID 文档". "Serving a representation of the DID subject" is "提供 DID 主体的表示". "Multiple DID controllers" is "多个 DID 控制器". "Independent Control" is "独立控制". "Changing the DID subject" is "更改 DID 主体". "Changing the DID controller" is "更改 DID 控制器". "Path" is "路径". "Query" is "查询". "Fragment" is "片段". "Metadata Structure" is "元数据结构". "Data Model" is "数据模型". "Extensibility" is "可扩展性". "Representations" is "表示". "Production and Consumption" is "生成与消费". "JSON" is "JSON". "JSON-LD" is "JSON-LD". "Production" is "生成". "Consumption" is "消费". "Resolution" is "解析". "DID Resolution" is "DID 解析". "DID Resolution Metadata" is "DID 解析元数据". "DID Document Metadata" is "DID 文档元数据". "DID Resolution Options" is "DID 解析选项". "DID URL Dereferencing Options" is "DID URL 解引用选项". "DID URL Dereferencing Metadata" is "DID URL 解引用元数据". "Key and Signature Expiration" is "密钥和签名过期". "Notification of DID Document Changes" is "DID 文档变更通知". "Authentication Service Endpoints" is "认证服务端点". "Service Privacy" is "服务隐私". "DID Correlation Risks" is "DID 关联风险". "DID Subject Classification" is "DID 主体分类". "Maintaining Herd Privacy" is "维护群体隐私". "Service properties" is "服务属性". "Also Known As" is "亦称". "Verification Methods" is "验证方法". "Verification Relationships" is "验证关系". "Authentication" is "认证". "Assertion" is "断言". "Key Agreement" is "密钥协议". "Capability Invocation" is "能力调用". "Capability Delegation" is "能力委托". "Service Endpoint Alternatives" we already have. "Core Properties" is "核心属性". "Identifiers" is "标识符". "Data Model" etc.

We need to keep the "§" symbol? Typically Chinese translations can keep the "§" as is, but maybe better to keep it.

We also need to translate "DID Document properties" as "DID 文档属性". "Service properties" as "服务属性". "DID Document properties" maybe "DID 文档属性". "Service properties" is "服务属性". "DID Document properties" may also be "DID 文档属性". Keep as is.

"Proving Control of a DID and/or DID Document" is "证明对 DID 和/或 DID 文档的控制". Keep.

We should produce a list with Chinese translations for each line. It's long, but we need to be thorough.

The user may want the translation for all headings, not for the content. So we will output a list.

We must keep the parentheses with numbers. The headings may appear multiple times; we can preserve them.

Thus final answer: a Chinese translation.

Now, we need to consider that the user might want a line-by-line translation with each heading preceded by "§" and Chinese translation. Provide the translation in Chinese, preserving the numbers and parentheses.

Also "Permalink" maybe not needed to translate, but we can translate as "永久链接". The user might want "Permalink" as is. It's fine.

Better to provide translation for all headings, also for "Referenced in:" we can translate to "被引用章节：" for clarity.

Thus produce a list:

§ B.6 发现更多关于 DID 主体的信息

(2)

(3)

...

And so on.

Make sure to keep line breaks and formatting similar.

We'll produce the translation accordingly.

Now let's go through each line as given in the prompt.

Given the input:

```
§ B.6 Discovering more information about the DID subject

(2)

(3)

§ B.8 Assigning DIDs to existing web resources

(2)

§ B.10 Multiple DID controllers

§ B.10.1 Independent Control

(2)

§ B.11 Changing the DID subject

(2)

§ B.12 Changing the DID controller

(2)

(3)

(4)

Permalink

Referenced in:

§ 2. Terminology

§ Fragment

(2)

(3)

(4)

(5)

§ 7.2 DID URL Dereferencing

(2)

§ 8.1 Method Syntax

Permalink

Referenced in:

§ 1.1 A Simple Example

§ 1.2 Design Goals

§ 1.3 Architecture Overview

(2)

(3)

(4)

(5)

§ 1.4 Conformance

(2)

(3)

(4)

§ 2. Terminology

(2)

(3)

(4)

§ 3. Identifier

§ 3.1 DID Syntax

§ 3.2 DID URL Syntax

§ Path

§ 3.2.1 DID Parameters

(2)

(3)

(4)

(5)

§ 3.2.2 Relative DID URLs

§ 5.1.1 DID Subject

§ 5.1.2 DID Controller

§ 5.3 Verification Relationships

§ 5.3.1 Authentication

(2)

(3)

(4)

§ 7. Resolution

§ 7.1 DID Resolution

§ 7.1.2 DID Resolution Metadata

§ 7.1.3 DID Document Metadata

(2)

(3)

(4)

(5)

(6)

(7)

(8)

§ 7.2 DID URL Dereferencing

§ 8. Methods

(2)

(3)

(4)

(5)

(6)

(7)

§ 8.1 Method Syntax

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

(13)

§ 8.2 Method Operations

(2)

(3)

(4)

(5)

(6)

(7)

(8)

§ 8.3 Security Requirements

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

§ 8.4 Privacy Requirements

(2)

§ 9.1 Choosing DID Resolvers

(2)

(3)

(4)

(5)

§ Proving Control of a DID and/or DID Document

(2)

§ 9.4 Non-Repudiation

§ 9.7 Verification Method Rotation

(2)

(3)

§ 9.8 Verification Method Revocation

(2)

(3)

§ Revocation Semantics

(2)

§ Revocation in Trustless Systems

§ 9.9 DID Recovery

(2)

(3)

(4)

(5)

§ 9.11 DIDs as Enhanced URNs

(2)

§ 9.12 Immutability

(2)

(3)

§ 9.14 Equivalence Properties

(2)

(3)

(4)

(5)

§ 9.16 Persistence

§ 10.1 Keep Personal Data Private

§ 10.5 Herd Privacy

§ Service Endpoint Alternatives

§ B.2 Creation of a DID

(2)

(3)

(4)

(5)

§ B.3 Determining the DID subject

(2)

§ B.4 Referring to the DID document

§ B.7 Serving a representation of the DID subject

(2)

Permalink

Referenced in:

§ 2. Terminology

§ Path

§ 8.1 Method Syntax

Permalink

Referenced in:

§ 2. Terminology

§ Query

§ 8.1 Method Syntax

Permalink

Referenced in:

§ 1.3 Architecture Overview

(2)

§ 2. Terminology

(2)

§ 3.2.1 DID Parameters

§ 5.1.1 DID Subject

§ 7. Resolution

(2)

§ 7.1 DID Resolution

(2)

(3)

§ 7.1.2 DID Resolution Metadata

§ 7.2 DID URL Dereferencing

(2)

§ 7.3 Metadata Structure

§ Proving Control of a DID and/or DID Document

§ 9.4 Non-Repudiation

§ B.4 Referring to the DID document

(2)

Permalink

Referenced in:

§ 1.3 Architecture Overview

(2)

§ 3.2.1 DID Parameters

(2)

§ 5.1.1 DID Subject

§ 7. Resolution

§ 7.1 DID Resolution

(2)

(3)

(4)

§ 7.1.1 DID Resolution Options

§ 7.1.2 DID Resolution Metadata

(2)

§ 7.2 DID URL Dereferencing

§ 8.2 Method Operations

(2)

§ 9.1 Choosing DID Resolvers

(2)

§ 9.6 Key and Signature Expiration

§ 9.12 Immutability

Permalink

Referenced in:

§ 2. Terminology

(2)

§ 3.1 DID Syntax

§ 8. Methods

§ 8.1 Method Syntax

Permalink

Referenced in:

§ Abstract

(2)

(3)

(4)

§ 1.3 Architecture Overview

(2)

(3)

§ 2. Terminology

(2)

(3)

(4)

(5)

(6)

(7)

(8)

§ 3.2 DID URL Syntax

§ 3.2.2 Relative DID URLs

§ 5. Core Properties

§ 5.1 Identifiers

§ 5.1.1 DID Subject

(2)

§ 5.1.2 DID Controller

(2)

§ 5.1.3 Also Known As

(2)

(3)

§ 5.2 Verification Methods

§ 5.3 Verification Relationships

(2)

(3)

§ 5.3.1 Authentication

(2)

§ 5.3.2 Assertion

(2)

§ 5.3.3 Key Agreement

(2)

§ 5.3.4 Capability Invocation

(2)

(3)

§ 5.3.5 Capability Delegation

(2)

(3)

§ 5.4 Services

(2)

§ 7.1.3 DID Document Metadata

(2)

(3)

(4)

(5)

§ 9.3 Authentication Service Endpoints

§ 9.5 Notification of DID Document Changes

§ 9.11 DIDs as Enhanced URNs

§ 10.1 Keep Personal Data Private

(2)

(3)

§ 10.2 DID Correlation Risks

§ 10.4 DID Subject Classification

(2)

(3)

§ 10.5 Herd Privacy

§ 10.6 Service Privacy

§ Maintaining Herd Privacy

(2)

(3)

(4)

(5)

§ B.3 Determining the DID subject

(2)

(3)

(4)

(5)

(6)

§ B.4 Referring to the DID document

(2)

(3)

(4)

(5)

(6)

§ B.5 Statements in the DID document

(2)

(3)

§ B.6 Discovering more information about the DID subject

(2)

(3)

(4)

(5)

§ B.7 Serving a representation of the DID subject

(2)

§ B.9 The relationship between DID controllers and DID subjects

§ B.9.1 Set #1: The DID subject is the DID controller

(2)

(3)

§ B.9.2 Set #2: The DID subject is not the DID controller

(2)

§ B.10.2 Group Control

§ B.11 Changing the DID subject

(2)

Permalink

Referenced in:

§ 1.3 Architecture Overview

(2)

(3)

§ 2. Terminology

(2)

(3)

(4)

(5)

(6)

(7)

(8)

§ 3. Identifier

(2)

§ 3.2 DID URL Syntax

(2)

(3)

§ 3.2.1 DID Parameters

(2)

(3)

(4)

(5)

§ 3.2.2 Relative DID URLs

(2)

(3)

(4)

(5)

(6)

§ 7.2 DID URL Dereferencing

(2)

(3)

(4)

(5)

(6)

(7)

(8)

§ 7.2.2 DID URL Dereferencing Metadata

§ 9.11 DIDs as Enhanced URNs

§ B.7 Serving a representation of the DID subject

Permalink

Referenced in:

§ 1.3 Architecture Overview

(2)

§ 2. Terminology

§ 3.2.1 DID Parameters

§ 7. Resolution

§ 7.2 DID URL Dereferencing

(2)

(3)

(4)

(5)

(6)

(7)

§ 7.2.1 DID URL Dereferencing Options

§ 7.2.2 DID URL Dereferencing Metadata

§ 7.3 Metadata Structure

Permalink

Referenced in:

§ 1.3 Architecture Overview

§ 7.2.2 DID URL Dereferencing Metadata

Permalink

Referenced in:

§ 1.3 Architecture Overview

§ 2. Terminology

§ 8.3 Security Requirements

(2)

§ 10.1 Keep Personal Data Private

Permalink

Referenced in:

Permalink

Referenced in:

§ 1.3 Architecture Overview

(2)

(3)

§ 2. Terminology

§ 3.2 DID URL Syntax

§ Fragment

§ 3.2.1 DID Parameters

(2)

(3)

(4)

(5)

§ 3.2.2 Relative DID URLs

§ 5.2.2 Referring to Verification Methods

§ 7.2 DID URL Dereferencing

(2)

(3)

Permalink

Referenced in:

§ 2. Terminology

(2)

(3)

§ Fragment

(2)

§ 4. Data Model

(2)

§ 4.1 Extensibility

(2)

(3)

(4)

(5)

(6)

§ 6. Representations

(2)

(3)

(4)

(5)

(6)

(7)

§ 6.1 Production and Consumption

(2)

(3)

(4)

(5)

(6)

(7)

(8)

(9)

(10)

(11)

(12)

(13)

(14)

(15)

(16)

(17)

(18)

(19)

(20)

(21)

(22)

§ 6.2 JSON

§ 6.2.1 Production

(2)

§ 6.2.2 Consumption

(2)

(3)

§ 6.3 JSON-LD

(2)

§ 6.3.1 Production

(2)

(3)

(4)

(5)

(6)

(7)

(8)

§ 6.3.2 Consumption

(2)

(3)

(4)

§ 7. Resolution

§ 7.1.1 DID Resolution Options

(2)

(3)

§ 7.1.2 DID Resolution Metadata

(2)

§ 7.2 DID URL Dereferencing


The user wants translation to Chinese, keep technical terms accurate. The user provided a huge list of sections with references. The user says "Translate to Chinese, keep technical terms accurate". So we need to produce a Chinese translation of the list (presumably a navigation block of references). The user didn't ask to translate everything, but just to translate the given content into Chinese. The content is mostly a set of references of a DID (Decentralized Identifier) spec. So the translation should keep technical terms like "DID", "DID document", "DID URL", "Verification Method", "Assertion", "Authentication", "Key Agreement", "Capability Invocation", "Capability Delegation", "Service Endpoint", etc., in English or transliterate them? Typically technical terms remain in English, but Chinese translation could add Chinese translations with English in parentheses. But user says keep technical terms accurate, so they may expect to keep the terms like "DID" as is, not translate. The translation can be something like:

§ B.4 引用 DID 文档

§ B.6 发现更多关于 DID 主体的信息

...

So we need to produce a Chinese version for each line.

The user included a large list of sections with parentheses (2), (3), etc. Should we preserve numbering? Yes.

The user wants translation to Chinese, keep technical terms accurate. So we can output something like:

§ B.4 引用 DID 文档

...

Referenced in: (which translates to "被引用章节：" or "引用位置：").

Probably "引用位置" is appropriate. Or "被引用章节". Let's think: "Referenced in:" can be translated as "引用位置：" or "参见". Typically spec references: "Referenced in:" might be "被引用章节". So we can use "被引用章节：". Then the sections list. In Chinese, we can use "§" as is. The section titles: "2. Terminology" -> "2. 术语". "5.3.2 Assertion" -> "5.3.2 断言". But sometimes "Assertion" is "断言". For "Authentication" -> "身份验证". For "Key Agreement" -> "密钥协商". For "Capability Invocation" -> "能力调用". For "Capability Delegation" -> "能力委托". For "DID Document Metadata" -> "DID 文档元数据". For "Method Syntax" -> "方法语法". For "Method Operations" -> "方法操作". For "Non-Repudiation" -> "不可否认性". For "Notification of DID Document Changes" -> "DID 文档更改通知". For "Verification Method Rotation" -> "验证方法轮换". For "Verification Method Revocation" -> "验证方法撤销". For "Revocation Semantics" -> "撤销语义". For "Revocation in Trustless Systems" -> "无信任系统中的撤销". For "Persistence" -> "持久性". For "Immutability" -> "不可变性". For "DID Resolution" -> "DID 解析". For "DID URL Dereferencing" -> "DID URL 取消引用". For "Service Endpoint Alternatives" -> "服务端点替代方案". For "Changing the DID controller" -> "更改 DID 控制器". For "Determining the DID subject" -> "确定 DID 主体". For "Statements in the DID document" -> "DID 文档中的声明". For "Changing the DID subject" -> "更改 DID 主体". For "Assigning DIDs to existing web resources" -> "为现有 Web 资源分配 DID". For "Service properties" -> "服务属性". For "Verification Method properties" -> "验证方法属性". For "Level of Assurance" -> "保证级别". For "Production and Consumption" -> "生成与消费". For "JSON" -> "JSON". For "JSON-LD" -> "JSON-LD". For "Abstract" -> "摘要". For "Architecture Overview" -> "架构概述". For "Binding to Physical Identity" -> "绑定物理身份". For "DID Document properties" -> "DID 文档属性". For "Also Known As" -> "别名". For "Equivalence Properties" -> "等价属性". For "DID Parameters" -> "DID 参数". For "Immutability" is above.

We also need to handle "Permalink" references: "Permalink" maybe "永久链接". "Referenced in:" we can translate as "被引用章节". If we want to keep it minimal, we can just put "被引用章节：" and then list the sections.

But the user gave a large list of references with multiple entries. It's basically a table of contents and references. The user wants to translate to Chinese. So we should produce the translation.

Potential approach: output a Chinese version of each entry. For each top-level line like "§ B.4 Referring to the DID document", we translate to Chinese: "§ B.4 引用 DID 文档". Then under that "Permalink" maybe we need to translate: "永久链接". Then "Referenced in:" -> "被引用章节：". Then list the sections.

Thus each entry would have three lines: the heading, "Permalink", "Referenced in:".

The content includes lines with (2), (3) etc. Those are additional references? Probably those are separate sections with same heading but with (2), (3) etc. In the spec they appear to indicate footnotes? Actually the original list seems to be a combined list of all references in the spec: for each item (like "§ B.4 Referring to the DID document") there is a "Permalink" line and a "Referenced in:" list of sections. For items that have multiple references (2), (3) etc. The original includes multiple entries with same heading and (2), (3) as separate entries. For each of them we need to translate similarly.

Thus we need to parse the input: It appears as multiple lines, each "§ ..." or "Permalink" or "Referenced in:". For each heading there may be a "Permalink" line, and then "Referenced in:" followed by sections. Then a blank line maybe. Then next heading.

But the input includes some entries with multiple "Referenced in:" lists and "Permalink". Actually we have a huge list. Let's isolate each top-level entry. The input is:

§ B.4 Referring to the DID document

Permalink

Referenced in:

§ 2. Terminology

§ 5.3.2 Assertion

(2)

§ Binding to Physical Identity

Permalink

Referenced in:

§ 1.3 Architecture Overview

§ 7.1.3 DID Document Metadata

§ 8. Methods

(2)

§ 8.1 Method Syntax

§ Proving Control of a DID and/or DID Document

§ 9.4 Non-Repudiation

§ 9.5 Notification of DID Document Changes

(2)

§ 9.7 Verification Method Rotation

§ 10.1 Keep Personal Data Private

§ 10.6 Service Privacy

§ Service Endpoint Alternatives

§ B.2 Creation of a DID

§ B.7 Serving a representation of the DID subject

Permalink

Referenced in:

§ Proving Control of a DID and/or DID Document

§ 9.4 Non-Repudiation

Permalink

...

So the input includes each "§ ..." heading line followed by "Permalink" and "Referenced in:" and then a list. Some entries have multiple "Referenced in:"? Actually after "Referenced in:" they list items, then a blank line, then another heading "§ ...". So we need to parse each heading block.

The input is a big continuous list with some repeating patterns. It seems each heading has a "Permalink" line and then a "Referenced in:" block. However some headings have (2), (3) etc after some references. That's probably because they are repeated entries for footnotes. The formatting may be a table of contents for each reference item (like "Referenced in: § 2. Terminology" appears multiple times for each occurrence. The (2) indicates that the same reference appears multiple times.

Thus we need to translate each heading and each reference in the list, preserving the numbering like (2), (3), etc.

Better approach: For each heading line, produce a Chinese translation of the heading (including the section number). Then produce a line "永久链接". Then a line "被引用章节：". Then list the references, translating each section title into Chinese.

We need to decide if we need to preserve the "§" symbol. In Chinese spec, we can keep "§" for sections. Then the section titles: We should translate them to Chinese, but keep the numbering like "2. 术语". For subsections, "5.3.2 断言". For "Assertion", we can translate as "断言". For "Authentication", "身份验证". For "Key Agreement", "密钥协商". For "Capability Invocation", "能力调用". For "Capability Delegation", "能力委托". For "Service Endpoint Alternatives", "服务端点替代方案". For "DID Document Metadata", "DID 文档元数据". For "DID Document properties", "DID 文档属性". For "Verification Method properties", "验证方法属性". For "Service properties", "服务属性". For "DID Resolution", "DID 解析". For "DID URL Dereferencing", "DID URL 取消引用". For "Method Syntax", "方法语法". For "Method Operations", "方法操作". For "Non-Repudiation", "不可否认性". For "Notification of DID Document Changes", "DID 文档更改通知". For "Verification Method Rotation", "验证方法轮换". For "Verification Method Revocation", "验证方法撤销". For "Revocation Semantics", "撤销语义". For "Revocation in Trustless Systems", "无信任系统中的撤销". For "Persistence", "持久性". For "Immutability", "不可变性". For "Level of Assurance", "保证级别". For "Production and Consumption", "生成与消费". For "JSON", "JSON". For "JSON-LD", "JSON-LD". For "Abstract", "摘要". For "Architecture Overview", "架构概述". For "Binding to Physical Identity", "绑定物理身份". For "DID Document properties", "DID 文档属性". For "Also Known As", "别名". For "Equivalence Properties", "等价属性". For "DID Parameters", "DID 参数". For "DID subject", "DID 主体". For "DID subject classification", "DID 主体分类". For "Service Privacy", "服务隐私". For "Personal Data Private", "个人数据隐私". For "DID Document Correlation Risks", "DID 文档关联风险". For "Immutability", "不可变性". For "Revocation in Trustless Systems", "无信任系统中的撤销". For "Revocation Semantics", "撤销语义". For "DID Document Metadata", "DID 文档元数据". For "DID Subject", "DID 主体". For "Also Known As", "别名". For "Changing the DID controller", "更改 DID 控制器". For "Changing the DID subject", "更改 DID 主体". For "Assigning DIDs to existing web resources", "为现有 Web 资源分配 DID". For "Statements in the DID document", "DID 文档中的声明". For "Determining the DID subject", "确定 DID 主体". For "Serving a representation of the DID subject", "提供 DID 主体的表示". For "Discovering more information about the DID subject", "发现更多关于 DID 主体的信息". For "Creation of a DID", "DID 的创建". For "Method Syntax", "方法语法". For "Method Operations", "方法操作". For "Proving Control of a DID and/or DID Document", "证明对 DID 和/或 DID 文档的控制". For "Non-Repudiation", "不可否认性". For "Notification of DID Document Changes", "DID 文档更改通知". For "Verification Method Rotation", "验证方法轮换". For "Verification Method Revocation", "验证方法撤销". For "Revocation Semantics", "撤销语义". For "Revocation in Trustless Systems", "无信任系统中的撤销". For "Persistence", "持久性". For "Immutability", "不可变性". For "Level of Assurance", "保证级别". For "Keep Personal Data Private", "保持个人数据私密". For "Service Privacy", "服务隐私". For "DID Document Correlation Risks", "DID 文档关联风险". For "DID Subject Classification", "DID 主体分类". For "DID Document properties", "DID 文档属性". For "Verification Method properties", "验证方法属性". For "Service properties", "服务属性". For "DID Parameters", "DID 参数". For "Production and Consumption", "生成与消费". For "Production", "生成". For "Consumption", "消费". For "JSON", "JSON". For "JSON-LD", "JSON-LD". For "Representation of the DID subject", "DID 主体的表示". For "Service Endpoint Alternatives", "服务端点替代方案". For "Assigning DIDs to existing web resources", "为现有 Web 资源分配 DID". For "Changing the DID controller", "更改 DID 控制器". For "Changing the DID subject", "更改 DID 主体". For "Statements in the DID document", "DID 文档中的声明". For "Determining the DID subject", "确定 DID 主体". For "Discovering more information about the DID subject", "发现更多关于 DID 主体的信息". For "Serving a representation of the DID subject", "提供 DID 主体的表示". For "Method Syntax", "方法语法". For "Method Operations", "方法操作". For "Proving Control of a DID and/or DID Document", "证明对 DID 和/或 DID 文档的控制". For "Non-Repudiation", "不可否认性". For "Notification of DID Document Changes", "DID 文档更改通知". For "Verification Method Rotation", "验证方法轮换". For "Verification Method Revocation", "验证方法撤销". For "Revocation Semantics", "撤销语义". For "Revocation in Trustless Systems", "无信任系统中的撤销". For "Persistence", "持久性". For "Immutability", "不可变性". For "Level of Assurance", "保证级别". For "Keep Personal Data Private", "保持个人数据私密". For "Service Privacy", "服务隐私". For "DID Document Correlation Risks", "DID 文档关联风险". For "DID Subject Classification", "DID 主体分类". For "DID Document properties", "DID 文档属性". For "Verification Method properties", "验证方法属性". For "Service properties", "服务属性". For "DID Parameters", "DID 参数". For "Production and Consumption", "生成与消费". For "Production", "生成". For "Consumption", "消费". For "JSON", "JSON". For "JSON-LD", "JSON-LD". For "Abstract", "摘要". For "Architecture Overview", "架构概述". For "Binding to Physical Identity", "绑定物理身份". For "Also Known As", "别名". For "Equivalence Properties", "等价属性". For "DID Document Metadata", "DID 文档元数据". For "DID Resolution", "DID 解析". For "DID URL Dereferencing", "DID URL 取消引用". For "Immutability", "不可变性". For "Persistence", "持久性". For "Revocation Semantics", "撤销语义". For "Revocation in Trustless Systems", "无信任系统中的撤销". For "Verification Method Rotation", "验证方法轮换". For "Verification Method Revocation", "验证方法撤销". For "DID Recovery", "DID 恢复". For "Level of Assurance", "保证级别". For "Service Privacy", "服务隐私". For "Keep Personal Data Private", "保持个人数据私密". For "DID Document Correlation Risks", "DID 文档关联风险". For "DID Subject Classification", "DID 主体分类". For "DID Document properties", "DID 文档属性". For "Verification Method properties", "验证方法属性". For "Service properties", "服务属性". For "DID Parameters", "DID 参数". For "Production and Consumption", "生成与消费". For "Production", "生成". For "Consumption", "消费". For "JSON", "JSON". For "JSON-LD", "JSON-LD". For "Abstract", "摘要". For "Architecture Overview", "架构概述". For "Binding to Physical Identity", "绑定物理身份". For "Also Known As", "别名". For "Equivalence Properties", "等价属性". For "DID Document Metadata", "DID 文档元数据". For "DID Resolution", "DID 解析". For "DID URL Dereferencing", "DID URL 取消引用". For "Immutability", "不可变性". For "Persistence", "持久性". For "Revocation Semantics", "撤销语义". For "Revocation in Trustless Systems", "无信任系统中的撤销". For "Verification Method Rotation", "验证方法轮换". For "Verification Method Revocation", "验证方法撤销". For "DID Recovery", "DID 恢复". For "Level of Assurance", "保证级别". For "Service Privacy", "服务隐私". For "Keep Personal Data Private", "保持个人数据私密". For "DID Document Correlation Risks", "DID 文档关联风险". For "DID Subject Classification", "DID 主体分类". For "DID Document properties", "DID 文档属性". For "Verification Method properties", "验证方法属性". For "Service properties", "服务属性". For "DID Parameters", "DID 参数". For "Production and Consumption", "生成与消费". For "Production", "生成". For "Consumption", "消费". For "JSON", "JSON". For "JSON-LD", "JSON-LD". For "Abstract", "摘要". For "Architecture Overview", "架构概述". For "Binding to Physical Identity", "绑定物理身份". For "Also Known As", "别名". For "Equivalence Properties", "等价属性". For "DID Document Metadata", "DID 文档元数据". For "DID Resolution", "DID 解析". For "DID URL Dereferencing", "DID URL 取消引用". For "Immutability", "不可变性". For "Persistence", "持久性". For "Revocation Semantics", "撤销语义". For "Revocation in Trustless Systems", "无信任系统中的撤销". For "Verification Method Rotation", "验证方法轮换". For "Verification Method Revocation", "验证方法撤销". For "DID Recovery", "DID 恢复". For "Level of Assurance", "保证级别". For "Service Privacy", "服务隐私". For "Keep Personal Data Private", "保持个人数据私密". For "DID Document Correlation Risks", "DID 文档关联风险". For "DID Subject Classification", "DID 主体分类". For "DID Document properties", "DID 文档属性". For "Verification Method properties", "验证方法属性". For "Service properties", "服务属性". For "DID Parameters", "

*原文请访问 [w3.org](https://www.w3.org/TR/did-core)*