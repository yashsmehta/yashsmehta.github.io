---
layout: post
title: "Y Combinator AI Startup School"
date: 2025-06-25 10:00:00
description: "My learnings from 2 days in the Bay area for YC's AI Startup School, on topics like agency, team building, and the future of AI."
tags: [AI, startups]
categories: general
---

Y Combinator hosted its inaugural AI Startup School on June 16-17 in San Francisco, bringing together about 2,500 ambitious students from across the globe. Initially, I questioned the value of enduring jet lag and a long flight from Tokyo for just a two-day conference. But in retrospect, it was absolutely worth it. Beyond the impressive lineup—Gary Tan, Sam Altman, Jared Kaplan, John Jumper, Andrej Karpathy, François Chollet, Elon Musk, Andrew Ng, and Satya Nadella—what stood out was the stimulating environment. I decided to document this experience primarily to distill my thoughts, clarify my learnings, and deepen my understanding. The insights here reflect my interpretations and takeaways, not necessarily the exact viewpoints of the speakers.

<figure style="margin: 2rem 0;">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/yc-banner.png' | relative_url }}" alt="Y Combinator AI Startup School" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);">
</figure>


<div class="speaker-heading">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/garrytan.jpeg' | relative_url }}" alt="Gary Tan" class="speaker-profile">
  <h3>Garry Tan - CEO, Y Combinator</h3>
</div>

#### Building Strong Teams
Garry Tan talks about "agency scales" - which means having team members who actually get things done instead of just talking about them. These people are self-motivated, share the company's goals, and don't need much supervision. Since AI now helps individual workers do more, startups benefit from having small teams of these action-oriented people.

#### The Success Mindset That Never Changes
Gary points out that while tools keep changing, the winning mindset stays the same. Success comes from talking directly to users. Start by giving your product to just 10 people. Keep improving it based on what they tell you until they really love it. Only after people love your product should you try to grow bigger or spend money on marketing. Make a few users happy before trying to reach many.

<div class="speaker-heading">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/samaltman.png' | relative_url }}" alt="Sam Altman" class="speaker-profile">
  <h3>Sam Altman - CEO, OpenAI</h3>
</div>

#### Transformation of Software and Work

Garry questioned whether traditional Software-as-a-Service (SaaS) models would survive? Sam predicting higher expectations for software quality overall (no crappy software!). This trend will lead to specialized teams developing highly focused software solutions. The gap between current AI capabilities and actual products presents significant opportunities for startups, which often succeed over established companies during major tech shifts due to greater agility.

AI will disrupt consulting, enabling individuals to access information independently, increasing the importance of small, highly capable teams.

#### Building the Right Team

Sam advises startups against hiring big-name, experienced executives. Instead, he emphasizes building teams of highly optimistic, determined individuals who strongly believe in eventual success—a strategy consistent with Elon Musk’s preference for low ego and high agency. Interestingly, ambitious and meaningful goals attract talented team members more easily. Sam describes launching a startup as extremely rewarding yet exceptionally challenging, similar to parenting.

#### Product and Interface Evolution

Sam highlights AI-driven memory as a key emerging feature, anticipating personalized AI assistants integrated into services and daily life. Technology interfaces will become increasingly subtle, personalized, and seamlessly embedded into daily routines, as illustrated by innovative companies like IO.



<div class="speaker-heading">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/jaredcaplan.png' | relative_url }}" alt="Jared Kaplan" class="speaker-profile">
  <h3>Jared Kaplan - Anthropic Co-founder</h3>
</div>

#### The Technical Landscape
Jared Kaplan emphasized the scaling laws of pretraining and reinforcement learning, drawing from his physics background to pose fundamental questions about computational resources and data usage. He highlighted that LLMs are doubling their task capabilities roughly every seven months!

#### Understanding AI
Jared noted significant gaps in mechanistic interpretability, emphasizing that current approaches resemble neuroscience more than engineering. Despite this, LLMs offer a unique advantage due to the extensive measurable data they generate, enabling unprecedented opportunities for reverse-engineering cognitive processes.

