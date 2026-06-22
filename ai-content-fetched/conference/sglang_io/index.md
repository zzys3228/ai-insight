---
title: High-Performance Serving Frameworkfor LLMs and Multimodal Models
source: www.sglang.io
url: https://www.sglang.io
category: conference
---
# High-Performance Serving Frameworkfor LLMs and Multimodal Models

# SGLang：高性能 LLM 和多模态模型服务框架

SGLang 为大型语言模型和多模态模型提供快速、可扩展的推理服务。

[快速开始](#快速开始步骤)

![SGLang 数据处理架构](/images/hero-illustrate.png)

行业领先企业信赖之选：

![NVIDIA](/images/nvidia-logo.png)

![xAI](/images/xai-logo.png)

![Oracle](/images/oracle-logo.png)

![AMD](/images/amd-logo.png)

![LinkedIn](/images/linkedin-logo.png)

![Google Cloud](/images/google-cloud-logo.png)

[查看完整列表](/community#partners)

### 生产级推理

专为大规模部署而构建，从单个 GPU 到分布式集群，提供可靠、低延迟、高吞吐量的服务。

### 模型与硬件灵活性

支持多种开源模型——从 LLM 到扩散模型——并可在多种硬件平台上运行。

### 高级优化

集成了分离式 prefill/decode、投机解码、并行策略、零开销调度器以及优化的 GPU 内核。

几秒内快速开始
----------------------

选择您的偏好设置并运行部署命令。SGLang 设计初衷即为便于安装和部署。

1

### 通过 pip 或 docker 安装

最简单的入门方式。

2

### 启动服务器

使用单条命令启动服务器并指向您的模型。

3

### 查询 API

使用标准 OpenAI 兼容端点与您的模型进行交互。

[查看文档](https://docs.sglang.io/)

构建版本

Stable（稳定版）Nightly（每日构建版）

平台

CUDAROCmXPUCPU

安装包

Python (uv)PythonDocker

CUDA 版本

CUDA 12.9CUDA 13.0

---

运行此命令：

```
uv pip install sglang sglang-kernel \
  --extra-index-url https://sgl-project.github.io/whl/cu129/ \
  --extra-index-url https://download.pytorch.org/whl/cu129 \
  --index-strategy unsafe-best-match
```

广泛的模型与硬件支持
------------------------------

一个引擎，多种模型与硬件。

### 支持的硬件

NVIDIA GPU

AMD GPU

CPU 服务器

TPU

昇腾 NPU

XPU

[查看所有支持的硬件](https://docs.sglang.io/platforms/amd_gpu.html)

### 支持的模型

DeepSeek

Qwen

GPT-OSS

Llama

Mistral

GLM

[查看所有支持的模型](/models)

加入社区
------------------

无论您是首次使用还是团队调试复杂部署，社区对所有人开放。

[GitHub](https://github.com/sgl-project/sglang)

报告问题、功能请求并贡献代码。[Slack](https://slack.sglang.io)

与社区交流并获取实时帮助。[Discord](https://discord.gg/4ugb2t6YY2)

技术讨论和办公时间的社区。[讨论区](https://github.com/sgl-project/sglang/discussions)

分享想法并讨论 SGLang 的未来。

*原文: https://www.sglang.io*