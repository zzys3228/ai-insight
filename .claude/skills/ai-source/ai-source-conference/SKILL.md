---
name: ai-source-conference
description: 管理综合性/行业性AI技术大会信息源，只做源发现不做内容追踪。追踪WAIC/开发者开源峰会/AI合规安全峰会等中立大会。Use when user mentions /ai-source-conference, or asks to check AI conferences, summits, events, AI summits.
---

> **状态**：✅ 已更新（2026-06-21）

# AI Source Conference Skill

## Quick Start

- `/ai-source-conference [大会名]` — 查看指定大会信息
- `/ai-source-conference --upcoming` — 查看近期大会
- `/ai-source-conference --check` — 检查URL有效性

## URL规则 ⚠️ 重要

### URL类型规则

| 优先级 | URL类型 | 示例 | 说明 |
|--------|---------|------|------|
| ✅首选 | 大会官网 | worldaic.com.cn | WAIC官方 |
| ✅次选 | 官方议程 | io.google | Google I/O |
| ✅可选 | 协会主页 | ciis.caai.cn | 学会主页 |

### URL验证要点 ⚠️ 必须

```
❌ 错误：直接使用跳转前的URL
- theaisummit.com/london → 301跳转

✅ 正确：用 curl -L 检查最终跳转URL
- theaisummit.com/london → london.theaisummit.com/ai-summit-event-series
```

**验证命令：**
```bash
curl -sI --max-time 10 -L {URL}  # 跟随跳转，检查Location头
```

**已知跳转：**
- AI Summit London: theaisummit.com/london → london.theaisummit.com
- AI Summit NYC: theaisummit.com/new-york → newyork.theaisummit.com

## 输出格式 ⚠️ 重要

### 编号规则

```
❌ 错误：全局连续编号
✅ 正确：分章节独立编号（第二章无编号）
```

### 输出模板

```markdown
## 二、中立技术大会

### 2.1 AI产业生态峰会

| 源名 | URL | 推荐理由 | 状态 | 代理 | 用途 |
|------|-----|---------|------|------|------|
| WAIC 世界AI大会 | https://worldaic.com.cn | 中国最大AI大会 | ✅ | 否 | daily |
```

### 状态标记

| 标记 | 含义 |
|------|------|
| ✅ | 可直接访问 |
| ✅302→ | 跳转后可达 |
| ⚠️403 | 需代理 |

## Workflows

### 阶段一：URL有效性检查
```bash
curl -x http://127.0.0.1:26001 -sI --max-time 15 {URL}
```

### 阶段二：分类检索

**❌ 错误做法**：随意搜索，不区分质量

**✅ 正确做法**：先检定国内大会清单，再扩展国际大会

```
# 必检清单（国内高质量大会）：
1. QCon全球软件开发大会 → https://qcon.infoq.cn
2. AICon全球人工智能大会 → https://aicon.infoq.cn
3. ML-Summit 奇点智能大会 → https://milvintech.com
4. ModelScope开发者大会 → https://modelscope.cn
5. WAIC世界AI大会 → https://worldaic.com.cn
6. GOSIM开源创新大会 → https://gosim-lang.org

# 扩展检索关键词（国际）：
- AI Summit London/New York
- AI Engineer Summit
- AI Summit San Francisco
```

### 阶段三：筛选规则核验
校验主办方和议程内容

### 阶段四：结构化输出
```
## Conference 大会检查结果

### 年度大会日历
| 月份 | 大会 | 分类 | 重要性 | 状态 |
|------|------|------|--------|------|
| 7月 | WAIC | 产业峰会 | ⭐⭐⭐ | ✅ |

### 建议新增大会
| 大会 | URL | 分类 | 时间 | 主办方 |

### 移除建议
| 大会 | 原因 |
|------|------|
| XXX | 停办/变质 |
```

## 分类体系（5类）

