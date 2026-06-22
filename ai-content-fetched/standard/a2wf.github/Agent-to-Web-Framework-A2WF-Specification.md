---
title: **Agent‑to‑Web 框架（A2WF）规范**
source: a2wf.github.io
url: https://a2wf.github.io/spec
date: 2026-06-22
category: standard/a2wf.github
translated: true
fetched_at: 2026-06-22T17:49:24.395857
---
# **Agent‑to‑Web 框架（A2WF）规范**

**来源**: a2wf.github.io | **日期**: 2026-06-22

---

The Agent-to-Web Framework (A2WF) defines

siteai.json

,
    a machine-readable policy file that website operators publish to declare
    which actions AI agents are permitted, restricted, or prohibited from
    performing on their site. Where robots.txt [[ROBOTS-TXT]]
    governs what may be

crawled

,

siteai.json

governs
    what an agent may

do

: submit forms, complete transactions,
    book appointments, or extract data.

This specification defines the file location, syntax, semantics, and
    conformance requirements for

siteai.json

, together with
    fields that support transparency and human-oversight obligations under
    the EU AI Act (in particular Articles 14, 26, and 50).

This document is a

work in progress

developed by the

A2WF Community Group

.
    Comments, issues, and pull requests are welcome at the

A2WF specification repository on GitHub

.

The Community Group was launched on 29 March 2026. This is the first
    ReSpec-based revision of the specification and corresponds to the same
    technical content as

specification-v1.0.md

in the repository, restructured to meet

W3C Community Group specification requirements

.

Introduction

AI agents now interact with websites in ways that go well beyond
    traditional crawling. Agents fill out forms, complete checkouts,
    schedule appointments, compare prices, and operate accounts on behalf
    of users. Existing web standards address only adjacent concerns:

robots.txt [[ROBOTS-TXT]] governs which URLs may be crawled, with a binary allow/deny model. It says nothing about actions.

IETF AIPREF expresses preferences about training and content reuse. It does not govern interactive behaviour.

Cookie consent banners govern client-side tracking by humans, not actions taken by autonomous agents.

A2WF fills this gap. A site operator places a

siteai.json

document at a well-known location and declares, in a structured form,
    the conditions under which an AI agent may operate on the site.

Problem statement

AI agents increasingly interact with websites — browsing products,
      comparing prices, booking appointments, filling forms, extracting data.
      Website operators face a critical gap: no standard exists that gives the
      website operator a machine-readable way to declare:

What agents are

ALLOWED

to do (read catalogues, search, compare prices).

What agents

MUST NOT

do (bulk scrape, post fake reviews, complete unauthorised transactions).

What requires

HUMAN VERIFICATION

(checkout, booking, contact forms).

How agents must

IDENTIFY

themselves (name, operator, purpose).

What

LEGAL TERMS

apply (Terms of Service, jurisdiction, regulatory compliance).

What

RATE LIMITS

are enforced (per action, per minute, per hour).

Current agent-side standards (MCP [[MCP]],
      A2A [[A2A]], enterprise IAM) govern agents from the
      agent operator's perspective. A2WF fills the gap by providing
      governance from the

website operator's

perspective.

Proposed solution:

siteai.json

siteai.json

is a JSON-based policy file provided by
      website operators to declare permissions, restrictions, agent
      identification requirements, and legal terms in machine-readable form.
      Its design intent is to give the website side of the agent ecosystem
      a single, discoverable, structured artifact — comparable in
      role to

robots.txt

[[ROBOTS-TXT]] for crawlers — but expressing actions, not just
      paths.

Relationship to Schema.org

This specification uses Schema.org [[SCHEMA-ORG]]
      vocabulary where applicable for site-level concepts (WebSite,
      Organization, ContactPoint), avoiding reinvention of standard terms.
      It complements Schema.org by introducing governance structures not
      covered there: permissions, scraping policies, agent identification,
      human verification, and legal enforcement metadata.

An AI agent uses

siteai.json

first to obtain the
      governance rules, then uses detailed Schema.org markup found on
      specific pages for in-depth entity information.

Relationship to existing standards

Standard

Scope

Relationship to A2WF

robots.txt

Crawling

Complementary — A2WF references robots.txt via

discovery.robotsTxt

.

sitemap.xml

URL listing

Independent — both files may coexist.

llms.txt

Content guidance for LLMs

Complementary — A2WF references it via

discovery.llmsTxt

.

MCP / A2A

Agent-side protocols

