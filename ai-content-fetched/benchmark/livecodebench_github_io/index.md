---
title: LiveCodeBench: Holistic and Contamination Free Evaluation of
              Large Language Models for Code
source: livecodebench.github.io
url: https://livecodebench.github.io
category: benchmark
---
# LiveCodeBench: Holistic and Contamination Free Evaluation of
              Large Language Models for Code

# LiveCodeBench：代码大语言模型的全面且无污染评估

===========================================================================================

[Naman Jain](https://naman-ntc.github.io/)¹,

[King Han](https://kinghan.info/)¹,

[Alex Gu](https://minimario.github.io/)²,

[Wen-Ding Li](https://wending.dev/)³,

[Fanjia Yan](https://fanjia-yan.github.io/)¹,

[Tianjun Zhang](https://tianjunz.github.io/)¹,

[Sida Wang](https://www.sidaw.xyz/),

[Armando Solar-Lezama](https://people.csail.mit.edu/asolar/)²,

[Koushik Sen](https://people.eecs.berkeley.edu/~ksen/)¹,

[Ion Stoica](https://people.eecs.berkeley.edu/~istoica/)¹

¹加州大学伯克利分校
²麻省理工学院
³康奈尔大学

[论文](https://arxiv.org/abs/2403.07974)

[代码](https://github.com/LiveCodeBench/LiveCodeBench)

[数据](https://huggingface.co/livecodebench/)

[排行榜](leaderboard.html)

![Teaser](./images/LCB_holistic_tasks.png)

LiveCodeBench从LeetCode、AtCoder和Codeforces平台的定期竞赛中收集问题，并利用它们构建一个全面的基准测试，用于持续评估代码大语言模型在各种代码相关场景中的表现。

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## 引言

LiveCodeBench是一个全面的、无污染的代码大语言模型评估基准，它随时间持续收集新问题。特别地，LiveCodeBench还关注更广泛的代码相关能力，如自我修复、代码执行和测试输出预测，而不仅仅是代码生成。目前，LiveCodeBench包含超过300道高质量编程问题，这些问题发布于2023年5月至2024年2月期间。我们在LiveCodeBench场景中对29个大语言模型进行了评估，并提出了先前基准测试中未揭示的新实证发现。

## 污染问题

LiveCodeBench为问题标注了发布日期，因此允许在特定时间段内发布的问题上评估模型。因此，对于具有训练截止日期D的新模型，我们可以在D之后发布的问题上评估它，以衡量其对**未见**问题的泛化能力。

![代码生成实时评估](./images/contamination1.png)
![测试输出预测实时评估](./images/contamination2.png)

上面的图表展示了模型在代码生成和测试输出预测场景中，在不同月份发布的问题上的表现。我们发现，DeepSeek模型在2023年9月（其发布日期）之后发布的LeetCode问题上的表现出现明显下降，表明早期的问题可能已被污染。相比之下，对于GPT模型，其在不同月份的表现相对稳定。

## 全面评估与开源模型对比闭源模型

LiveCodeBe

*原文: https://livecodebench.github.io*