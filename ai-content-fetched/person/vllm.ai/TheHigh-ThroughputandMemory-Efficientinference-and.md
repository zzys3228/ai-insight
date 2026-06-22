---
title: ## 翻译

**原文修正：**
The High-Throughput and Memory-Efficient inference and serving engine for LLMs

**中文翻译：**
面向大语言模型的高吞吐量、内存高效推理服务引擎

---

### 术语对照

| 英文术语 | 中文术语 |
|---------|---------|
| High-Throughput | 高吞吐量 |
| Memory-Efficient | 内存高效 |
| Inference | 推理 |
| Serving | 服务/ Serving |
| Engine | 引擎 |
| LLMs (Large Language Models) | 大语言模型 |

> **备注：** "Serving" 在大模型领域通常保留英文或译为"服务"，指模型部署后对外提供推理服务的过程。
source: vllm.ai
url: https://vllm.ai
date: 2026-06-22
category: person/vllm.ai
translated: true
fetched_at: 2026-06-22T17:56:23.803913
---
# ## 翻译

**原文修正：**
The High-Throughput and Memory-Efficient inference and serving engine for LLMs

**中文翻译：**
面向大语言模型的高吞吐量、内存高效推理服务引擎

---

### 术语对照

| 英文术语 | 中文术语 |
|---------|---------|
| High-Throughput | 高吞吐量 |
| Memory-Efficient | 内存高效 |
| Inference | 推理 |
| Serving | 服务/ Serving |
| Engine | 引擎 |
| LLMs (Large Language Models) | 大语言模型 |

> **备注：** "Serving" 在大模型领域通常保留英文或译为"服务"，指模型部署后对外提供推理服务的过程。

**来源**: vllm.ai | **日期**: 2026-06-22

---

# 高性能、高内存效率的 LLM 推理与服务引擎

让每个人都能轻松、快速、低成本地使用 LLM 服务。

开始使用 | 文档

## 简单

在任意硬件上部署最广泛的开源模型。包含即插即用的 OpenAI 兼容 API，可实现即时集成。

## 快速

通过 PagedAttention 最大化吞吐量。高级调度和连续批处理确保 GPU 利用率峰值。

## 成本高效

通过最大化硬件效率来降低推理成本。我们让高性能 LLM 变得人人可负担、人人可访问。

---

## 快速入门

选择您的偏好设置并运行安装命令。

**稳定版** 表示当前经过测试并支持的 vLLM 版本。
**每日构建版** 如果您想使用最新构建版本，可选择此项。

📦 需要 Python 3.10+。推荐使用 Python 3.12+。

⚡ 我们推荐使用 **uv** 以获得更快、更可靠的安装体验。

🔧 其他平台，请参阅 docs.vllm.ai

🎉 查看 🔍 查找哪个版本包含某个 PR 的新功能

## 构建

| 版本 | 平台 | 包 | CUDA 版本 |
|------|------|-----|-----------|
| Stable / Nightly | CUDA / ROCm / XPU / CPU | Python (uv) / Python / Docker | CUDA 13.0 / CUDA 12.9 |

运行此命令：
```
uv pip install vllm --torch-backend auto
```

💡 兼容所有 CUDA 13.x 版本 (13.0 - 13.1) · 故障排除 | 寻找旧版本？

---

## 赞助商

vLLM 是一个社区项目。以下组织为我们的开发和测试提供了计算资源。感谢您的支持！

**现金捐赠：** a16z | Sequoia Capital | Skywork AI | ZhenFund

**计算资源：** Alibaba Cloud | AMD | Anyscale | AWS | Crusoe Cloud | Google Cloud | IBM | Intel | Lambda Lab | Nebius | Novita AI | NVIDIA | Red Hat | Roblox | RunPod | UC Berkeley

**Slack 赞助商：** Inferact

**Stars:** ⭐ | **Contributors:** 👥 | **PyTorch Foundation**

我们通过 GitHub 和 OpenCollective 接受捐赠。我们计划使用这些资金来支持 vLLM 的开发、维护和推广。

---

## 通用兼容性

一个引擎，无限可能。在任意硬件上运行任意模型。

### 硬件 | 跨平台统一 API

| 厂商 | 硬件 | 状态 |
|------|------|------|
| NVIDIA | CUDA GPU | 热门 |
| AMD | ROCm GPU | |
| 华为 | 昇腾 NPU | |
| AWS | Neuron Accelerator | |
| 谷歌 | 云 TPU | |
| IBM | Spyre Accelerator | |
| 英特尔 | Gaudi / XPU | |
| CPU | CPU | |
| 苹果 | Apple Silicon | |

[查看所有支持的硬件]

---

## 开源模型

最新流行的开源模型，已优化并可投入生产

### DeepSeek
DeepSeek V4 | DeepSeek V3.2 | DeepSeek R1

### 谷歌
Gemma 4 | Gemma 3

### Meta
Llama 4 Scout | Llama 4 Maverick

### MiniMax
MiniMax M3 | MiniMax M2.7 | MiniMax M2.5

### Mistral AI
Mistral Small 4 | Mistral Large 3

### MoonshotAI
Kimi K2.6 | Kimi K2.5 | Kimi K2

### NVIDIA
Nemotron 3 Ultra | Nemotron 3 Super | Nemotron 3 Nano

### 通义千问
Qwen3.6 | Qwen3.5 | Qwen3

### 阶跃星辰
Step-3.7-Flash | Step-3.5-Flash

### 智谱AI
GLM 5.1 | GLM 5 | GLM 4.7

[查看所有支持的模型]

---

## 欢迎所有人！

**有问题？** 我们随时为您提供帮助。

无论您是刚开始使用还是在调试复杂的部署，我们的社区对所有人开放。没有任何问题是过于基础的！

- ⚡ 快速友好的回复
- 👥 活跃的维护者
- [加入 Slack](Join Slack) - 实时帮助与讨论
- [访问论坛](Visit Forum) - 可搜索的问答知识库
- [GitHub Issues](GitHub Issues) - 错误报告与功能请求

---

## 资源

探索教程、基准测试和路线图

| 资源 | 描述 | 链接 |
|------|------|------|
| 教程 | 示例笔记本和教程 | recipes.vllm.ai |
| 性能 | 基准测试和比较 | perf.vllm.ai |
| 路线图 | 项目路线图和里程碑 | roadmap.vllm.ai |

*原文请访问 [vllm.ai](https://vllm.ai)*