Complementary — A2WF references endpoints via

discovery.mcpEndpoint

/

discovery.a2aAgentCard

.

Schema.org

Page-level entity vocabulary

A2WF reuses Schema.org terms where applicable.

Approach to multilinguality

siteai.json

is a single canonical document in one language,
      identified via

identity.inLanguage

using a BCP 47 tag.
      Multilingual sites SHOULD provide alternate language versions through
      site infrastructure (separate origins, Accept-Language negotiation, or
      regional siteai.json variants) rather than embedding multilingual
      content inside a single file.

Intended audience

Website operators

publishing governance policies for AI agents.

AI agent operators

implementing conforming consumer behaviour.

Tool authors

building generators, validators, or auditing tools for siteai.json files.

Compliance and legal teams

mapping declared policies to regulatory frameworks.

Regulators & compliance officers

: how

siteai.json

enables machine-readable AI governance.

Conventions and terminology

The format is JSON [[RFC8259]], UTF-8 encoded. Data types
      used in this specification are: String, Object, Array, Boolean,
      Integer. URLs are valid URIs, preferably canonical and absolute.
      Language tags follow IETF BCP 47 [[BCP47]]. Date-time values follow
      ISO 8601 / [[RFC3339]]. Schema.org vocabulary is referenced from

https://schema.org/

[[SCHEMA-ORG]].

The key words

MUST

,

MUST NOT

,

REQUIRED

,

SHOULD

,

SHOULD NOT

,

RECOMMENDED

,

MAY

, and

OPTIONAL

in this document are to be
      interpreted as described in BCP 14 [[RFC2119]] [[RFC8174]] when, and
      only when, they appear in all capitals, as shown here.

This document defines two classes of products:

publishing site

(the website operator publishing a

siteai.json

) and

consuming agent

(the AI agent that retrieves and acts on it).
    Conformance criteria for each are stated in their respective sections.

File location and discovery

Preferred method: root URL

A publishing site MUST serve

siteai.json

from the
      well-known location at the root of its origin:

https://example.com/siteai.json

The file MUST be served with HTTP status

200 OK

and

Content-Type: application/json

.

Alternative:

robots.txt

directive

A publishing site MAY also declare the location of its

siteai.json

in

robots.txt

using the
      non-standard but conventional directive:

SiteAI: https://example.com/siteai.json

Alternative: HTML

<link>

tag

A publishing site MAY include a

<link>

element in
      the document head:

<link rel="siteai" href="https://example.com/siteai.json">

Alternative: well-known URI

A publishing site MAY also serve the file at

/.well-known/siteai.json

for compatibility with
      well-known URI conventions [[RFC8615]]. When both a root and
      well-known location are present, they MUST point to the same
      content.

Priority and retrieval

Consuming agents SHOULD retrieve

siteai.json

in the
      following order, stopping at the first successful retrieval:

Root URL (

/siteai.json

)

Well-known URI (

/.well-known/siteai.json

)

HTML

<link rel="siteai">

in the home page

SiteAI:

directive in

robots.txt

File serving requirements

The file MUST be served over HTTPS.

The file SHOULD be cacheable with reasonable

Cache-Control

headers (e.g.

max-age=3600

).

The file SHOULD be at most a few hundred kilobytes; consuming
          agents MAY truncate or reject responses larger than 1 MiB.

Format specification — required elements

Top-level structure

A

siteai.json

document MUST consist of a single JSON
      object [[RFC8259]]. The root object MUST contain:

specVersion

(String):

REQUIRED.

Must be

"1.0"

.

identity

(Object):

REQUIRED.

Core website identification.

permissions

(Object):

REQUIRED.

Agent access policies.

The root object SHOULD contain:

@context

(String): RECOMMENDED.

"https://schema.org"

.

agentIdentification

(Object): RECOMMENDED.

scraping

(Object): RECOMMENDED.

The root object MAY contain additional members defined in

Optional governance extensions

.
      Consuming agents MUST ignore any unrecognised members.

The

identity

object (REQUIRED)

Provides core identifying and contextual information about the
      publishing site. Where applicable, fields use Schema.org WebSite
      vocabulary.

Field

Type

Requirement

Description

@type

String

RECOMMENDED

"WebSite"

. Schema.org type declaration.

domain

String

REQUIRED

Canonical absolute URL (schema:WebSite.url).

name

String

REQUIRED

Official site / brand name (schema:WebSite.name).

description

String

OPTIONAL

General site description (schema:WebSite.description).

purpose

