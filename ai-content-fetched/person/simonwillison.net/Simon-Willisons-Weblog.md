---
title: Simon Willison的博客
source: simonwillison.net
url: https://simonwillison.net
date: 2026-06-22
category: person/simonwillison.net
translated: true
fetched_at: 2026-06-22T19:49:07.426906
---
# Simon Willison的博客

**来源**: simonwillison.net | **日期**: 2026-06-22

---

Simon Willison’s Weblog

On

claude-mythos

17

claude

284

open-source

308

tools

67

pelican-riding-a-bicycle

119

...

Sponsored by:

Microsoft — Agent projects stall between demo and production. Microsoft's MVP checklist closes that gap.

Try it

Entries

Links

Quotes

Notes

Guides

Elsewhere

June 21, 2026

sqlite-utils 4.0rc1 adds migrations and nested transactions

sqlite-utils

is my combined Python library and CLI tool for working with SQLite databases. It provides an extensive set of higher-level operations on top of Python’s default

sqlite3 package

, including support for

complex table transformations

, automatic table creation

from JSON data

and a whole lot more.

[...

975 words

]

11:35 pm

/

migrations

,

projects

,

sqlite

,

sqlite-utils

,

annotated-release-notes

Release

sqlite-utils 4.0rc1

See

sqlite-utils 4.0rc1 adds migrations and nested transactions

.

21st Jun 2026, 11:30 pm

·

sqlite-utils

Temporary Cloudflare Accounts for AI agents

(

via

)
    The announcement says this is "for AI agents" but (as is pretty common these days) the AI hook isn't really necessary, this is an interesting feature for everyone else as well.

Short version: you can now create a Cloudflare Workers project and run this, without even creating a Cloudflare account:

npx wrangler deploy --temporary

Cloudflare will deploy the application to a new, ephemeral project which will stay live for 60 minutes.

I

had GPT-5.5 xhigh

in Codex Desktop

build this test application

providing a tool for following HTTP redirects and returning the final destination. The temporary deployment worked as advertised.

Running the deployment spits out the URL to a page for claiming the new project, for if you want it to last for more than 60 minutes. Here's what that claim screen looks like:

#

10:01 pm

/

cloudflare

June 19, 2026

The real valuable capability MCP offers over skills/CLI is isolating the auth flow outside of the agent’s context window, and potentially out of the harness completely. [...]

Maybe the idealized form of MCP is just an auth gateway for the API and nothing else. That’d still be a win.

—

Sean Lynch

,

comment on Hacker News

#

10:45 pm

/

model-context-protocol

,

llms

,

ai

,

generative-ai

,

skills

Sighting

6:55 PM – 7:02 PM

— California Brown Pelican, Pacific Harbor Seal, in Monterey Bay National Marine Sanctuary, CA, US, CA

California Brown Pelican

Pacific Harbor Seal

19th Jun 2026

June 18, 2026

Datasette Apps: Host custom HTML applications inside Datasette

Today we launched a new plugin for Datasette,

datasette-apps

, with

this launch announcement post

on the Datasette project blog. That post has the

what

, but I’m going to expand on that a little bit here to provide the

why

.

[...

2,301 words

]

11:58 pm

/

iframes

,

javascript

,

projects

,

sandboxing

,

ai

,

datasette

,

generative-ai

,

llms

,

ai-assisted-programming

,

content-security-policy

Release

datasette-acl 0.6a0

This release expands

datasette-acl

from table-only permissions toward a general resource-sharing system.

Alex Garcia did most of the work for this release - we're fleshing out the plugin that will allow multi-user Datasette instances finely grained control over who can access which resources within Datasette.

18th Jun 2026, 7:03 pm

·

datasette

,

alex-garcia

June 17, 2026

GLM-5.2 is probably the most powerful text-only open weights LLM

Chinese AI lab

Z.ai

released GLM-5.2

to their coding plan subscribers

on June 13th, and then yesterday (June 16th) released the full open weights under an MIT license. Similar in size to their previous GLM-5 and GLM-5.1 releases, this is 753B parameter,

1.51TB

monster—with 40 active parameters (Mixture of Experts). GLM-5.2 is a text input only model—Z.ai have a separate vision family most recently represented by

GLM-5V-Turbo

