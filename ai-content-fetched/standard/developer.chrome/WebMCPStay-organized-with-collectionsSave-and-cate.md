---
title: **Chinese translation:**

WebMCP 使用集合保持井井有条。根据您的偏好保存并分类内容。
source: developer.chrome.com
url: https://developer.chrome.com/docs/ai/webmcp
date: 2026-06-22
category: standard/developer.chrome
translated: true
fetched_at: 2026-06-22T17:37:48.828013
---
# **Chinese translation:**

WebMCP 使用集合保持井井有条。根据您的偏好保存并分类内容。

**来源**: developer.chrome.com | **日期**: 2026-06-22

---


Home
Docs
AI on Chrome
WebMCP

Alexandra Klepper
GitHub
Bluesky

Published: May 18, 2026, Last updated: June 9, 2026

Published: May 18, 2026, Last updated: June 9, 2026

WebMCP
is a
proposed web standard to help you build and expose structured tools for AI
agents
. WebMCP provides JavaScript and
annotates HTML form elements so that agents know exactly how to interact with
page features, to support a user's experience. This can significantly improve
the performance and reliability of agent actuation.

AI agents are a newer technology. They can help human users better complete
tasks which are highly complex and technical. WebMCP offers higher accuracy for
agentic task completion, and it can be added as a progressive enhancement.

Explainer
Web
Extensions
Chrome Status
Intent
GitHub
Origin trial
View
Intent to Experiment

Why WebMCP?

WebMCP can help you bridge the gap between web applications and agents,
improving efficiency, reliability, and task completion, by providing rules for
interaction. Instead of an agent reviewing the element, such as a button or a
field, to understand its purpose, the website declares the element's purpose,
so it's used correctly

This is more reliable than actuation, which may have numerous steps and leaves
each step open to interpretation by the agent.

Websites can share explicit purpose, such as search or purchasing, by defining
a
tool
. Tools execute on your webpage visibly, so users gain trust
that tasks are completed as expected. This also keeps your brand and
human-centered design choices intact.

WebMCP supports:

Discovery
: A standard way for pages to register tools with agents, such
as
checkout
or
filter_results
.
JSON Schemas
: Explicit definitions of inputs and expected outputs, to reduce hallucination or misunderstanding.
State
: A shared understanding of the current page context, so the agent knows what resources are available to act on in real time.

Our goal is to build APIs that any browser with agentic capabilities can
implement and benefit from, so your users can more easily complete tasks. You
can follow along this process on
GitHub
.

Use cases

There are many ways you could use WebMCP on the web. For example:

Help your customers get support
. If you provide a software to customers, you may have a complex support flow to address many different questions. You can use WebMCP to help an agent more quickly navigate to the right form and fill in fields with user-provided information.
Improve travel booking
. Help agents book complex, multi-city and multi-passenger trips with fewer steps.

Some actions may be sensitive, such as making a purchase. You can include a
command to request user interaction with a confirmation dialog.

In a practical sense, your tools could accomplish the following tasks:

Fill in structured forms
: Build a
submit_application
tool to help agents map data collected from the conversation with the user to form fields correctly. For example, you can differentiate if a field requires a full name versus a separate first and last name.
Support agent interactions in human-first interfaces
: Certain fields are
designed for human users, but may not be understood by agents. You could build
a
date_pick
tool that allows for a complex date and time selection in a
reservation or event booking.
Quicker application debugging
: You can build a
run_diagnostics
tool on a
developer settings page, so an agent can trigger fixes that are otherwise
hidden behind nested menus.

Is your use case missing? Or do you have an idea you're excited to share for
WebMCP? Join the
early preview program
and share your feedback.

Get started

Join the
WebMCP origin trial
from Chrome 149. Learn more about how to
get started with origin trials
.

Local WebMCP

WebMCP is available as a Chrome flag for local development:

Open Chrome and navigate to
chrome://flags/#enable-webmcp-testing
Set the flag to
Enabled
.
Relaunch Chrome to apply the changes.

Use WebMCP APIs

There are two APIs you can use to set up your website tools:

Imperative API
: Define different types of
tools with standard JavaScript, such as form input, navigation tools, state
management, or other functions.
Declarative API
: Add annotations to a standard
HTML forms to create a WebMCP tool.

Limitations

While WebMCP aims to make complex tasks simpler for agents and humans, there are
some limitations:

Browsing context required
: As tool calls are handled in JavaScript,
a browser tab or a webview must be opened to provide a visible interface and
browser context. In other words, there is no support for agents or assistive
tools to call tools in a headless state.
More overhead for complex interfaces
: If your site is highly complex, you
likely need to refactor or add JavaScript to handle application and interface state.
Tool discoverability
: Clients and browsers must visit a site directly to
know if it has callable tools.

Security and permissions

WebMCP APIs are gated by both origin isolation requirements and permissions
policy.

Origin isolation

WebMCP is only available in
origin-isolated
documents. This ensures that the document's origin remains stable throughout
the tool's lifetime.

If a document has
document.domain
enabled (for example, by using the
Origin-Agent-Cluster: ?0
HTTP header), WebMCP APIs are disabled.

Permissions policy

Both APIs are gated by the
tools
Permissions Policy
.
The policy defaults to
self
, which allows tool registration in top-level and
same-origin contexts, and disables it for cross-origin iframes.

To allow WebMCP tools in a cross-origin iframe, add the
allow="tools"
attribute to the iframe.

Demo

Examples of demos covering both imperative and declarative implementations are
available:

WebMCP zaMaker
uses the WebMCP Imperative API.
Travel demo (React)
uses the WebMCP Imperative API.
Le Petit Bistro demo
uses the WebMCP Declarative API.

You can also review and explore the demo source code on
GitHub
.

Imitate agent chat with the inspector extension

Install the Model Context Tool Inspector Extension
to experiment with an agent and see how WebMCP tools work in live demos or your
own applications. Use natural language prompts to determine if the agent
interacts with WebMCP tools as expected.

With the extension, you can:

See which tools are registered on a page, by monitoring the WebMCP API.
Manually call tools and execute functions.
Verify your JSON Schema is correctly defined and that the browser can parse
data as the tool expects.
View structured output or error messages returned by your tool to ensure
they're written clearly and formatted correctly, so an agent can understand it.

Talk to the agent using natural language, to see if it can correctly identify
and invoke the appropriate WebMCP tools. Your prompts are sent by default to the
gemini-3-flash-preview
model.

Engage and share feedback

WebMCP is under active discussion and subject to change in the future. If you
try these APIs and have feedback, we'd love to hear it.

Read the WebMCP explainer
,
raise questions and participate in discussion.
Join the
WebMCP origin trial
Read
WebMCP best practices
.
Review the implementation for Chrome on
Chrome Status
.
Read our
WebMCP tool security guidance
and
best practices
.
Join the early preview program
for an early look at new APIs and access to our mailing list.
If you have feedback on Chrome's implementation, file a
Chromium bug
.

Except as otherwise noted, the content of this page is licensed under the
Creative Commons Attribution 4.0 License
, and code samples are licensed under the
Apache 2.0 License
. For details, see the
Google Developers Site Policies
. Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-09 UTC.


*原文请访问 [developer.chrome.com](https://developer.chrome.com/docs/ai/webmcp)*