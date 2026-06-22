---
title: The universal.discovery layer for AI agents.
source: dns-aid.org
url: https://dns-aid.org
date: 2026-06-22
category: standard/dns-aid.org
translated: true
fetched_at: 2026-06-22T18:27:22.201567
---
# The universal.discovery layer for AI agents.

**来源**: dns-aid.org | **日期**: 2026-06-22

---

IETF Draft · Open Source

The universal

.

discovery layer for AI agents.

Publish agents to DNS, discover them like websites, and verify trust with DNSSEC. No centralized registry, just signal.

Get started

Read IETF draft

Install the full SDK in one shot:

pip

docker

source

pip install "dns-aid[all]"

Copy

docker compose -f tests/integration/bind/docker-compose.yml up -d

Copy

git clone https://github.com/infobloxopen/dns-aid-core.git

Copy

Core capabilities

What DNS-AID gives you, built on the DNS-AID protocol.

Core principle

Zero new infrastructure.

Built on DNS you already run.

DNS-AID is a naming convention on top of existing SVCB, TXT, and TLSA records. No new record types, no new servers, no new protocols — just standards from RFC 9460 and RFC 4033.

Spec

RFC 9460

Security

DNSSEC

Status

IETF draft

Security

DNSSEC trust chain

Cryptographic proof that agent records are authentic and untampered.

Protocols

Protocol agnostic

MCP, A2A, HTTPS, and any future protocol via

alpn

.

Discovery

Three discovery modes

Lookup by name, search by capability, or crawl a domain index.

Enterprise

Split-horizon DNS

Different agents to internal vs. external. Built-in tenant isolation.

SDK

Open-source toolkit

CLI, Python SDK, MCP server. Eight backends ship in the box.

Performance

Cacheable & decentralized

DNS caches automatically. No central API. Distributed lookups.

The DNS-AID namespace

A deterministic, human-readable naming pattern for agent records.

DNS-AID Naming Pattern

_<agent-name>

.

_<protocol>

._agents.<your-domain>

Examples:

_chatbot

.

_mcp

._agents.example.com

MCP chatbot

_search

.

_a2a

._agents.example.com

A2A search agent

_data-cleaner

.

_a2a

._agents.acme.com

capability-based

_index._agents.example.com

full agent index

Multi-tenant:

_analytics

.

_mcp

._agents.customer1.saas.com

Anatomy of an agent record

Each agent is an SVCB record packed with machine-readable metadata.

_my-agent._mcp._agents.example.com.

3600 IN SVCB 1 agent.example.com. (

alpn

=

"mcp"

; protocol

port

=443

; service port

cap

=

"https://example.com/cap.json"

; capability doc

cap-sha256

=

"abc123..."

; integrity hash

bap

=

"mcp=1.0,a2a=0.2"

; protocol versions

policy

=

"https://example.com/policy"

; governance URL

realm

=

"production"

; tenant scope

ipv4hint

=192.0.2.1

; address hint

)

alpn

Communication protocol (mcp, a2a, h2)

port

Service port number

cap

Capability document URI

cap-sha256

Integrity hash for tamper detection

bap

Bulk protocol version declarations

policy

Governance and usage policy URL

realm

Tenant or environment scope

ipv4hint

Address hint to reduce extra lookups

How it works

Four steps from publish to connect.

1

Publish your agent

Use the CLI or SDK to create an SVCB record under your domain's _agents zone with endpoint, protocol, and capabilities.

2

DNSSEC signs the zone

Your authoritative DNS signs the records, creating a cryptographic chain of trust from root to your agent.

3

Agents discover yours

Remote agents query DNS for your SVCB record by name, capability type, or full domain index.

4

Validate & connect

The discoverer validates DNSSEC + DANE, then connects directly via the protocol in your SVCB record.

Quickstart

Get up and running with the dns-aid-core Python package.

CLI

Python

MCP Server

Docker

Install

pip install

"dns-aid[all]"

# everything

pip install

"dns-aid[cli]"

# CLI only

pip install

"dns-aid[route53]"

# AWS backend

pip install

"dns-aid[cloudflare]"

# Cloudflare backend

pip install

"dns-aid[nios]"

# Infoblox NIOS backend

pip install

"dns-aid[mcp]"

# MCP server

Publish

dns-aid publish \
  --name

my-chatbot

\
  --domain

example.com

\
  --protocol

mcp

\
  --endpoint

agent.example.com

\
  --capability

chat

Discover

dns-aid discover

example.com

dns-aid discover

example.com

--json
dns-aid discover

example.com

--use-http-index