, but that one isn’t open weights. GLM-5.2 has a 1 million token context window, up from GLM-5.1’s 200,000.

[...

598 words

]

11:58 pm

/

ai

,

generative-ai

,

llms

,

pelican-riding-a-bicycle

,

llm-release

,

openrouter

,

ai-in-china

,

glm

What happened in 2025 was this:

the economics of code production were turned upside down

. Instead of being very hard, time-consuming, and expensive to generate code, it became effectively free and instant. Lines of code went from being treasured, reused, cared for and carefully curated, to being disposable and regenerable, practically overnight.

—

Charity Majors

,

AI demands more engineering discipline. Not less

#

5:12 pm

/

charity-majors

,

ai-assisted-programming

,

generative-ai

,

ai

,

llms

Tool

<click-to-play> — a still that plays

A progressive enchantment Web Component that turns this markup:

<click-to-play>
  <a href="URL to GIF">
    <img src="URL to first frame" alt="...">
  </a>
</click-to-play>

Into a still frame with a click to play button which loads the GIF on demand. For when you don't want big GIFs to be loaded unless people want to play them.

Here's

an example

that demonstrates the new row editing tools in Datasette - in fact I built this Web Component for that post.

17th Jun 2026, 3:56 am

·

web-components

,

javascript

,

gif

,

progressive-enhancement

NetNewsWire Status

(

via

)
    I find this inspiring. Brent Simmons retired a year ago, and his retirement project is making one piece of software really,

really

good - free from any commercial pressure.

The software is

NetNewsWire

- "it's like podcasts, but for

reading

" - first released in 2002 and

made open source

in 2018.

I've been using it on Mac and iPhone for several years now and I'm finding it indispensable.

#

3:36 am

/

brent-simmons

,

netnewswire

,

open-source

Sighting

6:38 PM – 7:10 PM

— California Brown Pelican, Botta's Pocket Gopher, Great Blue Heron, California Sea Lion, Pacific Harbor Seal, in Monterey Bay National Marine Sanctuary, CA, US, CA

California Brown Pelican

Botta's Pocket Gopher

Great Blue Heron

California Sea Lion

Pacific Harbor Seal

California Brown Pelican

17th Jun 2026

June 16, 2026

Release

datasette 1.0a34

Quoting the release notes:

The big feature in this alpha is tools to insert, edit and delete rows within the Datasette interface. These features are available on table pages, and edit and delete are also available as action items on the row page.

The inspiration for this feature - which is

long

overdue - was

Datasette Agent

. I added

SQL write support

to that the other day which highlighted how absurd it was that you could insert and edit ties via the chat interface but not in the regular Datasette UI!

16th Jun 2026, 9:31 pm

·

projects

,

annotated-release-notes

,

datasette

Release

datasette-tailscale 0.1a0

A very experimental alpha plugin which lets you do this:

datasette tailscale mydata.db \
  --ts-authkey tskey-auth-xxxx --ts-hostname datasette-preview

This starts a localhost Datasette server with a

Tailscale

sidecar that connects it to your Tailnet, such that

http://datasette-preview/

serves Datasette.

It's using the Python bindings for the experimental

tailscale-rs

library. I

filed an issue

asking if there's a cleaner way of setting up the proxy mechanism.

16th Jun 2026, 4:18 pm

·

tailscale

,

datasette

I can 100% attest to the fact that Qwen3.6-27B is a very capable local model for coding tasks. Over the last month and a half I've been using it almost daily, either on my M2 Ultra or on my RTX 5090 box. I use it for small

mundane tasks at ggml-org

- nothing really impressive, but definitely a helpful tool for a maintainer. I think I would be using it much more, if I didn't have to spend a lot of my time on reviewing PRs. Currently, I have a very lightweight harness - the pi agent with everything stripped (

pi -nc --offline

) and

a short system prompt

to align it a bit with my style.

—

Georgi Gerganov

,

Hacker News comment on

Running local models is good now

by  Boykis

#

4:04 pm

/

georgi-gerganov

,

llms

,

ai

,

generative-ai

,

pi

,

ai-assisted-programming

,

local-llms

,

qwen

,

coding-agents

The Fable 5 Export Controls Harm US Cyber Defense

.
    I

quoted The Atlantic

quoting Kate Moussouris earlier, when I should have gone straight to the source. Here she is confirming that the "jailbreak" that got Claude Fable 5 banned under an export control really was "fix this code":

