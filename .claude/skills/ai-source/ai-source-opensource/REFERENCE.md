# AI Source OpenSource Reference

## 源列表

### 本地推理/量化
| 项目 | URL | Stars | 说明 |
|------|-----|-------|------|
| llama.cpp | github.com/ggerganov/llama.cpp | 70k+ | 本地推理标杆 |
| Ollama | github.com/ollama/ollama | 30k+ | 本地模型最易用 |
| GGUF | github.com/ggml-org/ggml | — | 本地大模型格式 |

### 社区Agent框架
| 项目 | URL | Stars | 说明 |
|------|-----|-------|------|
| OpenCode | github.com/anomalyco/opencode | 176k+ | 开源编码Agent |
| AutoGPT | github.com/Significant-Gravitas/AutoGPT | 185k+ | 最早自主Agent |
| OpenHands | github.com/All-Hands/Awesome-OpenHands | 78k+ | 自主Agent框架 |
| eliza | github.com/elizaOS/eliza | 19k+ | 开源Agent操作系统 |

### 本地AI应用
| 项目 | URL | Stars | 说明 |
|------|-----|-------|------|
| Open WebUI | github.com/open-webui/open-webui | 30k+ | 本地对话UI |
| AnythingLLM | github.com/Mintplex-Labs/anything-llm | 15k+ | 私人RAG知识库 |
| Jan | github.com/janhq/jan | 10k+ | 本地ChatGPT替代 |

## GitHub核心检索

```bash
# 基础模板（排除大厂）
topic:{topic} stars:>800 NOT org:meta NOT org:google NOT org:microsoft NOT org:nvidia

# 替换 topic：llm、agent、multimodal、robotics、rag、llm-safety
```

## 分类检索关键词

```
LLM基座: small llm from independent developer, nanoGPT community
本地推理: llama.cpp Ollama, k-quant GGUF
推理框架: inference server, text generation inference, vllm tgi
Agent框架: lightweight agent framework, OpenHands LocalAGI
编码Agent: coding agent, ai coding, code agent
多模态: open source diffusion model, lucidrains
本地应用: Open-WebUI AnythingLLM, local RAG knowledge base
安全: prompt injection detection, LLM audit logging
```

## 推理框架查找方法

### 问题：漏掉HuggingFace TGI、vLLM

这些是**官方推理框架**，不属于"个人开发者"但Stars极高需要收录。

### 查找方法
```bash
# 搜索官方推理框架
site:github.com/huggingface text-generation-inference
site:github.com/vllm-project vllm
site:github.com/NVIDIA TensorRT-LLM

# Stars门槛：≥10k
```

### 收录规则
| 类型 | Stars门槛 | 示例 |
|------|----------|------|
| 个人/社区推理框架 | ≥800 | llama.cpp, Ollama |
| 官方推理框架 | ≥10k | HuggingFace TGI, vLLM |

## 微软开源Agent查找方法

### 问题：漏掉Microsoft AutoGen

微软是"大厂"，但AutoGen Stars超过100k影响力极大，需要特殊处理。

### 查找方法
```bash
# 搜索微软开源Agent
site:github.com/microsoft autogen
site:github.com/microsoft promptflow

# Stars门槛：≥100k
```

### 收录规则
| 类型 | Stars门槛 | 示例 |
|------|----------|------|
| 微软开源Agent | ≥100k | AutoGen, PromptFlow |
| 个人Agent框架 | ≥800 | AutoGPT, OpenHands |

## 持续追踪

| 方式 | 操作 |
|------|------|
| GitHub Trending | 每日巡检，用排除语法过滤 |
| Awesome清单 | 订阅awesome系列，定期过滤新增大厂 |
| HF个人开发者 | 收藏个人开发者模型标签 |
| Reddit/HN | 订阅r/LocalLLaMA、HackerNews AI |

## 已知遗漏

| 遗漏 | 原因 |
|------|------|
| OpenCode | 编码Agent关键词未命中 |
| OpenHands | 未覆盖社区Agent框架 |
| Open WebUI | 未覆盖本地AI应用 |
| AnythingLLM | 未覆盖本地AI应用 |
