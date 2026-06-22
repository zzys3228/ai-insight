# AI 信息源单一来源（Single Source of Truth）

> 本文件是 AI 日报 / 30 分钟巡检 / 健康检查的唯一权威信息源。

---

## 一、AI头部公司 (Company)

> 追踪维度：产品线（API/文档）→ 官方博客 → 年度大会 → 开源项目

### 1.1 算力&底层硬件

| # | 三级 | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|------|-----|---------|------|------|------|
| 1 | NVIDIA | NVIDIA Blog | https://blogs.nvidia.com | 官方博客 | ✅ | - | - |
| 2 | | NVIDIA Developer Blog | https://developer.nvidia.com/blog | 开发者博客 | ✅ | - | - |
| 3 | | NVIDIA Research | https://research.nvidia.com | 研究博客 | ✅ | - | - |
| 4 | | GTC 大会 | https://www.nvidia.com/gtc/ | 年度最大大会 | ✅ | - | - |
| 5 | | CUDA Toolkit | https://developer.nvidia.com/cuda-toolkit | 基础设施 | ✅ | - | - |
| 6 | | CUDA Release Notes | https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/ | 产品更新日志 | ✅ | - | - |
| 7 | | cuDNN | https://developer.nvidia.com/cudnn | 加速库 | ✅ | - | - |
| 8 | | NCCL | https://developer.nvidia.com/nccl | 多卡通信 | ✅ | - | - |
| 9 | | TensorRT | https://developer.nvidia.com/tensorrt | 推理优化 | ✅ | - | - |
| 9.1 | | TensorRT Release Notes | https://docs.nvidia.com/deeplearning/tensorrt/release-notes/ | 产品更新日志 | ✅ | - | - |
| 10 | | TensorRT-LLM | https://developer.nvidia.com/tensorrt-llm | 大模型推理 | ✅ | - | - |
| 11 | | TensorRT-LLM GitHub | https://github.com/NVIDIA/TensorRT-LLM | 企业级LLM推理优化核心框架 | ✅ | 否 | daily |
| 12 | | Triton Inference Server | https://developer.nvidia.com/triton-inference-server | 模型服务 | ✅ | - | - |
| 13 | | NVIDIA NIM | https://developer.nvidia.com/nim | 推理微服务 | ✅ | - | - |
| 14 | | NeMo | https://developer.nvidia.com/nemo | 生成式AI套件 | ✅ | - | - |
| 15 | | Riva | https://developer.nvidia.com/riva | 语音AI | ✅ | - | - |
| 15.1 | | Riva Release Notes | https://docs.nvidia.com/riva/ | 产品更新日志 | ✅ | - | - |
| 16 | | DeepStream | https://developer.nvidia.com/deepstream-sdk | 视频AI | ✅ | - | - |
| 17 | | Isaac 机器人平台 | https://developer.nvidia.com/isaac | 机器人仿真 | ✅ | - | - |
| 18 | | Omniverse | https://www.nvidia.com/omniverse | 数字孪生 | ✅ | - | - |
| 19 | | NGC 容器仓库 | https://catalog.ngc.nvidia.com | 镜像仓库 | ✅ | - | - |
| 20 | | Cosmos 物理世界模型 | https://www.nvidia.com/en-us/ai/cosmos/ | 物理AI基座模型 | ✅ | - | - |
| 21 | | cuDF/RAPIDS | https://developer.nvidia.com/topics/ai/data-science/cuda-x-data-science-libraries/cudf | GPU数据分析库 | ✅ | - | - |
| 22 | | cuDNN GitHub | https://github.com/NVIDIA/cudnn | GPU加速库 | ✅ | - | - |
| 23 | | CUDA GitHub | https://github.com/NVIDIA/cuda | 基础工具包 | ✅ | - | - |
| 24 | AMD | AMD ROCm | https://rocm.docs.amd.com | 开源AI计算平台 | ✅ | - | - |
| 25 | | AMD Instinct | https://www.amd.com/en/accelerators/instinct.html | AI GPU | ✅ | - | - |
| 26 | Intel | Intel Gaudi | https://habana.ai | AI加速器 | ✅ | - | - |
| 27 | | oneAPI | https://www.intel.com/content/www/us/en/developer/tools/oneapi/overview.html | 异构计算框架 | ✅ | - | - |
| 28 | Cerebras | Cerebras WSE-3 | https://www.cerebras.net | 晶圆级AI芯片 | ✅ | 是 | daily |
| 29 | CoreWeave | CoreWeave Cloud | https://coreweave.com | AI云计算 | ✅ | 是 | daily |

### 1.2 大模型原生企业

| # | 三级 | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|------|-----|---------|------|------|------|
| 1 | OpenAI | OpenAI API | https://platform.openai.com/docs | API文档 | ✅302→ | 是 | both |
| 1.1 | | OpenAI Release Notes | https://platform.openai.com/docs/changelog | 产品更新日志 | ✅302→ | 是 | daily |
| 2 | | ChatGPT | https://chat.openai.com | 产品页 | ⚠️403 | 是 | both |
| 3 | | OpenAI Blog | https://openai.com/blog | 官方博客 | ⚠️403 | 是 | both |
| 4 | | OpenAI DevDay | https://openai.com/index | 年度开发者大会 | ⚠️403 | 是 | daily |
| 5 | | DALL-E | https://openai.com/index/dall-e-3 | 图像生成 | ⚠️403 | 是 | daily |
| 6 | Anthropic | Claude API | https://platform.claude.com | API文档 | ✅ | 否 | both |
| 7 | | Claude Code | https://platform.claude.com/claude-code | AI编程 | ✅ | 否 | both |
| 8 | | Claude Managed Agents | https://claude.com/platform | Agent编排API | ✅ | 是 | daily |
| 9 | | Anthropic News | https://www.anthropic.com/news | 官方新闻 | ✅ | 否 | daily |
| 10 | | Anthropic Research | https://www.anthropic.com/research | 研究博客 | ✅ | 是 | daily |
| 11 | | Anthropic Engineering | https://www.anthropic.com/engineering | 工程博客 | ✅ | 是 | daily |
| 12 | | Anthropic Events | https://www.anthropic.com/events | 发布会/演讲 | ✅ | 是 | daily |
| 13 | | Claude Blog | https://claude.com/blog | 用户博客/产品更新 | ✅302→ | 是 | daily |
| 13.1 | | Anthropic Releases | https://docs.anthropic.com/en/docs/about-claude/releases | 产品更新日志 | ✅ | 是 | daily |
| 14 | DeepSeek | DeepSeek 官网 | https://www.deepseek.com | 产品页 | ✅ | 否 | both |
| 15 | | DeepSeek API | https://api-docs.deepseek.com | API文档 | ✅ | 否 | both |
| 16 | | DeepSeek 开放平台 | https://platform.deepseek.com | 模型调用平台 | ✅ | 否 | both |
| 17 | | DeepSeek App | https://chat.deepseek.com | C端产品 | ✅ | 否 | both |
| 18 | | DeepSeek News | https://www.deepseek.com/en/news | 官方博客 | ✅ | 否 | daily |
| 19 | | DeepSeek-V3 | https://github.com/deepseek-ai/DeepSeek-V3 | 国产开源强模型 | ✅ | 否 | daily |
| 20 | | DeepSeek-R1 | https://github.com/deepseek-ai/DeepSeek-R1 | 推理优化模型 | ✅ | 否 | daily |
| 21 | | DeepSeek-Coder V2 | https://github.com/deepseek-ai/DeepSeek-Coder-V2 | 编程辅助模型 | ✅ | 否 | daily |
| 22 | Mistral | Mistral API | https://docs.mistral.ai | API文档 | ✅ | 是 | both |
| 22.1 | | Mistral Docs | https://docs.mistral.ai/getting-started/concepts | 产品文档 | ✅ | 是 | daily |
| 23 | | Mistral Studio | https://mistral.ai/products/studio/ | 模型部署平台 | ✅ | 是 | daily |
| 24 | | Mistral Forge | https://mistral.ai/products/forge/ | 模型训练/对齐/评估 | ✅ | 是 | daily |
| 25 | | Mistral Vibe | https://mistral.ai/products/vibe/ | Agent开发平台 | ✅ | 是 | daily |
| 26 | | Mistral Vibe Code | https://mistral.ai/products/vibe/code/ | 编码Agent | ✅ | 是 | daily |
| 27 | | Mistral Compute | https://mistral.ai/products/compute/ | 训练/推理基础设施 | ✅ | 是 | daily |
| 28 | | Voxtral | https://mistral.ai/news/voxtral-tts/ | 语音TTS/转录 | ✅ | 是 | daily |
| 29 | | Mistral OCR | https://mistral.ai/news/mistral-ocr-3/ | 文档OCR | ✅ | 是 | daily |
| 30 | | Codestral | https://mistral.ai/news/codestral-25-08/ | 编程模型 | ✅ | 是 | daily |
| 31 | | Pixtral | https://mistral.ai/news/pixtral-large/ | 多模态模型 | ✅ | 是 | daily |
| 32 | | Devstral | https://mistral.ai/news/devstral-2-vibe-cli/ | 代码Agent | ✅ | 是 | daily |
| 33 | | Le Chat | https://chat.mistral.ai | 对话助手 | ✅ | 是 | daily |
| 34 | | Mistral News | https://mistral.ai/news/ | 官方博客 | ✅ | 是 | daily |
| 35 | | La Plateforme | https://console.mistral.ai | 控制台 | ✅302→ | 是 | daily |
| 36 | xAI | Grok-4.3 | https://docs.x.ai | 文本生成模型 | ✅ | 是 | both |
| 37 | | Voice API | https://docs.x.ai | TTS/STT/实时语音 | ✅ | 是 | daily |
| 38 | | Imagine API | https://docs.x.ai | 图像/视频生成 | ✅ | 是 | daily |
| 39 | | xAI Blog | https://x.ai/blog | 官方博客 | ✅ | 是 | daily |
| 40 | Cohere | Command API | https://docs.cohere.com/docs/command | API文档 | ✅ | 否 | daily |
| 41 | | Command A+ | https://cohere.com/blog/command-a-plus | 高性能模型 | ✅ | 否 | daily |
| 42 | | Aya Models | https://docs.cohere.com/docs/aya | 多语言模型 | ✅ | 否 | daily |
| 43 | | Transcribe | https://cohere.com/blog/transcribe | 语音转文字 | ✅ | 否 | daily |
| 44 | | Embed API | https://docs.cohere.com/docs/embeddings | 向量API | ✅ | 否 | daily |
| 45 | | Rerank | https://docs.cohere.com/docs/rerank | 搜索重排 | ✅ | 否 | daily |
| 46 | | North | https://cohere.com/blog/north-mini-code | 企业AI平台 | ✅ | 否 | daily |
| 47 | | Cohere Blog | https://cohere.com/blog | 研究博客 | ✅ | 否 | daily |
| 48 | | Cohere Newsroom | https://cohere.com/newsroom | 产品更新 | ✅ | 否 | daily |
| 49 | AI21 Labs | Jurassic-2 | https://www.ai21.com | 文本生成AI | ✅ | 是 | daily |
| 50 | | AI21 Blog | https://www.ai21.com/blog | 研究博客 | ✅ | 是 | daily |
| 51 | Stability AI | Stability AI News | https://stability.ai/news-updates | 公司动态/发布 | ✅302→ | 是 | daily |
| 52 | Together AI | Together Blog | https://www.together.ai/blog | 研究博客 | ✅ | 是 | daily |
| 53 | Replicate | Replicate | https://replicate.com | 模型运行平台 | ✅ | 是 | daily |
| 54 | | Replicate Changelog | https://replicate.com/changelog | 产品更新日志 | ✅ | 是 | daily |
| 55 | Perplexity | Perplexity Blog | https://blog.perplexity.ai | 研究博客 | ✅ | 是 | daily |
| 56 | 01.AI | Yi系列博客 | https://www.lingyiwanwu.com/blog | 开源LLM | ✅ | 否 | daily |

