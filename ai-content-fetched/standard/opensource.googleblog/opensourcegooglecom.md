---
title: **直接保留原文：**

`opensource.google.com`

**（URL/网址通常不翻译，保持原样）**

如果需要说明性翻译，可译为：**Google 开源项目网站**
source: opensource.googleblog.com
url: https://opensource.googleblog.com/2026/04
date: 2026-06-22
category: standard/opensource.googleblog
translated: true
fetched_at: 2026-06-22T20:18:05.990475
---
# **直接保留原文：**

`opensource.google.com`

**（URL/网址通常不翻译，保持原样）**

如果需要说明性翻译，可译为：**Google 开源项目网站**

**来源**: opensource.googleblog.com | **日期**: 2026-06-22

---


```
git clone https://github.com/GoogleCloudPlatform/activation-model-scanner.git
cd activation-model-scanner && pip install -e .

# Standard scan (3 concepts: harmful_content, injection_resistance, refusal_capability)
ams scan ./my-model

# Quick scan (2 concepts, ~40% faster)
ams scan ./my-model --mode quick

# Full scan (4 concepts including truthfulness)
ams scan ./my-model --mode full

# JSON output for CI/CD pipelines
ams scan ./my-model --json

```

```
jobs:
model-safety-check:
  runs-on: ubuntu-latest
  steps:
    - uses: actions/checkout@v3

    - name: Install AMS
      run: pip install ams-scanner[cli]

    - name: Scan model
      run: |
        ams scan ./model \
          --verify meta-llama/Llama-3-8B-Instruct \
          --json > scan-results.json

    - name: Upload results
      uses: actions/upload-artifact@v3
      with:
        name: ams-scan-results
        path: scan-results.json

```

```
# First, create a baseline from the official model
ams baseline create ./my-model

# Then verify an unknown model against it
ams scan ./suspicious-model --verify ./my-model

```

```
# Standard scan (3 concepts: harmful_content, injection_resistance, refusal_capability)
ams scan ./my-model

# Quick scan (2 concepts, ~40% faster)
ams scan ./my-model --mode quick

# Full scan (4 concepts including truthfulness)
ams scan ./my-model --mode full

# JSON output for CI/CD pipelines
ams scan ./my-model --json

```

```
from jax.ad_checkpoint import checkpoint_name 
 
def layer_name(x, w): 
  w1, w2 = w 
  x = checkpoint_name(x, "x") 
  y = x @ w1 
  return y @ w2, None  

```

```
policy = cp.save_and_offload_only_these_names( 
  names_which_can_be_saved=[],         # No values stored on device 
  names_which_can_be_offloaded=["x"],  # Offload activations labeled "x" 
  offload_src="device",                # Move from device memory 
  offload_dst="pinned_host"            # To pinned host memory 
) 

```

Posts from April 2026

The Journey Begins: Meet the 2026 GSoC Contributors!

Thursday, April 30, 2026

by
Stephanie Taylor
,
Mary Radomile
&
Lucila Ortíz
, Google Summer of Code

A warm welcome to the 1,141 Contributors of Google Summer of Code (GSoC) 2026! We are excited to start this new edition alongside our 184 mentoring orgs. Organizations reviewed a record-breaking 23,371 proposals to find the best matches for their communities.

2026 Application Statistics:

15,245 applicants from 131 countries submitting a total of 23,371 proposals
Over 2,000 mentors and org admins

What's Next?

Before the first line of code is written, there is
Community Bonding
. This 3.5-week GSoC tradition is about more than just tool configuration; it's about immersion. It's a dedicated space for Contributors to master the codebase, align with community standards, and understand the 'why' behind their projects. By the time the coding period begins, every Contributor is ready to turn project fundamentals into real-world impact.

The official coding period
begins on
May 25
. For our contributors, this period represents a deep dive into collaborative development, offering the chance to learn new tools and contribute to the heartbeat of open source projects.

Thank you, Mentors!

Finally, we want to express our deepest gratitude to our phenomenal
Mentors
and
Org Admins
. As AI profoundly shifts the landscape of open source communities, GSoC is no exception. Your patience, grit, and tireless volunteer efforts are the heartbeat of this program, ensuring its continued success as we welcome a new generation of contributors into the open source ecosystem.

Introducing AMS: Activation-based model scanner for open-weight LLM safety verification

Monday, April 27, 2026

by
Glen Messenger
, Google Kubernetes Engine (GKE)

The open-weight model ecosystem is thriving—and so is its shadow. A 2025 study identified over 8,000 safety-modified model repositories on Hugging Face alone, with modified models complying with unsafe requests at rates of 74% compared to 19% for their original instruction-tuned counterparts.

For organizations deploying open-weight models, a critical question emerges: how do you know the model you downloaded is safe to run?

We believe defensive security tools should be widely available. AMS represents our contribution to a safer AI ecosystem—one where developers everywhere can verify model integrity before deployment.

Today we're releasing
AMS (Activation-based Model Scanner)
, an open source tool that answers this question in 10–40 seconds—without sending a single prompt.

The Problem with Behavioral Testing

Traditional safety verification relies on behavioral testing: send harmful prompts, check if the model refuses. This approach has three fundamental limitations.

It's slow.
Comprehensive benchmarks like HarmBench require hundreds of queries. For organizations running continuous integration pipelines or screening large model registries, this can be impractical.

It's incomplete.
No benchmark covers every harmful behavior. Models can exhibit safe behavior on known test sets while remaining unsafe on novel or out-of-distribution prompts.

It's gameable.
Models can be fine-tuned to refuse benchmark prompts while complying with novel attacks—a known limitation of purely behavioral evaluation approaches.

A Structural Approach

AMS takes a different approach entirely. Instead of testing what a model says, it measures how a model thinks.

Safety training creates measurable geometric structure in a model's activation space. Instruction-tuned models develop internal "direction vectors"—representations that separate harmful content from benign content with high statistical confidence (4–8σ separation). When safety training is removed—through fine-tuning, abliteration, or training on unfiltered data—this geometric structure collapses.

