---
title: **Translation:**

面向大语言模型（LLM）的高吞吐量、内存高效型推理与服务引擎
source: vllm.ai
url: https://vllm.ai
date: 2026-06-22
category: person/vllm.ai
translated: true
fetched_at: 2026-06-22T18:17:43.126568
---
# **Translation:**

面向大语言模型（LLM）的高吞吐量、内存高效型推理与服务引擎

**来源**: vllm.ai | **日期**: 2026-06-22

---

# vLLM 中文文档

## 高吞吐量、内存高效的 LLM 推理与服务引擎

简单、快速、低成本的 LLM 服务，让每个人都能使用。

[开始使用](#)
[文档](#)

### 简单

在任意硬件上部署最广泛的开源模型。包括与 OpenAI 兼容的即插即用 API，实现即时集成。

### 快速

通过 PagedAttention 最大化吞吐量。高级调度和连续批处理确保峰值 GPU 利用率。

### 成本高效

通过最大化硬件效率来降低推理成本。我们让高性能 LLM 变得人人可负担、人人可获取。

## 快速入门

选择您的偏好并运行安装命令。

**稳定版 (Stable)**
代表目前经过测试和支持的 vLLM 最新版本。

**每夜版 (Nightly)**
如果您想要最新的构建版本，可以使用此版本。

📦 需要 Python 3.10+。推荐 Python 3.12+。

⚡ 我们推荐使用 **uv** 以获得更快、更可靠的安装体验。

🔧 其他平台请参阅 [docs.vllm.ai](https://docs.vllm.ai)

🎉 查看 [新增功能](#)

🔍 查找哪个版本包含某个 PR

### 构建

[稳定版](#) [每夜版](#)

### 平台

[CUDA](#) [ROCm](#) [XPU](#) [CPU](#)

### 包

[Python (uv)](#) [Python](#) [Docker](#)

### CUDA 版本

[CUDA 13.0](#) [CUDA 12.9](#)

### 运行此命令：

```
uv pip install vllm --torch-backend auto
```

💡 兼容所有 CUDA 13.x 版本 (13.0 - 13.1) · [故障排除](#)

[需要旧版本？](#)

---

## 赞助商

vLLM 是一个社区项目。我们的开发和测试计算资源由以下组织提供支持。感谢您的支持！

### 现金捐赠

a16z · Sequoia Capital · Skywork AI · ZhenFund

### 计算资源

Alibaba Cloud · AMD · Anyscale · AWS · Crusoe Cloud · Google Cloud · IBM · Intel · Lambda Lab · Nebius · Novita AI · NVIDIA · Red Hat · Roblox · RunPod · UC Berkeley

### Slack 赞助

Inferact

— Stars ⭐ —

— 贡献者 👥 —

PyTorch Foundation

我们通过 GitHub 和 OpenCollective 接受捐赠。我们计划使用这些资金来支持 vLLM 的开发、维护和推广。

---

## 通用兼容性

一个引擎，无限可能。在任意硬件上运行任意模型。

### 硬件

跨平台统一 API

| 厂商 | 硬件类型 | 状态 |
|------|---------|------|
| NVIDIA | CUDA GPU | 热门 |
| AMD | ROCm GPU | |
| Huawei | Ascend NPU | |
| AWS | Neuron Accelerator | |
| Google | Cloud TPU | |
| IBM | Spyre Accelerator | |
| Intel | Gaudi XPU | |
| CPU | CPU | |
| Apple | Apple Silicon | |

[查看所有支持的硬件](#)

---

## 开源模型

最新热门开源模型，优化并可投入生产

### DeepSeek

DeepSeek V4 · DeepSeek V3.2 · DeepSeek R1

### Google

Gemma 4 · Gemma 3

### Meta

Llama 4 Scout · Llama 4 Maverick

### Minimax

MiniMax M3 · MiniMax M2.7 · MiniMax M2.5

### Mistral AI

Mistral Small 4 · Mistral Large 3

### MoonshotAI

Kimi K2.6 · Kimi K2.5 · Kimi K2

### NVIDIA

Nemotron 3 Ultra · Nemotron 3 Super · Nemotron 3 Nano

### Qwen

Qwen3.6 · Qwen3.5 · Qwen3

### StepFun

Step-3.7-Flash · Step-3.5-Flash

### Z-AI

GLM 5.1 · GLM 5 · GLM 4.7

[查看所有支持的模型](#)

---

## 欢迎所有人！

### 有问题？

我们随时为您提供帮助。

无论您是刚开始使用还是在调试复杂的部署问题，我们的社区对所有人开放。没有问题是太基础的！

- ⚡ 快速友好的响应
- 👨‍💻 活跃的维护者
- 💬 加入 [Slack](#) - 实时帮助与讨论
- 📖 访问 [论坛](#) - 可搜索的问答知识库
- 🐛 [GitHub Issues](#) - 错误报告与功能请求

---

## 资源

探索示例、基准测试和路线图

### 示例

示例笔记本和教程
[recipes.vllm.ai](https://recipes.vllm.ai)

### 性能

基准测试和比较
[perf.vllm.ai](https://perf.vllm.ai)

### 路线图

项目路线图和里程碑
[roadmap.vllm.ai](https://roadmap.vllm.ai)

*原文请访问 [vllm.ai](https://vllm.ai)*