---
title: TheHigh-ThroughputandMemory-Efficientinference and serving engine for LLMs
source: vllm.ai
url: https://vllm.ai
category: person
---
# TheHigh-ThroughputandMemory-Efficientinference and serving engine for LLMs

# vLLM 中文翻译

![vLLM](/vLLM-Full-Logo.svg)![vLLM](/vLLM-Full-Dark-Mode-Logo.svg)

高性能、高吞吐量、内存高效的大语言模型（LLM）推理与服务引擎
===============================================================================

为每个人提供简单、快速且经济高效的大语言模型服务。

开始使用[文档](https://docs.vllm.ai)

简单易用
----

在任何硬件上部署最广泛的开源模型。包含即插即用的 OpenAI 兼容 API，可实现即时集成。

快速高效
----

通过 PagedAttention 最大化吞吐量。先进的调度策略和连续批处理确保峰值 GPU 利用率。

成本高效
----

通过最大化硬件效率来降低推理成本。我们让高性能大语言模型对每个人都变得经济实惠且易于获取。

快速开始
-----------

选择您的偏好设置并运行安装命令。**Stable（稳定版）** 代表目前经过测试和支持最多的 vLLM 版本。**Nightly（每夜版）** 可供需要最新构建版本的用户使用。

📦 需要 Python 3.10+。推荐使用 Python 3.12+。

⚡ 我们推荐使用 [uv](https://docs.astral.sh/uv/) 以获得更快、更可靠的安装体验。

🔧 对于其他平台，请参阅 [docs.vllm.ai](https://docs.vllm.ai)

🎉 查看 [新增功能](https://github.com/vllm-project/vllm/releases)

🔍 [查找某个 PR 属于哪个版本](/pr-lookup)

构建

Stable（稳定版）Nightly（每夜版）

平台

CUDAROCmXPUCPU

软件包

Python (uv)PythonDocker

CUDA 版本

CUDA 13.0CUDA 12.9

运行此命令：

uv pip install vllm --torch-backend auto

💡 兼容所有 CUDA 13.x 版本（13.0 - 13.1）· [故障排除](https://docs.vllm.ai/en/latest/usage/troubleshooting/#cuda-error-the-provided-ptx-was-compiled-with-an-unsupported-toolchain)

[寻找旧版本？](/releases)

赞助商
-----------

vLLM 是一个社区项目。我们的开发和测试计算资源由以下组织提供支持。感谢您的支持！

### 现金捐赠

a16z

红杉资本

Skywork AI

真格基金（ZhenFund）

### 计算资源

阿里云

AMD

Anyscale

AWS

Crusoe Cloud

谷歌云

IBM

英特尔

Lambda Lab

Nebius

Novita AI

NVIDIA

红帽

Roblox

RunPod

加州大学伯克利分校

### Slack 赞助商

Inferact

[— Stars — ⭐](https://github.com/vllm-project/vllm/stargazers)[— 贡献者 — 👥](https://github.com/vllm-project/vllm/graphs/contributors)[PyTorch 基金会](https://pytorch.org/projects/vllm)

我们通过 [GitHub](https://github.com/sponsors/vllm-project) 和 [OpenCollective](https://opencollective.com/vllm) 接受捐赠。我们计划将资金用于支持 vLLM 的开发、维护和推广。

广泛兼容性
-----------------------

一个引擎，无限可能。在任何硬件上运行任何模型。

### 硬件

跨平台统一 API

[NVIDIACUDA GPU

热门选择](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#nvidia-cuda)[AMDROCm GPU](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#amd-rocm)[华为Ascend NPU](https://github.com/vllm-p

*原文: https://vllm.ai*