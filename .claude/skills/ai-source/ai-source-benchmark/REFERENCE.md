# AI Source Benchmark Reference

## 源列表

### 模型评测榜单
| 榜单 | URL | 核心用途 |
|------|-----|---------|
| LMSYS Chatbot Arena | lmarena.ai | 人类盲评对战榜，最权威 |
| Artificial Analysis | artificialanalysis.ai | 独立第三方性能/价格对比 |
| HF Open LLM Leaderboard | huggingface.co/spaces/open-llm-leaderboard | 开源大模型风向标 |
| OpenCompass | opencompass.org.cn | 国内大模型统一度量衡 |

### Agent评测榜单
| 榜单 | URL | 核心用途 |
|------|-----|---------|
| GAIA Benchmark | gaia-benchmark.dev | 微软+Meta通用AI助手评测 |
| AgentBench | github.com/THUDM/AgentBench | 清华多维度Agent能力 |
| OSWorld | osworld.world | Agent操作真实OS评测 |
| τ²-Bench | github.com/amazon-agi/tau2-bench-verified | 企业级复杂编码Agent |

### 代码评测榜单
| 榜单 | URL | 核心用途 |
|------|-----|---------|
| SWE-bench | swebench.com | Agent/Coding金标准 |
| LiveCodeBench | livecodebench.github.io | 代码生成持续评测 |
| Aider Leaderboard | aider.chat/docs/leaderboards | 本地IDE编码实战 |

## 分渠道检索

### 1. Papers With Code
1. 打开 paperswithcode.com
2. 搜索: agent / large language model / code generation
3. 左侧勾选: Leaderboards

### 2. HuggingFace Spaces
1. huggingface.co/spaces
2. 搜索: leaderboard
3. 过滤官方维护空间

### 3. GitHub检索
```bash
topic:benchmark leaderboard stars:>500 language:python
```

### 4. 高校/实验室
| 高校 | 榜单 | URL |
|------|------|-----|
| 伯克利 | LMSYS | arena.lmsys.org |
| 上海AI实验室 | OpenCompass | opencompass.org.cn |
| 清华 | AgentBench | github.com/THUDM/AgentBench |

## 四重核验

| 维度 | 权威榜单 | 野鸡榜单 |
|------|----------|----------|
| 维护主体 | 高校/开源联盟 | AI自媒体/付费机构 |
| 评测方案 | 数据集+代码开源 | 规则模糊 |
| 付费机制 | 禁止付费提分 | 支持充值 |
| 行业引用 | 大厂官方引用 | 仅自媒体引用 |

## 已知遗漏

| 遗漏 | 原因 |
|------|------|
| LMSYS Arena URL | lmarena.ai → arena.ai |
| HF Open LLM | 尚未加入 |
| OpenCompass | 尚未加入 |
| GAIA Benchmark | 尚未加入 |
| OSWorld | 尚未加入 |