Verify & Diagnose

dns-aid verify

_my-chatbot._mcp._agents.example.com

dns-aid doctor --domain

example.com

Invoke agents

# List tools on an MCP agent

dns-aid list-tools

https://mcp.example.com/mcp

# Call a specific tool

dns-aid call

https://mcp.example.com/mcp

analyze_security

\
  --arguments

'{"domain":"example.com"}'

# Send a message to an A2A agent (discover-first)

dns-aid message

"What is DNS-AID?"

\
  -d

ai.infoblox.com

-n

security-analyzer

Manage

# Delete an agent from DNS

dns-aid delete -n

my-chatbot

-d

example.com

-p

mcp

Publish

from

dns_aid

import

publish

result =

await

publish(
    name=

"my-chatbot"

,
    domain=

"example.com"

,
    protocol=

"mcp"

,
    endpoint=

"agent.example.com"

,
    capabilities=[

"chat"

,

"summarize"

],
    description=

"General-purpose chat agent"

,
)
print(f

"Published: {result.agent.fqdn}"

)
print(f

"Records:   {result.records_created}"

)

Discover

import

asyncio

from

dns_aid

import

discover, verify

async def

main

():
    result =

await

discover(

"example.com"

)

for

agent

in

result.agents:
        print(f

"  {agent.name} — {agent.protocol} @ {agent.endpoint_url}"

)

    check =

await

verify(

"_my-agent._mcp._agents.example.com"

)
    print(f

"DNSSEC valid: {check.dnssec_valid}"

)

asyncio.run(main())

Discover-then-Invoke

from

dns_aid

import

discover, invoke

async def

find_and_call

():
    result =

await

discover(

"partner.com"

, protocol=

"mcp"

)
    agent = result.agents[

0

]
    resp =

await

invoke(agent, method=

"tools/list"

)
    print(f

"Latency: {resp.signal.invocation_latency_ms}ms"

)
    print(f

"Data:    {resp.data}"

)

Run the MCP Server

# stdio transport (Claude Desktop)

dns-aid-mcp --transport stdio

# HTTP transport

dns-aid-mcp --transport http --port

8000

Tool

Description

publish_agent_to_dns

Publish an agent's endpoint and capabilities

discover_agents_via_dns

Find agents on any domain via DNS

verify_agent_dns

Verify DNSSEC, DANE, and endpoint for an agent

call_agent_tool

Invoke a tool on a discovered MCP agent

list_agent_tools

List available tools on a remote MCP agent

send_a2a_message

Message a discovered A2A agent

diagnose_environment

Check DNS-AID configuration and connectivity

delete_agent_from_dns

Remove an agent's DNS records

list_published_agents

List agents in your own DNS zone

list_agent_index

Read a domain's agent index record

sync_agent_index

Rebuild a domain's agent index from live records

Local Playground — zero credentials needed

git clone https://github.com/infobloxopen/dns-aid-core.git
cd dns-aid-core
pip install

"dns-aid[cli]"

docker compose -f tests/integration/bind/docker-compose.yml up -d

# Configure .env for local BIND9 (see .env.example)

dns-aid publish --name

test-agent

--domain

test.dns-aid.local

\
  --protocol

mcp

--endpoint

localhost

--backend

ddns

\
  --capability

chat

dns-aid discover

test.dns-aid.local

Three ways to discover agents

All via standard DNS queries. No special client needed.

Targeted

Lookup by name

You know the agent. Query its SVCB record directly for endpoint details.

dig SVCB _chatbot._mcp._agents.example.com

Capability

Search by function

Find agents by what they do. Query a capability type under the agent zone.

dig SVCB _data-cleaner._a2a._agents.example.com

Index

Crawl the catalog

Fetch a domain's full agent inventory from a well-known index entry point.

dig TXT _index._agents.example.com

Architecture

Cross-organization agent discovery flow.

ORG 1 (Discovering)

ORG 2 (Publishing)

+----------------+                                    +-------------------+
  |   AI Agent     |---- 1. DNS SVCB Query ----------->|   Authoritative   |
  |   (org1)       |     _search._a2a._agents.org2.com |   DNS Server      |
  |                |<--- 2. SVCB Response -------------|   (DNSSEC-signed) |
  +-------+--------+     alpn="a2a" port=443           +-------------------+
          |               ipv4hint=198.51.100.10
          |
          |   3. DNSSEC + DANE Validation
          |
          |   4. Direct A2A / MCP / HTTPS Connection
          v
  +----------------+
  |   AI Agent     |   Running at 198.51.100.10:443
  |   (org2)       |
  +----------------+

