---
title: **Translation:**

AGENTS.TXT：Web代理能力声明
draft-car-agents-txt-wellknown-00

**Notes:**
- "AGENTS.TXT" is kept as a technical identifier/specification name
- "draft-car-agents-txt-wellknown-00" is an IETF draft identifier, kept as-is
- "Capability Declarations" translated as "能力声明"
- "Web Agents" translated as "Web代理" (commonly used term in Chinese technical context)
source: datatracker.ietf.org
url: https://datatracker.ietf.org/doc/draft-car-agents-txt-wellknown
date: 2026-06-22
category: standard/datatracker.ietf.org
translated: true
fetched_at: 2026-06-22T20:15:21.639023
---
# **Translation:**

AGENTS.TXT：Web代理能力声明
draft-car-agents-txt-wellknown-00

**Notes:**
- "AGENTS.TXT" is kept as a technical identifier/specification name
- "draft-car-agents-txt-wellknown-00" is an IETF draft identifier, kept as-is
- "Capability Declarations" translated as "能力声明"
- "Web Agents" translated as "Web代理" (commonly used term in Chinese technical context)

**来源**: datatracker.ietf.org | **日期**: 2026-06-22

---


```
Independent Submission                                       K. Cardillo
Internet-Draft                                               Independent
Intended status: Informational                              12 June 2026
Expires: 14 December 2026

           AGENTS.TXT: Capability Declarations for Web Agents
                   draft-car-agents-txt-wellknown-00

Abstract

   This document requests registration of two Well-Known URIs under the
   "/.well-known/" path: "agents.txt" and "agents.json".  These URIs
   define a machine-readable capability declaration format: a positive
   statement of what web agents CAN do on a site -- which endpoints are
   sanctioned for agent use, which protocols (REST, MCP, A2A, GraphQL,
   WebSocket) are supported, what authentication mechanisms are
   expected, and what rate limits the site advertises.

   This is distinct from "robots.txt", which uses a restriction syntax
   to declare what crawlers may not do.  Where "robots.txt" expresses
   prohibition, "agents.txt" expresses capability -- a sanctioned
   channel for agent interaction that is otherwise routinely blocked by
   bot detection, CAPTCHAs, and rate limiters because no positive
   declaration surface exists.

Status of This Memo

   This Internet-Draft is submitted in full conformance with the
   provisions of BCP 78 and BCP 79.

   Internet-Drafts are working documents of the Internet Engineering
   Task Force (IETF).  Note that other groups may also distribute
   working documents as Internet-Drafts.  The list of current Internet-
   Drafts is at https://datatracker.ietf.org/drafts/current/.

   Internet-Drafts are draft documents valid for a maximum of six months
   and may be updated, replaced, or obsoleted by other documents at any
   time.  It is inappropriate to use Internet-Drafts as reference
   material or to cite them other than as "work in progress."

   This Internet-Draft will expire on 14 December 2026.

Copyright Notice

   Copyright (c) 2026 IETF Trust and the persons identified as the
   document authors.  All rights reserved.

Cardillo                Expires 14 December 2026                [Page 1]
Internet-Draft                 agents-txt                      June 2026

   This document is subject to BCP 78 and the IETF Trust's Legal
   Provisions Relating to IETF Documents (https://trustee.ietf.org/
   license-info) in effect on the date of publication of this document.
   Please review these documents carefully, as they describe your rights
   and restrictions with respect to this document.  Code Components
   extracted from this document must include Revised BSD License text as
   described in Section 4.e of the Trust Legal Provisions and are
   provided without warranty as described in the Revised BSD License.

Table of Contents

   1.  Introduction  . . . . . . . . . . . . . . . . . . . . . . . .   3
     1.1.  Relationship to Existing Standards  . . . . . . . . . . .   3
     1.2.  Related Work  . . . . . . . . . . . . . . . . . . . . . .   4
     1.3.  Requirements Language . . . . . . . . . . . . . . . . . .   4
   2.  The "agents.txt" Well-Known URI . . . . . . . . . . . . . . .   5
     2.1.  Location  . . . . . . . . . . . . . . . . . . . . . . . .   5
     2.2.  Format  . . . . . . . . . . . . . . . . . . . . . . . . .   5
     2.3.  Header Fields . . . . . . . . . . . . . . . . . . . . . .   6
     2.4.  Site Fields . . . . . . . . . . . . . . . . . . . . . . .   6
     2.5.  Capability Blocks . . . . . . . . . . . . . . . . . . . .   6
     2.6.  Access Control Fields . . . . . . . . . . . . . . . . . .   7
     2.7.  Agent Policy Blocks . . . . . . . . . . . . . . . . . . .   8
   3.  The "agents.json" Well-Known URI  . . . . . . . . . . . . . .   8
     3.1.  Location  . . . . . . . . . . . . . . . . . . . . . . . .   8
     3.2.  Format  . . . . . . . . . . . . . . . . . . . . . . . . .   8
   4.  Agent Behavior  . . . . . . . . . . . . . . . . . . . . . . .   9
     4.1.  Discovery . . . . . . . . . . . . . . . . . . . . . . . .   9
     4.2.  Identification  . . . . . . . . . . . . . . . . . . . . .  10
     4.3.  Rate Limiting . . . . . . . . . . . . . . . . . . . . . .  10
   5.  Server Behavior . . . . . . . . . . . . . . . . . . . . . . .  10
     5.1.  Caching . . . . . . . . . . . . . . . . . . . . . . . . .  10
     5.2.  CORS  . . . . . . . . . . . . . . . . . . . . . . . . . .  10
     5.3.  Security Considerations . . . . . . . . . . . . . . . . .  10
   6.  IANA Considerations . . . . . . . . . . . . . . . . . . . . .  11
     6.1.  Well-Known URI Registration: "agents.txt" . . . . . . . .  11
     6.2.  Well-Known URI Registration: "agents.json"  . . . . . . .  11
   7.  References  . . . . . . . . . . . . . . . . . . . . . . . . .  11
     7.1.  Normative References  . . . . . . . . . . . . . . . . . .  11
     7.2.  Informative References  . . . . . . . . . . . . . . . . .  12
   Appendix A.  Example: E-Commerce Site . . . . . . . . . . . . . .  12
   Appendix B.  Acknowledgments  . . . . . . . . . . . . . . . . . .  13
   Author's Address  . . . . . . . . . . . . . . . . . . . . . . . .  13

Cardillo                Expires 14 December 2026                [Page 2]
Internet-Draft                 agents-txt                      June 2026

1.  Introduction

   Automated AI agents increasingly interact with websites to perform
   tasks on behalf of users: searching product catalogs, retrieving
   structured data, executing transactions, and calling APIs.  These
   agents are routinely blocked by bot detection systems, CAPTCHAs, and
   rate limiters because no sanctioned channel for agent interaction
   exists.

   Simultaneously, website operators have no standard mechanism to
   declare which agent behaviors they support, which endpoints are
   designed for machine access, or how agents should authenticate.

   "agents.txt" addresses this gap.  It is an opt-in capability
   declaration file, served at a well-known location, that communicates
   to AI agents:

   *  What capabilities are available (search, browse, transact, etc.)

   *  Which protocols are supported (REST, MCP [MCP], A2A, GraphQL,
      WebSocket)

   *  What authentication mechanisms are required (and where to obtain
      tokens)

   *  What rate limits the site declares

   *  Which agents are permitted and under what conditions

1.1.  Relationship to Existing Standards

   "agents.txt" is complementary to, and does not replace, existing
   standards:

   robots.txt:  Declares crawling restrictions. "agents.txt" declares
      what agents are explicitly permitted to do.  Both files may
      coexist.

   llms.txt [LLMSTXT]:  Provides human-readable content for LLMs to
      read. "agents.txt" declares machine-callable endpoints and
      capabilities.

   security.txt [RFC9116]:  Declares security vulnerability disclosure
      contacts. "agents.txt" declares AI agent interaction policies.

   OpenAPI:  Documents individual API endpoints in detail. "agents.txt"
      is a discovery layer; it may reference OpenAPI specifications per
      capability.

Cardillo                Expires 14 December 2026                [Page 3]
Internet-Draft                 agents-txt                      June 2026

   MCP (Model Context Protocol):  A protocol for AI tools. "agents.txt"
      can declare MCP endpoints, making them discoverable without prior
      configuration.

1.2.  Related Work

   The following efforts overlap with or are adjacent to this document.
   None of them provide a site-side capability declaration in the form
   defined here.

   draft-srijal-agents-policy-00 (expired) [SRIJAL-AGENTS-POLICY]:  A
      prior Internet-Draft using the "AGENTS.TXT" name.  Its design is a
      strict policy file with path-based ALLOW/DISALLOW directives
      modeled on "robots.txt".  It expired April 2026 with no -01
      revision.  The present document differs in scope (capability
      declaration, not policy restriction) and structure (typed
      capability and agent blocks with protocol and authentication
      metadata).

   MCP server-card.json [MCP-SERVER-CARD]:  The Model Context Protocol
      defines a "/.well-known/mcp/server-card.json" file describing an
      individual MCP server's tools and resources. "agents.txt" operates
      one layer up: it declares that a site offers capabilities,
      including (optionally) MCP endpoints, and points to the MCP
      server-card for tool-level detail.  The two are complementary.

   A2A agent-card.json [A2A-AGENT-CARD]:  The Agent-to-Agent (A2A)
      protocol defines a "/.well-known/agent-card.json" file describing
      the capabilities of a single agent endpoint. "agents.txt" operates
      at the site level and may reference one or more A2A agent cards
      via Capability blocks with Protocol: A2A.

   llms.txt [LLMSTXT]:  A site-level Markdown file at "/llms.txt" that
      summarizes site content for LLM consumption.  It is a content-
      summary surface, not a capability declaration. "agents.txt" and
      "llms.txt" can coexist on the same site without conflict; they
      answer different questions ("what content is here" vs. "what
      actions are sanctioned").

1.3.  Requirements Language

   The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
   "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
   "OPTIONAL" in this document are to be interpreted as described in BCP
   14 [RFC2119] [RFC8174] when, and only when, they appear in all
   capitals, as shown here.

Cardillo                Expires 14 December 2026                [Page 4]
Internet-Draft                 agents-txt                      June 2026

2.  The "agents.txt" Well-Known URI

2.1.  Location

   The "agents.txt" file MUST be served at:

   https://example.com/.well-known/agents.txt

   Agents SHOULD also check the root path as a fallback:

   https://example.com/agents.txt

   The "/.well-known/agents.txt" path takes precedence when both exist.

   The file MUST be served over HTTPS in production deployments.  HTTP
   is permitted only in development or testing environments.

   The file MUST be served with Content-Type "text/plain; charset=utf-
   8".

2.2.  Format

   The "agents.txt" file uses a block-based key-value format inspired by
   "robots.txt".  Each line contains a key, a colon, and a value.  Lines
   beginning with "#" are comments.  Indented lines (two or more spaces,
   or one or more tabs) belong to the preceding block.

   A minimal "agents.txt" file:

   # agents.txt
   Spec-Version: 1.0
   Site-Name: Example Store
   Site-URL: https://example.com

   Capability: product-search
     Endpoint: https://example.com/api/search
     Method: GET
     Protocol: REST
     Auth: none
     Rate-Limit: 60/minute
     Description: Search the product catalog

   Allow: /api/*
   Disallow: /admin/*

   Agent: *

Cardillo                Expires 14 December 2026                [Page 5]
Internet-Draft                 agents-txt                      June 2026

2.3.  Header Fields

   Spec-Version (REQUIRED):  The specification version.  MUST be "1.0"
      for documents conforming to this specification.

   Generated-At (OPTIONAL):  ISO 8601 timestamp of when the file was
      generated.

   Declaration-Type (OPTIONAL):  One of "platform" or "agent".  Default:
      "platform".  A platform declaration states what agents may do on
      this site (the standard case).  An agent declaration, published by
      an agent operator at the operator's own domain, states what the
      operator's agent does on external platforms.

   Operates-On (OPTIONAL):  URL of a platform this agent operates on.
      MAY appear multiple times.  Expected when Declaration-Type is
      "agent"; not used in platform declarations.

2.4.  Site Fields

   Site-Name (REQUIRED):  Human-readable name of the site or service.

   Site-URL (REQUIRED):  Canonical HTTPS URL of the site.

   Site-Description (OPTIONAL):  Brief description of the site.

   Site-Contact (OPTIONAL):  Contact email address for agent-related
      inquiries.

   Site-Privacy-Policy (OPTIONAL):  URL of the site's privacy policy.

2.5.  Capability Blocks

   A Capability block declares a single action available to agents.
   Capability identifiers MUST consist of lowercase letters, digits, and
   hyphens only.

   Capability (REQUIRED):  Identifier for this capability.

   Endpoint (REQUIRED):  Full HTTPS URL of the endpoint.

   Protocol (REQUIRED):  The interaction protocol.  One of: REST, MCP,
      A2A, GraphQL, WebSocket.

   Method (OPTIONAL):  HTTP method for REST endpoints.  Default: GET.

   Auth (OPTIONAL):  Authentication type.  One of: none, api-key,

Cardillo                Expires 14 December 2026                [Page 6]
Internet-Draft                 agents-txt                      June 2026

      bearer-token, oauth2, hmac.  Default: none.  Servers MUST NOT
      include actual credentials in this field.

   Auth-Endpoint (OPTIONAL):  URL where agents obtain authentication
      tokens.  MUST be present when Auth is "bearer-token" or "oauth2".

   Auth-Docs (OPTIONAL):  URL of human-readable documentation describing
      the authentication flow for this capability.

   Scopes (OPTIONAL):  Comma-separated list of OAuth2 scopes required by
      this capability.

   Rate-Limit (OPTIONAL):  Advisory rate limit in the format "N/window"
      where window is one of: second, minute, hour, day.  Agents SHOULD
      respect declared limits.  Servers MUST enforce limits
      independently.

   Description (OPTIONAL):  Human-readable description of the
      capability.

   OpenAPI (OPTIONAL):  URL to an OpenAPI specification document
      describing the endpoint.

   Param (OPTIONAL):  Declares one parameter of a REST endpoint.  MAY
      appear multiple times within a Capability block.  The value uses
      the form:

   name (location, type[, required]) [- description]

   : where "location" is one of "query", "path", "header", or "body";
   "type" is one of "string", "integer", "number", or "boolean"; the
   literal token "required", when present, marks the parameter as
   required; and the free-text description after "-" is optional.
   Example:

   Param: q (query, string, required) - Search query

   Fields not defined in this document MUST be ignored by parsers, to
   permit forward-compatible extension.

2.6.  Access Control Fields

   Allow (OPTIONAL):  Glob pattern for paths agents may access.
      Semantics follow "robots.txt" conventions.

   Disallow (OPTIONAL):  Glob pattern for paths agents MUST NOT access.

Cardillo                Expires 14 December 2026                [Page 7]
Internet-Draft                 agents-txt                      June 2026

   More specific patterns take precedence over less specific patterns.
   When no access control is declared, only paths referenced by
   capabilities are implicitly permitted.

2.7.  Agent Policy Blocks

   Agent blocks declare per-agent policies.  The wildcard "*" declares
   the default policy for all agents.

   Agent: *

   Agent: claude
     Rate-Limit: 200/minute
     Capabilities: product-search, store-assistant

   Agent identifiers SHOULD match the first token of the agent's User-
   Agent header (case-insensitive).

   Capabilities (OPTIONAL within an Agent block):  Comma-separated list
      of capability identifiers this agent is permitted to use.  If
      omitted, all declared capabilities are permitted.

   Agent-Declaration (OPTIONAL within an Agent block):  URL of the agent
      operator's own "agents.txt" file (a declaration with Declaration-
      Type "agent").  Enables cross-referencing between a platform's
      grant of capabilities and the agent operator's published statement
      of what the agent does and where it operates.

3.  The "agents.json" Well-Known URI

3.1.  Location

   The JSON companion file MUST be served at:

   https://example.com/.well-known/agents.json

   The file MUST be served with Content-Type "application/json;
   charset=utf-8".

3.2.  Format

   The JSON format contains equivalent information to "agents.txt" in a
   typed JSON structure suitable for direct consumption by programmatic
   clients.  The "agents.txt" file MAY reference the JSON file via:

   Agents-JSON: https://example.com/.well-known/agents.json

   A minimal "agents.json" document:

Cardillo                Expires 14 December 2026                [Page 8]
Internet-Draft                 agents-txt                      June 2026

   {
     "specVersion": "1.0",
     "generatedAt": "2026-02-01T00:00:00.000Z",
     "site": {
       "name": "Example Store",
       "url": "https://example.com"
     },
     "capabilities": [
       {
         "id": "product-search",
         "description": "Search the product catalog",
         "endpoint": "https://example.com/api/search",
         "method": "GET",
         "protocol": "REST",
         "auth": { "type": "none" },
         "rateLimit": { "requests": 60, "window": "minute" }
       }
     ],
     "access": {
       "allow": ["/api/*"],
       "disallow": ["/admin/*"]
     },
     "agents": {
       "*": {}
     }
   }

   Field semantics are identical to those defined in Section 2 for the
   text format.

4.  Agent Behavior

4.1.  Discovery

   Agents SHOULD fetch "/.well-known/agents.txt" and/or "/.well-known/
   agents.json" before interacting with an unfamiliar site.

   Agents SHOULD prefer the JSON format when both are available, as it
   is more precisely typed and unambiguous.

   Agents SHOULD cache the capability declaration for the duration
   declared by the HTTP Cache-Control header.  Implementations SHOULD
   use a minimum cache TTL of 60 seconds to reduce server load.

Cardillo                Expires 14 December 2026                [Page 9]
Internet-Draft                 agents-txt                      June 2026

4.2.  Identification

   Agents SHOULD identify themselves via the User-Agent HTTP header when
   calling capability endpoints.  The agent name in the User-Agent
   header is matched (case-insensitively) against Agent blocks to apply
   per-agent policies.

4.3.  Rate Limiting

   Agents SHOULD respect Rate-Limit declarations as advisory limits.
   Servers MUST enforce rate limits independently and MUST NOT rely on
   agents to self-enforce.

5.  Server Behavior

5.1.  Caching

   Servers SHOULD serve "agents.txt" and "agents.json" with appropriate
   Cache-Control headers.  A max-age of 300 seconds (5 minutes) is
   RECOMMENDED for most deployments.

5.2.  CORS

   Servers SHOULD include the following headers to permit cross-origin
   discovery:

   Access-Control-Allow-Origin: *
   Access-Control-Allow-Methods: GET, OPTIONS

5.3.  Security Considerations

   Capability declarations MUST NOT include actual credentials, API
   keys, tokens, or secrets of any kind.  The Auth and Auth-Endpoint
   fields describe mechanisms only.

   Servers MUST enforce all declared restrictions (rate limits, access
   control, agent policies) independently of the declarations in
   "agents.txt".  The file is advisory to agents; it is not a trust
   boundary.

   Agents MUST validate that capability endpoints use HTTPS before
   sending authentication credentials.

   Site owners SHOULD review their capability declarations periodically
   to ensure they accurately reflect current server capabilities and
   access policies.

Cardillo                Expires 14 December 2026               [Page 10]
Internet-Draft                 agents-txt                      June 2026

6.  IANA Considerations

6.1.  Well-Known URI Registration: "agents.txt"

   This document requests registration of the following Well-Known URI
   in the "Well-Known URIs" registry established by [RFC8615]:

   URI suffix:  agents.txt

   Change controller:  Kayla Cardillo

   Specification document(s):  This document.

   Related information:  Text-format capability declaration file for AI
      agent discovery.

6.2.  Well-Known URI Registration: "agents.json"

   URI suffix:  agents.json

   Change controller:  Kayla Cardillo

   Specification document(s):  This document.

   Related information:  JSON-format capability declaration file for AI
      agent discovery.  Companion format to agents.txt.

7.  References

7.1.  Normative References

   [RFC2119]  Bradner, S., "Key words for use in RFCs to Indicate
              Requirement Levels", BCP 14, RFC 2119,
              DOI 10.17487/RFC2119, March 1997,
              <https://www.rfc-editor.org/rfc/rfc2119>.

   [RFC8174]  Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC
              2119 Key Words", BCP 14, RFC 8174, DOI 10.17487/RFC8174,
              May 2017, <https://www.rfc-editor.org/rfc/rfc8174>.

   [RFC8615]  Nottingham, M., "Well-Known Uniform Resource Identifiers
              (URIs)", RFC 8615, DOI 10.17487/RFC8615, May 2019,
              <https://www.rfc-editor.org/rfc/rfc8615>.

   [RFC9110]  Fielding, R., Ed., Nottingham, M., Ed., and J. Reschke,
              Ed., "HTTP Semantics", STD 97, RFC 9110,
              DOI 10.17487/RFC9110, June 2022,
              <https://www.rfc-editor.org/rfc/rfc9110>.

Cardillo                Expires 14 December 2026               [Page 11]
Internet-Draft                 agents-txt                      June 2026

7.2.  Informative References

   [A2A-AGENT-CARD]
              "A2A Agent Card", 2025, <https://a2aproject.github.io/>.

   [LLMSTXT]  "llms.txt", 2024, <https://llmstxt.org>.

   [MCP]      "Model Context Protocol", 2025,
              <https://modelcontextprotocol.io/specification>.

   [MCP-SERVER-CARD]
              "Model Context Protocol Server Card", 2024,
              <https://modelcontextprotocol.io>.

   [RFC9116]  Foudil, E. and Y. Shafranovich, "A File Format to Aid in
              Security Vulnerability Disclosure", April 2022.

   [ROBOTS]   "Robots Exclusion Protocol", September 2022,
              <https://www.rfc-editor.org/rfc/rfc9309>.

   [SRIJAL-AGENTS-POLICY]
              "AGENTS.TXT: Strict Policy File for Automated Clients",
              Work in Progress, Internet-Draft, draft-srijal-agents-
              policy-00 (expired), 2025,
              <https://datatracker.ietf.org/doc/draft-srijal-agents-
              policy/>.

Appendix A.  Example: E-Commerce Site

Cardillo                Expires 14 December 2026               [Page 12]
Internet-Draft                 agents-txt                      June 2026

   # agents.txt
   Spec-Version: 1.0
   Generated-At: 2026-02-01T00:00:00Z
   Site-Name: Outdoor Supply Co.
   Site-URL: https://outdoorsupply.example
   Site-Description: Gear for outdoor adventures
   Site-Contact: agents@outdoorsupply.example

   Capability: product-search
     Endpoint: https://outdoorsupply.example/api/search
     Method: GET
     Protocol: REST
     Auth: none
     Rate-Limit: 60/minute
     Description: Search the product catalog
     Param: q (query, string, required) - Search query
     Param: limit (query, integer) - Max results, default 20
     Param: category (query, string) - Filter by category

   Capability: store-assistant
     Endpoint: https://outdoorsupply.example/mcp
     Protocol: MCP
     Auth: bearer-token
     Auth-Endpoint: https://outdoorsupply.example/auth/token
     Description: Full store interaction via MCP

   Allow: /api/*
   Allow: /mcp
   Disallow: /admin/*
   Disallow: /internal/*

   Agent: *
   Agent: claude
     Rate-Limit: 200/minute
     Capabilities: product-search, store-assistant

Appendix B.  Acknowledgments

   The "agents.txt" format draws on the design of "robots.txt" [ROBOTS],
   "security.txt" [RFC9116], and OpenAPI for structural inspiration.
   The MCP protocol reference is to the Model Context Protocol
   specification.

Author's Address

   Kayla Cardillo
   Independent
   Email: contactkaylacard@gmail.com

Cardillo                Expires 14 December 2026               [Page 13]

```

Status
Email expansions
History

00

Document
Type
Active Internet-Draft
(individual)
Author
Kayla Cardillo
Last updated
2026-06-12
RFC stream
(None)
Intended RFC status
(None)
Formats
txt
html
xml
htmlized
bibtex
bibxml
Stream
Stream state
(No stream defined)
Consensus boilerplate
Unknown
RFC Editor Note
(None)
IESG
IESG state
I-D Exists
Telechat date
(None)
Responsible AD
(None)
Send notices to
(None)


*原文请访问 [datatracker.ietf.org](https://datatracker.ietf.org/doc/draft-car-agents-txt-wellknown)*