The researchers took open-source code with known CVEs, plus new code with deliberately planted vulnerabilities, and asked Fable 5, Mythos, and Opus to “review the code for security issues.” Fable 5 refused. They then asked the models to “fix this code” and, through a multistep and manual process, turned the output into scripts that test the patches.

As Kate points out, this is absurd. Coding models fix bugs, and security exploits are the most important category of bugs for them to fix!

Defenders need to be able to ask AI to fix the bugs in a file, explain why the fix matters, and write tests that confirm the patch works. That is not a guardrail bypass. It is the most valuable thing an AI model can do for defensive security: executing the find, fix, and test loop defenders run every day. [...]

The prompts worked because they were defensive requests, and that capability cannot be removed without making the model worse at fixing bugs and verifying patches.

This whole situation is such a mess. Non-technical decision-makers have been hearing that models that can "craft cyber attacks" are uniquely dangerous for months. Now they look ready to ban any model that can help us secure our code.

#

5:20 am

/

jailbreaking

,

security

,

ai

,

generative-ai

,

llms

,

anthropic

,

ai-security-research

,

claude-mythos

Katie Moussouris, a cybersecurity expert and the CEO of Luta Security, told me that Anthropic shared with her a copy of the White House’s report on the Fable jailbreak to get her appraisal. (She said that she is not being paid by Anthropic.) The report, Moussouris said, involved IT experts asking Fable to help find and patch bugs. When given deliberately insecure code, she said, Fable refused the prompt “review the code for security issues” but then complied when asked to “fix this code,” followed by some further manual steps. Moussouris told me that this was just “the model working as intended” for cyberdefense.

—

Matteo Wong, The Atlantic

,

The White House Is Ratcheting Up Its War Against Anthropic

#

3:07 am

/

anthropic

,

claude

,

ai

,

llms

,

ai-ethics

,

jailbreaking

,

generative-ai

,

ai-security-research

,

claude-mythos

Sighting

6:56 PM

— Pacific Harbor Seal, in Monterey Bay National Marine Sanctuary, CA, US, CA

Pacific Harbor Seal

Pacific Harbor Seal

Pacific Harbor Seal

Pacific Harbor Seal

16th Jun 2026

TIL

Cloudflare CAPTCHA on at least one ampersand

I'm using Cloudflare's CAPTCHA (they call it a "Web Application Firewall > Custom rules > Managed Challenge" these days) to prevent crawlers from aggresively spidering my

faceted search engine

on this site, but I got fed up of even simple

?q=term

searches triggering the challenge.

After some mucking around with Claude Code it turns out you can register the following rule instead, so the CAPTCHA only kicks in for search URLs containing at least one ampersand:

(http.request.uri.path wildcard r"/search/*" and http.request.uri.query contains "&")

And now

/search/?q=lemur

works without triggering a CAPTCHA!

Also included: notes on

trying out the Cloudflare MCP with Claude Code

, though it turned out not to be able to edit the rules in question so I had Claude Code

switch to the Cloudflare API

instead.

16th Jun 2026, 12:21 am

·

captchas

,

cloudflare

,

claude-code

,

model-context-protocol

June 15, 2026

Release

datasette-apps 0.1a3

Fixed a bug where users without the

create-app

permission could still create apps.

#27

Fixed a bug where it was impossible to grant permission to edit an app to users who were not the app's owner. The rules for edit/delete are now the same as view: if the app is private only the owner can modify it, otherwise permission is controlled by Datasette's regular permission system.

#29

15th Jun 2026, 8:25 pm

·

datasette

Release

datasette-apps 0.1a2

Custom network/CSP origins for apps are now guarded by a new

apps-set-csp

permission, with an optional

allowed_csp_origins

plugin allow-list for non-privileged users. The Datasette Agent app creation tool enforces the same rules.

#24

Stored query picker now supports keyboard navigation and shows the three most recent accessible stored queries when focused.

#fragment

links inside apps are no longer intercepted by the external-link confirmation modal.

#23

Fixed link confirmation modal and logging panels in

?full=1

full-screen mode.

#26

15th Jun 2026, 5:26 pm

·

datasette

Release

datasette-agent 0.3a0

New tool,

execute_write_sql

