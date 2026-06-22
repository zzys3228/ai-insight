---
title: **面向大语言模型(LLM)的高吞吐量、内存高效型推理服务引擎**
source: vllm.ai
url: https://vllm.ai
date: 2026-06-22
category: person/vllm.ai
translated: true
fetched_at: 2026-06-22T18:34:53.102183
---
# **面向大语言模型(LLM)的高吞吐量、内存高效型推理服务引擎**

**来源**: vllm.ai | **日期**: 2026-06-22

---

# vLLM 中文翻译

## 高吞吐量、内存高效的大语言模型推理与服务引擎

让每个人都能简单、快速、低成本地使用大语言模型服务。

开始使用 | 文档

### 简单易用

在任意硬件上部署最广泛的开源模型。包含开箱即用的 OpenAI 兼容 API，实现即时集成。

### 极速高效

通过 PagedAttention 最大化吞吐量。高级调度和连续批处理确保 GPU 利用率达到峰值。

### 成本效益

通过最大化硬件效率来降低推理成本。我们让高性能大语言模型变得人人可负担、人人可及。

## 快速开始

选择您的偏好设置并运行安装命令。

**Stable（稳定版）** 代表目前经过测试和支持的最新版本 vLLM。

**Nightly（每日构建版）** 如果您需要最新构建版本，可以使用此版本。

📦 需要 Python 3.10+。推荐 Python 3.12+。

⚡ 我们推荐使用 **uv** 以获得更快、更可靠的安装体验。

🔧 其他平台，请参阅 docs.vllm.ai

🎉 查看最新更新内容

🔍 查找某个 PR 所属的发布版本

## 构建版本

| Stable | Nightly |
|--------|---------|
| 稳定版 | 每日构建版 |

## 平台

| CUDA | ROCm | XPU | CPU |
|------|------|-----|-----|

## 安装包

| Python (uv) | Python | Docker |
|-------------|--------|--------|

## CUDA 版本

| CUDA 13.0 | CUDA 12.9 |
|-----------|-----------|

运行此命令：

```bash
uv pip install vllm --torch-backend auto
```

💡 兼容所有 CUDA 13.x 版本（13.0 - 13.1）

故障排除 | 寻找旧版本？

## 赞助商

vLLM 是一个社区项目。我们开发和测试所需的计算资源由以下组织提供支持。感谢您的支持！

### 现金捐赠

a16z | Sequoia Capital | Skywork AI | ZhenFund

### 计算资源

Alibaba Cloud | AMD | Anyscale | AWS | Crusoe Cloud | Google Cloud | IBM | Intel | Lambda Lab | Nebius | Novita AI | NVIDIA | Red Hat | Roblox | RunPod | UC Berkeley

### Slack 赞助商

Inferact

— Stars — ⭐ — 贡献者 — 👥 | PyTorch Foundation

我们通过 GitHub 和 OpenCollective 接受捐赠。我们计划利用这些资金支持 vLLM 的开发、维护和推广。

## 通用兼容性

一个引擎，无限可能。在任意硬件上运行任意模型。

### 硬件

| NVIDIA CUDA GPU | AMD ROCm GPU | Huawei Ascend NPU | AWS Neuron Accelerator | Google Cloud TPU | IBM Spyre Accelerator | Intel Gaudi XPU | CPU | Apple Apple Silicon |
|-----------------|--------------|-------------------|----------------------|------------------|----------------------|-----------------|-----|---------------------|

[查看所有支持的硬件]

## 开源模型

最新流行的开源模型，已优化并可直接用于生产

**DeepSeek**: DeepSeek V4, DeepSeek V3.2, DeepSeek R1

**Google**: Gemma 4, Gemma 3

**Meta**: Llama 4 Scout, Llama 4 Maverick

**MiniMax**: MiniMax M3, MiniMax M2.7, MiniMax M2.5

**Mistral AI**: Mistral Small 4, Mistral Large 3

**MoonshotAI**: Kimi K2.6, Kimi K2.5, Kimi K2

**NVIDIA**: Nemotron 3 Ultra, Nemotron 3 Super, Nemotron 3 Nano

**Qwen**: Qwen3.6, Qwen3.5, Qwen3

**StepFun**: Step-3.7-Flash, Step-3.5-Flash

**Z-AI**: GLM 5.1, GLM 5, GLM 4.7

[查看所有支持的模型]

## 欢迎所有人！

有问题？我们随时为您服务。

无论您是刚开始使用还是在调试复杂的部署问题，我们的社区对所有人开放。没有问题是太基础的！

- 快速友好的回复
- 活跃的维护者

[加入 Slack] - 实时帮助与讨论

[访问论坛] - 可搜索的问答知识库

[GitHub Issues] - Bug 报告与功能请求

## 资源

探索配方、基准测试和路线图

**配方**: 示例笔记本和教程 | recipes.vllm.ai

**性能**: 基准测试和对比 | perf.vllm.ai

**路线图**: 项目路线图和里程碑 | roadmap.vllm.ai

*原文请访问 [vllm.ai](https://vllm.ai)*