AMS measures this collapse directly. The approach is grounded in recent research on representation engineering, which demonstrates that high-level concepts are encoded linearly in LLM activation space and can be reliably extracted via simple linear probes on intermediate-layer hidden states.

What AMS Detects

AMS operates as a two-tier scanner. Tier 1 measures whether safety-relevant activation structure exists at all—no baseline required. Tier 2 compares a model's activation fingerprint against a verified baseline to detect subtle modifications, including supply chain substitution.

In our validation across 14 model configurations:

Instruction-tuned models
(Llama, Gemma, Qwen) show 3.8–8.4σ separation—consistent with strong safety training
Uncensored variants
(Dolphin, Lexi) show collapsed separation at 1.1–1.3σ—flagged as CRITICAL
Abliterated models
show partial degradation at 3.3σ—flagged as WARNING
Base models
(no safety training) show 0.69σ—confirming the absence of safety structure
Quantized models
(INT4/INT8) show less than 5% separation drift—safe to scan production deployments

Use Cases

CI/CD Safety Gates

Integrate AMS into your model deployment pipeline to block unsafe models before they reach production. An example Github Actions workflow:

Supply Chain Verification

Confirm that downloaded weights match their claimed identity using Tier 2 fingerprint comparison.

Registry Screening

Automatically screen models at upload or download time to flag degraded safety structure before deployment.

How It Works

AMS processes a set of contrastive prompt pairs—examples that differ only in whether they contain harmful content—through the model under inspection. It extracts hidden states at an intermediate layer (typically 35–40% depth), computes a direction vector that separates the two classes, and measures class separation as a σ score.

The key insight is that this measurement requires no generation, no benchmark queries, and no ground-truth labels. The entire scan completes in a single forward pass per prompt pair, typically 10–40 seconds on GPU hardware.

The probe consists of a single direction vector (~16KB for standard 4096-dimensional models). No model weights are modified. The tool works with any Hugging Face-compatible model.

Get Started

AMS is available now under Apache 2.0:

GitHub:
github.com/GoogleCloudPlatform/activation-model-scanner/

We welcome contributions, baseline additions for new model families, and feedback from the communities. See the contributing guide in the repository for details.

Meet the A2Family

Thursday, April 23, 2026

by
Daryl Ducharme
, Google Open Source &
Alan Blount
, Cloud AI

At Google, we know that building on open source gives teams the freedom and flexibility to use meaningful technologies faster. Openness drives innovation and security, and it is core to our mission. As we look toward the future of computing, we want to ensure that developers across all open source communities have the foundational tools they need to build secure and collaborative AI systems.

That is why we are excited for you to get to know the "A2Family"—a suite of open source protocols and tools designed to help you build, connect, and scale your AI agents.

A2A: The cornerstone of agent interoperability

The
Agent2Agent (A2A) Protocol
is an open standard designed to enable seamless communication and collaboration between AI agents. It provides the definitive common language for agent interoperability in a world where agents are built using diverse frameworks and by different vendors.

Originally developed by Google, A2A has now been donated to the Linux Foundation. As a famous open source aphorism reminds us: "If you want to go fast, go alone. If you want to go far, go together." A2A brings this collaborative philosophy to AI, allowing agents to delegate sub-tasks, exchange information, and coordinate actions to solve complex problems that a single agent cannot.

MCP & Skills: Agents need tools and skills

Since day one A2A has loved MCP, and we love skills too ♥️.  Agents discover, negotiate, converse, make plans, adapt when those plans don't work out – that's a different interaction pattern than a tool and that's what A2A was built for.  But for your agents to function, they need access to tools, and instructions on how to use those tools safely and securely. While MCP and A2A might not be from the same origin story, they are a family that works better together.

When you're not sure – if it's a quick deterministic resource or action, it's a tool, but if you may end up with a conversation, it's an agent. Another good mental model is "are you the expert agent which uses tools" (MCP) or "is there some other expert agent you are collaborating with" (A2A).

A2UI: A protocol for agent-driven interfaces

When agents need to communicate with humans, how can they safely send rich interfaces across trust boundaries? Instead of relying on text-only responses or risky code execution, we use
A2UI
.

A2UI enables AI agents to generate rich, interactive user interfaces that render across web, mobile, and desktop platforms—without executing arbitrary code. It is secure by design, allowing agents to use only pre-approved components from your catalog through declarative component descriptions.

You may also have heard of
MCP Apps
(formerly MCP UI). It is a complementary alternative to A2UI which ships your agent driven widget inside of an iframe orchestrated with MCP events and tool calls.  There are some interesting ways of configuring A2UI and MCP Apps together, for generative UI inside of an iframe or generative UI driving the iframe.

The
AG UI protocol
, developed by CopilotKit, is a standard for connecting agents to front ends with low latency. It makes developer lives much easier, with integrations to most agent frameworks and front ends.  If you are using AG UI, you already have both A2UI and A2A support!

AP2: Securing the agent economy

When an autonomous agent initiates a payment, current systems struggle with questions of authorization, authenticity, and accountability. To solve this, we introduced the
Agent Payments Protocol (AP2)
, an open protocol for the emerging Agent Economy.

Available as an open extension for the A2A protocol, AP2 is designed to enable secure, reliable, and interoperable agent commerce for developers, merchants, and the payments industry. The protocol engineers trust into the system using verifiable digital credentials (VDCs), which are tamper-evident, cryptographically signed digital objects that serve as the building blocks of a transaction.

UCP: The common language for agentic commerce

While AP2 secures the transaction, the
Universal Commerce Protocol (UCP)
defines the building blocks for the entire shopping journey, from discovering and buying to post-purchase experiences. UCP provides a common language for platforms, agents, and businesses, allowing the diverse commerce ecosystem to interoperate through a single standard without the need for custom builds.

UCP seamlessly connects different systems using open industry standards, featuring built-in support for both the A2A and AP2 protocols. It empowers retailers to meet customers wherever they are, ensuring that businesses retain control of their own rules and remain the Merchant of Record with full ownership of the customer relationship.