R53

Amazon Route 53

AWS hosted zones

CF

Cloudflare

Global edge DNS

IB

Infoblox NIOS

Enterprise DDI

UD

Infoblox UDDI

Universal DDI cloud

AZ

Azure DNS

Microsoft cloud

GC

Google Cloud DNS

GCP managed

NS1

NS1

Managed DNS & traffic steering

RFC

RFC 2136 DDNS

Any standards-compliant DNS

B9

BIND9

Self-hosted & local dev

Policy enforcement

Discovery gets agents to the right endpoint. Policy helps deployments express who may call, what auth is required, and which runtime checks to apply without turning the homepage into a protocol memo.

Current

Runtime policy today

The DNS-AID learning materials already describe runtime policy evaluation alongside discovery metadata, auth requirements, and deployment-specific policy bundles such as

policy.json

.

Layers

Caller, target, and infrastructure

Teams can start with caller-side and target-side checks, then add resolver or proxy enforcement only if their DNS or traffic infrastructure supports it.

Extensions

Local inspection patterns

Some deployments may add local request or response inspection for PII, prompt injection, or data handling checks without routing traffic through a central policy service.

What gets enforced

Documented policy examples on this site include caller-domain restrictions, required auth types, availability windows, rate limits, DNSSEC-sensitive decisions, and CEL expressions for tighter runtime checks.

Why it matters

You can start with the current runtime policy model and extend into resolver or proxy enforcement later, instead of committing to a heavyweight centralized security architecture on day one.

Open policy guide

Continue with the interactive course

Use cases

Real-world agent discovery scenarios.

Enterprise

Cross-org agent collaboration

An internal agent queries DNS to discover a partner's authorized agents, validates delegation, and initiates a secure session automatically.

Academic

Research consortiums

Universities publish agents under their own domains. Collaborators discover services by capability while respecting institutional trust boundaries.

SaaS

Multi-tenant platforms

SaaS providers host agents under tenant-specific zones. DNS zone delegation provides natural isolation and scoped discovery per customer.

Edge

IoT and edge agents

Lightweight agents on constrained devices benefit from DNS's distributed, cacheable architecture with SVCB hints for low-latency bootstrapping.

Security & trust

Built on the internet's battle-tested security infrastructure.

DNSSEC

Mandatory for public zones. Cryptographic chain of trust prevents spoofing and tampering.

DANE / TLSA

Binds TLS certificates to DNS records. Endpoint verification without certificate authority trust issues.

Domain Control Validation

Agents prove authorization via DCV TXT records. Scoped, verifiable, and ideal for ephemeral agents.

Capability Integrity

cap-sha256 hash ensures capability documents haven't been tampered with.

Split-Horizon DNS

Internal agents stay invisible externally. Different views for different resolver contexts.

Scoped Authorization

TXT records define per-agent roles and permissions scoped to specific services and operations.

FAQ

Does DNS-AID require changes to my DNS servers?

No. DNS-AID introduces no new DNS record types, opcodes, or message formats. It's a naming convention on top of existing SVCB, TXT, and TLSA records. Any DNS server supporting DNSSEC and SVCB will work.

What agent communication protocols does it support?

DNS-AID is protocol-agnostic. Agents declare protocols in the SVCB alpn field. The SDK supports MCP, A2A, and HTTPS. New protocols work by using new alpn identifiers.

How is this different from a centralized agent registry?

DNS-AID is decentralized. Each organization publishes records under its own domain. No central registry, no vendor lock-in, no single point of failure.

What DNS providers are supported?

AWS Route 53, Cloudflare, Infoblox NIOS, and RFC 2136. A Docker BIND9 playground is included for local dev. The backend architecture is extensible.

Is DNSSEC required?

For public agent zones, yes. Without DNSSEC, discovering agents can't verify records are authentic. For private zones, network-level controls may suffice.

What if my DNS provider doesn't support custom SVCB parameters?

The SDK handles this automatically. Custom parameters are gracefully demoted to TXT records with dnsaid_ prefixes. All metadata is preserved losslessly.

Can I try it without a cloud account?

Yes. The repo includes a Docker Compose setup with a local BIND9 server at tests/integration/bind/. Run

docker compose -f tests/integration/bind/docker-compose.yml up -d

and experiment entirely on your local machine using the DDNS backend.

Start discovering agents.

Install the SDK, publish your first agent, and build on the open universal discovery layer for AI.

View on GitHub

Read the IETF Draft

*原文请访问 [dns-aid.org](https://dns-aid.org)*