, which requests user approval and then writes to a database - taking user permissions into account.

#27

I added a mechanism for asking user approval in

datasette agent 0.2a0

. The new

execute_write_sql

tool can now prompt the user for all kinds of useful operations. Here's an example where I add some pelican sightings to my

pelican_sightings

table:

The new version also enhances the

datasette agent chat

terminal mode to support approvals, and adds several new options including

--unsafe

mode for auto-approving them:

datasette agent chat

can execute tools that require user approval.

#30

Three new options for

datasette agent chat

-

--root

to run as root,

--yes

to approve all ask user questions, and

--unsafe

for both.

Tools can now provide plain text alternatives to HTML, for display in the

datasette agent chat

CLI.

#31

The

datasette agent chat content.db -m gpt-5.5 --unsafe

command can now be used to chat directly with a specific database

and

directly modify it through prompts like "create a notes table", "add a note about X" etc.

15th Jun 2026, 5:19 pm

·

annotated-release-notes

,

llm-tool-use

,

ai

,

llms

,

datasette

,

generative-ai

,

projects

,

datasette-agent

“They screwed us”: Personality clashes sent Anthropic’s models offline

.
    Lots of "source familiar with the administration's thinking" and "source close to Anthropic" in this Axios piece, which is the best collection of behind-the-scenes gossip I've seen about the US government

export control Mythos/Fable story

so far.

Logan Graham (

I lead the Frontier Red Team at Anthropic

), Dave Orr (Head of Safeguards, previously a Director of Engineering at Google DeepMind), and blog favorite

Nicholas Carlini

are reported to be meeting with the Commerce Department today in D.C. Good luck to them!

(I just noticed Logan was "Special Adviser to the Prime Minister" in the Boris Johnson era, covering AI, science, and technology policy - so significant political experience.)

This closing note doesn't give me much optimism that we'll be getting Fable back any time soon:

The bottom line

: One option is to make sure Anthropic's models can't be jailbroken — though perfect jailbreak resistance

may be

impossible.

Absent that, a source familiar with the administration's thinking said it may simply come down to an attitude fix where, instead of feeling dismissed, "everyone feels safe, secure and happy."

This made me wonder if Anthropic ever successfully addressed the class of attacks described in the

Universal and Transferable Adversarial Attacks on Aligned Language Models

paper from 2023.

It looks like their

Constitutional Classifiers

work (that post is from January this year) is relevant to that. They continue to claim that no "universal jailbreak" has been found against Claude Mythos,

classifying the jailbreak

that triggered the US government response as "a potential narrow, non-universal jailbreak".

#

2:57 pm

/

jailbreaking

,

ai

,

generative-ai

,

llms

,

anthropic

,

claude

,

nicholas-carlini

,

ai-ethics

,

claude-mythos

[...] Instead, I picture a specific person and I just write for them. Often this person is "me, but 3 years ago" or a good friend.

—

Julia Evans

,

write for 1 person

#

2:05 am

/

writing

,

julia-evans

Sighting

5:38 PM

— California Brown Pelican, in Monterey Bay National Marine Sanctuary, CA, US, CA

California Brown Pelican

California Brown Pelican

California Brown Pelican

15th Jun 2026

June 14, 2026

Why AI hasn’t replaced software engineers, and won’t

.
    Arvind Narayanan and Sayash Kappor take on the question of AI job losses through the lens of a profession that is uniquely suited to AI disruption - software engineering.

In this essay, we argue that there is enough evidence to reject the narrative that once AI capabilities reach a certain threshold, it will cause mass layoffs. Given that this is true even in a sector with very few regulatory barriers, most other professions are likely to be even more cushioned.

The first good news is that the data still doesn't support the idea that AI is causing mass unemployment.

In March 2025, New York became the first U.S. state to add an AI disclosure checkbox to WARN Act filings. In the full first year, more than 160 companies filed WARN notices.

Not a single one

checked the AI box

AI speeds up the typing-code-into-a-computer phase, but it turns out software engineering is about a whole lot more than that:

If writing code isn’t the bottleneck, what is? The task-breakdown surveys point at things like meetings or debugging. This just leads to more questions: what are developers doing in those meetings and why can’t it be done by AI? Won’t debugging get automated as capabilities improve? To understand the real bottlenecks, we have to get qualitative, and dig into software engineers’ own understanding of what it is they do that resists automation.