Bringing it all together with ADK

Protocols need a solid foundation to run on. Enter the
Agent Development Kit (ADK)
.

Technically not part of the A2Family, ADK is an open-source agent development framework that lets you build, debug, and deploy reliable AI agents at enterprise scale. Available in Python, TypeScript, Go, and Java, ADK helps you build production agents, not just prototypes. It connects everything together, allowing you to easily equip your agents with tools, integrate them with the A2A protocol, and scale them globally on your infrastructure of choice.

Google champions collaboration, transparency, and shared progress to build a better future for everyone through open technologies. We are thrilled to share these tools with you and cannot wait to see what we can build together.

What kind of multi-agent workflows are you planning to build with the A2Family? Let us know in the comments below or tag us on social media!

A year of open collaboration: Celebrating the anniversary of A2A

Thursday, April 16, 2026

by
Patricia Cruz
, Google Open Source

One year ago, on April 9th, 2025 Google
announced the Agent2Agent(A2A) protocol
. We saw the need for a "common language" that allows AI agents built on different frameworks to collaborate well across diverse systems. Then, on June 23, 2025 at the Open Source Summit North America in Denver, Mike Smith stood on stage to share a pivotal moment for the future of AI interoperability when Google officially
donated the A2A protocol to the Linux Foundation
, establishing it as a vendor-neutral, community-governed standard.

This move was driven by a core belief: for AI agents to truly transform how we work and live, they must be able to communicate across framework boundaries and organizational silos without being locked into a single provider's ecosystem. By placing A2A under the neutral stewardship of the Linux Foundation, we opened the doors for the entire industry to build, contribute, and innovate together.

A Foundation of Partners

The formation of the A2A Project was made possible through the support of our founding members, including Amazon Web Services, Cisco, Microsoft, Salesforce, SAP, and ServiceNow. Over the past twelve months, this coalition has grown, with over 100 technology companies now supporting the project.

From Prototype to Production

The momentum since the donation has been remarkable. What began as a Google-led initiative has evolved into critical infrastructure for horizontal, peer-to-peer collaboration. Just one month ago, in March, the project reached a major milestone with the release of
A2A Protocol v1.0
, the first stable, fully production-ready version of the standard.

Key achievements from the community this year include:

Enhanced Security
: The implementation of Signed Agent Cards for cryptographic identity verification, ensuring trust in multi-agent workflows.
Web-Aligned Architecture
: Refined specifications that support familiar load-balancing and security patterns for enterprise-scale deployments.
Ecosystem Interoperability
: Demonstrating how diverse agents built with ADK, LangGraph, AG2 and CrewAI can delegate tasks and coordinate complex workflows seamlessly.
Experts teaching experts:
We have learned from our open collaboration and have
shared our knowledge
.

Looking Ahead

This flourishing ecosystem of agent protocols helps standardize how agents communicate, interact with the world, and solve real-world problems. The A2Family includes AP2 (Agent Payment Protocol), A2UI (Agent to User Interface), and UCP (Universal Commerce Protocol), which are examples of new protocols created using A2A's open extensibility model for agent communication.

As we celebrate this first anniversary, we are more committed than ever to the "A2Family." The A2A protocol is designed to be complementary to existing standards like the Model Context Protocol (MCP); while MCP manages internal tool integration, A2A handles the vital external coordination between autonomous entities.

We want to thank the vibrant ecosystem of developers, contributors, and partners who have helped harden this protocol into a world-class standard over the last year.

Join the A2April Celebration!

We're celebrating the first anniversary of A2A all month long with "A2April". You can join the fun by sharing a photo of yourself in the community using the hashtag #A2April. To help you get festive, we've put together a
commemorative party hat template
with full assembly instructions.

Here's to many more years of innovation and open collaboration!

Acknowledgements

Thank you to the following contributors: Mike Smith, Alan Blount, Kassandra Dhillon, Daryl Ducharme, and April Kyle Nassi

Jaspr: Why web development in Dart might just be a good idea

Wednesday, April 15, 2026

by
Kilian Schulte
, Netlight

Most developers know Dart as the language that powers Flutter, the multi-platform app framework. But the Dart ecosystem has so much more to offer. For example: Jaspr, a web framework that provides a familiar Flutter-like experience, but is made for building fast, SEO-friendly, and dynamic websites natively in Dart.

Dart on the web is not a new idea. Initially, Dart was designed to run natively in browsers, similar to JavaScript. Google even developed AngularDart, a pure-Dart version of the popular JS framework. And although this is no longer supported, it resulted in some surprisingly powerful web tooling for Dart.
Back in 2016
, teams at Google chose Dart for its strong type safety and excellent development experience, and it has only improved since then.

However, all of this was unknown to me when I started building Jaspr in 2022. As a web developer who had transitioned to Flutter, I had grown to love Dart and wanted to explore using it for web development. So Jaspr started as a personal challenge: What would a modern web framework look like if it was built entirely in Dart?

Creating Jaspr as an open source project has been one of the most challenging, but also rewarding journeys of my career. Starting out as a solo maintainer is definitely hard work, but it comes with absolute creative freedom. I can explore unconventional ideas, design APIs exactly how I envision them, and integrate modern features seen in other frameworks. All without being slowed down by processes or roadmaps. I poured more than three years of late nights and weekends into the framework. That dedication finally paid off in a way I had never imagined: Google selected Jaspr to completely rebuild and power the official Dart and Flutter websites.

Architecture & design

To understand how Jaspr actually works, let's look at its underlying design. Jaspr is primarily targeted at Flutter developers venturing into web development. Having a clearly defined niche like this greatly helped me shape the framework and prioritize features, while not getting spread too thin as a maintainer.

One of Jaspr's core design principles is that it should look and feel familiar to Flutter, while relying on native web technologies like HTML and CSS. This sets it apart from Flutter, which since 2021 can also target the web, but instead optimizes for rendering consistency between platforms. It relies fully on the Canvas API for rendering, which comes at the cost of slower loading times and lower SEO. Therefore, Jaspr is the missing piece for Flutter developers wanting to build fast and optimized websites with great SEO.