### 1.3 综合科技-海外

| # | 三级 | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|------|-----|---------|------|------|------|
| 1 | Google Cloud | Vertex AI | https://cloud.google.com/vertex-ai | ML平台 | ✅ | 是 | daily |
| 2 | | Vertex AI Release Notes | https://cloud.google.com/vertex-ai/docs/release-notes | 产品更新日志 | ✅ | 是 | daily |
| 3 | | Gemini API | https://ai.google.dev/gemini-api | 生成式AI | ✅ | 是 | daily |
| 4 | | Gemini in Workspace | https://workspace.google.com | 企业AI | ✅ | 是 | daily |
| 5 | | Google I/O | https://io.google | 年度开发者大会 | ✅ | 是 | daily |
| 6 | | Google Cloud Next | https://cloud.google.com/events/google-cloud-next | Cloud年度大会 | ✅ | 是 | daily |
| 7 | | Google AI Blog | https://blog.google/technology/ai | AI博客 | ✅ | 是 | daily |
| 8 | | Google Cloud Blog | https://cloud.google.com/blog | Cloud博客 | ✅ | 是 | daily |
| 9 | Google DeepMind | Gemini | https://deepmind.google/models/gemini/ | Google基础模型总览 | ✅ | 是 | daily |
| 10 | | Gemini Omni | https://deepmind.google/models/gemini-omni/ | 多模态端侧模型 | ✅ | 是 | daily |
| 11 | | Veo | https://deepmind.google/models/veo/ | 视频生成 | ✅ | 是 | daily |
| 12 | | Imagen | https://deepmind.google/models/imagen/ | 图像生成 | ✅ | 是 | daily |
| 13 | | Lyria | https://deepmind.google/models/lyria/ | 音乐生成 | ✅ | 是 | daily |
| 14 | | Gemma | https://ai.google.dev/gemma | 开源LLM | ✅ | 是 | daily |
| 15 | | Jules | https://ai.google.dev/jules | 编程Agent | ✅ | 是 | daily |
| 16 | | AlphaFold | https://deepmind.google/models/alphafold/ | 蛋白质结构预测 | ✅ | 是 | daily |
| 17 | | SIMA | https://deepmind.google/models/sima/ | 3D世界Agent | ✅ | 是 | daily |
| 18 | | DeepMind Blog | https://deepmind.google/blog | 研究博客 | ✅ | 是 | daily |
| 19 | AWS | AWS AI服务总览 | https://aws.amazon.com/machine-learning | AI服务入口 | ✅ | 否 | daily |
| 20 | | Amazon Bedrock | https://aws.amazon.com/bedrock/ | 生成式AI | ✅ | 否 | both |
| 21 | | Bedrock Release Notes | https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html | 产品更新日志 | ✅ | 否 | daily |
| 22 | | Bedrock AgentCore | https://aws.amazon.com/bedrock/agentcore | Agent编排 | ✅ | 否 | daily |
| 23 | | Amazon Q Business | https://aws.amazon.com/q/business | 企业AI | ✅ | 否 | daily |
| 24 | | Amazon Q Developer | https://aws.amazon.com/q/developer/ | AI编程 | ✅ | 否 | both |
| 25 | | Amazon SageMaker | https://aws.amazon.com/sagemaker | ML平台 | ✅ | 否 | both |
| 26 | | SageMaker Release Notes | https://docs.aws.amazon.com/sagemaker/latest/dg/whatis-changelog.html | 产品更新日志 | ✅ | 否 | daily |
| 27 | | AWS re:Invent | https://aws.amazon.com/reinvent/ | 年度大会 | ✅ | 否 | daily |
| 28 | | AWS ML Blog | https://aws.amazon.com/blogs/machine-learning | 发布博客 | ✅ | 否 | daily |
| 29 | Microsoft Azure | Azure OpenAI | https://oai.azure.com | 生成式AI | ✅ | 否 | daily |
| 30 | | Azure AI Studio | https://ai.azure.com | ML平台 | ✅ | 否 | daily |
| 31 | Microsoft | Microsoft 365 Copilot | https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes | 企业办公AI | ✅ | 否 | daily |
| 32 | | Copilot Studio | https://copilotstudio.microsoft.com | 对话平台 | ✅ | 否 | daily |
| 33 | | Microsoft Build | https://build.microsoft.com | 年度开发者大会 | ✅302→ | 否 | daily |
| 34 | | Microsoft Ignite | https://ignite.microsoft.com | 企业大会 | ✅ | 否 | daily |
| 35 | | Azure Blog | https://azure.microsoft.com/blog | 发布博客 | ✅ | 否 | daily |
| 36 | Apple | Apple Intelligence | https://www.apple.com/apple-intelligence | AI功能 | ✅ | 否 | daily |
| 37 | | Apple ML | https://machinelearning.apple.com | ML研究博客 | ✅ | 否 | daily |
| 38 | Meta AI | Llama | https://llama.meta.com | 开源LLM | ✅ | 是 | daily |
| 39 | | Meta AI Blog | https://ai.meta.com/blog | 研究博客 | ✅ | 是 | daily |
| 40 | | PyTorch | https://pytorch.org | ML框架 | ✅ | 否 | daily |
| 41 | | PyTorch Blog | https://pytorch.org/blog/ | 产品更新博客 | ✅ | 否 | daily |
| 42 | | PyTorch GitHub | https://github.com/pytorch/pytorch | 全球最大ML框架 | ✅ | 是 | daily |
| 43 | | Llama GitHub | https://github.com/meta-llama/llama | 开源LLM基座 | ✅ | 是 | daily |
| 44 | Microsoft | AutoGen | https://github.com/microsoft/autogen | 多Agent协作框架 | ✅ | 是 | daily |
| 45 | | DeepSpeed | https://github.com/microsoft/DeepSpeed | 分布式训练/ZeRO | ✅ | 是 | daily |
| 46 | | Semantic Kernel | https://github.com/microsoft/semantic-kernel | AI应用编排 | ✅ | 是 | daily |
| 47 | | Playwright | https://github.com/microsoft/playwright | 浏览器自动化 | ✅ | 是 | daily |
| 48 | Google | TensorFlow | https://www.tensorflow.org | ML框架 | ✅ | 是 | daily |
| 49 | | BERT | https://github.com/google-research/bert | 预训练模型 | ✅ | 是 | daily |
| 50 | | JAX/Flax | https://github.com/google/jax | 高性能ML框架 | ✅ | 是 | daily |
| 51 | HuggingFace | Transformers | https://github.com/huggingface/transformers | NLP标准库 | ✅ | 是 | daily |
| 52 | | HuggingFace Blog | https://huggingface.co/blog | 产品更新博客 | ✅ | 是 | daily |
| 53 | | Diffusers | https://github.com/huggingface/diffusers | 图像生成库 | ✅ | 是 | daily |
| 54 | | TGI | https://github.com/huggingface/text-generation-inference | 推理框架 | ✅ | 是 | daily |
| 55 | OpenAI开源 | Whisper | https://github.com/openai/whisper | 语音识别 | ✅ | 是 | daily |
| 56 | | CLIP | https://github.com/openai/CLIP | 图文对比学习 | ✅ | 是 | daily |
| 57 | Salesforce | Einstein AI | https://www.salesforce.com/ai | 企业AI | ✅ | 是 | daily |
| 58 | | Salesforce Release Notes | https://help.salesforce.com/s/articleView?id=sf.release_notes | 产品更新日志 | ✅ | 是 | daily |
| 59 | Adobe | Firefly AI | https://www.adobe.com/firefly | 生成式AI | ✅ | 是 | daily |
| 60 | | Adobe Release Notes | https://helpx.adobe.com/firefly/user-guide.html | 产品更新日志 | ✅ | 是 | daily |
| 61 | | Adobe Sensei | https://www.adobe.com/sensei.html | AI/ML平台 | ✅ | 是 | daily |
| 62 | IBM | watsonx | https://www.ibm.com/watsonx | 企业AI平台 | ✅ | 否 | daily |
| 63 | | watsonx Release Notes | https://www.ibm.com/docs/en/watsonx/saas | 产品更新日志 | ✅ | 否 | daily |
| 64 | | IBM Research | https://research.ibm.com | 研究博客 | ✅ | 是 | daily |
| 64 | Baidu | ERNIE Bot | https://yiyan.baidu.com | 文心一言 | ✅ | 否 | daily |
| 65 | | 百度AI Lab | https://research.baidu.com | 研究博客 | ✅ | 否 | daily |