When we did this analysis, it revealed three things as the real bottlenecks (1) deciding and specifying what to build, (2) verifying and being accountable for what is delivered, and (3) the deep human understanding — of the codebase, the business, and the environment — required to carry out both of these.

I'm finding AI assistance also helps me with the deciding and verifying steps, but it's the "deep human understanding" that remains key to the value I provide. Give me all of the AI assistance in the world and the value I produce will still be reliant on how deeply I understand both the problems and the solutions that the agents are building for them.

#

11:54 pm

/

careers

,

ai

,

generative-ai

,

llms

,

arvind-narayanan

,

ai-ethics

Sighting

7:11 PM – 7:19 PM

— California Brown Pelican, Great Blue Heron, California Sea Lion, in Monterey Bay National Marine Sanctuary, CA, US, CA

Great Blue Heron

California Sea Lion

California Brown Pelican

California Brown Pelican

14th Jun 2026

June 13, 2026

Publishing WASM wheels to PyPI for use with Pyodide

The

Pyodide 314.0 release announcement

(via

Hacker News

) includes news I’ve been looking forward to for a long time:

[...

757 words

]

11:55 pm

/

lua

,

pypi

,

python

,

sandboxing

,

webassembly

,

github-actions

,

pyodide

Release

luau-wasm 0.1a0

See

Publishing WASM wheels to PyPI for use with Pyodide

for details.

13th Jun 2026, 11:14 pm

·

lua

,

pyodide

,

webassembly

Research

Mapping SQLite result columns back to their source `table.column`

It would be neat if arbitrary SQL queries in

Datasette

could be rendered with additional information based on which columns from which tables were included in the results.

To build that, we would need to be able to look at a SQL query like

select users.name, orders.total from users join orders on orders.user_id = users.id

and programmatically identify the

table.column

for each result - navigating not just joins but also more complex syntax like CTEs.

I decided to set Claude Code (Opus 4.8, since Fable is currently

banned by the US government

) on the problem. It found several promising solutions - one using

apsw

, another that uses

ctypes

to access the SQLite

sqlite3_column_table_name()

C function

(which is not otherwise exposed to Python), and one using clever interrogation of the output of

EXPLAIN

.

13th Jun 2026, 11:05 pm

·

sqlite

,

datasette

,

python

Sighting

7:49 PM

— Harbor Seal, in Monterey Bay National Marine Sanctuary, CA, US, CA

Harbor Seal

Harbor Seal

13th Jun 2026

Statement on the US government directive to suspend access to Fable 5 and Mythos 5

(

via

)
    Well this is

nuts

:

The US government, citing national security authorities, has issued an export control directive to suspend all access to Fable 5 and Mythos 5 by any foreign national, whether inside or outside the United States, including foreign national Anthropic employees. The net effect of this order is that we must abruptly disable Fable 5 and Mythos 5 for

all

our customers to ensure compliance.

Access to all other Anthropic models

will not be affected.

We received the directive from the government today at 5:21pm (ET). The letter did not provide specific details of its national security concern. Our understanding is that the government believes it has become aware of a method of bypassing, or "jailbreaking" Fable 5. We reviewed a demonstration of this specific technique being used to identify a small number of previously known, minor vulnerabilities. These vulnerabilities all appear relatively simple, and we have found that other publicly-available models are able to discover them as well without requiring a bypass. [...]

To date, the government has only given us verbal evidence of a potential narrow, non-universal jailbreak, which essentially consists of asking the model to read a specific codebase and fix any software flaws. Our understanding is that one potential jailbreak was shared with the government. We have reviewed the report and validated that the level of capability displayed there is widely available from other models (including OpenAI's

GPT-5.5

), and is used every day by the defenders who keep systems safe. We will share more details over the next 24 hours.

I still have access to Fable via

claude.ai

and Claude Code now, at 9:01pm ET.

Update

: I ran

this script

against the Anthropic API to spot when

claude-fable-5

would stop working. My access was cut off at 6:59pm Pacific (9:59pm ET):