Jaspr results in a syntax that is remarkably close to Flutter's, and functionality that is much closer to something like React with an efficient, DOM-based rendering algorithm.

As you can see, Jaspr's
StatelessComponent
mirrors Flutter's
StatelessWidget
, but constructs HTML similar to React with JSX. Jaspr also provides a type-safe API for writing CSS rules directly in Dart.

Client-side rendering is only one aspect of what Jaspr can do. Jaspr is built as a full-stack general purpose framework supporting both Server-Side Rendering (SSR) and Static Site Generation (SSG). In the JavaScript ecosystem, you usually find a hard split between rendering libraries (React, Vue) and meta-frameworks (Next, Nuxt, Astro). Jaspr combines these concepts into one versatile and coherent framework.

In order to achieve this wide range of features with the limited resources I had, I naturally had to make compromises. Since I didn't want to limit the quality of any feature, my strategy focuses more on limiting features to what's important. I also learned to prioritize simple solutions and to design APIs that are flexible and composable.

For instance, I built
jaspr_content
as a plugin for developing content-driven sites from Markdown and other sources, similar to Astro or VitePress. It provides all the core features needed to build massive documentation websites, and instead of serving every use case out of the box, it is flexible and open enough to be fully customizable. In fact,
jaspr_content
is what currently powers the new
flutter.dev
and
dart.dev
documentation, which contain over 3,900 pages.

Tooling and developer experience

In my opinion, a framework is only as good as its tooling, and this is where Dart truly shines and has provided Jaspr developers with a great developer experience. For example, Flutter is known for its stateful hot-reload, enabling you to swap out code instantly without losing client-side state. But hot-reload is actually a
Dart
feature, enabled by its unique compiler architecture.

For browser development, the
dartdevc
compiler performs modular and incremental compilation to JavaScript. It supports stateful hot-reload and provides a seamless debugging experience. By cleverly leveraging source-maps, you can step through native Dart code right in the browser, complete with breakpoints, value inspection, and runtime expression evaluation.

For production builds, Dart uses the
dart2js
compiler to generate a heavily optimized, tree-shaken JavaScript bundle, or the newer
dart2wasm
compiler for even better runtime performance through WebAssembly. On the server side, Dart's JIT compiler provides that same hot-reload and debugging capabilities, while its AOT compiler compiles your server code to optimized, platform-specific, native binaries for production environments.

Jaspr builds on top of these and other capabilities, for example by giving developers full-stack debugging, custom lints and code assists, and something I call
component scopes
. This is a neat editor feature that adds inline hints to your components, showing whether they are rendered on the server, the client, or both. When building full-stack apps, this makes it much easier to reason about which platform APIs or libraries you can safely use in a specific file. I'm also working on more features to make the full-stack development aspect even smoother. For example, a full-stack hot-reload where on any server-side change, whether updating code or (for example), editing a markdown file, the new pre-rendered HTML is "hot-reloaded" into the page while keeping all client-side state. Features like these are only possible due to Jaspr's approach to combine both server- and client-side rendering into one framework.

Impact and outlook

Last year, Google selected Jaspr for the Dart and Flutter websites, including
dart.dev
,
flutter.dev
and
docs.flutter.dev
(
repo
), which is used by over a million monthly active users. The sites were migrated from JS- and python-based static site generators to Jaspr and
jaspr_content
, resulting in a unified setup with less context switching and an easier contribution experience. The move to Jaspr also streamlined the development of brand-new interactive tutorials on
dart.dev/learn
and
docs.flutter.dev/learn
. For me this is not only an incredible trust in the capabilities of Jaspr, but also a great way to dogfood Jaspr at scale; it allowed me to invest more time and resources into improving Jaspr.

With AI constantly shifting the scope of software development, I believe the concept of being a strict "domain expert" (a purely mobile or purely web developer) will matter less. However, developers and teams will increasingly value coherent tech stacks to reduce context-switching and leverage unified tooling. Just as React Native became massively popular because it allowed web developers to reuse their skills for mobile (or for companies to "reuse" their developers), Jaspr is a great option for teams working with both Flutter and the web. Apart from using existing skills, Jaspr and Flutter projects can also share up to 100% of their business logic, models, and validation code.

Dart's type safety and high-quality tooling position it well for modern web development. Jaspr evolved to be the missing piece, a cohesive framework with modern features and a great development experience.

I personally see Jaspr as an antithesis to the trend of AI causing everyone to converge onto the same stack, especially in web development. While this also has some benefits, I believe there is immense value in exploring alternative ecosystems. This can push boundaries, surface new ideas, and keep our industry vibrant.

If there's one takeaway from my journey, it's this: Don't be afraid to build the tools you want to use. You never know where that codebase will take you, and it can be incredibly rewarding.

If you're a Dart or Flutter developer curious about building websites with the skills you already have, there's never been a better time to start. Try out Jaspr now on its
online playground
(which is also built with Jaspr!) or by following the
Jaspr quickstart
.

Learn more about Flutter's migration in
We rebuilt Flutter's websites with Dart and Jaspr
.

Oh, and if you're wondering where the name "Jaspr" came from — it's named after my dog, Jasper. If you ever find yourself wandering around
jaspr.site
and want to
Meet Jasper
, keep an eye out… you just might find a little easter egg tribute to him.

Leveraging CPU memory for faster, cost-efficient TPU LLM training

Friday, April 10, 2026

by
Keyur Ruganathbhai Ranipa
,
Qinglan Xiang
,
Vrushabh Sanghavi
,
Ramesh AG
&
Weilin Wang
, Intel
and
Penporn Koanantakool
, Google

Host offloading with JAX on Intel® Xeon® processors

As Large Language Models (LLMs) continue to scale into the hundreds of billions of parameters, device memory capacity has become a big limiting factor in training, as intermediate activations from every layer in the forward pass are needed in the backward pass. To reduce device memory pressure, these activations can be rematerialized during the backward pass, trading memory for recomputation. While rematerialization enables larger models to fit within limited device memory, it significantly increases training time and cost.