### 1.4 阿里云产品

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | 通义千问 Qwen | https://qwenlm.github.io | 生成式AI | ✅ | 否 | both |
| 1.1 | | Qwen Release Notes | https://help.aliyun.com/zh/qwen | 产品更新日志 | ✅ | 否 | daily |
| 2 | 模型服务灵积 | https://dashscope.console.aliyun.com | API平台 | ✅ | 否 | both |
| 3 | PAI ML平台 | https://help.aliyun.com/zh/pai | ML平台 | ✅ | 否 | both |
| 3.1 | | PAI Release Notes | https://help.aliyun.com/zh/pai/user-guide/pai-release-notes | 产品更新日志 | ✅ | 否 | daily |
| 4 | 云栖大会 | https://yunqi.aliyun.com | 年度大会 | ✅ | 否 | both |
| 5 | 阿里云天基博客 | https://yq.aliyun.com | 技术博客 | ✅ | 否 | daily |
| 6 | 千问云 MaaS | https://tongyi.aliyun.com | Agent驱动MaaS平台 | ✅ | 否 | both |
| 7 | 百炼大模型平台 | https://www.aliyun.com/product/bailian | 一站式大模型开发平台 | ✅ | 否 | both |
| 7.1 | | 百炼 Release Notes | https://www.alibabacloud.com/help/en/model-studio/latest/release-notes | 产品更新日志 | ✅ | 否 | daily |
| 8 | PAI-灵骏 | https://www.aliyun.com/product/pai | 万亿参数模型训推一体 | ✅ | 否 | daily |
| 9 | 无影 AgentBay | https://www.aliyun.com/product/agentbay | AI Agent云端沙箱环境 | ✅ | 否 | daily |
| 10 | OpenTrek 智能体工厂 | https://www.aliyun.com/product/opentrek | 智能体全链路闭环构建 | ✅ | 否 | daily |
| 11 | 通义灵码 Qoder CN | https://www.aliyun.com/product/qoder | 智能编码辅助 | ✅ | 否 | daily |
| 12 | 骡子快跑 MuleRun | https://www.aliyun.com/product/mulerun | AI原生智能办公平台 | ✅ | 否 | daily |
| 13 | DashVector | https://www.aliyun.com/product/dashvector | 向量检索服务 | ✅ | 否 | daily |
| 14 | 虚拟数字人 | https://www.aliyun.com/product/eiam | AI数字人构建 | ✅ | 否 | daily |
| 15 | AI应用市场 | https://marketplace.aliyun.com | 一站式AI产品交易平台 | ✅ | 否 | daily |
| 16 | Agentic Cloud | https://summit.aliyun.com/2026 | 全栈Agent云服务 | ✅ | 否 | daily |

### 1.5 百度智能云产品

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | 文心大模型 ERNIE 5.0 | https://wenxin.baidu.com | 原生全模态大模型 | ✅ | 否 | both |
| 2 | 千帆大模型平台 | https://cloud.baidu.com/product/wenxin | 企业级Agent开发平台 | ✅ | 否 | both |
| 2.1 | | ERNIE Release Notes | https://cloud.baidu.com/doc/user_guide/releaseNotes | 产品更新日志 | ✅ | 否 | daily |
| 3 | Create开发者大会 | https://create.baidu.com | 年度大会 | ✅ | 否 | both |
| 4 | 百度研究院 | https://research.baidu.com | 研究博客 | ✅ | 否 | daily |
| 5 | 百度百舸 AI计算平台 | https://cloud.baidu.com/product/aigc | 大模型训推一体化 | ✅ | 否 | daily |
| 6 | DuClaw Agent服务 | https://cloud.baidu.com/product/duclaw | 零部署Agent服务 | ✅ | 否 | daily |
| 7 | 数字员工 | https://cloud.baidu.com/product/digital | 可进化企业级Agent | ✅ | 否 | daily |
| 8 | 百度伐谋 | https://cloud.baidu.com/product/bdfm | 超级决策智能体 | ✅ | 否 | daily |
| 9 | 智能文档分析 | https://cloud.baidu.com/doc | 文档处理智能助手 | ✅ | 否 | daily |
| 10 | 视频生成 | https://cloud.baidu.com/product/vid | 文生视频/图生视频 | ✅ | 否 | daily |
| 11 | 司南内容审核 | https://cloud.baidu.com/product/content-moderation | 多模态内容审核 | ✅ | 否 | daily |
| 12 | 百度胜算 | https://cloud.baidu.com/product/shengsuan | AI超级数据库 | ✅ | 否 | daily |
| 13 | 数字人实时语音 | https://cloud.baidu.com/product/digital-human | AI数字人 | ✅ | 否 | daily |
| 14 | 智能推荐引擎 | https://cloud.baidu.com/product/recommend | 个性化推荐 | ✅ | 否 | daily |
| 15 | 百度一见·视觉智能体 | https://cloud.baidu.com/product/vip | 云边协同视觉智能 | ✅ | 否 | daily |

### 1.6 腾讯云产品

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | 混元大模型 Hy3 | https://cloud.tencent.com/product/hunyuan | 生成式AI，OpenRouter周榜第一 | ✅ | 否 | both |
| 1.1 | | 混元 Release Notes | https://cloud.tencent.com/document/product/845 | 产品更新日志 | ✅ | 否 | daily |
| 2 | 腾讯云TI平台 | https://cloud.tencent.com/product/ti | ML平台 | ✅ | 否 | both |
| 3 | 腾讯全球数字生态大会 | https://cloud.tencent.com/event/tencent-conference | 年度大会 | ✅ | 否 | both |
| 4 | WorkBuddy 云电脑 | https://cloud.tencent.com/developer/article/2651884 | C端AI桌面智能体 | ✅ | 否 | both |
| 5 | ADP 3.0 智能体平台 | https://cloud.tencent.com/product/adp | 企业级智能体开发底座 | ✅ | 否 | daily |
| 6 | 企微AI智能体 | https://work.weixin.qq.com | 企业微信专属AI | ✅ | 否 | daily |
| 7 | 腾讯会议AI同传 | https://meeting.tencent.com | 会议实时翻译 | ✅ | 否 | daily |
| 8 | 全场景出行智能体 | https://cloud.tencent.com/product/transport-ai | 出行行业Agent方案 | ✅ | 否 | daily |
| 9 | 腾讯云智服 | https://cloud.tencent.com/product/ics | 智能客服Agent | ✅ | 否 | daily |
| 10 | TDSQL 数据库智能体 | https://cloud.tencent.com/product/tdsql | 数据库+AI增强 | ✅ | 否 | daily |
| 11 | Agent Runtime | https://cloud.tencent.com/product/ags | Agent运行时 | ✅ | 否 | daily |
| 12 | Agent 沙箱服务 | https://cloud.tencent.com/product/agsx | Agent安全沙箱 | ✅ | 否 | daily |
| 13 | Agent 网关服务 | https://cloud.tencent.com/product/agw | Agent流量管理 | ✅ | 否 | daily |
| 14 | Agent 记忆服务 | https://cloud.tencent.com/product/agm | Agent记忆存储 | ✅ | 否 | daily |
| 15 | 数据库AI服务 | https://cloud.tencent.com/product/tdai | 数据库开发运维Agent | ✅ | 否 | daily |
| 16 | 数据分析智能体 | https://cloud.tencent.com/product/dataagent | 数据分析Agent | ✅ | 否 | daily |
| 17 | 腾讯云代码助手 | https://cloud.tencent.com/product/acc | AI编程辅助 | ✅ | 否 | daily |
| 18 | Cloud Mate | https://cloud.tencent.com/product/cloudmate | 智能运维AI Agent | ✅ | 否 | daily |
| 19 | TokenHub | https://cloud.tencent.com | 大模型API服务平台 | ✅ | 否 | daily |

### 1.7 火山引擎产品

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | 豆包大模型 2.0 | https://www.volcengine.com/product/doubao | 多模态模型，深度思考与视觉理解 | ✅ | 否 | both |
| 2 | Seedance 2.0 视频生成 | https://www.volcengine.com/product/seedance | 视频生成，指令精准运动表现 | ✅ | 否 | daily |
| 3 | Seedream 5.0 图像创作 | https://www.volcengine.com/product/seedream | 文生图/图生图，联网检索 | ✅ | 否 | daily |
| 4 | 火山方舟 | https://www.volcengine.com/product/ark | 一站式大模型服务平台 | ✅ | 否 | both |
| 5 | 扣子 Coze Pro | https://www.coze.cn | 企业级AI Agent开发平台 | ✅ | 否 | both |
| 6 | HiAgent | https://www.volcengine.com/product/hiagent | 1+N+X智能体工作站 | ✅ | 否 | daily |
| 7 | ArkClaw | https://www.volcengine.com/product/arkclaw | 7×24专属智能伙伴 | ✅ | 否 | daily |
| 8 | 安全运营智能体 | https://www.volcengine.com/product/sec-agent | 企业安全Agent | ✅ | 否 | daily |
| 9 | TRAE CN | https://www.volcengine.com/product/trae | AI代码助手 | ✅ | 否 | daily |
| 10 | 联网问答Agent | https://www.volcengine.com/product/chatbot | 通用chatbot构建 | ✅ | 否 | daily |
| 11 | 数据智能体 | https://www.volcengine.com/product/data-agent | 企业数据专家 | ✅ | 否 | daily |
| 12 | 剧创Agent | https://www.volcengine.com/product/drama-agent | AI短剧生成 | ✅ | 否 | daily |
| 13 | KickArt | https://www.volcengine.com/product/kickart | 创意广告生成 | ✅ | 否 | daily |
| 14 | 火山引擎 Force大会 | https://volcengine.com | 年度大会 | ✅ | 否 | both |
| 15 | Seed团队博客 | https://seed.bytedance.com/blog | 研究博客 | ✅302→ | 否 | daily |

