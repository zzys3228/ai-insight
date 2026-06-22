---
name: ai-source-opensource
description: 检查个人/社区AI开源项目源列表，只做源发现不做内容追踪。追踪llama.cpp/vLLM/Ollama等独立开发者或社区维护的开源项目。核心定位：个人/社区，排除大厂官方开源（大厂开源归 ai-source-company）。Use when user mentions /ai-source-opensource, or asks to check AI open source projects, GitHub repositories, community tools.
---

> **状态**：✅ 已更新（2026-06-21）

# AI Source OpenSource Skill

## Quick Start

- `/ai-source-opensource` — 全量检查，输出建议新增/更新的开源项目源

## URL规则 ⚠️ 重要

### URL类型规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | GitHub仓库 | github.com/ggml-org/llama.cpp | 官方仓库 |
| ✅可选 | 官方文档 | vllm.ai | 项目官网 |
| ✅可选 | 官方博客 | pytorch.org/blog | 框架博客 |

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（第三章及以后无编号）
```

### 输出模板

```markdown
## 三、开源社区项目

### 3.1 本地推理/量化

| 源名 | URL | Stars | 推荐理由 | 状态 | 代理 | 用途 |
|------|-----|-------|---------|------|------|------|
| llama.cpp | https://github.com/ggml-org/llama.cpp | 70k+ | 本地推理标杆 | ✅ | - | - |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ⚠️403 | 需代理 |

## Workflows

### 阶段一：GitHub个人/社区检索
```bash
# 搜索个人/社区开源项目（排除公司官方org）
topic:{分类} stars:>800
NOT org:microsoft
NOT org:google
NOT org:meta
NOT org:nvidia
NOT org:anthropic
NOT org:openai
NOT org:huggingface
NOT org:alibaba
NOT org:tencent
NOT org:baidu
NOT org:bytedance
NOT org:huawei
NOT org:deepseek-ai
NOT org:QwenLM
```

### 阶段零（可选）：URL有效性验证
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段二：分类检索
按8类分别检索关键词

### 阶段三：三重核验
仓库归属/Stars门槛/活跃度

### 阶段四：结构化输出
```
## OpenSource 源检查结果

### 建议新增源
| 项目 | URL | 分类 | Stars | 验证依据 |

### 移除建议
| 项目 | 原因 |
|------|------|
| XXX | 停更/Stars下降 |
```

## 分类体系（8类）

| 分类 | 定义 | 示例 |
|------|------|------|
| LLM轻量化基座 | 独立开发者自研小型基座 | nanoGPT、llama民间复现 |
| 本地推理/量化 | 模型加速、量化、本地引擎 | llama.cpp、Ollama、GGUF |
| 推理框架 | 社区推理引擎（非公司官方） | vLLM、SGLang、TGI（归公司） |
| Agent框架 | 个人/社区Agent编排框架 | AutoGPT、OpenHands、CrewAI |
| 多模态项目 | 个人文生图/VLA模型 | lucidrains系列 |
| RAG/知识库 | 本地RAG知识库、向量数据库 | Qdrant、Weaviate、Chroma |
| AI编程工具 | AI代码助手、本地UI工具 | Continue.dev、Cline、Open WebUI |
| AI安全/可观测 | 社区LLM审计、提示词防护 | 提示词注入检测 |

## 分类边界

- 评测榜单归 Benchmark
- 大厂官方开源 → 归 ai-source-company 开源维度
- 个人/社区开源 → 归 ai-source-opensource

**大厂开源归属对照**：

| 项目 | 归属 | 原因 |
|------|------|------|
| vLLM | ai-source-opensource | vllm-project 独立org |
| SGLang | ai-source-opensource | 个人/社区维护 |
| HuggingFace TGI | ai-source-company | HuggingFace公司官方 |
| AutoGen | ai-source-company | Microsoft公司官方 |
| PyTorch | ai-source-company | Meta公司官方 |
| TensorRT-LLM | ai-source-company | NVIDIA公司官方 |

## 必检Agent框架（社区维护）

| 框架 | GitHub仓库 | 备注 |
|------|-----------|------|
| OpenHands | All-Hands/Handbooks | 开源社区 |
| CrewAI | crewAI/crewai | 社区流行 |
| LangChain Agents | langchain-ai/langchain | 框架内置 |
| AutoGPT | significant/gravitas | 独立开发者 |

## 准入门槛

| 条件 | 标准 |
|------|------|
| 仓库归属 | GitHub仓库，非企业首页 |
| 主导维护 | 个人或社区，非公司官方org |
| 热度 | GitHub Star ≥ 800 |
| 活跃度 | 近3个月有更新 |

## 发现方法：如何发现新的AI开源项目

**❌ 错误做法**：只维护现有项目列表

**✅ 正确做法**：定期扫描以下渠道

```
# 方法一：GitHub Trending（每日必查）
- github.com/trending?since=daily → AI相关
- github.com/trending?l=python&since=weekly → Python AI
- github.com/trending?l=typescript&since=weekly → TS AI
- 搜索 filter:stars>100 pushed:>2024-01-01 AI

# 方法二：Awesome列表追踪（核心渠道）
- awesome-ai → AI全景列表
- awesome-ai-agents → Agent项目汇总
- awesome-mcp-servers → MCP生态（每次必查）
- awesome-llm-inference → 推理优化项目
- awesome-rag → RAG项目汇总
- awesome-llms → 大模型列表
- awesome-ai-tools → AI工具列表
- awesome-local-llms → 本地LLM

# 方法三：特定分类搜索
本地推理：
- site:github.com llama.cpp Ollama GGML
- site:github.com quantized model LLM

Agent框架：
- site:github.com AI agent framework
- site:github.com autonomous agent

RAG/向量：
- site:github.com RAG retrieval augmented
- site:github.com vector database

# 方法四：HuggingFace发现
- huggingface.co/models → trending模型
- huggingface.co/spaces → 有趣的AI应用
- huggingface.co/hub → 新模型/数据集

# 方法五：Reddit/社区发现
- reddit.com/r/LocalLLaMA → 新工具推荐
- reddit.com/r/MachineLearning → 论文+代码
- HN "Show HN" → 新AI项目

# 方法六：框架官方GitHub
- LangChain → github.com/langchain-ai
- LlamaIndex → github.com/run-llama
- vLLM → github.com/vllm-project
- Ollama → github.com/ollama/ollama

# 方法七：MLSys顶会开源项目
- NeurIPS/ICML开源实现
- Papers With Code → 新算法实现
```

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