Intel® Xeon® processors (5th and 6th Gen) with Advanced Matrix Extensions (AMX) enable practical host offloading of selected memory- and compute-intensive components in JAX training workflows. This approach can help teams train larger models, relieve accelerator memory pressure, improve end-to-end throughput, and reduce total cost of ownership—particularly on TPU-based Google Cloud instances.

By publishing these results and implementation details, Google and Intel aim to promote transparency and share practical guidance with the community. This post describes how to enable activation offloading for JAX on TPU platforms and outlines considerations for building scalable, cost-aware hybrid CPU–accelerator training workflows.

Host offloading

Traditional LLM training is usually done on device accelerators alone. However, modern host machines have much larger memory size than accelerators (512GB or more) and can offer extra compute power, e.g., TFLOPS in case of Intel® Xeon® Scalable Processor with AMX capability. Leveraging host resources can be a great alternative to rematerialization.
Host offloading
selectively moves computation or data between host and device to optimize performance and memory usage.

Host memory offloading
keeps frequently-accessed tensors on the device and spills the rest to CPU memory as an extra level of cache.
Activation offloading
transfers activations computed on-device in the forward pass to the host, stores them in the host memory, and brings them back to the device in the backward pass for gradient computation. This unlocks the ability to train larger models, use bigger batch sizes, and improve throughput.

In this blog post, we provide a practical guide to offload activations through JAX to efficiently train larger models on TPUs with an Intel® Xeon® Scalable Processor.

Enabling memory offloading in JAX

JAX offers
multiple strategies
for offloading activations, model parameters, and optimizer states to the host. Users can use
checkpoint_names()
to create a checkpoint for a tensor. The snippet below shows how to create a checkpoint
x
:

Users can provide
checkpoint_policies()
to select the appropriate memory optimization strategy for intermediate values. There are three strategies:

Recomputing during backward pass (default behavior)
Storing on device
Offloading to host memory after forward pass and loading back during backward pass

The code below moves
x
from device to the pinned host memory after the forward pass.
from jax import checkpoint_policies as cp

Measuring Host Offloading Benefits on TPU v5p

We examined TPU host-offloading on JAX on both fine-tuning and training workloads. All our experiments were run on Google Cloud Platform, using a single
v5p-8 TPU
instance with single host 4th Gen Intel® Xeon® Scalable Processor.

Fine-tuning PaliGemma2
: Using the base PaliGemma2 28B model for vision-language tasks, we
fine-tuned
the attention layers of the language model (Gemma2 27B) while keeping all other parameters frozen. During fine-tuning, we set the LLM sequence length to 256 and the batch size to 256.

The default checkpoint policy is
nothing_saveable
, which does not keep any activations on-device during the forward pass. The activations are rematerialized during the backward pass for gradient computation. While this approach reduces memory pressure on the TPU, it increases compute time. To apply host offloading, we offload Q, K, and V projection weights using
save_and_offload_only_these_names
. These activations are transferred to host memory (D2H) during the forward pass and fetched back during the backward pass (H2D), so the device neither stores nor recomputes them. Figure 2 shows 10% reduction in training time from host offloading. This translates directly into a similar reduction in TPU core-hours, yielding meaningful cost savings. The complete fine-tuning recipe is available at [
JAX host offloading
].

Training Llama2-13B using MaxText:
MaxText
offers several
rematerialization strategies
that can be specified in the training configuration file. We used the policy
remat_policy: 'qkv_proj_offloaded'
to offload Q, K, and V projection weights. Figure 3 shows ~5% reduction in per-step training time compared to fully rematerializing all activations (
remat_policy: 'full'
).

When to offload activations

Activation offloading is beneficial when the time to transfer activations across host and device is lower than the time to recompute them. The timing depends on multiple factors such as PCIe bandwidth, model size, batch size, sequence length, activation tensor sizes, compute capabilities of the device, etc. An additional factor is how much the data movement can be overlapped with computation to keep the device busy.  Figure 4 demonstrates an efficient overlap of the device-to-host transfer with compute during the backward pass in PaliGemma2 28B training.

Smaller model variants such as PaliGemma2 3B and 9B did not see benefits from host offloading because it is faster to rematerialize all tensors than to transfer them to and from the host. Therefore, identifying the appropriate workload and offloading policy is crucial to realizing performance gain from host offloading

Call to Action

If you train on TPUs and are limited by device memory, consider evaluating activation offloading. Start by labeling candidate activations (for example, Q/K/V projections) and compare step time, memory headroom, and overall cost across representative workloads.

In our experiments, we observed up to ~10% improvement in end-to-end training time for larger workloads, which can reduce total cost of ownership (TCO) by shortening time-to-train or enabling the same workload on smaller instances.

Acknowledgments

Emilio Cota, and Karlo Basioli from Google and Eugene Zhulenev (formerly at Google).

Celebrate A2April!

Thursday, April 9, 2026

by
Patricia Cruz
&
Daryl Ducharme
, Google Open Source

Happy 1st Birthday to A2A! Join the community in celebrating the first anniversary of the A2A and
its recent 1.0 release
. April 9th marks the
official birthday
, and we're celebrating all month long with
#A2April
. To help you celebrate, we've used Gemini to make a party hat.

Use the template and instructions below to create your commemorative party hat.

Assembly Instructions

Print:
Print this document on heavy cardstock for the best results.
Cut:
Carefully cut along the solid outer border of the semi-circle template.
Fold:
Gently curve the template into a cone shape, overlapping the "Glue/Tape Tab" underneath the opposite edge.
Secure:
Use double-sided tape or a glue stick along the tab to hold the cone shape.
Finish:
Punch two small holes on opposite sides of the base and thread through an elastic string or ribbon to secure the hat to your head.

Party Hat Visualization

Ways to Celebrate