### 1.8 华为云产品

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | 盘古大模型 | https://www.huaweicloud.com/product/pangu.html | 生成式AI | ✅ | 否 | both |
| 2 | ModelArts | https://console.huaweicloud.com/modelarts | ML平台 | ✅ | 否 | both |
| 3 | 昇思MindSpore | https://www.mindspore.cn | ML框架 | ✅ | 否 | daily |
| 4 | 华为云码道 CodeArts | https://www.huaweicloud.com/product/codearts | AI代码智能体 | ✅ | 否 | both |
| 5 | 智果AgentArts | https://www.huaweicloud.com/product/agentarts | 企业Agent开发平台 | ✅ | 否 | daily |
| 6 | 智果园 | https://www.huaweicloud.com/product/zgpy | 百模Agent平台 | ✅ | 否 | daily |
| 7 | OfficeAce | https://www.huaweicloud.com/product/officeace | 办公场景桌面AI助手 | ✅ | 否 | daily |
| 8 | MaaS模型服务 | https://www.huaweicloud.com/product/maas | 一键模型调用 | ✅ | 否 | both |
| 9 | DataArts Studio | https://www.huaweicloud.com/product/dataarts | 数据治理+AI | ✅ | 否 | daily |
| 10 | 行业AI梦工厂 | https://www.huaweicloud.com/product/ai-factory | 行业AI创新平台 | ✅ | 否 | daily |
| 11 | 具身智能专区 | https://www.huaweicloud.com/product/embodied | 具身AI数据合成开发 | ✅ | 否 | daily |
| 12 | HDC开发者大会 | https://www.huaweicloud.com/events/ | 年度大会 | ✅ | 否 | both |
| 13 | 黄大年茶思屋 | https://www.chaspark.com | 华为技术社区·学术交流 | ✅ | 否 | daily |

### 1.9 国产AI芯片

| # | 三级 | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|------|-----|---------|------|------|------|
| 1 | 海光 | 海光DCU | https://www.hengguangda.com | 国产GPU | ✅ | 否 | daily |
| 2 | 寒武纪 | 寒武纪官网 | https://www.cambricon.com | AI芯片 | ✅ | 否 | daily |
| 3 | | MLU370 | https://www.cambricon.com | MLU系列 | ✅ | 否 | daily |
| 4 | 摩尔线程 | 摩尔线程 | https://www.mthreads.com | 国产GPU | ✅ | 否 | daily |
| 5 | | MUSA SDK | https://www.mthreads.com | 开发者SDK | ✅ | 否 | daily |
| 6 | 沐曦 | 沐曦官网 | https://www.metax.tech | AI GPU | ✅ | 否 | daily |
| 7 | 燧原科技 | 燧原官网 | https://www.enflame-tech.com | 训练推理芯片 | ✅ | 否 | daily |
| 8 | 昇腾 | 华为昇腾AI | https://www.hiascend.com | 国产AI芯片 | ✅ | 否 | daily |
| 9 | | 鲲鹏计算 | https://www.huaweicloud.com/product/kunpeng.html | 通用处理器 | ✅ | 否 | daily |

### 1.10 AI产品与应用

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Cursor | https://cursor.com | AI代码编辑器 | ✅ | 是 | daily |
| 2 | v0 | https://v0.dev | 前端生成AI | ✅307 | 是 | daily |
| 3 | BentoML | https://www.bentoml.com | 模型服务平台 | ✅ | 是 | daily |
| 4 | Dify | https://dify.ai | 开源LLM应用平台 | ✅ | 否 | both |
| 5 | Notion AI | https://notion.so/ai | AI笔记助手 | ✅ | 否 | daily |
| 6 | Gamma | https://gamma.app | AI演示文稿 | ✅ | 是 | daily |
| 7 | Runway | https://runwayml.com | AI视频生成 | ✅ | 是 | daily |
| 8 | ElevenLabs | https://elevenlabs.io | AI语音合成 | ✅ | 是 | daily |
| 9 | HeyGen | https://heygen.com | AI数字人 | ✅301→ | 是 | daily |
| 10 | NotebookLM | https://notebooklm.google | AI研究助手 | ✅ | 是 | daily |
| 11 | Suno | https://suno.ai | AI音乐生成 | ✅ | 是 | daily |
| 12 | Udio | https://udio.com | AI音乐生成 | ✅ | 是 | daily |
| 13 | Character.AI | https://character.ai | AI角色对话 | ✅ | 是 | daily |
| 14 | Leonardo AI | https://leonardo.ai | AI图像创作 | ✅ | 是 | daily |
| 15 | Ideogram | https://ideogram.ai | AI图像生成 | ✅ | 是 | daily |
| 16 | Notion AI Q&A | https://notion.so | AI问答助手 | ✅ | 否 | daily |

---

## 二、中立技术大会 (Conference)

### 2.1 AI产业生态峰会

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | QCon全球软件开发大会 | https://qcon.infoq.cn | 国内第一综合技术峰会，AI重塑软件研发体系 | ✅302→ | 是 | daily |
| 2 | AICon全球人工智能大会 | https://aicon.infoq.cn | QCon姊妹场，纯AI工程落地 | ✅302→ | 是 | daily |
| 3 | WAIC 世界AI大会 | https://worldaic.com.cn | 中国最大AI大会 | ✅ | 否 | daily |
| 4 | CIIS 中国人工智能产业大会 | https://ciis.caai.cn | 中国人工智能学会主办 | ✅ | 否 | daily |
| 5 | The AI Summit London | https://london.theaisummit.com/ai-summit-event-series | 伦敦第三方产业峰会 | ✅301→ | 是 | daily |
| 6 | The AI Summit NYC | https://newyork.theaisummit.com | 纽约第三方产业峰会 | ✅301→ | 是 | daily |

### 2.2 行业垂直AI峰会

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | 中国金融AI创新峰会 | https://www.fintechweek.hk | 金融科技创新 | ✅ | 否 | daily |
| 2 | AI in Healthcare Summit | https://www.aiinhealthcare.com | 医疗AI国际峰会 | ✅ | 是 | daily |
| 3 | AI Finance Summit | https://www.aifinancesummit.com | 金融AI国际峰会 | ✅ | 是 | daily |

### 2.3 AI开发者开源峰会

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | ModelScope魔搭开发者大会 | https://modelscope.cn | 国内最大开源模型社区 | ✅ | 否 | daily |
| 2 | GOSIM开源创新大会 | https://gosim-lang.org | 全球开源模型/推理框架实践 | ✅ | 是 | daily |
| 3 | FOSDEM | https://archive.fosdem.org | 欧洲最大开源社区会议 | ✅ | 是 | daily |
| 4 | HF Open Source Summit | https://huggingface.co/blog | Hugging Face全球峰会 | ✅ | 是 | daily |
| 5 | Linux Foundation Open Source | https://events.linuxfoundation.org | 开源基金会活动 | ✅ | 是 | daily |
| 6 | PyCon AI | https://us.pycon.org | Python社区AI大会 | ✅ | 是 | daily |
| 7 | Strange Loop | https://thestrangeloop.com | 技术创新大会 | ✅ | 是 | daily |

### 2.4 AI合规与安全峰会

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | RSA Conference | https://rsaconference.com | AI安全交叉大会 | ✅ | 是 | daily |
| 2 | AI Ethics & Governance Summit | https://ai-ethics-and-governance.institute | AI伦理与治理 | ✅ | 是 | daily |
| 3 | 全球AI治理峰会 | https://oecd.ai | OECD AI政策观察站 | ✅ | 是 | daily |
| 4 | 生成式AI合规发展论坛 | https://cac.gov.cn | 国内AI合规源头 | ✅ | 是 | daily |

---

## 三、开源社区项目 (OpenSource)

### 3.1 本地推理/量化

| # | 源名 | URL | Stars | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|-------|---------|------|------|------|
| 1 | llama.cpp | https://github.com/ggml-org/llama.cpp | 70k+ | 本地推理标杆 | ✅ | - | - |
| 2 | Ollama | https://github.com/ollama/ollama | 85k+ | 本地模型运行 | ✅ | - | - |
| 3 | GGUF/GGML | https://github.com/ggml-org/ggml | - | 本地大模型格式 | ✅ | - | - |
| 4 | llamafile | https://github.com/Mozilla-Ocho/llamafile | 15k+ | 单文件LLM运行 | ✅ | - | - |

### 3.2 社区Agent框架

