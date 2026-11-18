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
- `_layouts/default.html` — design tokens (CSS custom properties on `:root`), typography, page frame, navbar, generic page header, footer, mobile overrides
- `_layouts/about.html` — all homepage-specific styles and markup: hero (name, affiliations, intro, tools, portrait), then three full-width sections in order: Experience (Academia row, then Industry row), Representative work, News. The sections share a left rail (`--rail`) that holds the group labels, years and dates
- `_includes/pub_styles.html` — publication entry styles + abstract toggle JS, included by the publications page
- `_includes/pub_figures.html` — the live schematics drawn in publication thumbnails and in the homepage's Representative work rows, and the playback of a paper's teaser clip in the same plates (inline `<script>`), included by the publications page and by `about.html`
- `_pages/publications.md` — the "Research areas" section (its cards are the topic filter) with its styles and JS
- `blog/index.html`, `_layouts/post.html`, `_pages/repositories.md` — their own page styles

The SCSS files (`_sass/`) remain close to upstream al-folio defaults, so inline rules sometimes need extra specificity to beat them (e.g. `.profile`, `.header-bar`, `.post h3`, `.publications ol.bibliography li .author > em`).

**Design tokens** (defined once in `default.html`, use these instead of hex literals): the site is blue-black ink on warm paper. `--paper` (page background), `--surface` (cards and anything laid on the page), `--wash` (darker paper tone for fills), `--line`, `--ink`, `--ink-soft`, `--ink-faint`, `--navy` (JHU heritage blue #002D72), `--link`, `--sky` (JHU spirit blue #68ACE5), class colours `--c-green`, `--c-mint`, `--c-orange`, `--c-red`, and fonts `--display` (Bricolage Grotesque) / `--text` (Source Serif 4). Logos with white backgrounds sit on the paper via `mix-blend-mode: multiply`.

### About Page Content
- `about.html` extracts the intro from `about.md` with a Liquid `split` on the `<div class="intro-section">` marker. The markdown file must contain that exact div wrapper as raw HTML — changing it breaks the layout.
- Current affiliations (logo, role, name, link) come from the `affiliations` list in `about.md` front matter and are shown under the name.
- Experience (Academia, then Industry) is driven by `_data/experience.yml`: each entry has `id`, `org`, `logo`, `role` (shown under the logo), `period`, `summary`, optional `unit` / `title` / `logo_class` (`logo-boost` darkens a pale logo), and optional `people` (name, relation, url, photo). Hovering, clicking or tapping a logo opens a panel in the page under that row of logos (the chip is `display: contents`, so its button and its panel are both items of the row's grid; the panel takes `order: 1` and all columns). The panel is deliberately not a card (no border, background or shadow, by request): it is set straight on the page and unfolds slowly (`grid-template-rows: 0fr → 1fr`, 0.65s), with the organisation, position and dates, the entry's `summary` (about three sentences in the first person, drawn from the CV) in the body serif, the people in a row, and the papers from that position in a second column; its × is a faint mark in the corner, with portraits from `assets/img/people/` (square, ~160px) or initials when no photo is set. The panel stays open when the pointer leaves; another logo in the same row takes it over, and a click on the open logo, its × button or Escape closes it. Each row (Academia, Industry) keeps its own panel on purpose: closing a panel above the logo being hovered would move that logo out from under the pointer. The portraits were taken from each person's public Scholar, institute or personal page. Industry entries list no supervisors.
- **Experience ↔ papers:** a paper with `place={id}` in `papers.bib` is listed in that entry's panel (rendered by `_layouts/bib_out.html`, via a `{% bibliography --query @*[place={{ item.id }}] %}` call per entry). Hovering a logo marks its papers' titles and hovering a paper tints its logo (`.linked`). The rows under Representative work no longer repeat the origin logo, by request.
- The hover cue on the logos is deliberate and quiet: a dotted rule under each role, a one-line hint beside the heading ("Hover or click" / "Tap" by input type), a faint `--wash` tint on hover (no border, no shadow, by request), and a single staggered hop of the logos when the row first scrolls fully into view.
- The two tool cards are hardcoded in `about.html`.
- "Representative work" lists the papers with `selected={true}` in `papers.bib`, rendered by `_layouts/bib_line.html`. Each row is the paper's clip on the left (a 10:7 plate, 13rem wide on desktop, 10.5rem on tablets, 7.25rem on phones, all on one edge), then title, venue and year, and icon links (arXiv/Paper, Code, Website, with the same FontAwesome icons as the publications page), centred on the clip.
- **Scroll reveals:** anything with class `reveal` rises 10px and fades in as it enters the viewport; things arriving together go in turn (70ms apart). A small script above the markup sets `reveal-on` on `<html>` before first paint (and removes it after 3s if the main script never runs, so content cannot stay hidden); the script at the end adds `is-in`. Revealed elements get a paper background so the multiply-blended logos inside stay correct mid-fade. Nothing is hidden under `prefers-reduced-motion` or without JS. Don't put `reveal` on an element that has its own background or transition (the rule overrides both).
- News comes after Representative work and shows the latest 7 items (`news_visible` in `_includes/news.html`), with a toggle for the rest.
- `_base.scss` sets a colour on every `span`, so a span that should take its parent's colour needs `color: inherit`.

### Publications System
- BibTeX source: `_bibliography/papers.bib`
- Entry template: `_layouts/bib.html` (renders preview image or live schematic, authors, venue, topic tag, links, abstract)
- Homepage row template: `_layouts/bib_line.html`, selected with `--template bib_line` (clip, title, venue, year, links)
- Experience panel template: `_layouts/bib_out.html`, selected with `--template bib_out` (title, venue, year)
- Custom BibTeX fields beyond standard al-folio: `topic` (drives filtering), `abstract`, `selected={true}` (lists the paper under "Representative work" on the homepage), `place` (the `id` of the Experience entry in `_data/experience.yml` the work was done at; ties the paper to that logo on the homepage), `home_figure` (a live schematic shown in the paper's homepage row only; rename it to `figure` to show it on the publications page too), `figure` (name of a live schematic drawn in the paper's thumbnail on the publications page and in its homepage row; the `preview` image remains the no-JS fallback), `teaser` (file name of a short clip in `assets/video/`, played in the same two plates in place of the schematic; see "Teaser clips" below)
- **Order is the order of entries in `papers.bib`** (newest first), both on the publications page and on the homepage. This version of jekyll-scholar has no `--sort_by`/`--order` tag options; passing them silently stops option parsing, so anything after them (e.g. `--template`) is ignored.
- The publications page groups entries by year (`--group_by year`).
- **Research areas / topic filtering** (in `publications.md`): the page opens with a "Research areas" section of three cards, one per topic (name, one-line description, paper count and years filled in by JS). The cards are toggle buttons (`data-topic`, `aria-pressed`) that filter the list. OR logic — papers matching any selected area show; year headings with no visible papers are hidden.
- **Abstracts** expand inline under the entry (toggle JS in `_includes/pub_styles.html`). Note: the old al-folio abstract toggle system (`common.js` + `_base.scss`) still exists in code but is inert.

### ScholarBoard — Embedded React App
A separate React/Vite SPA at `/scholarboard/` with its own HTML, JS bundle, CSS, and data files.

**Source repo:** `/Users/mehtay/Research/scienta-ai/ScholarBoard-ai/`
**Sync workflow (automatic):**
1. Make changes in the source repo (frontend code, data, etc.)
2. Commit in the source repo — a **post-commit hook** (`.git/hooks/post-commit`) automatically runs `./bin/sync-scholarboard`, which builds with `VITE_BASE=/scholarboard/` and copies dist + data files to this repo
3. Commit & push from this website repo to deploy

**Sync workflow (manual):**
Run `./bin/sync-scholarboard` from this website repo, then commit & push.

**Important:** Never edit `scholarboard/` files directly in this repo — they get overwritten on next sync. All changes (including onboarding text in `Onboarding.tsx` and the beta banner in `frontend/index.html`) must go in the source repo.

**Note:** The post-commit hook is local to the source repo's `.git/hooks/` — it won't survive a re-clone. See the source repo's CLAUDE.md for re-installation instructions.

**Protection mechanisms:**
1. `_config.yml`: `exclude: [scholarboard]` (skip Jekyll processing) + `keep_files: [scholarboard]` (survive `jekyll clean`)
2. `bin/deploy`: explicit `! -name 'scholarboard'` in the `find`/`rm` cleanup
3. Hardcoded feature card in `about.html`, linking to the absolute `https://yashsmehta.com/scholarboard/` (the folder is excluded from Jekyll, so a relative link 404s on the dev server)

Any new deploy script or build process must preserve the `scholarboard/` directory.

### Publication Schematics
`_includes/pub_figures.html`. A paper with a `figure` field gets a `<canvas data-figure="…">` in its thumbnail on the publications page and in its row on the homepage (`home_figure` gives a homepage-only one); the script draws a small illustration of the paper's main idea from **synthetic** data (seeded RNG, identical on every load):
- `kernel` — two 7×7 filters filled in cell by cell, then the operation applied to them, with "0 gradient steps" (interpretable weight-space programming). Each replay shows the next of three programs from the paper's figure: Gabor energy, surface geometry, color contrast.
- `cloud` — a 3-D point cloud re-coloured by which side of its first 1–3 principal components each point falls on: 1,000 → 2 → 4 → 8 classes (Fig. 1a of arXiv:2605.05556). Follows the pointer while hovered.
- `rule` — Taylor coefficients of a candidate plasticity rule over training; two settle at +1 and −1, the rest decay to 0, leaving Oja's rule Δw = xy − y²w (model-based inference of plasticity rules).
- `perturb` — a small network run forward twice, clean (navy front) then with noise on its hidden units (orange rings, orange front); every weight then changes at once, with "0 backward passes" (node perturbation). Currently homepage-only (`home_figure`).
- `suite` — a 5×5 grid of benchmarks, each taking the colour of the search method that scored best on it, beside five bars re-ranking from one benchmark to the next; the sweep starts slowly and speeds up (NAS-Bench-Suite: no method wins everywhere). Currently homepage-only (`home_figure`).

Each schematic plays once when it scrolls into view (those arriving together start 450ms apart), replays on hover or tap of its entry or row, then rests on its final frame; under `prefers-reduced-motion` only the final frame is drawn. Plates narrower than 170px (the homepage rows, at 160px, and phones) get a label-free version. To add one: write a factory returning `{ duration, draw(ctx, W, H, t) }` that handles both the labelled and the label-free size, register it in `FIGURES`, and add its alt text to `_data/figures.yml` (read by both `bib.html` and `bib_line.html`).

### Teaser clips
A paper with `teaser={name.mp4}` in `papers.bib` shows that clip (`assets/video/name.mp4`, poster `assets/video/name.jpg`) in its thumbnail plate on the publications page and in its homepage row, **in place of** its schematic: `bib.html` and `bib_line.html` render a `<video data-teaser>` instead of the canvas, and the script in `pub_figures.html` (`mountClip`) gives it the schematics' behaviour — plays once when it scrolls into view (in turn with the others), replays on hover or tap, stops on its last frame; under `prefers-reduced-motion` it does not play and rests on the last frame. Remove the `teaser` field and the paper's `figure` comes back. Alt text lives in `_data/figures.yml`, keyed by the file name. The iWSP paper's clip is cut from a slide animation (its `figure={kernel}` is kept in the entry but not shown). Every other paper has a generated clip, so all eleven papers now show a clip on the publications page and all five Representative work rows show one on the homepage; the live schematics (`cloud`, `rule`, `perturb`, `suite`, `kernel`) remain in `pub_figures.html` and in the entries' `figure` / `home_figure` fields, and come back if a `teaser` field is removed. The generated ones (`coarse2026`, `plasticity2024`, `nodepert2022`, `nasbench2022`, `fgcs2022`, `bioconv2021`, `personality2020`, `personality_icdm2020`, `personality_bert2020`, `mtl2020`) are each a 640×448 HTML animation in `bin/teasers/<name>/index.html` exposing `window.DURATION` and a pure `window.renderAt(t)`, rendered frame by frame in headless Chromium and encoded by `python3 bin/teasers/render.py bin/teasers/<name> assets/video/<name>` (needs Python `playwright` and an ffmpeg with libx264; on PATH or given as `$FFMPEG`; none is installed on PATH on this machine). Their data is schematic, not the papers' results.

Alt text goes into an `aria-label`, so it must not contain double quotes.

How the clip is prepared (ffmpeg; source was a 25.6s 1080p slide animation):
- muted H.264, 640×448, i.e. the publications plate's 10:7; the homepage plate is 10:7 too, so nothing is cropped
- cropped to the slides' heading and diagram (no title card, footer or progress dashes), then padded to 10:7 by stretching its own top and bottom rows so the background carries on into the bars
- 2× speed with the long static hold trimmed, about 10s and 190 KB (`-crf 26 -preset veryslow -tune animation -movflags +faststart`)
- the poster is the clip's **first** frame, so playback starts from what was already showing

### Font Loading
- Display and body fonts (Bricolage Grotesque, Source Serif 4): Google Fonts, loaded in `default.html`
- Icon fonts: FontAwesome 5.15.4 and Academicons loaded in `_includes/head.html`

### Navigation
`_includes/header.html` iterates `site.pages | sort: "nav_order"` for pages with `nav: true` (About, Publications, Code, CV). The site name on the left links home and is hidden on the homepage, which already opens with the name. The Blog link was removed from the nav; `blog/index.html` and `_posts/` still build and are reachable by URL. ScholarBoard is linked from the tool card on the homepage.

## Adding Content

### New Publication
1. Add the BibTeX entry **at the top** of `_bibliography/papers.bib` (file order is display order) with custom fields: `topic`, `abstract`, `preview`, `place` (the Experience `id` it came out of, e.g. `jhu`, `msr`); add `selected={true}` to list it under "Representative work" on the homepage, where its row also shows a live schematic if it has a `figure` or `home_figure`
2. Add preview image to `assets/img/publication_preview/[key].jpg`
3. Valid topic values: `neuro-ai` (NeuroAI), `discovery` (Automated discovery), `personality` (Computational personality) (a new topic needs a label in `bib.html`, a colour in `pub_styles.html`, and a research-area card in `publications.md` with its own `.area-card.<id>` colour; the `.area-grid` there is three columns, one column at 640px and below)

### New CV
The CV page (`_pages/cv.md`) embeds `assets/pdf/ym_resume.pdf`. To update it, overwrite that file and keep the name, so the page and any outside links to the PDF keep working.

### New News Item
Create markdown in `_news/` with format `announcement_N.md`. Use `inline: true` in frontmatter for items that render directly in the news feed.
