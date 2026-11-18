---
layout: page
permalink: /publications/
title: Publications
nav: true
nav_order: 1
---

{% include pub_styles.html %}

<style>
/* ── Research areas: a short overview that doubles as the topic filter ── */
.areas { margin: 0 0 2.75rem; }
.areas-heading {
  font-family: var(--display);
  font-weight: 700;
  font-size: 1.3rem;
  line-height: 1.2;
  letter-spacing: -0.025em;
  color: var(--navy);
  margin: 0 0 0.6rem;
}
.areas p { max-width: 74ch; margin: 0; color: var(--ink-soft); }
.area-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.75rem;
  margin: 1.1rem 0 1rem;
}
.area-card {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 0.25rem;
  padding: 0.7rem 0.9rem 0.75rem;
  border: 1px solid var(--line);
  border-radius: 10px;
  background: var(--surface);
  text-align: left;
  color: var(--ink);
  cursor: pointer;
  transition: border-color 0.15s ease, background 0.15s ease;
}
.area-card:hover { border-color: var(--topic); }
.area-card[aria-pressed="true"] {
  border-color: var(--topic);
  background: color-mix(in srgb, var(--topic) 9%, var(--surface));
  box-shadow: inset 0 0 0 1px var(--topic);
}
.area-name {
  display: flex;
  align-items: baseline;
  gap: 0.5rem;
  font-family: var(--display);
  font-weight: 650;
  font-size: 0.97rem;
  line-height: 1.25;
  letter-spacing: -0.012em;
}
.area-name .topic-dot { transform: translateY(-0.05em); }
.area-desc { font-size: 0.88rem; line-height: 1.4; color: var(--ink-soft); }
.area-count {
  margin-top: auto;
  padding-top: 0.15rem;
  font-family: var(--display);
  font-size: 0.8rem;
  font-weight: 500;
  font-variant-numeric: tabular-nums;
  color: var(--ink-faint);
}
.area-card.neuro-ai     { --topic: var(--c-red); }
.area-card.discovery    { --topic: var(--link); }
.area-card.personality  { --topic: var(--c-green); }
.areas .areas-note { font-size: 0.95rem; }

@media (max-width: 640px) {
  .area-grid { grid-template-columns: minmax(0, 1fr); }
}
@media (max-width: 480px) {
  .area-card { padding: 0.7rem 0.8rem 0.75rem; }
  .area-name { font-size: 0.95rem; }
  .area-desc { font-size: 0.85rem; }
}
</style>

<section class="areas" aria-labelledby="areas-heading">
  <h2 class="areas-heading" id="areas-heading">Research areas</h2>
  <p>I've had the opportunity to explore several research areas and work in different labs in 🇺🇸, 🇯🇵, 🇩🇪, 🇬🇧, 🇸🇬, and 🇮🇳. Select an area to see only its papers.</p>

  <div class="area-grid" role="group" aria-label="Filter publications by research area">
    <button type="button" class="area-card neuro-ai" data-topic="neuro-ai" aria-pressed="false">
      <span class="area-name"><span class="topic-dot"></span>NeuroAI</span>
      <span class="area-desc">Brain-like representations and biologically plausible learning</span>
      <span class="area-count"></span>
    </button>
    <button type="button" class="area-card discovery" data-topic="discovery" aria-pressed="false">
      <span class="area-name"><span class="topic-dot"></span>Automated discovery</span>
      <span class="area-desc">Searching for models, learning rules and architectures instead of hand-designing them</span>
      <span class="area-count"></span>
    </button>
    <button type="button" class="area-card personality" data-topic="personality" aria-pressed="false">
      <span class="area-name"><span class="topic-dot"></span>Computational personality</span>
      <span class="area-desc">Predicting personality traits from text</span>
      <span class="area-count"></span>
    </button>
  </div>

  <p class="areas-note">I also completed a short PhD rotation project at <em>Harvard Medical School</em> with <a href="https://pranavrajpurkar.com/">Pranav Rajpurkar</a>, focusing on knowledge graphs for automating radiology report generation.</p>
</section>

<p class="pubs-hint"><i class="far fa-hand-pointer" aria-hidden="true"></i>Tap a paper for the question, my contribution and findings</p>

<div class="publications">
{% bibliography --file papers %}
</div>

<script>
document.addEventListener('DOMContentLoaded', function () {
  // Research areas filter the list. OR logic: a paper shows if it matches any selected area.
  const cards = document.querySelectorAll('.area-card');
  const papers = document.querySelectorAll('.publication-item');
  const active = new Set();

  // Each card states how many papers it covers and over which years. An entry's year
  // is its data-year attribute (the list has no year headings).
  cards.forEach(card => {
    const years = [];
    document.querySelectorAll('.publication-item.topic-' + card.dataset.topic).forEach(paper => {
      const year = parseInt(paper.dataset.year, 10);
      if (year) years.push(year);
    });
    if (!years.length) return;
    const first = Math.min(...years), last = Math.max(...years);
    card.querySelector('.area-count').textContent =
      years.length + (years.length === 1 ? ' paper, ' : ' papers, ') + (first === last ? first : first + '–' + last);
  });

  cards.forEach(card => {
    card.addEventListener('click', function () {
      const topic = this.dataset.topic;
      const on = this.getAttribute('aria-pressed') !== 'true';
      this.setAttribute('aria-pressed', on ? 'true' : 'false');
      if (on) active.add(topic); else active.delete(topic);

      papers.forEach(paper => {
        const show = active.size === 0 ||
          Array.from(active).some(t => paper.classList.contains('topic-' + t));
        paper.classList.toggle('hidden', !show);
      });
    });
  });
});
</script>

{% include pub_figures.html %}