#### Advice for AI Founders
Kaplan advised founders to build products anticipating future capabilities rather than current limitations. He emphasized the importance of identifying areas poised for exponential growth and preparing for deep AI integration into practical, real-world applications.

<div class="speaker-heading">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/aravindsrinivas.png' | relative_url }}" alt="Aravind Srinivas" class="speaker-profile">
  <h3>Aravind Srinivas - CEO, Perplexity</h3>
</div>

#### Ultimate Product Signal
Aravind highlighted sustained user retention as the definitive indicator of product success, surpassing initial adoption spikes or media hype. Technological shifts favor agile startups, which can pivot quickly, despite incumbents' resource advantages, precisely because startups can take greater risks.

<div class="speaker-heading">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/johnjumper.png' | relative_url }}" alt="John Jumper" class="speaker-profile">
  <h3>John Jumper - DeepMind</h3>
</div>

#### Power of Small Teams
John Jumper advocated for small, focused, high-agency teams with clear objectives to achieve outsized impacts. He described DeepMind's practice of using internal leaderboards for rapid iteration and competition, analogous to hyperparameter tuning using limited data subsets for quick prototyping. This approach combines rapid experimentation with periodic validation to maintain rigor.

There is increasing industry emphasis on AI-driven scientific discovery, with almost all frontier AI labs creating specialized teams for this purpose.

<div class="speaker-heading">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/andrejkarpathy.png' | relative_url }}" alt="Andrej Karpathy" class="speaker-profile">
  <h3>Andrej Karpathy</h3>
</div>

#### Software Evolution
Andrej Karpathy outlined AI's evolution within software paradigms. He categorized traditional software as "Software 1.0," neural networks as "Software 2.0," and large language models as "Software 3.0," emphasizing fluency across these paradigms. Karpathy views AI as akin to electricity—a foundational technological shift—with LLMs functioning as new operating systems and OpenRouter acting as a switching layer.

#### Why AI is Different
Karpathy argued AI fundamentally differs from previous tech revolutions because of its immediate consumer accessibility (for e.g. as opposed to the internet or computer, that started as DARPA projects). He described LLMs as "stochastic simulations of people's spirits".

<div class="speaker-heading">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/francoischollet.png' | relative_url }}" alt="François Chollet" class="speaker-profile">
  <h3>François Chollet</h3>
</div>

#### Rethinking Intelligence

Chollet questioned common beliefs about AI progress. He highlighted that true intelligence, called "fluid intelligence," relies on adapting and generalizing knowledge rather than memorizing benchmark tasks. Simply making models larger doesn't lead to fluid intelligence, as shown by results from the ARC-AGI benchmark.

#### Two Visions of AGI

François compared two ideas of AGI: Minsky's vision focused on automating tasks and McCarthy's vision emphasizing adaptability. He argued that real innovation comes from models designed for adaptability and generalization, not just automation through memorization.

#### Path to Fluid Intelligence

To achieve fluid intelligence, AI must dynamically use abstract concepts learned from past experiences. Chollet identified two abstraction types: Type 1 (basic abstractions) and Type 2 (complex abstractions involving combinations). Transformers handle Type 1 well, but true fluid intelligence requires using Type 1 effectively to manage the complexity of Type 2.


<div class="speaker-heading">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/elonmusk.png' | relative_url }}" alt="Elon Musk" class="speaker-profile">
  <h3>Elon Musk</h3>
</div>

#### Timeline and Scale

Elon Musk predicts digital superintelligence by 2026 but points out that AI progress will be uneven, though increasingly rapid as AI starts improving itself. He believes computational power will be the main limitation and expects artificial intelligence based on silicon to eventually become far more powerful than biological intelligence.

#### Lessons from Company Building

From his experience with Zip2, Musk highlights practical thinking, humility, taking initiative, and reasoning from first principles. He predicts a future where humanoid robots outnumber humans, greatly boosting global productivity and economic growth.

#### Future of Human Enhancement