Social Media:
Share a photo of yourself wearing your hat with the tag #A2April to help generate that social media buzz.
Blog Series:
Keep an eye out for the upcoming A2April blog series featuring quotes from the team and stories from the open source community.
Community Quotes:
If you're using A2A in production, reach out to us via social media and share your story for the birthday post.

Kubernetes goes AI-First: Unpacking the new AI conformance program

Monday, April 6, 2026

by
Duncan Campbell
,
Kaslin Fields
, Developer Source & Signal
&
Janet Kuo
,
Federico Bongiovanni
, Google Kubernetes Engine(GKE)

As AI workloads move from experimental notebooks into massive production environments, the industry is rallying around a new standard to ensure these workloads remain portable, reliable, and efficient.

At the heart of this shift is the launch of the
Certified Kubernetes AI Conformance program
.

This initiative represents a significant investment in common, accessible, industry-wide standards, ensuring that the benefits of AI-first Kubernetes are available to everyone.

Traditional Kubernetes was built for stateless, cloud-first applications. However, AI workloads introduce unique complexities that standard conformance doesn't fully cover:

Specific Hardware Demands:
AI models require precise control over accelerators like GPUs and TPUs.
Networking and Latency:
Inference and distributed training require low-latency networking and specialized configurations.
Stateful Nature:
Unlike traditional web apps, AI often relies on complex, stateful data pipelines.

The AI Conformance program acts as a
superset
of standard Kubernetes conformance. To be AI-conformant, a platform must first pass all standard Kubernetes tests and then meet additional requirements specifically for AI.

Key Pillars of the AI Conformance Program

The Kubernetes AI Conformance program is being driven in the open via the
AI Conformance
program. This cross-company effort is led by industry experts Janet Kuo (Google), Mario Fahlandt (Kubermatic GmbH), Rita Zhang (Microsoft), and Yuan Tang (RedHat). This program is a collaborative effort within the open source ecosystem, involving multiple organizations and individuals. By developing this program in the open, the community ensures the standard is built on trust and directly addresses the diverse needs of the global ecosystem. The program establishes a verified set of capabilities that platforms across the industry, like Google Kubernetes Engine (GKE) and Azure Kubernetes Service (AKS) are already adopting.

Dynamic Resource Allocation (DRA)

DRA
is the cornerstone of the new standard. It shifts resource allocation from simple accelerator quantity to fine-grained hardware control via attributes. For data scientists, this means they can now request specific hardware based on characteristics such as memory capacity or specialized capabilities, ensuring the environment perfectly matches the model's needs.

All-or-Nothing Scheduling

Distributed training jobs often face "deadlocks" where some pods start while others wait for resources, wasting expensive GPU time. AI Conformance mandates support for solutions like
Kueue
, allowing developers to ensure a job only begins when
all
required resources are available, improving cluster efficiency.

Intelligent Autoscaling for AI Workloads

Conformant clusters must support
Horizontal Pod Autoscaling (HPA)
based on custom AI metrics, such as GPU or TPU utilization, rather than just standard CPU/memory. This allows clusters to scale up for heavy inference demand and scale down to save costs when idle.

Standardized Observability for High Performance

To manage AI at scale, you need deep visibility. The program requires platforms to expose rich accelerator performance metrics directly, enabling teams to monitor inference latency, throughput, and hardware health in a standardized way.

What's Next?

The launch of AI Conformance is just the beginning. As we head further into 2026, the community is adding
automated testing
for certification and expanding the standard to include more advanced inference patterns and stricter security requirements.

The ultimate goal? Making "AI-readiness" an inherent, invisible part of the Kubernetes standard.

To get involved and help shape the future of AI on Kubernetes, consider joining
AI Conformance in Open Source Kubernetes
. We welcome diverse perspectives, as your expertise and feedback are crucial to building a robust and inclusive standard for all.

Gemma 4: Expanding the Gemmaverse with Apache 2.0

Thursday, April 2, 2026

by
Nia Castelly
&
amanda casari
, Google Open Source &
Olivier Lacombe
, Google DeepMind

Gemma 4: Expanding the Gemmaverse with Apache 2.0

For over 20 years, Google has maintained an unwavering commitment to the open-source community. Our belief has been simple: open technology is
good for our company, good for our users, and good for our world
. This commitment to fostering collaborative learning and rigorous testing has consistently proven more effective than pursuing isolated improvements. It's been our approach ever since the 2005 launch of
Google Summer of Code
, and through our open-sourcing of
Kubernetes
,
Android
, and
Go
, and it remains central to our ongoing, daily work alongside maintainers and organizations.

Today, we are taking a significant step forward in that journey. Since first launch, the community has downloaded Gemma models over 400 million times and built a vibrant universe of over 100,000 inspiring variants, known in the community as the
Gemmaverse
.

The
release of Gemma 4
under the
Apache 2.0 license
— our most capable open models ranging from edge devices to 31B parameters — provides cutting-edge AI models for this community of developers. The industry-standard Apache license broadens the horizon for Gemma 4's applicability and usefulness, providing well-understood terms for modification, reuse, and further development.

A long legacy of open research

We are committed to making helpful, accessible AI technology and research so that everyone can innovate and grow. That's why many of our innovations are freely available, easy to deploy, and useful to developers across the globe. We have a long history of making our foundational machine-learning research, including
word2vec
,
Jax
, and the seminal
Transformers paper
, publicly available for anyone to use and study.

We accelerated this commitment last year. By sharing models that
interpret complex genomic data
and
identify tumor variants
, we contributed to the "
magic cycle
" of research breakthroughs that translate into real-world impact. This week, however, marks a pivotal moment —
Gemma 4 models are the first in the Gemmaverse to be released under the OSI-approved Apache 2.0 license.

Empowering developers and researchers to deliver breakthrough innovations

Since we first launched Gemma in 2024, the community of early adopters has grown into a vast ecosystem of builders, researchers, and problem solvers. Gemma is already supporting sovereign digital infrastructure, from automating
state licensing in Ukraine
to scaling
Project Navarasa across India's 22 official languages
. And we know that developers need autonomy, control, and clarity in licensing for further AI innovation to reach its full potential.