| # | 源名 | URL | Stars | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|-------|---------|------|------|------|
| 1 | AutoGPT | https://github.com/Significant-Gravitas/AutoGPT | 185k+ | 最早出圈自主Agent | ✅ | - | - |
| 2 | OpenCode | https://github.com/anomalyco/opencode | 176k+ | 开源编码Agent | ✅ | - | - |
| 3 | OpenHands | https://github.com/OpenHands/OpenHands | 78k+ | 自主Agent框架 | ✅ | - | - |
| 4 | eliza | https://github.com/elizaOS/eliza | 19k+ | 开源Agent操作系统 | ✅ | - | - |
| 5 | SuperAGI | https://github.com/TransformerOptimus/SuperAGI | 18k+ | 开发者优先Agent框架 | ✅ | - | - |
| 6 | CrewAI | https://github.com/crewAIInc/crewAI | 25k+ | 多Agent编排框架 | ✅ | - | - |
| 7 | LangGraph | https://github.com/langchain-ai/langgraph | 28k+ | Agent编排引擎 | ✅ | 是 | - |
| 8 | headroom | https://github.com/useheadroom/headroom | 3.7k+ | LLM输入压缩60-95% | ✅ | - | daily |

### 3.3 本地AI应用

| # | 源名 | URL | Stars | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|-------|---------|------|------|------|
| 1 | Open WebUI | https://github.com/open-webui/open-webui | 30k+ | 本地对话UI | ✅ | - | - |
| 2 | AnythingLLM | https://github.com/Mintplex-Labs/anything-llm | 15k+ | 私人RAG知识库 | ✅ | - | - |
| 3 | Jan | https://github.com/janhq/jan | 10k+ | 本地ChatGPT替代 | ✅ | - | - |
| 4 | LocalAI | https://github.com/mudler/LocalAI | 8k+ | 本地API兼容层 | ✅ | - | - |

### 3.4 MCP生态

| # | 源名 | URL | Stars | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|-------|---------|------|------|------|
| 1 | codebase-memory-mcp | https://github.com/GreptimeTeam/codebase-memory-mcp | 1.2k+ | 代码MCP服务器158语言 | ✅ | - | daily |
| 2 | kilocode | https://github.com/kilocodeai/kilocode | 500+ | Agentic工程平台 | ✅ | - | daily |
| 3 | OpenMontage | https://github.com/Tiklabs/OpenMontage | 600+ | Agentic视频制作系统 | ✅ | - | daily |
| 4 | flue | https://github.com/astroslabsai/flue | 300+ | 沙盒Agent框架 | ✅ | - | daily |

### 3.5 框架生态

| # | 源名 | URL | Stars | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|-------|---------|------|------|------|
| 1 | vLLM | https://github.com/vllm-project/vllm | 42k+ | 推理引擎事实标准 | ✅ | - | - |
| 2 | SGLang | https://www.sglang.io | 12k+ | 高效LLM框架 | ✅ | - | - |
| 3 | lightLLM | https://github.com/ModelTC/lightllm | 8k+ | 轻量LLM框架 | ✅ | - | - |
| 4 | Dify | https://github.com/langgenius/dify | 42k+ | 国产AI应用平台 | ✅ | 否 | - |
| 5 | ComfyUI | https://github.com/comfyanonymous/ComfyUI | 38k+ | 图像/视频生成工作流 | ✅ | - | - |
| 6 | Ray Blog | https://www.anyscale.com/blog | - | 分布式ML调度 | ✅ | 是 | - |
| 7 | MLX | https://github.com/ml-explore/mlx | 20k+ | Apple Silicon ML | ✅ | - | - |
| 8 | Tabby | https://www.tabbyml.com | 18k+ | 自托管AI代码补全 | ✅ | - | - |
| 9 | Continue | https://github.com/continuedev/continue | 12k+ | 开源AI代码助手 | ✅ | - | - |

### 3.6 学术/独立开源模型

| # | 源名 | URL | Stars | 推荐理由 | 状态 | 代理 |
|---|------|-----|-------|---------|------|------|
| 1 | ChatGLM | https://github.com/THUDM/ChatGLM | 30k+ | 清华THUDM独立org | ✅ | 否 |
| 2 | Yi | https://github.com/01-ai/Yi | 20k+ | 零一万物开源LLM | ✅ | 否 |
| 3 | InternLM | https://github.com/InternLM/InternLM | 25k+ | 上海AI Lab开源 | ✅ | 否 |
| 4 | Falcon | https://github.com/tiiuae/scai-falcon | - | 阿布扎比TII机构 | ✅ | 是 |
| 5 | LLaVA | https://github.com/haotian-liu/LLaVA | - | 多模态模型 | ✅ | 是 |
| 6 | BLIP | https://github.com/salesforce/BLIP | - | 图文预训练 | ✅ | 是 |
| 7 | Stable Diffusion | https://github.com/CompVis/stable-diffusion | - | CompVis独立org | ✅ | 是 |

---

## 四、学术前沿论文 (Academic)

### 4.1 预印本平台

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | HF Papers | https://huggingface.co/papers | 每日精选论文·可看全文 | ✅302 | - | - |
| 2 | Papers With Code | https://paperswithcode.com | 论文+代码+指标 | ✅ | 是 | daily |
| 3 | arXiv cs.CL | https://arxiv.org/list/cs.CL/recent | NLP最新论文列表 | ✅ | - | daily |
| 4 | arXiv cs.AI | https://arxiv.org/list/cs.AI/recent | AI最新论文列表 | ✅ | - | daily |
| 5 | arXiv cs.LG | https://arxiv.org/list/cs.LG/recent | ML最新论文列表 | ✅ | - | daily |
| 6 | JMLR/TMLR | https://jmlr.org | ML理论最权威期刊 | ✅ | - | - |

### 4.2 学术期刊

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Nature AI | https://nature.com | 里程碑式突破首发 | ✅ | - | - |
| 2 | Science AI | https://science.org/topic/artificial-intelligence | 顶级科学期刊 | ✅ | - | - |
| 3 | IEEE TPAMI | https://cscieeexplore.ieee.org/xpl/recentissue.jsp?punumber=83 | CV顶级期刊 | ✅ | - | - |

### 4.3 学术会议

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | NeurIPS | https://nips.cc | ML顶会 | ✅ | 是 | daily |
| 2 | ICML | https://icml.cc | 机器学习头号会议 | ✅ | 是 | daily |
| 3 | ICLR | https://iclr.cc | 深度学习前沿 | ✅ | 是 | daily |
| 4 | CVPR | https://cvpr.thecvf.com | 计算机视觉顶会 | ✅ | 是 | daily |
| 5 | ICCV | https://iccv2027.thecvf.com | 计算机视觉顶会 | ✅ | 是 | daily |
| 6 | ECCV | https://eccv2026.org | 计算机视觉顶会 | ✅ | 是 | daily |
| 7 | ACL | https://aclrollingreview.org | NLP顶会 | ✅ | 是 | daily |
| 8 | EMNLP | https://2026.emnlp.org | NLP顶会 | ✅ | 是 | daily |
| 9 | AAAI | https://aaai.org | 综合AI会议 | ✅ | 是 | daily |
| 10 | IJCAI | https://ijcai.org | 综合AI会议 | ✅ | 是 | daily |
| 11 | SIGGRAPH | https://siggraph.org | 合成内容/3D AI | ✅ | 是 | daily |
| 12 | MLSys | https://mlsys.org | ML系统顶会 | ✅ | 是 | daily |
| 13 | RSS | https://www.robotics-science.org | 机器人顶会 | ✅ | 是 | daily |

### 4.4 高校研究

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Stanford SAIL | https://ai.stanford.edu/blog/ | Fei-Fei Li实验室 | ✅ | 是 | daily |
| 2 | Berkeley BAIR | https://bair.berkeley.edu/blog/ | Pieter Abbeel RL重镇 | ✅ | 是 | daily |
| 3 | CMU ML Blog | https://blog.ml.cmu.edu | CMU机器学习 | ✅ | 是 | daily |
| 4 | MIT CSAIL | https://csail.mit.edu | 全球AI论文产出第一 | ✅ | 是 | daily |
| 5 | NYU CILVR | https://wp.nyu.edu/cilvr | LeCun世界模型组 | ✅ | 否 | daily |
| 6 | 清华THUDM | https://api.github.com/orgs/THUDM/repos | GLM-4/ChatGLM发源地 | ✅ | 否 | daily |
| 7 | 上海AI实验室 | https://shlab.org.cn | 书生大模型 | ✅ | 否 | daily |
| 8 | 北京智源研究院 | https://baai.ac.cn | 悟道大模型 | ✅ | 否 | daily |
| 9 | Mila | https://mila.quebec/ | Yoshua Bengio实验室 | ✅301→ | 是 | daily |
| 10 | Vector Institute | https://vectorinstitute.ai | Hinton联结 | ✅ | 是 | daily |

### 4.5 独立研究机构

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | AI2 (Allen Institute) | https://allenai.org | OLMo完全开源大模型 | ✅ | 是 | daily |
| 2 | Tübingen AI Center | https://www.tuebingen-ai.de | 欧洲最强理论AI | ✅ | 是 | daily |
| 3 | Oxford ML | https://www.ox.ac.uk | DeepMind人才源头 | ✅ | 是 | daily |
| 4 | Cambridge ML | https://mlmi.eng.cam.ac.uk | AI研究重镇 | ✅ | 是 | daily |
| 5 | EPFL AI | https://ai.epfl.ch | 瑞士AI核心 | ✅ | 是 | daily |
| 6 | ETH AI | https://ai.ethz.ch | 欧洲大陆最强AI | ✅ | 是 | daily |
| 7 | 清华IIIS | https://iiis.tsinghua.edu.cn | 姚期智院 | ✅ | 否 | daily |
| 8 | 复旦NLP | https://nlp.fudan.edu.cn | MOSS大模型 | ✅ | 否 | daily |
| 9 | 港中文MMLab | https://mmlab.ie.cuhk.edu.hk | CV重镇 | ✅ | 否 | daily |
| 10 | 中科院自动化所 | https://www.ia.cas.cn | 国内AI论文最高 | ✅ | 否 | daily |

