---
title: MMMU
source: mmmu-benchmark.github.io
url: https://mmmu-benchmark.github.io
category: benchmark
---
# MMMU

# 翻译

Logo
MMMU
=========

## 面向专家级AGI的大规模多学科多模态理解与推理基准

[Xiang Yue\*†](https://xiangyue9607.github.io/),

[Yuansheng Ni\*](https://yuanshengni.github.io/),

[Kai Zhang\*](https://drogozhang.github.io/),

[Tianyu Zheng\*](https://scholar.google.com/citations?hl=en&user=Vq-VZnUAAAAJ),

Ruoqi Liu,
Ge Zhang,
Samuel Stevens,
Dongfu Jiang,
Weiming Ren,
Yuxuan Sun,
Cong Wei,
Botao Yu,
Ruibin Yuan,
Renliang Sun,
Ming Yin,
Boyuan Zheng,
Zhenzhu Yang,
Yibo Liu,
Wenhao Huang,

[Huan Sun\*](https://web.cse.ohio-state.edu/~sun.397/),

[Yu Su\*†](https://ysu1989.github.io/),

[Wenhu Chen\*†](https://wenhuchen.github.io/)

**MMMU团队**

\*核心贡献者
†通讯作者：
[xiangyue.work@gmail.com](mailto:xiangyue.work@gmail.com),
[su.809@osu.edu](mailto:su.809@osu.edu),
[wenhuchen@uwaterloo.ca](mailto:wenhuchen@uwaterloo.ca)

[arXiv](https://arxiv.org/abs/2311.16502)

[🤗
MMMU-Pro](https://huggingface.co/datasets/MMMU/MMMU_Pro)

[🤗
MMMU](https://huggingface.co/datasets/MMMU/MMMU)

[代码](https://github.com/MMMU-Benchmark/MMMU)

[排行榜](#leaderboard)

[Twitter](https://twitter.com/xiangyue96/status/1729698316554801358)

[示例](#examples)

![几何推理](static/images/overview_mmlu.Jpeg)

MMMU数据集概述。MMMU呈现四大挑战：
1) **全面性**：涵盖六个大学学科和30个大学专业的11.5K道大学水平问题；
2) 高度**异构**的图像类型；
3) 文本与图像**交织**；
4) 根植于深厚学科知识的**专家级**感知与推理。

🔔最新消息
---------

**‼️[2026-02-12] 我们已发布MMMU测试集的答案！您现在可以在本地对模型进行测试集评估！🎉**

**🔥[2024-09-05] 推出[MMMU-Pro](https://arxiv.org/abs/2409.02813)，这是一个用于多模态AI评估的鲁棒版MMMU基准！🚀**

**🚀[2024-01-31]：我们在[排行榜](#leaderboard)上添加了人类专家的表现！🌟**

**🔥[2023-12-04]：~~我们的测试集评估服务器已在[**EvalAI**](https://eval.ai/web/challenges/challenge-page/2179/overview)上线。~~ 欢迎所有提交，期待您的参与！😆**

简介
------------

我们推出MMMU：一个旨在评估多模态模型在需要大学水平学科知识和深思熟虑推理的大规模多学科任务上的表现的新基准。MMMU包含来自大学考试、测验和教科书的**11.5K**道精心收集的多模态问题，涵盖六个核心学科：艺术与设计、商业、科学、健康与医学、人文与社会科学以及技术与工程。这些问题横跨**30**个专业和**183**个子领域，包含30种高度异构的图像类型，如图表、图解、地图、表格、乐谱和化学结构。与现有基准不同，MMMU专注于深度学科知识支撑的高级感知与推理。

*原文: https://mmmu-benchmark.github.io*