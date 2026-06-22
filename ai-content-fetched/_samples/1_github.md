---
title: vllm
source: github.com
url: https://github.com/vllm-project/vllm
date: 2026-06-22
category: github
translated: true
fetched_at: 2026-06-22T09:55:55.794926
---

# vllm-project/vllm

**Stars**: 83,496 | **Forks**: 18,296 | **语言**: Python

**描述**: 高吞吐量、内存高效的LLM推理和服务引擎

**Topics**: amd, blackwell, cuda, deepseek, deepseek-v3, gpt, gpt-oss, inference, kimi, llama, llm, llm-serving

---

## 项目介绍

vLLM 是一个用于 LLM 推理和服务的快速、易用库，可帮助用户轻松获得高效的 LLM 服务。

vLLM 最初由加州大学伯克利分校的 [Sky Computing Lab](https://sky.cs.berkeley.edu) 开发，现已发展成为最活跃的开源 AI 项目之一，由来自 2000 多位贡献者的数十个学术机构和公司组成的多元化社区构建和维护。

vLLM 速度极快，具有以下特性：

- 领先的推理吞吐量
- 使用 [**PagedAttention**](https://blog.vllm.ai/2023/06/20/vllm.html) 高效管理注意力键值内存
- 对传入请求进行连续批处理、分块预填充、前缀缓存
- 使用分段和完整 CUDA/HIP 图实现快速灵活的模型执行
- 量化：FP8、MXFP8/MXFP4、NVFP4、INT8、INT4、GPTQ/AWQ、GGUF、compressed-tensors、ModelOpt、TorchAO 等[更多](https://docs.vllm.ai/en/latest/features/quantization/index.html)
- 优化的注意力内核，包括 FlashAttention、FlashInfer、TRTLLM-GEN、FlashMLA 和 Triton
- 使用 CUTLASS、TRTLLM-GEN、CuTeDSL 针对各种精度优化的 GEMM/MoE 内核
- 推测解码，包括 n-gram、suffix、EAGLE、DFlash
- 使用 torch.compile 自动生成内核和图级变换
- 分解式预填充、解码和编码

vLLM 灵活易用，具有以下特性：

- 与流行的 Hugging Face 模型无缝集成
- 使用各种解码算法实现高吞吐量服务，包括*并行采样*、*束搜索*等
- 用于分布式推理的张量、管道、数据、专家和上下文并行
- 流式输出
- 使用 xgrammar 或 guidance 生成结构化输出
- 工具调用和推理解析器
- 兼容 OpenAI 的 API 服务器，以及 Anthropic Messages API 和 gRPC 支持
- 高效支持密集层和 MoE 层的多 LoRA
- 支持 NVIDIA GPU、AMD GPU 和 x86/ARM/PowerPC CPU。此外还支持多种硬件插件，如 Google TPU、Intel Gaudi、IBM Spyre、华为昇腾、Rebellions NPU、Apple Silicon、MetaX GPU 等。

vLLM 无缝支持 Hugging Face 上的 200+ 种模型架构，包括：

- 仅解码器的 LLM（如 Llama、Qwen、Gemma）
- 混合专家 LLM（如 Mixtral、DeepSeek-V3、Qwen-MoE、GPT-OSS）
- 混合注意力状态空间模型（如 Mamba、Qwen3.5）
- 多模态模型（如 LLaVA、Qwen-VL、Pixtral）
- 嵌入和检索模型（如 E5-Mistral、GTE、ColBERT）
- 奖励和分类模型（如 Qwen-Math）

在此处查找[支持的模型完整列表](https://docs.vllm.ai/en/latest/models/supported_models.html)。

## 快速开始

使用 [`uv`](https://docs.astral.sh/uv/)（推荐）或 `pip` 安装 vLLM：

```bash
uv pip install vllm
```

或[从源码构建](https://docs.vllm.ai/en/latest/getting_started/installation/gpu/index.html#build-wheel-from-source)用于开发。

访问我们的[文档](https://docs.vllm.ai/en/latest/)了解更多。

- [安装](https://docs.vllm.ai/en/latest/getting_started/installation.html)
- [快速入门](https://docs.vllm.ai/en/latest/getting_started/quickstart.html)
- [支持的模型列表](https://docs.vllm.ai/en/latest/models/supported_models.html)

## 贡献

我们欢迎并珍视任何贡献和合作。
请查看[为 vLLM 做贡献](https://docs.vllm.ai/en/latest/contributing/index.html)了解如何参与。

## 引用

如果您在研究中使用 vLLM，请引用我们的[论文](https://arxiv.org/abs/2309.06180)：

```bibtex
@inproceedings{kwon2023efficient,
  title={Efficient Memory Management for Large Language Model Serving with PagedAttention},
  author={Woosuk Kwon and Zhuohan Li and ...},
  booktitle={Proceedings of the ACM SIGOPS 29th Symposium on Operating Systems Principles (SOSP '23)},
  year={2023},
  publisher={ACM}
}
```

---

## 发布记录（近半年）

### v0.23.0（2026-06-15）

请注意，Minimax M3 在此版本中尚未支持。

此版本包含来自 200 位贡献者（63 位新增）的 408 次提交！

* **DeepSeek-V4 在各后端日趋成熟**：继在 v0.22.0 中引入后，DeepSeek-V4 获得了又一次大规模加固和优化。其稀疏 MLA 元数据现已与 DeepSeek-V3.2 解耦 (#44699)，新增了 TRTLLM-gen 注意力内核 (#43827)，Mega-MoE 的 EPLB 支持 (#43339)，用于滑动窗口 KV 缓存的选择性前缀缓存保留 (#43447)，以及 DSA MTP 的索引共享功能 (#44420)。该模型也已从 `torch.compile` 中分离出来 (#43746, #43891)，其注意力和 RoPE 路径已重构 (#44569, #44262, #43926)，并添加了 XPU 注意力解码路径 (#42953)。
* **Model Runner V2 扩展至更多稠密模型**：MRv2 现已默认为 **Ll

【v0.22.1】2026-06-05

此版本包含来自 6 位贡献者（1 位新增）的 8 次提交！

v0.22.1 是基于 v0.22.0 的补丁版本，包含针对性错误修复以及一些补充：新增对 JetBrains 的 Mellum v2 模型支持、在 AMD Zen CPU 上进行 zentorch 加速的量化线性推理，以及多项修复：多节点 Ray 数据并行服务、DeepSeek-V4 初始化和一些模型加载回归问题。

### 模型支持
* 新增模型：JetBrains 的 **Mellum v2**，一款开源权重的混合专家代码生成模型 (#43992)。
* **DeepSeek-V4**：解决导致初始化失败的 CUTLASS `fmin` 兼容性问题 (0decac0d)。
* 修复 `OlmoHybridForCausalLM` 在检查点将 `rope_parameters` 从 `None` 更改为 `{"rope_type": None}` 后初始化失败的问题 (#43846)。
* 修复 **HyperCLOVAX** 加载问题（上游 HuggingFace 仓库移除了其远程代码，现已原生支持于 `transformers >= 5.9.0`）：注册 `hyperclovax` model_type 以便 vLLM 使用其自带的配置而非远程代码 (

【v0.22.0】2026-05-29

此版本包含来自 230 位贡献者（63 位新增）的 459 次提交！

* **DeepSeek V4 成熟度提升**：DeepSeek V4 在本周期获得了重要的加固处理——模型被重新组织为专用 `vllm/models/deepseek_v4/` 包 (#43004, #43039, #43073, #43077, #43149)，新增 NVFP4 融合 MoE 支持 (#42209)，完整 + 分段 CUDA 图 (#42604)，以及 MTP 投机解码 (#43385)。大量融合内核（MegaMoE、`mhc`、Q-norm、索引器、稀疏 MLA）和 ROCm 兼容性修复以及精度修复也同时落地 (#42810, #43710)。
* **Model Runner V2 迈向默认选项**：MRv2 现为 Qwen3 稠密模型的默认选项。vLLM 将回退到 MRv1 以支持 MRv2 尚不支持的功能 (#39337)。睡眠模式权重重载 (#42673)、`update_config` (#42783) 和共享 KV 缓存层 (#35045)，以及众多正确性修复。
* **实验性 Rust 前端**：新的 Rust 前端集成已落地 (#40848)，实现已移入代码树 (#43283)，

【v0.21.0】2026-05-15

此版本包含来自 202 位贡献者（49 位新增）的 367 次提交！

* **Transformers v4 已弃用**：此版本正式弃用 `transformers` v4 支持 (#40389)。用户应迁移至 `transformers` v5。
* **C++20 构建要求**：vLLM 现需 C++20 兼容编译器以确保与 PyTorch 的兼容性 (#40380)。这是**破坏性构建变更**。
* **KV 卸载 + 混合内存分配器 (HMA)**：KV 卸载子系统现与混合内存分配器集成，包括调度器端滑动窗口组支持和完整 HMA 启用 (#41228, #41445, #39571)。
* **带思考预算的投机解码**：投机解码现支持遵守推理/思考预算，为推理模型启用正确的投机解码 (#34668)。
* **Blackwell 上的 TOKENSPEED_MLA 后端**：DeepSeek-R1/Kimi-K 的新 TOKENSPEED_MLA 注意力后端已可用 (#

---

*原文请访问 [GitHub仓库](https://github.com/vllm-project/vllm)*