Gemma 4 brings three essential elements of free and open-source software directly to the community:

Autonomy:
By letting people build on and modify the Gemma 4 models, we are empowering researchers and developers with the freedom to advance their own breakthrough innovations however they see fit.
Control:
We understand that many developers require precise control over their development and deployment environments. Gemma 4 allows for local, private execution that doesn't rely on cloud-only infrastructure.
Clarity:
By applying the industry-standard Apache 2.0 license terms, we are providing clarity about developers' rights and responsibilities so that they can build freely and confidently from the ground up without the need to navigate prescriptive terms of service.

Building together to drive real-world impact

Gemma 4, as a release, is an invitation. Whether you are
a scientific researcher exploring the language of dolphins
, an industry developer building the next generation of open AI agents, or a public institution looking to provide more effective, efficient, and localized services to your citizens, Google is excited to continue building with you. The Gemmaverse is your playground, and with Apache 2.0, the possibilities are more boundless than ever.

We can't wait to see what you build.

Search This Blog

Popular Posts

The Journey Begins: Meet the 2026 GSoC Contributors!
Journey to JPEG XL: How open source experiments shaped the future of image coding
A new pkg.go.dev API for Go
Announcing Apache Iceberg 1.11.0
Introducing AMS: Activation-based model scanner for open-weight LLM safety verification

Archive

▼
2026
(35)
►
June
(8)
►
May
(3)
▼
April
(9)
The Journey Begins: Meet the 2026 GSoC Contributors!
Introducing AMS: Activation-based model scanner fo...
Meet the A2Family
A year of open collaboration: Celebrating the anni...
Jaspr: Why web development in Dart might just be a...
Leveraging CPU memory for faster, cost-efficient T...
Celebrate A2April!
Kubernetes goes AI-First: Unpacking the new AI con...
Gemma 4: Expanding the Gemmaverse with Apache 2.0
►
March
(5)
►
February
(5)
►
January
(5)

►
June
(8)

►
May
(3)

▼
April
(9)
The Journey Begins: Meet the 2026 GSoC Contributors!
Introducing AMS: Activation-based model scanner fo...
Meet the A2Family
A year of open collaboration: Celebrating the anni...
Jaspr: Why web development in Dart might just be a...
Leveraging CPU memory for faster, cost-efficient T...
Celebrate A2April!
Kubernetes goes AI-First: Unpacking the new AI con...
Gemma 4: Expanding the Gemmaverse with Apache 2.0

The Journey Begins: Meet the 2026 GSoC Contributors!
Introducing AMS: Activation-based model scanner fo...
Meet the A2Family
A year of open collaboration: Celebrating the anni...
Jaspr: Why web development in Dart might just be a...
Leveraging CPU memory for faster, cost-efficient T...
Celebrate A2April!
Kubernetes goes AI-First: Unpacking the new AI con...
Gemma 4: Expanding the Gemmaverse with Apache 2.0

►
March
(5)

►
February
(5)

►
January
(5)

►
2025
(47)
►
December
(6)
►
November
(5)
►
October
(3)
►
September
(5)
►
August
(5)
►
July
(5)
►
June
(3)
►
May
(5)
►
April
(1)
►
March
(1)
►
February
(3)
►
January
(5)

►
December
(6)

►
November
(5)

►
October
(3)

►
September
(5)

►
August
(5)

►
July
(5)

►
June
(3)

►
May
(5)

►
April
(1)

►
March
(1)

►
February
(3)

►
January
(5)

►
2024
(39)
►
December
(4)
►
November
(1)
►
October
(1)
►
September
(3)
►
August
(4)
►
July
(4)
►
June
(4)
►
May
(5)
►
April
(4)
►
March
(2)
►
February
(6)
►
January
(1)

►
December
(4)

►
November
(1)

►
October
(1)

►
September
(3)

►
August
(4)

►
July
(4)

►
June
(4)

►
May
(5)

►
April
(4)

►
March
(2)

►
February
(6)

►
January
(1)

►
2023
(44)
►
December
(5)
►
November
(6)
►
October
(2)
►
September
(3)
►
August
(1)
►
July
(2)
►
June
(5)
►
May
(5)
►
April
(2)
►
March
(6)
►
February
(3)
►
January
(4)

►
December
(5)

►
November
(6)

►
October
(2)

►
September
(3)

►
August
(1)

►
July
(2)

►
June
(5)

►
May
(5)

►
April
(2)

►
March
(6)

►
February
(3)

►
January
(4)

►
2022
(44)
►
December
(4)
►
November
(2)
►
October
(7)
►
September
(6)
►
August
(2)
►
July
(3)
►
June
(5)
►
May
(1)
►
April
(2)
►
March
(4)
►
February
(5)
►
January
(3)

►
December
(4)

►
November
(2)

►
October
(7)

►
September
(6)

►
August
(2)

►
July
(3)

►
June
(5)

►
May
(1)

►
April
(2)

►
March
(4)

►
February
(5)

►
January
(3)

►
2021
(55)
►
December
(3)
►
November
(7)
►
October
(4)
►
September
(7)
►
August
(5)
►
June
(2)
►
May
(2)
►
April
(6)
►
March
(6)
►
February
(8)
►
January
(5)

►
December
(3)

►
November
(7)

►
October
(4)

►
September
(7)

►
August
(5)

►
June
(2)

►
May
(2)

►
April
(6)

►
March
(6)

►
February
(8)

►
January
(5)

►
2020
(83)
►
December
(7)
►
November
(6)
►
October
(7)
►
September
(5)
►
August
(13)
►
July
(1)
►
June
(7)
►
May
(9)
►
April
(5)
►
March
(13)
►
February
(5)
►
January
(5)

►
December
(7)

►
November
(6)

►
October
(7)

►
September
(5)

►
August
(13)

►
July
(1)

►
June
(7)

►
May
(9)

►
April
(5)

►
March
(13)

►
February
(5)

►
January
(5)

