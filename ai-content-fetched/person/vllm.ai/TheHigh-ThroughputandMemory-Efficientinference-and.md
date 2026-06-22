---
title: ## 翻译结果：

**面向大语言模型的高吞吐量、内存高效型推理服务引擎**

---

### 术语对照：

| 英文术语 | 中文术语 |
|---------|---------|
| High-Throughput | 高吞吐量 |
| Memory-Efficient | 内存高效型 |
| inference | 推理 |
| serving engine | 服务引擎 |
| LLMs (Large Language Models) | 大语言模型 |

---

### 备选版本：

1. **面向LLM的高吞吐、内存高效推理服务引擎**
2. **大语言模型高吞吐量内存高效推理服务引擎**

如需更口语化或更正式的版本，请告诉我。
source: vllm.ai
url: https://vllm.ai
date: 2026-06-22
category: person/vllm.ai
translated: true
fetched_at: 2026-06-22T17:44:08.189749
---
# ## 翻译结果：

**面向大语言模型的高吞吐量、内存高效型推理服务引擎**

---

### 术语对照：

| 英文术语 | 中文术语 |
|---------|---------|
| High-Throughput | 高吞吐量 |
| Memory-Efficient | 内存高效型 |
| inference | 推理 |
| serving engine | 服务引擎 |
| LLMs (Large Language Models) | 大语言模型 |

---

### 备选版本：

1. **面向LLM的高吞吐、内存高效推理服务引擎**
2. **大语言模型高吞吐量内存高效推理服务引擎**

如需更口语化或更正式的版本，请告诉我。

**来源**: vllm.ai | **日期**: 2026-06-22

---

# vLLM 中文翻译

## 主标题

高吞吐量、内存高效的
大语言模型推理与服务引擎

为每个人提供简单、快速且成本高效的大语言模型服务。

开始使用
文档

### 简单

在任何硬件上部署最广泛的开源模型。包含即插即用的 OpenAI 兼容 API，可实现即时集成。

### 快速

通过 PagedAttention 最大化吞吐量。高级调度和连续批处理确保峰值 GPU 利用率。

### 成本高效

通过最大化硬件效率降低推理成本。我们让高性能大语言模型变得经济实惠、人人可及。

## 快速入门

选择您的偏好并运行安装命令。

**稳定版** 表示当前经过测试和支持的最新版本 vLLM。

**每日构建版** 适用于想要最新构建版本的用户。

📦 需要 Python 3.10+。推荐 Python 3.12+。

⚡ 我们推荐使用 **uv** 以获得更快、更可靠的安装体验。

🔧 对于其他平台，请参阅 docs.vllm.ai

🎉 查看 what's new

🔍 查找哪个版本包含某个 PR

### 构建版本

- [ ] 稳定版
- [ ] 每日构建版

### 平台

- CUDA
- ROCm
- XPU
- CPU

### 包

- Python (uv)
- Python
- Docker

### CUDA 版本

- CUDA 13.0
- CUDA 12.9

运行此命令：

```
uv pip install vllm --torch-backend auto
```

💡 兼容所有 CUDA 13.x 版本 (13.0 - 13.1) · 故障排除

寻找旧版本？

## 赞助商

vLLM 是一个社区项目。我们开发和测试的计算资源由以下组织提供支持。感谢您的支持！

### 现金捐赠

a16z · Sequoia Capital · Skywork AI · ZhenFund

### 计算资源

Alibaba Cloud · AMD · Anyscale · AWS · Crusoe Cloud · Google Cloud · IBM · Intel · Lambda Lab · Nebius · Novita AI · NVIDIA · Red Hat · Roblox · RunPod · UC Berkeley

### Slack 赞助商

Inferact

— · ⭐ Stars · — · 👥 Contributors · —

PyTorch Foundation

我们通过 GitHub 和 OpenCollective 接受捐赠。我们计划使用这些资金支持 vLLM 的开发、维护和推广。

## 通用兼容性

一个引擎，无限可能。在任何硬件上运行任何模型。

### 硬件

跨平台统一 API

- NVIDIA CUDA GPU · 热门
- AMD ROCm GPU
- Huawei Ascend NPU
- AWS Neuron Accelerator
- Google Cloud TPU
- IBM Spyre Accelerator
- Intel Gaudi XPU
- CPU
- Apple Apple Silicon

查看所有支持的硬件

## 开源模型

最新的热门开源模型，已优化并可投入生产

DeepSeek

- DeepSeek V4
- DeepSeek V3.2
- DeepSeek R1

Google

- Gemma 4
- Gemma 3

Meta

- Llama 4 Scout
- Llama 4 Maverick

MiniMax

- MiniMax M3
- MiniMax M2.7
- MiniMax M2.5

Mistral AI

- Mistral Small 4
- Mistral Large 3

MoonshotAI

- Kimi K2.6
- Kimi K2.5
- Kimi K2

NVIDIA

- Nemotron 3 Ultra
- Nemotron 3 Super
- Nemotron 3 Nano

Qwen

- Qwen3.6
- Qwen3.5
- Qwen3

StepFun

- Step-3.7-Flash
- Step-3.5-Flash

Z-AI

- GLM 5.1
- GLM 5
- GLM 4.7

查看所有支持的模型

## 欢迎所有人！

有问题吗？

我们在这里提供帮助。

无论您是刚开始使用还是在调试复杂的部署问题，我们的社区对所有人开放。没有问题过于基础！

- ⚡ 快速友好的响应
- 🔧 活跃的维护者

加入 Slack · 实时帮助与讨论

访问论坛 · 可搜索的问答知识库

GitHub Issues · Bug 报告与功能请求

## 资源

探索配方、基准测试和路线图

配方

示例笔记本和教程 · recipes.vllm.ai

性能

基准测试和对比 · perf.vllm.ai

路线图

项目路线图和里程碑 · roadmap.vllm.ai

*原文请访问 [vllm.ai](https://vllm.ai)*