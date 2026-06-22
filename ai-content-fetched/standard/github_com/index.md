---
title: github.com
source: github.com
url: https://github.com/ggml-org
category: standard
---

# github.com

### 概述

Github 上的 `ggml-org` 组织开发和维护 [ggml](https://github.com/ggml-org/ggml) 机器学习库及相关项目。

* <https://huggingface.co/ggml-org> - `ggml-org` 在 Hugging Face 上的主页
* <https://llama.app> - `llama.cpp` 官方网站

```
graph TD;
ggml --> whisper.cpp
ggml --> llama.cpp
llama.cpp --> coding
llama.cpp --> providers

subgraph coding[编码]
    llama.vim
    llama.vscode
    llama.qtcreator
end

subgraph providers[提供者]
    llama
    LlamaBarn
end

ggml[<a href="https://github.com/ggml-org/ggml"                       style="text-decoration:none;">ggml</a>            <br><span style="font-size:10px;">机器学习库</span>];
whisper.cpp[<a href="https://github.com/ggml-org/whisper.cpp"         style="text-decoration:none;">whisper.cpp</a>     <br><span style="font-size:10px;">语音转文字</span>];
llama.cpp[<a href="https://github.com/ggml-org/llama.cpp"             style="text-decoration:none;">llama.cpp</a>       <br><span style="font-size:10px;">LLM 推理</span>];
llama.vim[<a href="https://github.com/ggml-org/llama.vim"             style="text-decoration:none;">llama.vim</a>       <br><span style="font-size:10px;">Vim/Neovim 插件</span>];
llama.vscode[<a href="https://github.com/ggml-org/llama.vscode"       style="text-decoration:none;">llama.vscode</a>    <br><span style="font-size:10px;">VSCode 插件</span>];
llama.qtcreator[<a href="https://github.com/ggml-org/llama.qtcreator" style="text-decoration:none;">llama.qtcreator</a> <br><span style="font-size:10px;">Qt Creator 插件</span>];
llama[<a href="https://llama.app"                                     style="text-decoration:none;">llama</a>           <br><span style="font-size:10px;">命令行应用</span>];
LlamaBarn[<a href="https://github.com/ggml-org/Llama-macOS"           style="text-decoration:none;">Llama-macOS</a>     <br><span style="font-size:10px;">macOS 应用</span>];
```

 加载中

### 最新动态

* `[2026 年 5 月 29 日]` [llama.app 发布](https://llama.app)
* `[2026 年 5 月 29 日]` [whisper.cpp v1.8.5](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.8.5)
* `[2026 年 3 月 22 日]` [VMware Private AI Foundation with NVIDIA 9.0](https://techdocs.broadcom.com/us/en/vmware-cis/private-ai/foundation-with-nvidia/9-0/private-ai-release-notes/vmware-private-ai-services-release-notes.html)
* `[2026 年 3 月 19 日]` [whisper.cpp v1.8.4](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.8.4)
* `[2026 年 3 月 16 日]` [ggml v0.9.8 发布](https://github.com/ggml-org/ggml/releases/tag/v0.9.8)
* `[2026 年 2 月 20 日]` [ggml.ai 加入 Hugging Face 🎉](https://github.com/ggml-org/llama.cpp/discussions/19759)
* `[2026 年 1 月 28 日]` [LlamaBarn v0.24.0 发布](https://github.com/ggml-org/LlamaBarn/releases/tag/0.24.0)
* `[2026 年 1 月 15 日]` [whisper.cpp v1.8.3 发布](https://github.com/ggml-org/whisper.cpp/releases/tag/v1.8.3)

2025 年动态

* `[2025 年 12 月 31 日]` [ggml v0.9.5 发布](https://github.com/ggml-org/ggml/releases/tag/v0.9.5)
* `[2025 年 12 月 12 日]` [使用 AWS Nitro Enclaves 构建医疗领域的零信任生成式 AI 应用](https://aws.amazon.com/blogs/compute/building-zero-trust-generative-ai-applications-in-healthcare-with-aws-nitro-enclaves/)
* `[2025 年 10 月 28 日]` [ggml-org/llama.cpp 入选 GitHub Octoverse 2025 报告，按贡献者数量位列顶级开源项目](https://github.blog/news-insights/octoverse/octoverse-a-new-developer-joins-github-every-second-as-ai-leads-typescript-to-1/)
* `[2025 年 10 月 21 日]` [NVIDIA RTX 5090 在本地运行 OpenAI 语言模型方面超越 AMD 和 Apple](https://www.pcworld.com/article/2916928/nvidia-rtx-5090-outperforms-amd-and-apple-running-local-openai-language-models.html)
* `[2025 年 9 月 18 日]` [AMD 最新开源优化使 Llama.cpp 在 Windows 11 上的 AI 性能表现更佳](https://www.phoronix.com/review/llama-cpp-windows-linux)
* `[2025 年 9 月 9 日]` [Llama.cpp 遇上 Instinct：开源 AI 加速的新时代](https

*原文: https://github.com/ggml-org*