String

RECOMMENDED

Concise AI-focused description of the site's primary goal and audience. A2WF-specific.

inLanguage

String

REQUIRED

Primary language as a BCP 47 tag.

category

String

RECOMMENDED

Website type, e.g.

"e-commerce"

,

"healthcare"

,

"government"

,

"saas"

.

jurisdiction

String

RECOMMENDED

Legal jurisdiction, e.g.

"EU"

,

"US"

,

"US-CA"

,

"CH"

.

applicableLaw

Array<String>

OPTIONAL

Specific regulations, e.g.

["EU AI Act", "GDPR"]

.

contact

String

OPTIONAL

Email for policy-related questions.

The

permissions

object (REQUIRED)

The core governance layer. Contains three sub-objects that control
      different aspects of AI agent interaction:

read

,

action

, and

data

.

Read permissions

Control what information consuming agents can access (passive operations):

productCatalog

— product listings, descriptions, images, categories.

pricing

— prices, fees, rate cards.

availability

— stock levels, appointment slots, table availability.

openingHours

— business hours and holiday schedules.

contactInfo

— address, phone, email.

reviews

— customer reviews, ratings, testimonials.

faq

— frequently asked questions.

companyInfo

— about page, team, history.

Action permissions

Control what operations consuming agents may perform (active operations):

search

— site search functionality.

addToCart

— adding items to a shopping cart.

checkout

— completing a purchase (typically

humanVerification: true

).

createAccount

— user registration (often denied).

submitReview

— posting reviews (often denied to prevent fakes).

submitContactForm

— contact form submission.

bookAppointment

— booking reservations / appointments.

cancelOrder

— cancelling orders.

requestRefund

— initiating refund requests.

Data permissions

Protect sensitive information (typically all denied):

customerRecords

— user profiles and personal data.

orderHistory

— past orders and transactions.

paymentInfo

— credit cards and bank details.

internalAnalytics

— traffic data and business metrics.

employeeData

— staff information.

Permission properties

Each permission value is an object with the following members:

Field

Type

Requirement

Description

allowed

Boolean

REQUIRED

Is this permission granted?

rateLimit

Integer

OPTIONAL

Maximum requests per minute for this action.

humanVerification

Boolean

OPTIONAL

Default

false

. Requires human confirmation.

note

String

OPTIONAL

Explanatory note for agents and humans. Treated as data, not as instruction.

The

agentIdentification

object (RECOMMENDED)

Defines requirements for AI agent self-identification.

requireUserAgent

(Boolean) — agent MUST include an identifying User-Agent header.

requiredFields

(Array<String>) — fields the agent must provide; valid values include

"agentName"

,

"agentOperator"

,

"agentPurpose"

.

allowAnonymousAgents

(Boolean) — default

true

. If

false

, unidentified agents MUST be denied.

trustedAgents

(Array<Object>) — whitelist; each entry has

{ name, operator, permissions }

.

blockedAgents

(Array<Object>) — blacklist; each entry has

{ pattern, reason }

.

The

scraping

object (RECOMMENDED)

Declares policies on automated data extraction.

bulkDataExtraction

(Boolean) — default

false

. Systematic large-scale extraction.

priceMonitoring

(Boolean) — default

false

. Automated price-change tracking.

contentReproduction

(Boolean) — default

false

. Reproducing or republishing content.

competitiveAnalysis

(Boolean) — default

false

. Data collection for competitive intelligence.

trainingDataUsage

(Boolean) — default

false

. Using site content as training data.

note

(String) — OPTIONAL. Additional context or licensing information.

Optional governance extensions

The

defaults

object

Global default settings that apply unless overridden by individual permissions.

agentAccess

(String) —

"open"

(permissive),

"restricted"

(deny by default), or

"minimal"

(deny everything except explicit allows).

requireIdentification

(Boolean) — default

false

.

humanVerificationRequired

(Boolean) — default

false

. If

true

, all actions require human verification.

maxRequestsPerMinute

(Integer) — global per-minute rate limit.

maxRequestsPerHour

(Integer) — global per-hour rate limit.

respectRobotsTxt

(Boolean) — default

true

.

The

humanVerification

object

Defines human-in-the-loop requirements for sensitive actions.

methods

(Array<String>) — accepted methods:

"redirect-to-browser"

,

"email-confirmation"

,

"sms-otp"

.

requiredFor

(Array<String>) — names of actions that require human verification.

note

(String) — additional human-readable instructions.

The

legal

object

