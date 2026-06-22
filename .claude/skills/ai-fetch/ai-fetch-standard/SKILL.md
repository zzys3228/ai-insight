# AI Fetch Standard Skill

## Description
Fetch AI protocol specifications and standards documentation. Covers MCP, A2A, AGENTS.md, and other AI protocols.

## Usage
```
/ai-fetch-standard           # Fetch all standards
/ai-fetch-standard --mcp  # Fetch MCP specification
/ai-fetch-standard --a2a  # Fetch A2A protocol
```

## Supported Standards
| Standard | URL | Content |
|---------|-----|---------|
| MCP | modelcontextprotocol.io | Model Context Protocol |
| A2A | a2a-protocol.org | Agent-to-Agent Protocol |
| AGENTS.md | agentics.org | Agent capability declarations |
| OpenAI Function Calling | platform.openai.com | Function calling spec |
| Anthropic Messages API | docs.anthropic.com | Claude API spec |

## Output
Files saved to: `ai-content-fetched/standard/{protocol}/{doc_slug}.md`
- Complete specification documents
- Technical details preserved
- Translated to Chinese

## Technical
- Documentation page scraping
- Multi-page traversal
- Code examples preserved in original format