---

## 五、AI关键人物 (Person)

> **URL规则**：个人X/博客 > 公司官方X（无个人账号时）> 避免公司首页

### 5.1 知名AI企业CEO

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Sam Altman (OpenAI) | https://x.com/sama | OpenAI CEO风向标 | ✅ | - | - |
| 2 | 黄仁勋 (NVIDIA) | https://blogs.nvidia.com | 算力风向·CEO署名文章 | ✅ | - | - |
| 3 | Dario Amodei (Anthropic) | https://darioamodei.com | Claude CEO·个人博客 | ✅ | - | - |
| 4 | Elon Musk (xAI) | https://x.com/elonmusk | xAI CEO | ✅ | - | - |
| 5 | Marc Andreessen (a16z) | https://x.com/pmarca | a16z创始人·AI投资风向 | ✅ | - | - |

### 5.2 企业首席科学家/CTO

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Yann LeCun (Meta) | https://x.com/ylecun | AI教父·Meta首席科学家 | ✅ | - | - |
| 2 | Demis Hassabis (DeepMind) | https://x.com/demishassabis | Gemini/AlphaFold负责人 | ✅ | - | - |
| 3 | Ilya Sutskever (SSI) | https://x.com/ilyasut | AI安全先驱·SSI创始人 | ✅ | - | - |
| 4 | Jim Fan (NVIDIA) | https://x.com/DrJimFan | AI Agent/机器人 | ✅ | - | - |
| 5 | Jeff Dean (Google) | https://x.com/JeffDean | Google首席科学家 | ✅ | - | - |
| 6 | Nat Friedman (GitHub前CEO) | https://x.com/natfriedman | 开源/AI投资观点 | ✅ | - | - |

### 5.3 AI研究员/科学家

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Jan Leike (OpenAI前超级对齐) | https://x.com/janleike | 对齐研究·OpenAI离职后独立 | ✅ | - | - |
| 2 | Amanda Askell (Anthropic) | https://x.com/amandaaskell | 模型对齐·红队测试 | ✅ | - | - |
| 3 | Jim Keller (AI投资人) | https://x.com/jimkeller | 芯片/AI系统观点 | ✅ | - | - |

### 5.4 高校学术学者

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Geoffrey Hinton (多伦多) | https://x.com/geoffreyhinton | 图灵奖得主·AI风险观点 | ✅ | 是 | daily |
| 2 | 李飞飞 (World Labs) | https://www.worldlabs.ai | CV先驱·World Labs创始人 | ✅ | 是 | daily |
| 3 | Yoshua Bengio (Mila) | https://x.com/YoshuaBengio | 图灵奖得主·Mila创始人 | ✅ | 是 | daily |
| 4 | 吴恩达 (DeepLearning.ai) | https://www.deeplearning.ai/blog | ML教育教父 | ✅ | 否 | daily |

### 5.5 技术博主/KOL

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Andrej Karpathy | https://karpathy.ai | AI教育/Vibe Coding先驱 | ✅ | - | - |
| 2 | Lilian Weng | https://lilianweng.github.io | Agent/安全深度技术 | ✅ | - | - |
| 3 | Simon Willison | https://simonwillison.net | 新模型独立评测 | ✅ | - | - |
| 4 | Chip Huyen | https://huyenchip.com | ML系统/数据工程 | ✅ | - | - |
| 5 | Jay Alammar | https://jalammar.github.io | 直观ML解释博客 | ✅ | 是 | daily |
| 6 | Sebastian Raschka | https://magazine.sebastianraschka.com | AI研究深度分析 | ✅ | 否 | daily |

### 5.6 开源社区关键人物

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | ggerganov | https://github.com/ggerganov | llama.cpp奠基人 | ✅ | 是 | daily |
| 2 | Soumith Chintala | https://soumith.ch | PyTorch联合创始人 | ✅ | 是 | daily |
| 3 | Thomas Wolf (Hugging Face) | https://huggingface.co | Hugging Face联合创始人 | ✅ | 是 | daily |
| 4 | vLLM团队 | https://vllm.ai | 高效推理引擎团队 | ✅ | 是 | daily |

### 5.7 AI安全专家

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Stuart Russell | https://sites.google.com/view/stuart-russell | 《人工智能》作者·CSER创始人 | ✅ | - | - |

### 5.8 AI专业投资人

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Sarah Guo (Conviction) | https://sarahguo.com | AI专项VC·深度分析 | ✅ | - | - |

---

## 六、权威评测榜单 (Benchmark)

### 6.1 通用大模型综合榜单

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | LMSYS Chatbot Arena | https://arena.ai | 人类盲评对战榜，全球黄金标准 | ✅302→ | 是 | daily |
| 2 | Artificial Analysis | https://artificialanalysis.ai | 独立第三方对比 | ✅ | 是 | daily |
| 3 | HF Open LLM Leaderboard | https://huggingface.co/spaces/open-llm-leaderboard | 开源大模型风向标 | ✅ | 是 | daily |
| 4 | OpenCompass（司南） | https://opencompass.org.cn | 国内大模型度量衡 | ✅ | 否 | daily |
| 5 | LLM Stats | https://llm-stats.com | 300+模型排行榜 | ✅ | 是 | daily |
| 6 | DataLearner | https://www.datalearner.com | 闭源+开源模型横向对比 | ✅ | 是 | daily |

### 6.2 代码/编码Agent榜单

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | SWE-bench Verified | https://www.swebench.com | GitHub bug修复，工业编码金标准 | ✅ | 是 | daily |
| 2 | LiveCodeBench | https://livecodebench.github.io | 实时竞赛级代码评测 | ✅ | 是 | daily |
| 3 | Aider Leaderboard | https://aider.chat/docs/leaderboards | 本地IDE编码实战 | ✅ | 是 | daily |
| 4 | BigCodeBench | https://huggingface.co/spaces/bigcode/bigcodebench | 多语言代码评测 | ✅ | 是 | daily |
| 5 | HumanEval | https://github.com/openai/human-eval | OpenAI代码评测基准 | ✅ | 否 | daily |

### 6.3 通用Agent榜单

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | GAIA Benchmark | https://huggingface.co/gaia-benchmark | 微软+牛津，真实多步骤Agent | ✅ | 是 | daily |
| 2 | AgentBench | https://github.com/THUDM/AgentBench | 清华THUDM多领域任务 | ✅ | 否 | daily |
| 3 | Agent Arena | https://www.designarena.ai/?arena=agents&harness=standard | LMSYS衍生，商用Agent体验 | ✅301→ | 是 | daily |
| 4 | BrowseComp Plus | https://browsecomp.com | 网页浏览Agent专项 | ✅ | 是 | daily |
| 5 | HAL Leaderboard | https://arxiv.org/abs/hal-agent | 多Agent协同，成本+准确率 | ✅ | 是 | daily |
| 6 | WebArena | https://webarena.gitlab.io | 网页操作Agent | ✅ | 是 | daily |
| 7 | MiniWob++ | https://github.com/Farama-Foundation/miniwob-plusplus | Agent微操评测 | ✅ | 是 | daily |

### 6.4 多模态评测

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | MMMU | https://mmmu-benchmark.github.io | 多模态理解评测 | ✅ | 是 | daily |
| 2 | MMBench | https://opencompass.org.cn/MMBench | 国内多模态评测 | ✅ | 否 | daily |
| 3 | MathVista | https://mathvista.github.io | 数学视觉评测 | ✅ | 是 | daily |
| 4 | SEED-Bench | https://huggingface.co/spaces/THUDM/SEED-Bench | 多模态理解评测 | ✅ | 是 | daily |
| 5 | AI2D | https://allenai.org | 科学图表理解 | ✅ | 是 | daily |

### 6.5 推理能力评测

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | ARC-AGI | https://arcprize.org/arc-agi | 抽象推理评测 | ✅ | 是 | daily |
| 2 | GPQA | https://paperswithcode.com/dataset/gpqa | 研究生水平问答 | ✅ | 是 | daily |
| 3 | MMLU | https://paperswithcode.com/sota/multiple-choice-on | 多任务语言理解 | ✅ | 是 | daily |
| 4 | MATH | https://paperswithcode.com/sota/mathematics-tutoring-on | 数学问题评测 | ✅ | 是 | daily |

### 6.6 算力/芯片榜单

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | MLPerf | https://mlperf.org | 训练/推理统一跑分标准 | ✅ | 是 | daily |
| 2 | TechInsights | https://techinsights.com | AI芯片性能榜 | ✅ | 是 | daily |
| 3 | Gartner AI芯片创新指数 | https://gartner.com | 架构/生态综合排名 | ✅ | 是 | daily |

---

## 七、协议与标准 (Standard)

### 7.1 标准治理组织

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | AAIF | https://agentic.ai | MCP/A2A/AGENTS.md托管方 | ✅ | 否 | daily |
| 2 | W3C WebAgents工作组 | https://www.w3.org/groups/wg/agents/ | ANP/A2WF等Web标准 | ✅301→ | 否 | daily |
| 3 | W3C CG AI Agent组 | https://w3c-cg.github.io | 去中心化Agent协议 | ✅ | 否 | daily |
| 4 | NIST CAISI | https://www.nist.gov/caisi | AI标准/框架 | ✅ | 是 | daily |
| 5 | ISO/IEC JTC 1/SC 42 | https://www.iso.org/committee/6794475.html | AI国际标准委员会 | ✅ | 否 | daily |
| 6 | IEEE AI标准委员会 | https://standards.ieee.org | P7007等自主Agent标准 | ✅ | 否 | daily |
| 7 | IETF | https://www.ietf.org | DNS-AID/AGENTS.TXT等RFC草案 | ✅ | 否 | daily |
| 8 | OWASP GenAI | https://genai.owasp.org | Agent安全Top10 | ✅ | 是 | daily |
| 9 | CNCF OpenTelemetry | https://opentelemetry.io | LLM/Agent可观测标准 | ✅ | 是 | daily |
| 10 | OpenAI | https://platform.openai.com | Function Calling标准 | ✅ | 否 | daily |
| 11 | Anthropic | https://docs.anthropic.com | MCP/Claude Messages API | ✅ | 否 | daily |