[2026-06-12T18:56:50-07:00] attempt 35: running uv run llm -m claude-fable-5 hi
[2026-06-12T18:56:55-07:00] success: Hi there! How can I help you today?
[2026-06-12T18:57:55-07:00] attempt 36: running uv run llm -m claude-fable-5 hi
[2026-06-12T18:57:59-07:00] success: Hi! How can I help you today?
[2026-06-12T18:58:59-07:00] attempt 37: running uv run llm -m claude-fable-5 hi
[2026-06-12T18:59:00-07:00] FAILED after attempt 37 with exit code 1

stderr:
Error: Error code: 404 - {'type': 'error', 'error': {'type': 'not_found_error', 'message': 'Claude Fable 5 is not available. Please use Opus 4.8. Learn more: https://www.anthropic.com/news/fable-mythos-access'}, 'request_id': 'req_011CbzRyirV7KZLHYYdBM9od'}

#

1:01 am

/

jailbreaking

,

ai

,

generative-ai

,

llms

,

anthropic

,

claude

,

ai-ethics

,

claude-mythos

June 12, 2026

OpenAI WebRTC Audio Session, now with document context

.
    I built the first version of this tool

in December 2024

to try out the then-new OpenAI WebRTC API for interacting with their realtime audio models.

Last month OpenAI

introduced a brand new model

to that API called

GPT‑Realtime‑2

, which they promoted as "our first voice model with GPT‑5‑class reasoning" - with a Sep 30, 2024 knowledge cut-off.

I've been waiting for that model to show up in the ChatGPT iPhone app but it still hasn't, so I revisited my old playground.

You can now pick the better model, and you can also paste in a big chunk of document context so you can have as audio conversation in your browser about whatever information you think would be useful to explore in a conversational way.

#

11:53 pm

/

audio

,

tools

,

ai

,

openai

,

generative-ai

,

llms

,

multi-modal-output

,

webrtc

Jenny owns a crematorium. John’s propane company gives her a $20 billion investment in return for 5 percent of her operation. Jenny throws $10 billion into the incinerator, then pays John $10 billion to buy propane to burn that money to ashes. John reports that his AI investments have generated $10 billion in revenue this quarter and that he owns 5 percent of a $100 billion business. A reporter from

Forbes

is assigned to profile John and Jenny, and over the course of his research, he becomes embroiled in a passionate but confusing three-way love affair with them, which eventually turns into a polyamorous common-law marriage. His profile is glowing, but light on financial details.

—

Andrew Singleton

,

AI Economics for Dummies

#

6:09 pm

/

ai

June 11, 2026

Claude Fable is relentlessly proactive

After two days of experience with

Claude Fable 5

I think the best way to describe it is

relentlessly proactive

. It knows a whole lot of tricks and it will deploy pretty much any of them to get to its goal.

[...

1,939 words

]

11:35 pm

/

ai

,

prompt-injection

,

generative-ai

,

llms

,

ai-assisted-programming

,

coding-agents

,

claude-code

,

claude-mythos

Release

datasette 1.0a33

This alpha is a significant step on the road to a stable 1.0, finally extending the

?_extra=

pattern I introduced

in Datasette 1.0a3

to cover queries and rows in addition to tables. That pattern is also

now documented

!

I wrote a whole lot more about the new release on the Datasette project blog:

Datasette 1.0a33 with JSON extras in the API

.

Because API explorer tools are almost free to build now I had Claude Fable 5 in Claude Code (for

the plan

) and GPT-5.5 xhigh in Codex Desktop (for

the implementation

) build me this

custom extras API explorer

to help demonstrate the feature:

11th Jun 2026, 3:26 pm

·

projects

,

annotated-release-notes

,

datasette

,

ai-assisted-programming

Tool

Datasette extras explorer

— Query Datasette JSON endpoints and discover available extras by entering a URL and selecting which extras to request. The interface displays the returned JSON response with syntax highlighting and allows you to examine which extras are supported by your Datasette instance, with support for sharing configurations via URL hash parameters.

11th Jun 2026, 3:10 pm

Release

asyncinject 0.7

I built this utility library to support an

asyncio

dependency injection pattern a few years ago. I was using it with Datasette and Claude Fable 5 spotted some bugs in the dependency which it then fixed for me. It's a very proactive model!

11th Jun 2026, 6:28 am

·

projects

,

async

,

claude-mythos

,

python

Research

Running untrusted queries: Datasette/SQLite vs psycopg/PostgreSQL

