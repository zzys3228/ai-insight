---
name: ai-source-robot
description: 检查机器人/具身智能公司的AI源列表，只做源发现不做内容追踪。追踪Tesla Optimus/Figure/智元机器人/宇树科技等人形整机厂商和具身AI模型公司。Use when user mentions /ai-source-robot, or asks to check humanoid robot companies, embodied AI sources, robotics startups.
---

> **状态**：✅ 已更新（2026-06-22）

# AI Source Robot Skill

## Quick Start

- `/ai-source-robot` — 全量检查，输出建议新增/更新的机器人公司源

## URL规则 ⚠️ 重要

### URL类型规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | 公司产品页 | figure.ai/news, bostondynamics.com/products/atlas | 能直接看产品信息 |
| ✅次选 | 新闻/博客 | bostondynamics.com/news, agilityrobotics.com/press-releases | 官方动态 |
| ✅备选 | 官方X账号 | x.com/Tesla, x.com/elonmusk | Tesla等公司无产品页时用 |
| ❌避免 | 403的产品页 | tesla.com/optimus | 无法访问的页面 |

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（每个10.x节独立编号1-N）
```

### 输出模板

```markdown
## 十、机器人公司

### 10.1 海外人形整机

| # | 公司 | 维度 | 内容 | URL | 状态 |
|---|------|------|------|-----|------|
| 1 | Tesla Optimus | 官方X | Tesla官方动态 | https://x.com/Tesla | ✅ |
| 2 | | 官方X | Elon Musk | https://x.com/elonmusk | ✅ |
| 3 | Figure AI | 产品线 | Figure 01/02 | https://www.figure.ai | ✅ |
```

### 新表格格式 ⚠️ 必须

**必须包含 # 列和公司列**，用于后续追踪：
- #：节内唯一编号
- 公司：便于关联同公司不同维度

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ⚠️403 | 需代理 |

## Workflows

### 阶段一：URL有效性检查
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段二：分类检索
按5类分别检索海外人形/海外具身/国内人形/国内四足/大厂机器人

### 阶段三：四重核验
公司主体/产品真实/商业化/时间有效

### 阶段四：结构化输出
```
## Robot 机器人公司检查结果

### 建议新增公司
| 公司 | URL | 分类 | 核心产品 | 验证依据 |

### URL更新
| 公司 | 原URL | 新URL |

### 移除建议
| 公司 | 原因 |
|------|------|
| XXX | 停更/已倒闭 |
```

## 分类体系（5类）

| 分类 | 定义 | 企业示例 |
|------|------|---------|
| 海外人形整机 | 海外研发/量产人形机器人整机 | Tesla、Figure AI、波士顿动力、1X、Agility |
| 海外具身AI模型 | 不造硬件，专注VLA/世界模型 | Physical Intelligence、World Labs、Covariant |
| 国内人形整机 | 自研人形机器人硬件+具身大模型 | 智元机器人、优必选、宇树科技、银河通用、傅利叶 |
| 国内四足机器人 | 主打四足机器狗，布局人形/具身 | 云深处、松延动力 |
| 大厂机器人 | 科技巨头内部机器人/仿真业务 | NVIDIA Isaac、Google DeepMind Robotics |

## 筛选规则

**必须满足**：
- 独立公司主体、工商/海外注册主体
- 主营机器人硬件整机 或 专用机器人VLA模型商业化服务

**必须剔除**：
- 高校实验室（CMU Robotics等）
- 非营利研究所
- 纯开源项目（非商业化）

**时间范围**：仅收录2024-2026有产品发布/量产/大额融资的活跃企业

## 发现方法：如何发现新的机器人公司

**❌ 错误做法**：只维护现有机器人公司列表

**✅ 正确做法**：按公司追踪每个维度的信息源

### 追踪维度（每个公司都按这4个维度检查）

| 维度 | 内容 | 信源 |
|------|------|------|
| 产品线 | 人形机器人/具身AI模型 | 产品页/官方文档 |
| 官方博客/新闻 | 公司动态/技术进展 | 博客RSS/新闻页 |
| 年度大会 | 技术大会/发布会 | 大会主页/演讲回放 |
| 开源项目 | 机器人仿真/控制框架 | GitHub仓库 |

### 海外人形整机必检公司

**Tesla Optimus**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | Optimus人形机器人 | tesla.com/optimus |
| 年度大会 | AI Day/ Robot Day | tesla.com/ai |
| 开源 | - | - |

**Figure AI**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | Figure 01/02 | figure.ai |
| 官方博客 | 新闻动态 | figure.ai/news |

**Boston Dynamics**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | Atlas/Spot | bostondynamics.com |
| 官方博客 | 新闻动态 | bostondynamics.com/news |

**1X Technologies**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | NEO、EVE | 1x.tech |

**Agility Robotics**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | Digit | agilityrobotics.com |
| 官方博客 | 新闻动态 | agilityrobotics.com/news |
| 开源 | arcOS | github.com/agilityrobotics/arcOS |

**Sanctuary AI**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | Phoenix | sanctuaryai.com |

### 海外具身AI模型公司

**Physical Intelligence**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | π0 VLA模型 | pi.website |
| 官方博客 | 技术博客 | pi.website/blog |

**World Labs (李飞飞)**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | 世界模型 | worldlabs.ai |

**Covariant**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | RFM-1机器人大脑 | covariant.ai |

### 国内人形整机必检公司

**智元机器人**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | 远征/灵犀系列 | agibot.com |
| 官方博客 | 新闻动态 | agibot.com/news |

**宇树科技**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | G1/H1人形 | unitree.com |

**优必选**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | Walker | ubtrobot.com |

**傅利叶智能**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | GR-1 | fourier.cn |

**星动纪元**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | 小星系列 | xingdongjiyuan.com |

### 大厂机器人必检

**NVIDIA Isaac**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | Isaac机器人平台 | nvidia.com/isaac |
| 开源 | Isaac Sim | github.com/NVIDIA-Omniverse/Isaac-Sim |
| 开源 | Isaac ROS | github.com/NVIDIA-ISAAC/isaac_ros |

**DeepMind Robotics**
| 维度 | 内容 | URL |
|------|------|-----|
| 产品线 | RT系列 | deepmind.google/robotics |

### 发现新公司渠道

| 渠道 | URL | 说明 |
|------|-----|------|
| 融资榜单 | Crunchbase humanoid robot funding | 发现新公司 |
| 行业媒体 | techcrunch.com/category/robotics | 最新动态 |
| 专业媒体 | therobotreport.com | 机器人行业 |
| 36氪 | 36kr.com 机器人/具身智能 | 国内发现 |
| 学术转商业 | robotics.cmu.edu, air.tsinghua.edu.cn | 实验室孵化 |
| GitHub | site:github.com humanoid robot | 开源项目 |
| 社交媒体 | X搜索 "humanoid robot" "Figure 01" "Optimus" | 最新消息 |

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
