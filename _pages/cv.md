---
layout: page
title: CV
permalink: /cv/
nav: true
nav_order: 4
---

{%- assign cv_pdf = '/assets/pdf/ym_resume.pdf' | relative_url -%}
{%- assign cv_pages = site.static_files | where_exp: "file", "file.path contains '/assets/img/cv/page-'" | sort: "path" -%}
<style>
/* Phones and touch screens do not scroll a PDF inside a frame (iOS shows its first page
   only, Android nothing), so they get the pages as images, each a link to the PDF, under
   a button that opens it. The images are made from the PDF: see "New CV" in CLAUDE.md. */
.cv-pages { display: none; }
.cv-open {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 1.15rem;
  border: 1px solid var(--line);
  border-radius: 999px;
  background: var(--surface);
  font-family: var(--display);
  font-size: 0.93rem;
  font-weight: 550;
  color: var(--link);
  transition: border-color 0.15s ease, color 0.15s ease;
}
.cv-open:hover { border-color: var(--navy); color: var(--navy); text-decoration: none; }
.cv-open i { font-size: 0.85em; }
.cv-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  margin: -0.6rem 0 1.25rem;
}
.cv-meta { font-family: var(--display); font-size: 0.85rem; font-weight: 500; color: var(--ink-faint); }
.cv-page {
  display: block;
  margin: 0 0 1rem;
  border: 1px solid var(--line);
  border-radius: 8px;
  overflow: hidden;
  background: #fff;
}
.cv-page img { display: block; width: 100%; height: auto; }
@media (max-width: 575.98px), (hover: none) and (pointer: coarse) {
  .cv-frame { display: none; }
  .cv-pages { display: block; max-width: 46rem; }
}
</style>
<div class="post">
    <link rel="preload" as="document" href="{{ cv_pdf }}">
    <div class="cv-frame" style="margin: -120px auto 0; max-width: 100%;">
        <iframe src="{{ cv_pdf }}" width="100%" height="800" frameborder="0" allowfullscreen loading="eager" importance="high" style="display: block;"></iframe>
    </div>
    <script>
      /* A touch screen never shows the frame: take it out before it has fetched the PDF. */
      if (window.matchMedia && window.matchMedia('(hover: none) and (pointer: coarse)').matches) {
        var cvFrame = document.querySelector('.cv-frame');
        if (cvFrame) cvFrame.parentNode.removeChild(cvFrame);
      }
    </script>
    <div class="cv-pages">
        <p class="cv-bar">
            <a class="cv-open" href="{{ cv_pdf }}"><i class="fas fa-file-pdf" aria-hidden="true"></i>Open as PDF</a>
            {%- if cv_pages.size > 0 %}<span class="cv-meta">{{ cv_pages.size }} {% if cv_pages.size == 1 %}page{% else %}pages{% endif %}</span>{% endif -%}
        </p>
        {%- for file in cv_pages %}
        <a class="cv-page" href="{{ cv_pdf }}" aria-label="Open the CV as a PDF (page {{ forloop.index }})"><img src="{{ file.path | relative_url }}" alt="CV, page {{ forloop.index }} of {{ cv_pages.size }}" width="910" height="1287"{% unless forloop.first %} loading="lazy"{% endunless %}></a>
        {%- endfor %}
    </div>
</div>
