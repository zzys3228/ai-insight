---
title: MathVista
source: mathvista.github.io
url: https://mathvista.github.io
category: benchmark
---
# MathVista

# Logo
# MathVista

==============

在视觉情境中评估数学推理
--------------------------------------------

[潘璐](https://lupantech.github.io/)¹,

[Hritik Bansal](https://sites.google.com/view/hbansal)¹,

[Tony Xia](https://tonyxia2001.github.io/)¹,

[刘家成](https://liujch1998.github.io/)²,

[李春媛](https://chunyuan.li/)³,

[Hannaneh Hajishirzi](https://homes.cs.washington.edu/~hannaneh/)²,

[程浩](https://sites.google.com/site/hcheng2site/Home)³,

[常凯伟](http://web.cs.ucla.edu/~kwchang/)¹,

[Michel Galley](https://www.microsoft.com/en-us/research/people/mgalley/?from=https://research.microsoft.com/~mgalley&type=exact)³,

[高建峰](https://www.microsoft.com/en-us/research/people/jfgao/)³

¹加利福尼亚大学洛杉矶分校,
²华盛顿大学,
³微软研究院
**ICLR 2024 Oral** (85/7304, 1.2%)




[论文](https://arxiv.org/pdf/2310.02255.pdf)

[arXiv](https://arxiv.org/abs/2310.02255)




[代码](https://github.com/lupantech/MathVista)


[🤗

数据集](https://huggingface.co/datasets/AI4Math/MathVista)


[🔮

可视化](https://mathvista.github.io/#visualization)


[🏆

排行榜](https://mathvista.github.io/#leaderboard)


[🌐

Twitter](https://twitter.com/lupantech/status/1717313355780964608)

![几何推理](static/images/tease_scores_version4_gemini.png)

一个领先的大语言模型（即 PoT GPT-4）、四个主要的大型多模态模型、随机概率和人类表现在我们提出的
![Logo](static/images/mathvista.png)
MathVista
上的准确率，涵盖数学推理和视觉情境类型。PoT 指思维程序提示（program-of-thought prompting），PoT GPT-4 是一个通过加入图像描述和 OCR 文本增强的文本大语言模型。GPT-4V 通过 playground 聊天机器人进行人工评估。**Gemini Ultra 的成绩来自谷歌 Gemini 团队。**

![几何推理](static/images/tease_scores_gpt4v.png)

一个领先的大语言模型（即 PoT GPT-4）、四个主要的大型多模态模型、随机概率和人类表现在我们提出的
![Logo](static/images/mathvista.png)
MathVista
上的准确率，涵盖数学推理和视觉情境类型。PoT 指思维程序提示（program-of-thought prompting），PoT GPT-4 是一个通过加入图像描述和 OCR 文本增强的文本大语言模型。GPT-4V 通过 playground 聊天机器人进行人工评估。

## 引言

------------

**大语言模型（LLMs）** 和 **大型多模态模型（LMMs）** 在许多任务和领域中展现出令人印象深刻的问题解决能力，但它们在视觉情境中数学推理的能力尚未得到系统研究。

为填补这一空白，我们提出了 ![Logo](static/images/mathvista.png)
MathVista，这是一个旨在整合来自不同数学和视觉任务挑战的基准测试。它由 **6,141 个示例** 组成，来源于 **28 个涉及数学的多模态现有数据集** 和 **3 个新创建的数据集**（即 **IQTest、FunctionQA 和 PaperQA**）。完成这些任务需要细粒度的深度视觉理解和组合推理。

*原文: https://mathvista.github.io*