References Terms of Service and regulatory frameworks.

termsUrl

(String) — RECOMMENDED. URL to AI-specific Terms of Service.

complianceNote

(String) — OPTIONAL human-readable compliance statement.

dataRetention

(String) — OPTIONAL rules for agent data retention.

euAiActCompliance

(Object) — OPTIONAL. EU AI Act-specific metadata
        supporting Regulation (EU) 2024/1689 [[EU-AI-ACT]]:

transparencyRequired

(Boolean) — agents must identify as AI.

riskClassification

(String) —

"minimal"

,

"limited"

,

"high"

, or

"unacceptable"

.

humanOversightMandatory

(Boolean).

The

discovery

object

Links to complementary web resources.

mcpEndpoint

(String) — URL to an MCP server card.

a2aAgentCard

(String) — URL to an A2A agent card.

robotsTxt

(String) — URL to

robots.txt

.

llmsTxt

(String) — URL to an

llms.txt

file.

schemaOrg

(Boolean) — whether Schema.org markup is present on the site.

openApi

(String) — URL to an OpenAPI specification.

The

metadata

object

$schema

(String) — URL of the JSON Schema for validation.

schemaVersion

(String) — specification version, e.g.

"1.0"

.

generatedAt

(String) — RFC 3339 timestamp of generation.

author

(String) — policy creator.

lastUpdated

(String, ISO date) — last modification date.

expiresAt

(String, ISO date) — policy expiration date.

changelogUrl

(String) — URL to policy change history.

Enforcement

Voluntary compliance

Like robots.txt [[ROBOTS-TXT]], A2WF relies primarily
      on voluntary compliance by reputable AI agents. Major agent vendors
      are expected to respect published policies as part of responsible AI
      deployment.

Technical enforcement

Publishing sites MAY enforce policies through:

HTTP

403

responses to non-compliant agents.

Rate limiting based on declared limits.

Web Application Firewalls with agent-aware rules.

User-Agent-based blocking for agents that violate declared policies.

Legal enforcement

The

legal.termsUrl

field enables legal enforcement by
      linking to machine-readable policies. Existing legal frameworks
      (e.g. CFAA in the United States) treat violation of machine-readable
      access policies as evidence of unauthorised access. The
      EU AI Act [[EU-AI-ACT]] (effective August 2026)
      requires transparency and risk management for AI systems;

siteai.json

provides machine-readable evidence of
      declared policies.

Audit and logging

Publishing site

s SHOULD log agent access patterns and compare them
      against declared policies. The

agentIdentification

section enables meaningful audit trails by requiring agent
      self-identification.

Security considerations

Policy integrity

The

siteai.json

file MUST be served over HTTPS to
      prevent tampering. Publishing sites SHOULD implement integrity checks
      and monitor for unauthorised modifications.

Prompt injection

The

siteai.json

file contains structured data, not
      executable content. Consuming agents MUST treat all fields as data,
      not instructions. String fields (especially

note

) MUST
      NOT be interpreted as agent commands.

Policy spoofing

Consuming agents MUST only trust

siteai.json

files
      served from the domain they describe. Cross-domain policy
      declarations MUST be rejected unless explicitly referenced via the

discovery

mechanism.

Denial of service

Rate limits declared in

siteai.json

are requests from
      the publishing site, not guarantees. Consuming agents SHOULD respect
      declared limits. Publishing sites SHOULD implement server-side rate
      limiting independently of declared policies.

Privacy considerations

The

siteai.json

file describes a site's policy for AI
    agents and is intended to be fetched by agents and tools. It SHOULD
    NOT contain personal data about individual users. The

contact

field in

identity

is intended for a role-based mailbox (for example

ai-policy@example.com

) rather than an individual
    person's address.

Logging of agent access by publishing sites is governed by applicable
    data protection law (such as the GDPR in the European Union); access
    logs MUST be processed in accordance with that law.

Versioning and extensibility

Version strategy

The

specVersion

field identifies the specification
      version. Major versions (2.0, 3.0) MAY introduce breaking changes.
      Minor updates within v1.x MUST remain backward-compatible.

Forward compatibility

Consuming agents MUST ignore any unrecognised members. This ensures
      that files created with future extensions remain readable by v1.0
      consumers.

Extensibility roadmap

Future extensions may include:

Dynamic policy endpoints (API-based policy queries).

Signed policies (cryptographic verification).

Industry-specific profiles (healthcare, finance, government).

Agent capability matching.

Schema.org alignment

