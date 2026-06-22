# AI Source Standard Reference

## 协议制定组织

| 组织 | URL | 能找到什么 |
|------|-----|-----------|
| AAIF | agentic.ai | MCP/A2A/AGENTS.md托管 |
| W3C | w3.org/groups/wg/agents | WebAgents/A2WF等工作组 |
| NIST CAISI | nist.gov/caisi | AI标准/框架/风险管控 |
| OWASP | genai.owasp.org | Agent安全标准 |
| IEEE | standards.ieee.org | AI标准系列 |
| ISO/IEC SC42 | iso.org/committee/6794475 | AI国际标准 |
| IETF | ietf.org | Agent相关RFC草案 |
| OpenTelemetry | opentelemetry.io | LLM/Agent可观测标准 |

## 正式标准

| 协议 | URL | 说明 |
|------|-----|------|
| ISO/IEC 42001 AIMS | iso.org/standard/81506 | AI管理体系认证 |
| ISO/IEC 22989 | iso.org/standard/81505 | AI术语定义 |
| IEEE P7007 | standards.ieee.org | 自主智能体安全规范 |
| W3C DID | w3.org/TR/did-core | W3C推荐标准 |
| NIST AI RMF 1.0 | nist.gov/ai-rmf | NIST正式发布 |

## 行业事实协议

| 协议 | URL | 说明 |
|------|-----|------|
| MCP | modelcontextprotocol.io | Agent连接工具/文件（Linux Foundation） |
| A2A | a2a-protocol.org | Agent↔Agent协作（150+组织） |
| AGENTS.md | agentics.org | 网站向Agent声明规则 |
| MCP Servers Awesome | github.com/punkpeye/awesome-mcp-servers | MCP服务器生态列表 |
| OWASP Agentic Top10 | genai.owasp.org | Agent安全Top10风险 |
| OpenTelemetry GenAI | opentelemetry.io/docs/specs/semconv/gen-ai | LLM全链路追踪 |
| OpenAI Compatible API | platform.openai.com | LLM推理统一接口 |
| OpenAI Function Calling | platform.openai.com/docs/guides/function-calling | LLM工具调用 |
| Anthropic Messages API | docs.anthropic.com/en/api/messages | Claude多模态规范 |
| GGUF/GGML | github.com/ggml-org/ggml | 本地大模型格式 |
| AG-UI | docs.ag-ui.com | Agent↔用户前端交互 |

## MCP生态（新兴热门）

| 项目 | URL | Stars | 说明 |
|------|-----|-------|------|
| headroom | github.com/useheadroom/headroom | 3.7k+ | LLM输入压缩60-95%，支持MCP |
| codebase-memory-mcp | github.com/GreptimeTeam/codebase-memory-mcp | 1.2k+ | 高性能代码MCP服务器，158语言 |
| kilocode | github.com/kilocodeai/kilocode | 500+ | Agentic工程平台 |
| OpenMontage | github.com/Tiklabs/OpenMontage | 600+ | Agentic视频制作系统 |
| flue | github.com/astroslabsai/flue | 300+ | 沙盒Agent框架 |

## 实验/新兴协议

| 协议 | URL | 类型 |
|------|-----|------|
| A2WF | a2wf.github.io/spec | W3C CG draft v1.1 |
| AGENTS.TXT | datatracker.ietf.org/doc/draft-car-agents-txt-wellknown | IETF draft |
| DNS-AID | dns-aid.org | IETF draft |
| WebMCP | developer.chrome.com/docs/ai/webmcp | Chrome origin trial |
| ANP | w3c-cg.github.io/ai-agent-protocol | W3C CG |
| AITP | aitp.dev | 0.x版本 |
| AGNTCY | linuxfoundation.org/projects/agntcy | Agent目录发现 |

## 检索关键词

```
国际标准: ISO SC42 AI standard, W3C WebAgents protocol, IEEE P7007
厂商协议: MCP Claude Messages API, A2A WebMCP AP2
MCP生态: awesome-mcp-servers, headroom LLM compression
Awesome清单: awesome-ai-agent-protocol, awesome-mcp-servers
学术: arXiv agent protocol, agent communication
```

## 清洗规则

| 类型 | 处理 |
|------|------|
| IETF draft | ≠ 正式标准（未RFC） |
| Goose | 是agent框架，不是协议 |
| 局部私有规范 | 单一产品内部规则，剔除 |