Musk spoke about Neuralink's progress, mentioning successful experiments with vision implants in monkeys. While Neuralink initially aims to restore lost functions, its long-term goal is human enhancement, including abilities like infrared vision or direct connections to digital superintelligence. He mentioned the Kardashev scale, suggesting humanity could eventually harness energy from an entire star system. Musk's overall approach focuses on maximizing usefulness to humanity and pursuing truth, advocating humility and personal responsibility. He views AI as essential for expanding human understanding of the universe.


<figure style="margin: 2rem 0;">
  <img src="{{ '/assets/img/blog/yc-ai-startup-school/yc-ym.png' | relative_url }}" alt="The author at YC AI Startup School" style="width: 100%; height: auto; border-radius: 8px; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);">
</figure>

### General Insights

#### You Don't Need SOTA Models
A key takeaway is that building AI startups significantly differs from AI research. Cutting-edge models aren't necessary for success. For instance, one startup effectively used basic logistic regression in steel manufacturing optimization, generating $1M revenue with a simple algorithm for a highly specific use case.

**Key takeaway:** Rapidly build a functional prototype and deploy it to users. Your solution doesn't need to be research-level or employ advanced models.

#### B2C vs. B2B
- **B2C:** Selling directly to consumers can yield massive rewards if the product resonates strongly (e.g., Cursor). However, breakout consumer successes remain uncommon.
- **B2B:** Selling to enterprises is typically more straightforward. An illustrative example is a consultant from South Africa serving global pharma enterprises with basic AI tool proficiency rather than deep expertise.

#### Enterprise Pitch Strategy
A compelling enterprise pitch often boils down to demonstrating clear financial value: "You're currently spending X on a process; I can reduce it by 50% while maintaining or improving outcomes."

This works because:
- Large corporations struggle to keep pace with rapid AI advancements.
- Enterprises lack internal expertise to integrate AI effectively.
- Non-tech industries are particularly fertile grounds for such solutions.
- Even straightforward applications using Claude and basic coding skills can be highly profitable in enterprise consulting.

#### Founder Observations
- First-time founders typically guard their ideas closely.
- Second-time founders freely share ideas to gather early feedback and users.
- Additionally, many young founders overly associate their identities with prestigious universities or companies, which can negatively impact networking.

#### Happy Robot After-Party
Engaging with the successful Happy Robot founders (YC alumni) highlighted the deep personal bonds among co-founders—two brothers and college friends—which significantly contributed to their resilience during challenging periods.

They described "pivot hell," a common, painful experience for startups navigating toward product-market fit. The strength of founder relationships often determines success during these pivots.

### My prediction on future of Human-AI interaction
Current smartphone interfaces will soon become obsolete, replaced by seamless, voice-driven interactions likely enabled through augmented reality (AR) smart glasses. Physical keyboards will disappear entirely. Ultra-high-speed internet will become crucial, facilitating intensive AI computations in the cloud, with voice as the primary interaction method. Visual outputs would be delivered via subtle smart glasses or integrated VR headsets, making technology less intrusive and increasingly ambient.

With minimal latency and widespread connectivity, localized AI language modules on devices may become unnecessary. Instead, computational tasks will migrate entirely to cloud servers, rendering personal computing devices like laptops and phones less central. Technology will fade into the background—always on, listening, and contextually aware, activating precisely when needed. A central personal agent, functioning as a comprehensive, permissioned assistant, will manage specialized sub-agents. Users would primarily interact with this main agent, which orchestrates tasks, manages permissions, and coordinates with other individuals’ personal agents. These agents would securely handle sensitive personal information, like health records, limiting exposure to sub-agents.

Interpersonal communications, including emails, will become redundant as personal agents autonomously manage calls, messages, and scheduling based on user preferences and context. Essentially, this system would serve as an advanced personal secretary, constantly available and interactive primarily through voice. While traditional screens may lose prominence, mobile and movable visual interfaces will become valuable. Projection-based glasses or AR screens will provide convenient, glanceable information. Though AR interfaces may initially face comfort limitations, ongoing innovations will enhance daily integration, making smart glasses the likely favored solution.
