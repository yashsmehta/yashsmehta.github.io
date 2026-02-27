# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Jekyll-based academic portfolio site (al-folio theme) for a JHU PhD student. Deployed to GitHub Pages. Also hosts a standalone React/Vite SPA at `/scholarboard/`.

## Development Commands

```bash
bundle install                              # Install Ruby dependencies
bundle exec jekyll serve --livereload       # Dev server at localhost:4000
JEKYLL_ENV=production bundle exec jekyll build  # Production build
bundle exec jekyll clean                    # Clean _site/ artifacts
```

## Deployment

Two-branch strategy: source on `master`, built site on `gh-pages`. The `bin/deploy` script builds, wipes everything except `_site/`, `.git/`, `CNAME`, and `scholarboard/`, then force-pushes to `gh-pages`. Also triggered via GitHub Actions on push to `master`.

## Architecture

### Layout Inheritance
```
default.html → about.html (homepage)
             → page.html  (publications, cv, projects, teaching)
             → post.html  (blog posts, news)
```

### Inline Style Override Pattern (critical)
Most visual customizations are NOT in SCSS. Instead, they live in inline `<style>` blocks:
- `_layouts/default.html` — glassmorphism, typography (Factoria/Proxima Nova), navbar colors, mobile overrides, **and the entire network animation JS** (inline `<script>`)
- `_layouts/about.html` — all homepage-specific styles (profile layout, institution logos, ScholarBoard card)
- `_pages/publications.md` — all publication page styles, topic filter system, abstract popup modal JS

The SCSS files (`_sass/`) remain close to upstream al-folio defaults. Custom JHU colors (#002D72, #68ACE5) are hardcoded as hex literals in the inline styles, not defined in `_variables.scss`.

### About Page Content Parsing
`about.html` extracts sections from `about.md` using Liquid `split` filters on `<div class="intro-section">` and `<div class="research-section">` markers. The markdown file must contain those exact div wrappers as raw HTML — changing them breaks the layout.

### Publications System
- BibTeX source: `_bibliography/papers.bib`
- Entry template: `_layouts/bib.html` (renders preview image, authors, links, topic icon)
- Custom BibTeX fields beyond standard al-folio: `topic` (drives filtering), `abstract` (shown in popup modal)
- **Topic filtering** (in `publications.md`): Vanilla JS using `data-topic` attributes and a `Set` of active filters. OR logic — papers matching any active filter show.
- **Abstract popup** (in `publications.md`): Dynamic modal positioned at click coordinates with spring animation. Reads from hidden `.abstract-content` divs in `bib.html`. Note: the old al-folio abstract toggle system (`common.js` + `_base.scss`) still exists in code but is inert.

### ScholarBoard — Embedded React App
A separate React/Vite SPA at `/scholarboard/` with its own HTML, JS bundle, CSS, and data files.

**Source repo:** `/Users/mehtay/Research/scienta-ai/ScholarBoard-ai/`
**Sync workflow:**
1. Make changes in the source repo (frontend code, data, etc.)
2. Run `./bin/sync-scholarboard` from this website repo — builds with `VITE_BASE=/scholarboard/`, copies dist + data files, injects beta banner
3. Commit & push from this repo to deploy

**Important:** Never edit `scholarboard/` files directly in this repo — they get overwritten on next sync. All changes (including onboarding text in `Onboarding.tsx`) must go in the source repo. The only website-repo-side customization is the beta banner template at `bin/scholarboard-banner.html`, which gets injected into `index.html` during sync.

**Protection mechanisms:**
1. `_config.yml`: `exclude: [scholarboard]` (skip Jekyll processing) + `keep_files: [scholarboard]` (survive `jekyll clean`)
2. `bin/deploy`: explicit `! -name 'scholarboard'` in the `find`/`rm` cleanup
3. Hardcoded nav link in `_includes/header.html` and feature card in `about.html`

Any new deploy script or build process must preserve the `scholarboard/` directory.

### Network Animation
Inline in `default.html` (not a separate JS file). 100 nodes with JHU color palette, connection lines within 150px, mouse interaction within 120px. Disabled on mobile via CSS `display: none` at `max-width: 768px` and conditionally excluded on blog pages via Liquid.

### Font Loading
- Body fonts (Factoria, Proxima Nova): Adobe Typekit CDN loaded in `default.html`
- Icon fonts: FontAwesome 5.15.4 loaded in `_includes/head.html`; publications page additionally loads FontAwesome 6.0 from a separate CDN (two FA versions coexist on that page)

### Navigation
`_includes/header.html` iterates `site.pages | sort: "nav_order"` for pages with `nav: true`. The ScholarBoard link is hardcoded after the loop, outside the normal page system.

## Adding Content

### New Publication
1. Add BibTeX entry to `_bibliography/papers.bib` with custom fields: `topic`, `abstract`, `preview`, `selected={true}` for featured
2. Add preview image to `assets/img/publication_preview/[key].jpg`
3. Valid topic values: `bio-learning`, `nas`, `personality`

### New News Item
Create markdown in `_news/` with format `announcement_N.md`. Use `inline: true` in frontmatter for items that render directly in the news feed.
