---
title: AI agents need verifiable identity.
source: ansinfo.ai
url: https://ansinfo.ai
date: 2026-06-22
category: standard/ansinfo.ai
translated: true
fetched_at: 2026-06-22T18:27:26.754381
---
# AI agents need verifiable identity.

**来源**: ansinfo.ai | **日期**: 2026-06-22

---

ANS | Trust Layer for AI Agents

AI agents need verifiable identity.

As AI agents begin to act across websites, apps, and business systems, every interaction needs a simple way to confirm which agents are legitimate and who operates it. ANS is an open standard that assigns agents identity through domain names and DNS.

Support the standard

See how ANS works

Soon, agents will act on your behalf.

Your agent books a barber before your next haircut. A finance agent pays an approved supplier. A procurement agent compares vendors. A customer support agent resolves an issue with another company's agent.

This is where AI is headed: agents moving across services, systems, and organizations to get work done.

🧑

▲

"Book me a haircut for Thursday."

You

tell your AI assistant / agent

← Back

Next →

▶ Play

🧑

You

🤖

AI Assistant / Agent

🏅

ANS Registry

📅

Calendar Agent

✅

Done

The internet was not built to recognize agents.

Identities are foundational to how the web works. Websites have domains. People have accounts and profiles. Businesses have verified digital properties. Without clear identities, it's hard to verify who or what you're interacting with.

And right now, agents have nothing standard. As more come online, there is no shared way to identify them across websites, apps, or platforms.

Without a standard, every agent interaction needs to ask the same questions, each time: Is this agent what it claims to be? How should it be handled?

✓

🌐

Website

Domain name

DNS + TLS certificate

✓

👤

Person

Account / profile

OAuth, OpenID Connect

✓

🏢

Business

Verified property

Google Business, EV cert

?

🤖

Agent

No standard

Nothing shared yet

Every actor on the web has an identity standard.

Agents do not — yet.

ANS gives agents a standard way to identify themselves.

ANS is an open standard that connects an AI agent to a domain name, creating a recognizable and verifiable identity that can be discovered through DNS.

That means an agent can show who or what it represents, where its identity is anchored, and how other agents, platforms, and systems should interact with it.

Instead of every company inventing its own way to identify agents, ANS gives the ecosystem a shared starting point.

Ecosystem fit

ANS complements — it doesn't compete

Discovery and trust are different problems. ANS is the trust layer that works with any discovery mechanism.

Standards Convergence in Progress

Infoblox (DNS-AID), GoDaddy (ANS), and Nemethi (AID) are actively collaborating on a shared DNS profile under the

_ag

label. This is the first concrete evidence that the fragmented landscape is consolidating rather than continuing to diverge. The convergence on shared SVCB records — one record per protocol, carrying discovery metadata for all participating drafts — provides a strong trust signal for anyone evaluating whether to build on ANS.

Request layer

Web Bot Auth

Cloudflare / IETF WebBotAuth WG

Per-request HTTP signature authentication. ANS adds the identity backstop: who's behind that signing key?

Discovery layer

DNS-AID

Infoblox / IETF dnsop

SVCB-based agent endpoint discovery. ANS adds trust verification for the endpoints DNS-AID finds.

Bootstrap layer

AID

agentcommunity.org

Minimal TXT-based bootstrap. ANS adds version binding, transparency logs, and graduated verification.

Protocol layer

A2A / MCP

Linux Foundation AAIF

How agents communicate. ANS wraps Protocol Cards into Trust Cards with identity fields and SCITT receipts.

Built on the naming system the internet already uses.

Just like websites use domain names and DNS to make it easy for people to find them, ANS extends that familiar model to AI agents, using domain names and DNS as the foundation for agent identity. And the infrastructure is already built and being used.

The idea is simple: if an agent acts for an organization or individual, its identity should be anchored to a domain.

Support the standard

Help shape how AI agents identify themselves on the internet. Get in touch or explore how ANS works.

Support the standard

See how ANS works

*原文请访问 [ansinfo.ai](https://ansinfo.ai)*