| 分类 | 核心价值 | 典型大会 |
|------|----------|----------|
| AI产业生态峰会 | 产业政策、投融资、全链路商业化 | WAIC世界AI大会 |
| 综合软件技术峰会 | 大模型/AI原生研发/Agent工程/LLMOps全链路 | QCon全球软件开发大会 |
| AI工程落地峰会 | ML工程、私有化推理、AI应用全链路实践 | AICon全球人工智能大会 |
| 行业垂直AI峰会 | 细分行业数字化、行业大模型落地 | 工业AI、金融AI、医疗AI |
| AI开发者开源峰会 | 开源模型/推理框架、本地部署实践 | GOSIM、ModelScope开发者大会 |

## 国内高质量大会清单（必检）

| 大会 | URL | 定位 | 主办方 |
|------|-----|------|--------|
| QCon全球软件开发大会 | https://qcon.infoq.cn | 国内第一综合技术峰会，AI重塑软件研发体系 | InfoQ |
| AICon全球人工智能大会 | https://aicon.infoq.cn | QCon姊妹场，纯AI工程落地 | InfoQ |
| ML-Summit 奇点智能技术大会 | https://milvintech.com | 聚焦Agent工程、AI软件基础设施、AIGC研发工具 | CSDN |
| ModelScope魔搭开发者大会 | https://modelscope.cn | 国内最大开源模型社区，模型开发/微调/部署工具链 | 阿里 |
| WAIC 世界AI大会 | https://worldaic.com.cn | 中国最大AI大会 | 政府+多方 |
| GOSIM开源创新大会 | https://gosim-lang.org | 开源模型/推理框架实践 | GOSIM |

## 强制排除

| 排除类型 | 说明 |
|---------|------|
| 单一大厂主办 | Google I/O、微软 Build、百度世界 |
| 纯学术论文顶会 | NeurIPS、ICLR、CVPR、ICML |
| 机器人专项展会 | Robot skill追踪 |

## 准入标准

| 标准 | 要求 |
|------|------|
| 主办方 | 政府、协会、中立第三方，无头部企业独家冠名 |
| 内容主线 | 产业落地、投融资，开源实操，不以产品宣讲为主 |
| 时效 | 每年稳定举办，近2年有完整公开议程 |

## 发现方法：如何发现新的技术大会

**❌ 错误做法**：只维护已知大会列表

**✅ 正确做法**：定期扫描以下渠道

```
# 方法一：国内必检清单（每次必查）
- QCon全球软件开发大会 → qcon.infoq.cn
- AICon全球人工智能大会 → aicon.infoq.cn
- ML-Summit 奇点智能大会 → milvintech.com
- ModelScope开发者大会 → modelscope.cn
- WAIC世界AI大会 → worldaic.com.cn
- GOSIM开源创新大会 → gosim-lang.org

# 方法二：InfoQ大会追踪
- infoq.cn/conferences → 所有InfoQ主办大会
- infoq.cn/qcon → QCon专题页
- 搜索 "site:infoq.cn AI大会" 或 "site:infoq.cn 开发者大会"

# 方法三：CSDN大会追踪
- csdn.net/summit → CSDN主办大会
- 搜索 "site:csdn.net 机器学习大会"

# 方法四：国际大会发现
- The AI Summit → theaisummit.com （伦敦/纽约）
- AI Engineer Summit → ai.engineering
- AI World Conference → aiworld.com
- ODSC (Open Data Science) → odsc.com

# 方法五：学术顶会转产业
- NeurIPS/ICML除了学术，也有人才/产业论坛
- CVPR Workshop → 工业界分享

# 方法六：行业协会
- 中国人工智能学会 → caai.cn
- 中国信通院 → caict.ac.cn
- IEEE/ACM → 会议列表

# 方法七：GitHub/社交媒体
- GitHub Trending上的会议公告
- X/Twitter搜索 "conference CFP" "call for papers AI"
```

## 源列表文件

`D:\aicoding\startup\ppt-test\ai-news-sources.md`

详细查找方法 → See [REFERENCE.md](REFERENCE.md)
