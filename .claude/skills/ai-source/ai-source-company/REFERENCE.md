# AI Source Company Reference

> 详细方法论和源列表

## 核心原则

每个AI公司追踪**三个维度**：
1. **产品线** — 具体AI产品，像AWS有20+个AI服务
2. **官方博客** — 公司发布重要信息的渠道
3. **年度大会** — 公司发布战略/产品的重要场合

## 三类AI产品区分

| 分类 | 定义 | 示例 |
|------|------|------|
| 底层基座 | 通用大模型、多模态基础模型 | GPT-4, Claude, Gemini |
| C端独立应用 | 聊天、绘图、视频、代码工具 | ChatGPT, DALL-E, Cursor |
| B端/内嵌能力 | 云AI平台、软件内置AI插件 | Bedrock, Office Copilot |

## 四步闭环查找

### 1. 优先扒官方一手信息

| 渠道 | 说明 |
|------|------|
| 产品中心/AI专区 | 百度千帆、阿里云通义、Azure AI Marketplace |
| 技术博客/研究院 | 白皮书、年度技术大会演讲稿 |
| 软件内置AI | 剪映AI、Office Copilot、钉钉AI（最易忽略） |

### 2. 第三方数据库补全

| 渠道 | URL | 用途 |
|------|-----|------|
| AIProductHub | aiproducthub.com | 一键导出公司全部AI工具 |
| 天眼查/企查查 | tianyancha.com | 「产品服务」板块 |
| PitchBook | pitchbook.com | AI融资榜单附带产品清单 |
| App Store/Google Play | 应用商店 | 企业名下所有AI独立App |

### 3. 云厂商AI服务目录

| 云厂商 | 产品目录URL |
|--------|-------------|
| AWS | aws.amazon.com/machine-learning |
| Google Cloud | cloud.google.com/products/machine-learning |
| Azure | azure.microsoft.com/solutions/ai |
| 阿里云 | aliyun.com/product/machine-learning |
| 华为云 | huaweicloud.com/product |

### 4. 行业峰会参展名录

| 大会 | URL | 可找到的公司 |
|------|-----|-------------|
| NVIDIA GTC | nvidia.com/gtc | 算力/AI芯片/机器人 |
| Google I/O | io.google | 全品类AI公司 |
| WAIC | worldaic.com.cn | 国内AI全品类 |

## 输出格式

```
## [公司名]

### 产品线
| # | 产品 | URL | 追踪信源 | 状态 |

### 官方博客
| # | 博客 | URL | RSS | 状态 |

### 年度大会
| # | 大会 | URL | 状态 |

### ⚠️ 待验证
| # | 类型 | 原因 | 建议 |

### ❌ 已废弃/停服
| # | 类型 | 原URL |
```

## 已知遗漏

| 遗漏 | 原因 | 正确做法 |
|------|------|---------|
| NVIDIA Cosmos | 搜索词太泛 | 搜索"NVIDIA Cosmos physical world model" |
| AMD Instinct | 只搜了NVIDIA | 需了解AMD GPU产品线 |
| Stability AI | 只搜了大厂 | 需了解AI创业公司 |

## 预装知识

| 公司类型 | 产品清单 |
|----------|----------|
| NVIDIA | Cosmos, cuDF/RAPIDS, NIM, Nemotron, Triton, cuDNN, NCCL, TensorRT-LLM |
| 大模型创业 | AI21 Labs Jurassic-2, Stability AI Stable Diffusion, Together AI |

## 必检GitHub官方仓库

### 推理框架
| 框架 | GitHub搜索词 | 验证方法 |
|------|------------|---------|
| TensorRT-LLM | `site:github.com/NVIDIA TensorRT-LLM` | 检查NVIDIA官方仓库 |
| HuggingFace TGI | `site:github.com/huggingface text-generation-inference` | 检查HF官方仓库 |

### 开源Agent框架
| 框架 | GitHub搜索词 | Stars门槛 |
|------|------------|---------|
| Microsoft AutoGen | `site:github.com/microsoft autogen` | ≥100k |

## 国产大模型公司官网

### 必检公司
| 公司 | 官网搜索词 | 代表产品 |
|------|----------|---------|
| 智谱AI | `site:zhipuai.cn` | GLM系列 |
| 阶跃星辰 | `site:stepfun.com` | Step-Video |
| 面壁智能 | `site:modelbest.cn` | 端侧小模型 |
| MiniMax | `site:minimaxi.com` | Hailuo视频 |
| 月之暗面 | `site:kimi.com` | 长上下文LLM |
| 百川智能 | `site:baichuan-ai.com` | 开源+闭源 |

### 查找方法
1. 搜索 `{公司名} 官网` → 获取官网URL
2. 检查官网的"产品"或"AI产品"板块
3. 验证产品URL是否可访问