### 7.2 国际正式标准

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | ISO/IEC 42001 AIMS | https://www.iso.org/standard/81506.html | AI全生命周期治理认证 | ✅ | 否 | daily |
| 2 | ISO/IEC 22989 | https://www.iso.org/standard/83138.html | AI术语定义标准 | ✅ | 否 | daily |
| 3 | IEEE P7007 | https://standards.ieee.org | 自主Agent安全生命周期 | ✅ | 否 | daily |
| 4 | W3C DID + VC | https://www.w3.org/TR/did-core | Agent去中心化身份授权 | ✅ | 否 | daily |
| 5 | NIST AI RMF | https://www.nist.gov/ai-rmf | AI风险管控框架 | ✅ | 是 | daily |
| 6 | A2WF | https://a2wf.github.io/spec | Agent↔网站交互规范 | ✅ | 否 | daily |
| 7 | AGENTS.TXT | https://datatracker.ietf.org/doc/draft-car-agents-txt-wellknown | IETF网站Agent能力声明 | ✅ | 否 | daily |

### 7.3 行业事实协议

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | MCP | https://modelcontextprotocol.io | Agent↔工具统一接口 | ✅ | 否 | daily |
| 2 | A2A | https://a2a-protocol.org | 跨框架Agent互相通信 | ✅ | 否 | daily |
| 3 | AGENTS.md | https://agentics.org | 项目Agent能力声明 | ✅ | 否 | daily |
| 4 | MCP Servers Awesome | https://github.com/punkpeye/awesome-mcp-servers | MCP服务器生态列表 | ✅ | 是 | daily |
| 5 | codebase-memory-mcp | https://github.com/GreptimeTeam/codebase-memory-mcp | 高性能代码MCP服务器 | ✅ | 否 | daily |
| 6 | headroom MCP | https://github.com/useheadroom/headroom | LLM输入压缩MCP | ✅ | 否 | daily |
| 7 | OWASP Agentic Top10 | https://genai.owasp.org | Agent安全风险检测 | ✅ | 是 | daily |
| 8 | OpenTelemetry GenAI | https://opentelemetry.io/docs/specs/semconv/gen-ai/ | LLM全链路追踪埋点 | ✅301→ | 是 | daily |
| 9 | OpenAI Compatible API | https://platform.openai.com | /v1/chat/completions通用接口 | ✅ | 否 | daily |
| 10 | OpenAI Function Calling | https://platform.openai.com | LLM工具调用JSON Schema | ✅ | 否 | daily |
| 11 | Anthropic Messages API | https://docs.anthropic.com | Claude多模态消息结构 | ✅ | 否 | daily |
| 12 | AG-UI | https://docs.ag-ui.com | Agent↔前端双向交互 | ✅ | 是 | daily |
| 13 | GGUF/GGML | https://github.com/ggml-org | 本地LLM权重格式 | ✅ | 否 | daily |
| 14 | AP2 | https://opensource.googleblog.com/2026/04 | Agent跨平台支付协议 | ✅ | 是 | daily |

### 7.4 实验/草案协议

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | WebMCP | https://developer.chrome.com/docs/ai/webmcp | 浏览器内置MCP实验 | ✅ | 是 | daily |
| 2 | ANP | https://w3c-cg.github.io/ai-agent-protocol | W3C CG去中心化协议 | ✅ | 是 | daily |
| 3 | AITP | https://aitp.dev | Agent价值交换结算 | ✅ | 是 | daily |
| 4 | DNS-AID | https://dns-aid.org | IETF草案Agent服务发现 | ✅ | 否 | daily |
| 5 | ANS | https://ansinfo.ai | Agent身份域名规范 | ✅ | 否 | daily |
| 6 | AGNTCY | https://linuxfoundation.org/projects/agntcy | Cisco Agent目录发现 | ✅ | 是 | daily |
| 7 | CHAP | https://arxiv.org/abs/2606.09751 | 人-Agent协同审计 | ✅ | 否 | daily |

---

## 八、行业洞察报告 (Industry)

### 8.1 VC/风投机构

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | a16z AI | https://a16z.com/ai | AI投资趋势 | ✅ | - | - |
| 2 | Y Combinator | https://www.ycombinator.com/blog | AI初创最大摇篮 | ✅ | - | - |
| 3 | 红杉中国 | https://sequoiacap.cn | 国产AI最活跃VC | ✅ | 否 | - |
| 4 | Sequoia AI | https://sequoiacap.com/stories | 硅谷VC | ✅ | 是 | daily |
| 5 | Bessemer Venture Partners | https://www.bvp.com | 企业SaaS/AI投资 | ✅ | - | - |
| 6 | Air Street Capital | https://air-street.com | AI专项VC | ✅302→ | 是 | - |
| 7 | Lightspeed VP | https://lsvp.com | AI基础设施VC | ✅ | 是 | daily |
| 8 | 高瓴资本 | https://www.hillhousecap.com | AI重仓VC | ✅ | 否 | daily |
| 9 | NFX | https://www.nfx.com | AI SaaS VC | ✅ | 是 | daily |
| 10 | Index Ventures | https://www.indexventures.com | 欧洲VC | ✅ | 是 | daily |

### 8.2 国际组织

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | WEF AI | https://www.weforum.org/topics/artificial-intelligence | 全球治理/就业颠覆 | ✅ | 是 | daily |
| 2 | UN AI Advisory | https://www.un.org/digital-emerging-technologies/ai-advisory-body | 最高层AI治理 | ✅ | 是 | daily |

### 8.3 中立智库

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Stanford HAI | https://hai.stanford.edu | AI Index年度报告 | ✅ | - | - |
| 2 | State of AI Report | https://www.stateof.ai | 欧洲视角年度全景 | ✅ | 是 | daily |
| 3 | Epoch AI | https://epoch.ai | scaling laws/算力数据 | ✅ | 是 | daily |
| 4 | MAD Landscape | https://mattturck.com/mad-landscape | ML/AI/Data全景图 | ✅307→ | 是 | daily |
| 5 | 中国信通院 | https://caict.ac.cn | 工信部，行业白皮书 | ✅ | 否 | daily |
| 6 | 量子位智库 | https://www.qbitai.com/tag/报告 | 国内AI产业图谱 | ✅ | 否 | daily |
| 7 | 甲子光年智库 | https://www.jazzyear.com | 产业深度报告 | ✅ | 否 | daily |

### 8.4 专业咨询公司

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Gartner AI | https://gartner.com/en/topics/artificial-intelligence | AI技术成熟度曲线 | ✅ | - | - |
| 2 | McKinsey Digital | https://mckinsey.com/capabilities/mckinsey-digital | 年度AI采用率调查 | ✅ | - | - |
| 3 | Forrester AI | https://www.forrester.com/bold | AI平台评估 | ✅ | - | - |
| 4 | BCG AI | https://www.bcg.com/capabilities/artificial-intelligence | AI落地/市场规模 | ✅ | - | - |
| 5 | IDC AI | https://www.idc.com/topic/generative-ai | AI市场规模预测 | ✅ | 否 | daily |
| 6 | Deloitte AI | https://www2.deloitte.com/us/en/pages/deloitte-analytics/topics/artificial-intelligence | AI采用率报告 | ✅ | 否 | daily |
| 7 | Accenture AI | https://www.accenture.com/us-en/services/applied-intelligence | 企业AI落地 | ✅ | 否 | daily |
| 8 | PwC AI | https://www.pwc.com/gx/en/issues/artificial-intelligence | AI战略咨询 | ✅ | 否 | daily |

### 8.5 政策监管机构

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | EU AI Office | https://digital-strategy.ec.europa.eu | 全球第一个AI法律 | ✅ | - | - |
| 2 | 中国网信办 | https://cac.gov.cn | 国内AI监管源头 | ✅ | 是 | - |
| 3 | OECD AI | https://oecd.ai | 成员国AI政策数据库 | ✅ | 是 | daily |

### 8.6 AI安全机构

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | METR | https://metr.org | 前沿模型危险能力评估 | ✅ | - | - |
| 2 | Apollo Research | https://www.apolloresearch.ai | 欺骗性/scheming评估 | ✅ | - | - |
| 3 | UK AISI | https://www.aisi.gov.uk | 英国政府AI安全机构 | ✅ | - | - |

### 8.7 企业研究院

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | 腾讯研究院 | https://tisi.org | AI治理/伦理报告 | ✅ | 否 | - |
| 2 | 阿里达摩院 | https://damo.alibaba.com | 十大科技趋势 | ✅ | 否 | - |
| 3 | 百度研究院 | https://research.baidu.com | ERNIE技术发源地 | ✅ | 否 | - |

---

## 九、媒体快讯 (Media)

### 9.1 Newsletter

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Import AI | https://importai.substack.com | Jack Clark政策/技术 | ✅ | 是 | daily |
| 2 | The Batch | https://www.deeplearning.ai/the-batch | Andrew Ng每周精选 | ✅307 | 否 | daily |
| 3 | Ben's Bites | https://bensbites.co | AI产品/工具日更 | ✅ | 是 | daily |
| 4 | TLDR AI | https://tldr.tech/ai | AI资讯简报 | ✅ | 是 | daily |
| 5 | TheSequence | https://thesequence.substack.com | AI技术深度分析 | ✅ | 是 | daily |
| 6 | Last Week in AI | https://lastweekin.ai | 详尽周报 | ✅ | 是 | daily |
| 7 | AI Daily | https://aidaily.dev | AI日报 | ✅ | 是 | daily |
| 8 | There's An AI For That | https://theresanaiforthat.com | AI工具聚合 | ✅ | 是 | daily |
| 9 | The Intelligence Age | https://www.intelligenceage.ai | AI深度分析 | ✅ | 是 | daily |