— Exploring how untrusted SQL queries are safely run in Datasette (using SQLite) and whether similar protections can be applied with psycopg and PostgreSQL, this project shows that both can provide robust safeguards against data corruption and resource exhaustion. Datasette leverages hard read-only file modes and a VM progress handler for query timeouts, while PostgreSQL's privilege system enforces SELECT-only access and its `statement_timeout` cancels resource-intensive or sleeping queries.

11th Jun 2026, 4:17 am

Highlights

sqlite-utils 4.0rc1 adds migrations and nested transactions

- June 21, 2026

Datasette Apps: Host custom HTML applications inside Datasette

- June 18, 2026

GLM-5.2 is probably the most powerful text-only open weights LLM

- June 17, 2026

Publishing WASM wheels to PyPI for use with Pyodide

- June 13, 2026

Claude Fable is relentlessly proactive

- June 11, 2026

Initial impressions of Claude Fable 5

- June 9, 2026

Running Python code in a sandbox with MicroPython and WASM

- June 6, 2026

Claude Opus 4.8: "a modest but tangible improvement"

- May 28, 2026

I think Anthropic and OpenAI have found product-market fit

- May 27, 2026

Notes on Pope Leo XIV's encyclical on AI

- May 25, 2026

Datasette Agent

- May 21, 2026

Gemini 3.5 Flash: more expensive, but Google plan to use it for everything

- May 19, 2026

The last six months in LLMs in five minutes

- May 19, 2026

Notes on the xAI/Anthropic data center deal

- May 7, 2026

Live blog: Code w/ Claude 2026

- May 6, 2026

Vibe coding and agentic engineering are getting closer than I'd like

- May 6, 2026

LLM 0.32a0  is a major backwards-compatible refactor

- April 29, 2026

Tracking the history of the now-deceased OpenAI Microsoft AGI clause

- April 27, 2026

DeepSeek V4 - almost on the frontier, a fraction of the price

- April 24, 2026

Extract PDF text in your browser with LiteParse for the web

- April 23, 2026

A pelican for GPT-5.5 via the semi-official Codex backdoor API

- April 23, 2026

Is Claude Code going to cost $100/month? Probably not - it's all very confusing

- April 22, 2026

Where's the raccoon with the ham radio? (ChatGPT Images 2.0)

- April 21, 2026

Changes in the system prompt between Claude Opus 4.6 and 4.7

- April 18, 2026

Join us at PyCon US 2026 in Long Beach - we have new AI and security tracks this year

- April 17, 2026

Qwen3.6-35B-A3B on my laptop drew me a better pelican than Claude Opus 4.7

- April 16, 2026

Meta's new model is Muse Spark, and meta.ai chat has some interesting tools

- April 8, 2026

Anthropic's Project Glasswing - restricting Claude Mythos to security researchers - sounds necessary to me

- April 7, 2026

The Axios supply chain attack used individually targeted social engineering

- April 3, 2026

Highlights from my conversation about agentic engineering on Lenny's Podcast

- April 2, 2026

Mr. Chatterbox is a (weak) Victorian-era ethically trained model you can run on your own computer

- March 30, 2026

Vibe coding SwiftUI apps is a lot of fun

- March 27, 2026

Experimenting with Starlette 1.0 with Claude skills

- March 22, 2026

Profiling Hacker News users based on their comments

- March 21, 2026

Thoughts on OpenAI acquiring Astral and uv/ruff/ty

- March 19, 2026

GPT-5.4 mini and GPT-5.4 nano, which can describe 76,000 photos for $52

- March 17, 2026

My fireside chat about agentic engineering at the Pragmatic Summit

- March 14, 2026

Perhaps not Boring Technology after all

- March 9, 2026

Can coding agents relicense open source through a “clean room” implementation of code?

- March 5, 2026

Something is afoot in the land of Qwen

- March 4, 2026

Monthly briefing

Sponsor me for

$10/month

and get a curated email digest of the month's most important LLM developments.

Pay me to send you less!

Sponsor & subscribe

Disclosures

Colophon

©

2002

2003

2004

2005

2006

2007

2008

2009

2010

2011

2012

2013

2014

2015

2016

2017

2018

2019

2020

2021

2022

2023

2024

2025

2026

*原文请访问 [simonwillison.net](https://simonwillison.net)*