►
2019
(65)
►
December
(6)
►
November
(9)
►
October
(8)
►
September
(5)
►
August
(3)
►
July
(5)
►
June
(4)
►
May
(8)
►
April
(3)
►
March
(7)
►
February
(4)
►
January
(3)

►
December
(6)

►
November
(9)

►
October
(8)

►
September
(5)

►
August
(3)

►
July
(5)

►
June
(4)

►
May
(8)

►
April
(3)

►
March
(7)

►
February
(4)

►
January
(3)

►
2018
(59)
►
December
(4)
►
November
(2)
►
October
(3)
►
September
(2)
►
August
(10)
►
July
(2)
►
June
(3)
►
May
(5)
►
April
(1)
►
March
(16)
►
February
(3)
►
January
(8)

►
December
(4)

►
November
(2)

►
October
(3)

►
September
(2)

►
August
(10)

►
July
(2)

►
June
(3)

►
May
(5)

►
April
(1)

►
March
(16)

►
February
(3)

►
January
(8)

►
2017
(73)
►
December
(4)
►
November
(5)
►
October
(6)
►
September
(7)
►
August
(3)
►
July
(3)
►
June
(3)
►
May
(5)
►
April
(4)
►
March
(13)
►
February
(7)
►
January
(13)

►
December
(4)

►
November
(5)

►
October
(6)

►
September
(7)

►
August
(3)

►
July
(3)

►
June
(3)

►
May
(5)

►
April
(4)

►
March
(13)

►
February
(7)

►
January
(13)

►
2016
(85)
►
December
(9)
►
November
(13)
►
October
(13)
►
September
(8)
►
August
(9)
►
July
(5)
►
June
(2)
►
May
(5)
►
April
(3)
►
March
(7)
►
February
(7)
►
January
(4)

►
December
(9)

►
November
(13)

►
October
(13)

►
September
(8)

►
August
(9)

►
July
(5)

►
June
(2)

►
May
(5)

►
April
(3)

►
March
(7)

►
February
(7)

►
January
(4)

►
2015
(80)
►
December
(5)
►
November
(7)
►
October
(6)
►
September
(6)
►
August
(4)
►
July
(1)
►
June
(6)
►
May
(6)
►
April
(10)
►
March
(10)
►
February
(11)
►
January
(8)

►
December
(5)

►
November
(7)

►
October
(6)

►
September
(6)

►
August
(4)

►
July
(1)

►
June
(6)

►
May
(6)

►
April
(10)

►
March
(10)

►
February
(11)

►
January
(8)

►
2014
(104)
►
December
(6)
►
November
(12)
►
October
(7)
►
September
(8)
►
August
(9)
►
July
(7)
►
June
(10)
►
May
(8)
►
April
(8)
►
March
(11)
►
February
(8)
►
January
(10)

►
December
(6)

►
November
(12)

►
October
(7)

►
September
(8)

►
August
(9)

►
July
(7)

►
June
(10)

►
May
(8)

►
April
(8)

►
March
(11)

►
February
(8)

►
January
(10)

►
2013
(100)
►
December
(7)
►
November
(10)
►
October
(8)
►
September
(9)
►
August
(10)
►
July
(7)
►
June
(7)
►
May
(8)
►
April
(10)
►
March
(9)
►
February
(7)
►
January
(8)

►
December
(7)

►
November
(10)

►
October
(8)

►
September
(9)

►
August
(10)

►
July
(7)

►
June
(7)

►
May
(8)

►
April
(10)

►
March
(9)

►
February
(7)

►
January
(8)

►
2012
(93)
►
December
(4)
►
November
(6)
►
October
(9)
►
September
(8)
►
August
(8)
►
July
(5)
►
June
(7)
►
May
(10)
►
April
(5)
►
March
(15)
►
February
(9)
►
January
(7)

►
December
(4)

►
November
(6)

►
October
(9)

►
September
(8)

►
August
(8)

►
July
(5)

►
June
(7)

►
May
(10)

►
April
(5)

►
March
(15)

►
February
(9)

►
January
(7)

►
2011
(117)
►
December
(7)
►
November
(14)
►
October
(13)
►
September
(10)
►
August
(6)
►
July
(13)
►
June
(11)
►
May
(5)
►
April
(11)
►
March
(10)
►
February
(10)
►
January
(7)

►
December
(7)

►
November
(14)

►
October
(13)

►
September
(10)

►
August
(6)

►
July
(13)

►
June
(11)

►
May
(5)

►
April
(11)

►
March
(10)

►
February
(10)

►
January
(7)

►
2010
(123)
►
December
(9)
►
November
(12)
►
October
(10)
►
September
(14)
►
August
(10)
►
July
(7)
►
June
(10)
►
May
(11)
►
April
(14)
►
March
(13)
►
February
(8)
►
January
(5)

►
December
(9)

►
November
(12)

►
October
(10)

►
September
(14)

►
August
(10)

►
July
(7)

►
June
(10)

►
May
(11)

►
April
(14)

►
March
(13)

►
February
(8)

►
January
(5)

►
2009
(124)
►
December
(6)
►
November
(5)
►
October
(11)
►
September
(11)
►
August
(8)
►
July
(13)
►
June
(6)
►
May
(11)
►
April
(16)
►
March
(17)
►
February
(10)
►
January
(10)

►
December
(6)

►
November
(5)

►
October
(11)

►
September
(11)

►
August
(8)

►
July
(13)

►
June
(6)

►
May
(11)

►
April
(16)

►
March
(17)

►
February
(10)

►
January
(10)

►
2008
(167)
►
December
(10)
►
November
(11)
►
October
(13)
►
September
(16)
►
August
(12)
►
July
(20)
►
June
(14)
►
May
(21)
►
April
(16)
►
March
(17)
►
February
(17)

►
December
(10)

►
November
(11)

►
October
(13)

►
September
(16)

►
August
(12)

►
July
(20)

►
June
(14)

►
May
(21)

►
April
(16)

►
March
(17)

►
February
(17)

Share


*原文请访问 [opensource.googleblog.com](https://opensource.googleblog.com/2026/04)*