### 9.2 播客音频

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | Lex Fridman Podcast | https://lexfridman.com | 业内最大人物访谈 | ✅ | 是 | daily |
| 2 | Dwarkesh Podcast | https://www.dwarkesh.com/feed | AI圈最深度访谈 | ✅ | 是 | daily |
| 3 | Latent Space Podcast | https://www.latent.space/feed | AI工程师访谈 | ✅ | 是 | daily |
| 4 | No Priors | https://feeds.megaphone.fm/nopriors | Sarah Guo投资视角 | ✅ | 是 | daily |
| 5 | The Gradient Podcast | https://thegradient.pub | AI学术深度访谈 | ✅ | 是 | daily |
| 6 | Hard Fork | https://www.nytimes.com/column/hard-fork | 科技趋势播客 | ✅ | 是 | daily |
| 7 | The AI Podcast | https://podcasts.apple.com/podcast/the-ai-podcast | NVIDIA主持 | ✅ | 是 | daily |
| 8 | Practical AI | https://practicalai.show | Charmed AI主持 | ✅ | 是 | daily |
| 9 | Eye on AI | https://www.eye-on.ai | AI行业分析 | ✅ | 是 | daily |
| 10 | 晚点聊 LateTalk | https://feeds.fireside.fm/latetalk/rss | 晚点团队·AI创始人/芯片高管访谈 | ✅ | 是 | daily |

### 9.3 AI社区讨论

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | r/LocalLLaMA | https://www.reddit.com/r/LocalLLaMA | 本地LLM最热社区 | ✅ | 是 | daily |
| 2 | r/MachineLearning | https://www.reddit.com/r/MachineLearning | ML学术社区 | ✅ | 是 | daily |
| 3 | r/Artificial | https://www.reddit.com/r/Artificial | AI通用讨论 | ✅ | 是 | daily |
| 4 | r/singularity | https://www.reddit.com/r/singularity | AI未来讨论 | ✅ | 是 | daily |
| 5 | Hacker News | https://news.ycombinator.com | 黑客社区AI讨论 | ✅ | 是 | daily |
| 6 | Hugging Face | https://huggingface.co | 开源模型中枢 | ✅ | 是 | daily |
| 7 | GitHub Trending | https://github.com/trending | AI开源趋势 | ✅ | 否 | daily |
| 8 | Product Hunt AI | https://www.producthunt.com/topics/artificial-intelligence | AI产品发布 | ✅ | 是 | daily |
| 9 | HuggingChat | https://huggingface.co/chat | 开源AI对话 | ✅ | 是 | daily |
| 10 | OpenRouter | https://openrouter.ai | 模型聚合平台 | ✅ | 是 | daily |

### 9.4 海外科技媒体

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | TechCrunch AI | https://techcrunch.com/category/artificial-intelligence | 硅谷科技媒体AI | ✅ | 是 | daily |
| 2 | VentureBeat AI | https://venturebeat.com/category/ai | AI行业新闻 | ⚠️429 | 是 | daily |
| 3 | The Verge AI | https://www.theverge.com/ai-artificial-intelligence | 科技产品/AI新闻 | ✅ | 是 | daily |
| 4 | MIT Tech Review AI | https://www.technologyreview.com/topic/artificial-intelligence | 学术媒体，深度报道 | ✅ | 是 | daily |
| 5 | Ars Technica AI | https://arstechnica.com/ai | 技术细节最扎实 | ✅ | 是 | daily |
| 6 | Wired AI | https://www.wired.com/tag/artificial-intelligence | 科技深度报道 | ✅ | 是 | daily |
| 7 | The Information AI | https://www.theinformation.com/topics/artificial-intelligence | 深度独家硅谷报道 | ⚠️403 | 是 | daily |
| 8 | Stratechery | https://stratechery.com | 科技战略分析 | ✅ | 是 | daily |
| 9 | Platformer | https://www.platformer.news | 科技政策深度 | ✅ | 是 | daily |

### 9.5 国内AI媒体

| # | 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|---|------|-----|---------|------|------|------|
| 1 | 机器之心 | https://jiqizhixin.com/articles | 国内AI权威媒体·文章页 | ✅ | 否 | daily |
| 2 | 量子位 | https://www.qbitai.com | AI/量子计算媒体 | ⚠️403 | 是 | daily |
| 3 | 智东西 | https://zdnet.com.cn | AI产业报道 | ✅ | 否 | daily |
| 4 | 36氪AI | https://36kr.com/newsflashes | 创业/科技快讯 | ✅ | 否 | daily |
| 5 | 雷峰网 | https://www.leiphone.com/category/AI | AI科技聚合·AI分类 | ✅ | 否 | daily |
| 6 | 虎嗅AI | https://www.huxiu.com | 科技深度报道 | ✅ | 否 | daily |
| 7 | 品玩AI | https://www.pingwest.com | 科技产品报道 | ✅ | 否 | daily |

---

## 十、机器人公司 (Robot)

> 追踪维度：产品线 → 官方博客/新闻 → 年度大会 → 开源项目（有什么看什么）

### 10.1 海外人形整机

| # | 公司 | 维度 | 内容 | URL | 状态 |
|---|------|------|------|-----|------|
| 1 | Tesla Optimus | 官方X | Tesla官方动态 | https://x.com/Tesla | ✅ |
| 2 | | 官方X | Elon Musk | https://x.com/elonmusk | ✅ |
| 3 | Figure AI | 产品线 | Figure 01/02 | https://www.figure.ai | ✅ |
| 4 | | 官方博客 | 新闻动态 | https://www.figure.ai/news | ✅ |
| 5 | Boston Dynamics | 产品线 | Atlas电动版 | https://bostondynamics.com/products/atlas | ✅301→ |
| 6 | | 产品线 | Spot机器狗 | https://bostondynamics.com/products/spot | ✅301→ |
| 7 | | 官方博客 | 新闻动态 | https://bostondynamics.com/news | ✅302→ |
| 8 | 1X Technologies | 产品线 | NEO人形机器人 | https://www.1x.tech/neo | ✅ |
| 9 | Agility Robotics | 产品线 | Digit | https://www.agilityrobotics.com | ✅ |
| 10 | | 官方博客 | 新闻动态 | https://www.agilityrobotics.com/press-releases | ✅302→ |
| 11 | | 开源 | arcOS | https://github.com/AgilityRobotics | ✅ |
| 12 | Sanctuary AI | 产品线 | Phoenix通用人形 | https://www.sanctuaryai.com/phoenix | ✅ |
| 13 | Apptronik | 产品线 | Apollo人形机器人 | https://apptronik.com/apollo | ✅301→ |

### 10.2 海外具身AI模型

| # | 公司 | 维度 | 内容 | URL | 状态 |
|---|------|------|------|-----|------|
| 1 | Physical Intelligence | 产品线 | π0 VLA模型 | https://www.pi.website | ✅ |
| 2 | | 官方博客 | 技术博客 | https://www.pi.website/blog | ✅ |
| 3 | World Labs (李飞飞) | 产品线 | 世界模型 | https://www.worldlabs.ai | ✅ |
| 4 | Covariant | 产品线 | RFM-1机器人大脑 | https://covariant.ai/robots | ✅301→ |

### 10.3 国内人形整机

| # | 公司 | 维度 | 内容 | URL | 状态 |
|---|------|------|------|-----|------|
| 1 | 智元机器人 | 产品线 | 远征/灵犀系列 | https://www.agibot.com | ✅ |
| 2 | | 官方博客 | 新闻动态 | https://www.agibot.com/news | ✅ |
| 3 | 宇树科技 | 产品线 | H1人形机器人 | https://www.unitree.com/h1 | ✅302→ |
| 4 | | 产品线 | G1人形机器人 | https://www.unitree.com/g1 | ✅302→ |
| 5 | 优必选 | 产品线 | Walker人形机器人 | https://www.ubtrobot.com/cn/walker | ✅301→ |
| 6 | 银河通用 | 产品线 | 银河人形机器人 | https://www.galaxybot.com | ✅ |

### 10.4 国内四足机器人

| # | 公司 | 维度 | 内容 | URL | 状态 |
|---|------|------|------|-----|------|
| 1 | 云深处科技 | 产品线 | 绝影机器狗 | https://www.deeprobotech.com | ✅ |

### 10.5 大厂机器人

| # | 公司 | 维度 | 内容 | URL | 状态 |
|---|------|------|------|-----|------|
| 1 | NVIDIA Isaac | 产品线 | Isaac机器人平台 | https://developer.nvidia.com/isaac | ✅ |
| 2 | | 开源 | Isaac Sim | https://github.com/isaac-sim | ✅ |
| 3 | | 开源 | Isaac ROS | https://github.com/isaac-ros | ✅ |
| 4 | DeepMind Robotics | 产品线 | Gemini Robotics | https://deepmind.google/models/gemini-robotics/ | ✅308→ |

---

**状态说明**：
- ✅ 可直接访问
- ✅301→/✅302→/✅307→/✅308→ 跳转后可达
- ⚠️403/429 反爬限制（需代理）
- ⚠️412 服务器前置条件失败（需特殊headers）

---
> ⚠️ Tome、Midjourney、OpenAI全站等需代理访问
> ⚠️ LMSYS Arena已迁移至 arena.ai
> ⚠️ QCon/AICon (infoq.cn) 451错误 - UA黑名单，需浏览器访问
> ⚠️ WAICF (eu.aiworldcongress.com) 超时 - 无法验证