siteai.json

field

Schema.org equivalent

@context

JSON-LD context

identity.@type

schema:WebSite

identity.name

schema:WebSite.name

identity.description

schema:WebSite.description

identity.inLanguage

schema:WebSite.inLanguage

identity.domain

schema:WebSite.url

legal.termsUrl

schema:WebSite.publishingPrinciples

permissions.*

A2WF extension (no Schema.org equivalent)

scraping.*

A2WF extension

agentIdentification.*

A2WF extension

humanVerification.*

A2WF extension

A2WF extends Schema.org rather than reinventing it. Fields without a
    Schema.org equivalent represent the novel governance concepts unique
    to A2WF.

File ecosystem

File

Purpose

Since

/robots.txt

Crawl permissions

1994

/sitemap.xml

URL listing for search engines

2005

/llms.txt

Content guide for LLMs

2024

/.well-known/mcp.json

MCP server discovery

2024

/siteai.json

AI agent access governance (A2WF)

2025

Each file serves a distinct purpose.

siteai.json

is the
    governance layer that sits alongside all of them. The

discovery

section of

siteai.json

can
    reference each of these files, creating a unified entry point for AI
    agents.

Complete example: e-commerce store

{
  "@context": "https://schema.org",
  "specVersion": "1.0",
  "identity": {
    "@type": "WebSite",
    "domain": "https://www.example-store.com",
    "name": "Example Online Store",
    "description": "Premium widgets and gadgets",
    "purpose": "E-commerce store selling premium widgets to consumers in the EU.",
    "inLanguage": "en",
    "category": "e-commerce",
    "jurisdiction": "EU",
    "applicableLaw": ["EU AI Act", "GDPR"],
    "contact": "ai-policy@example-store.com"
  },
  "defaults": {
    "agentAccess": "restricted",
    "requireIdentification": true,
    "maxRequestsPerMinute": 30,
    "respectRobotsTxt": true
  },
  "permissions": {
    "read": {
      "productCatalog": { "allowed": true, "rateLimit": 60 },
      "pricing": { "allowed": true },
      "availability": { "allowed": true, "rateLimit": 30 },
      "reviews": { "allowed": true, "rateLimit": 20 },
      "faq": { "allowed": true }
    },
    "action": {
      "search": { "allowed": true, "rateLimit": 20 },
      "addToCart": { "allowed": true },
      "checkout": {
        "allowed": true,
        "humanVerification": true,
        "note": "Final purchase requires human confirmation."
      },
      "createAccount": { "allowed": false },
      "submitReview": { "allowed": false }
    },
    "data": {
      "customerRecords": { "allowed": false },
      "paymentInfo": { "allowed": false },
      "internalAnalytics": { "allowed": false }
    }
  },
  "scraping": {
    "bulkDataExtraction": false,
    "priceMonitoring": false,
    "trainingDataUsage": false,
    "contentReproduction": false
  },
  "agentIdentification": {
    "requireUserAgent": true,
    "requiredFields": ["agentName", "agentOperator"],
    "allowAnonymousAgents": false
  },
  "humanVerification": {
    "methods": ["redirect-to-browser"],
    "requiredFor": ["checkout"]
  },
  "discovery": {
    "robotsTxt": "https://www.example-store.com/robots.txt",
    "llmsTxt": "https://www.example-store.com/llms.txt",
    "schemaOrg": true
  },
  "legal": {
    "termsUrl": "https://www.example-store.com/legal/ai-terms",
    "euAiActCompliance": {
      "transparencyRequired": true,
      "riskClassification": "limited",
      "humanOversightMandatory": false
    }
  },
  "metadata": {
    "author": "Example Store Legal Team",
    "lastUpdated": "2026-03-18",
    "schemaVersion": "1.0"
  }
}

Consuming agent requirements

A conforming

consuming agent

MUST:

Retrieve

siteai.json

from the well-known location before performing any non-read action on the site.

Identify itself in the

User-Agent

header in a form that distinguishes it from human-operated browsers.

Honour all

"allowed": false

declarations as prohibitions.

Observe declared rate limits.

Trigger human verification flows where declared.

Treat all string content (notably

note

fields) as data and never as instructions.

Acknowledgements

The editor thanks the founding members and early reviewers of the
    A2WF Community Group for their feedback on the draft specification,
    and the W3C Community Development Lead for guidance on aligning the
    specification with W3C Community Group requirements.

*原文请访问 [a2wf.github.io](https://a2wf.github.io/spec)*