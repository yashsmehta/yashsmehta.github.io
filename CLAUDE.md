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
- `_layouts/default.html` — design tokens (CSS custom properties on `:root`), typography, page frame, navbar, generic page header, footer, tablet and phone overrides (see "Small screens" below)
- `_layouts/about.html` — all homepage-specific styles and markup: hero (name, affiliations, intro, tools, portrait), then two full-width sections: Experience (Academia row, then Industry row; the papers are shown inside it) and News. The sections share a left rail (`--rail`) that holds the group labels and dates
- `_includes/pub_styles.html` — publication entry styles (and the tap handler that shows a paper's three lines on touch screens), included by the publications page
- `_includes/pub_figures.html` — the live schematics drawn in publication thumbnails and beside the papers in the homepage's Experience panels, and the playback of a paper's teaser clip in the same plates (inline `<script>`), included by the publications page and by `about.html`
- `_pages/publications.md` — the "Research areas" section (its cards are the topic filter) with its styles and JS
- `blog/index.html`, `_layouts/post.html`, `_pages/repositories.md`, `_pages/cv.md` — their own page styles

The SCSS files (`_sass/`) remain close to upstream al-folio defaults, so inline rules sometimes need extra specificity to beat them (e.g. `.profile`, `.header-bar`, `.post h3`, `.publications ol.bibliography li .author > em`).

**Design tokens** (defined once in `default.html`, use these instead of hex literals): the site is blue-black ink on warm paper. `--paper` (page background), `--surface` (cards and anything laid on the page), `--wash` (darker paper tone for fills), `--line`, `--ink`, `--ink-soft`, `--ink-faint`, `--navy` (JHU heritage blue #002D72), `--link`, `--sky` (JHU spirit blue #68ACE5), class colours `--c-green`, `--c-mint`, `--c-orange`, `--c-red`, and fonts `--display` (Bricolage Grotesque) / `--text` (Source Serif 4). Logos with white backgrounds sit on the paper via `mix-blend-mode: multiply`.

### About Page Content
- `about.html` extracts the intro from `about.md` with a Liquid `split` on the `<div class="intro-section">` marker. The markdown file must contain that exact div wrapper as raw HTML — changing it breaks the layout.
- Current affiliations (logo, role, name, link) come from the `affiliations` list in `about.md` front matter and are shown under the name.
- Experience (Academia, then Industry) is driven by `_data/experience.yml`: each entry has `id`, `org`, `logo`, `role` (shown under the logo), `period`, `summary`, optional `unit` / `title` / `logo_class` (`logo-boost` darkens a pale logo), and optional `people` (name, `title`, optional `at`, url, photo). A person is shown with their own current title under their name, not their relation to the owner (by request), followed by `at`, the institution, when it is not the entry's own (e.g. "Director of Research, Google DeepMind"); the title and the institution are each an inline-block, so a narrow column breaks the line between them and never inside either. Hovering, clicking or tapping a logo opens a panel in the page under that row of logos (the chip is `display: contents`, so its button and its panel are both items of the row's grid; the panel takes all the columns and comes after the logos by `order`). The panel stays open when the pointer leaves; another logo in the same row takes it over, and a click on the open logo, its × or Escape closes it. Each row (Academia, Industry) keeps its own panel on purpose: closing a panel above the logo being hovered would move that logo out from under the pointer. On phones (560px and below) the logos go three to a row, on a six-track grid so that a last row of one or two is centred, and each row of three has its panels ordered straight after it (`:nth-child` rules, up to nine logos), so a panel opens under the row its logo is in and not under the whole group. There the panel that gives way can be above the logo that takes over; `holdStill` in `about.html` then scrolls the page by as much as that logo moves while the panel folds, so the logo stays where it was tapped (a scroll by hand ends it; with one row of logos it does nothing). Microsoft Research and Sakana list their supervisors too; Amazon lists none. Portraits come from `assets/img/people/` (square, ~160px; taken from each person's public Scholar, institute or personal page), or initials when no photo is set. Chandan Singh's is the animated cartoon from his own site, at the site owner's request (`singh.gif`, cropped to the figure); its `photo_still` (`singh.jpg`) is served instead under `prefers-reduced-motion`.
- **The panel's layout.** It is deliberately not a card (no border, background or shadow, by request): it is set straight on the page in two equal columns (`.exp-card`, with `--gutter`, 2.5rem, between them). The first starts with `.exp-side`: organisation, then position, unit and dates on a line each (`.exp-head`), with the people beside that (a wrapping flex row, so they drop under it when the column is too narrow, below about 980px). The second is the entry's `summary` (about three sentences in the first person, drawn from the CV) in the body serif. The organisation's name, the first person's name and the summary's first line share a baseline, and the × is a faint mark in the top right corner, level with that line. Then "Paper(s) from this work", in the first column. Each paper is one unit: its clip on the left in a 10:7 plate (`--plate`: 10.5rem; 9rem from 861 to 1000px; about 30vw on phones) and, 1.1rem beside it and centred on it, the title, venue · year and icon links (arXiv/Paper, Code, Website); three lines of title are as tall as the plate. The clip is on the left and the text close beside it at the owner's request, after a version with the clip at the far right edge read as too much white space. A single paper sits in the first column, under the position and the people. Several papers go two abreast across the whole panel instead, the second of each pair on the summary's left edge: the card gets `exp-card-many` from the Liquid paper count, and in those panels the people are stacked under the position, which brings the first column down level with the summary before the papers start (the `li`s are grids, so a pair's clips stay level when one title runs longer). At 860px and below the panel is one column (`.exp-side` becomes `display: contents` and the parts are put in turn by `order`): organisation and position, summary, people in a row, then the papers one under another. Below 360px a title runs across above its clip, with the venue and links beside the clip; titles stay within four lines at every width. At 860px and below the × is the same faint mark in the same place with a 40px area for the finger, and the papers' links, the hero's links, "All publications" and the news toggle get taller tap areas without moving. An entry with no papers (Sakana) has the people beside the position and nothing under it; one with no people either (Amazon) is just the position and the summary.
- **The panel's motion.** It unfolds slowly: its row of the logos' grid goes `grid-template-rows: 0fr → 1fr` over 0.75s while the content fades in just behind. Closing takes 0.6s, and the content stays while its row folds, fading as it goes. The open panel is ordered before the closing one, so when another logo in the row takes over, the new panel grows in place and the old one gives its height back beneath it; `openChip` marks both with `swap`, which puts the two rows on the same 0.6s and curve (the row's height moves straight from one to the other, never dipping) and has the old content leave in 0.2s while the new arrives without the opening's delay. The papers' clips play in turn once the panel has opened (`setOpen` in `about.html`) and again when a paper is hovered (`mountClip`). Under `prefers-reduced-motion` the panel opens and closes at once, the clips rest on their last frame and the logos do not hop.
- **Experience ↔ papers:** a paper with `place={id}` in `papers.bib` is listed in that entry's panel (rendered by `_layouts/bib_out.html`, via a `{% bibliography --query @*[place={{ item.id }}] --template bib_out %}` call per entry). This is the only place the homepage shows papers: there is no separate list of selected papers any more, and the section's heading carries an "All publications →" link to the publications page.
- The hover cue on the logos is deliberate and quiet: a dotted rule under each role, a one-line hint beside the heading ("Hover or click" / "Tap" by input type; under the heading at 760px and below), a faint `--wash` tint on hover (no border, no shadow, by request), and a single staggered hop of the logos when the row first scrolls fully into view.
- The two tool cards are hardcoded in `about.html`.
- **Scroll reveals:** anything with class `reveal` rises 10px and fades in as it enters the viewport; things arriving together go in turn (70ms apart). A small script above the markup sets `reveal-on` on `<html>` before first paint (and removes it after 3s if the main script never runs, so content cannot stay hidden); the script at the end adds `is-in`. Revealed elements get a paper background so the multiply-blended logos inside stay correct mid-fade. Nothing is hidden under `prefers-reduced-motion` or without JS. Don't put `reveal` on an element that has its own background or transition (the rule overrides both).
- News comes after Experience and shows the latest 7 items (`news_visible` in `_includes/news.html`), with a toggle for the rest.
- `_base.scss` sets a colour on every `span`, so a span that should take its parent's colour needs `color: inherit`.

### Publications System
- BibTeX source: `_bibliography/papers.bib`
- Entry template: `_layouts/bib.html`. Left column (`.pub-media`): the clip (or schematic / preview image) and, under it, the venue's short name and the year, e.g. "NeurIPS 2024", "Preprint 2026" (`abbr`, else the journal or booktitle; an arXiv paper's `abbr` is `Preprint`, by request). Right column: `.pub-head` with the title and the topic tag at the top right, authors, links, then short lines in place of an abstract (`Question` / `My contribution` / `Findings`; `My contribution` is omitted on the two 3rd-author papers `li2020multitask` and `kazameini2020personality`) from `_data/paper_notes.yml` (`question`, `contribution`, `findings`), keyed by BibTeX key. The owner asked for these instead of abstracts, shown on hover, small and with no dropdown: the lines are always in the layout (so nothing moves) but invisible, and fade in one after another while the entry is hovered or has focus; each must stay on one line at desktop width (at most ~83 characters), and values in the YAML are double-quoted because they contain colons. On screens with no hover the lines are folded away until the entry is tapped (handler in `pub_styles.html`); they then fade in one after another (`@starting-style`), and a one-line hint above the list (`.pubs-hint` in `publications.md`, shown only under `hover: none`) says so, in the manner of the homepage's hint. Widths: at 768px and below `.pub-head` stacks the topic tag under the title; the clip column is 248px down to 641px and 11.5rem from 640 to 481px, where the notes' labels go above their lines; at 480px and below the entry is one column, the clip across the full width with the venue under it, then title, topic, authors and links, and the notes (label beside its line again; above it below 360px) get the whole width. The earlier phone layout, a 92px clip beside the text, was dropped because the clips were unreadable at that size. The `abstract` fields in `papers.bib` hold the full published abstracts (not shown on the page)
- Each entry has `id="<bibtex key>"`. On the homepage a paper's title and clip link to `/publications/#<key>` (the icon links still go to the paper, code and website themselves); `:target` shows that entry's three lines on arrival and tints it briefly
- Experience panel template: `_layouts/bib_out.html`, selected with `--template bib_out` (title, venue, year, links, and the paper's clip or schematic; title and clip link to the paper's entry on the publications page)
- Custom BibTeX fields beyond standard al-folio: `topic` (drives filtering), `abstract`, `place` (the `id` of the Experience entry in `_data/experience.yml` the work was done at; lists the paper in that logo's panel on the homepage), `home_figure` (a live schematic shown beside the paper on the homepage only; rename it to `figure` to show it on the publications page too), `figure` (name of a live schematic drawn in the paper's thumbnail on the publications page and beside it on the homepage; the `preview` image remains the no-JS fallback), `selected={true}` (still set on five entries but no longer read by the homepage), `teaser` (file name of a short clip in `assets/video/`, played in the same two plates in place of the schematic; see "Teaser clips" below)
- **Order is the order of entries in `papers.bib`** (newest first), both on the publications page and on the homepage. This version of jekyll-scholar has no `--sort_by`/`--order` tag options; passing them silently stops option parsing, so anything after them (e.g. `--template`) is ignored.
- The publications page is one list with no year headings (the owner asked for them to go; the year is in the label under each clip). Each entry carries `data-year`, which the research-area cards read for their year ranges.
- **Research areas / topic filtering** (in `publications.md`): the page opens with a "Research areas" section of three cards, one per topic (name, one-line description, paper count and years filled in by JS; an entry's year is read from its `data-year`). The cards are toggle buttons (`data-topic`, `aria-pressed`) that filter the list. OR logic — papers matching any selected area show.
- Abstracts are no longer shown (see the three lines above). The old al-folio abstract toggle system (`common.js` + `_base.scss`) still exists in code but is inert.

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
`_includes/pub_figures.html`. A paper with a `figure` field gets a `<canvas data-figure="…">` in its thumbnail on the publications page and beside it in its Experience panel on the homepage (`home_figure` gives a homepage-only one); the script draws a small illustration of the paper's main idea from **synthetic** data (seeded RNG, identical on every load):
- `kernel` — two 7×7 filters filled in cell by cell, then the operation applied to them, with "0 gradient steps" (interpretable weight-space programming). Each replay shows the next of three programs from the paper's figure: Gabor energy, surface geometry, color contrast.
- `cloud` — a 3-D point cloud re-coloured by which side of its first 1–3 principal components each point falls on: 1,000 → 2 → 4 → 8 classes (Fig. 1a of arXiv:2605.05556). Follows the pointer while hovered.
- `rule` — Taylor coefficients of a candidate plasticity rule over training; two settle at +1 and −1, the rest decay to 0, leaving Oja's rule Δw = xy − y²w (model-based inference of plasticity rules).
- `perturb` — a small network run forward twice, clean (navy front) then with noise on its hidden units (orange rings, orange front); every weight then changes at once, with "0 backward passes" (node perturbation). Currently homepage-only (`home_figure`).
- `suite` — a 5×5 grid of benchmarks, each taking the colour of the search method that scored best on it, beside five bars re-ranking from one benchmark to the next; the sweep starts slowly and speeds up (NAS-Bench-Suite: no method wins everywhere). Currently homepage-only (`home_figure`).

Each schematic plays once when it scrolls into view (those arriving together start 450ms apart), replays on hover or tap of its entry, then rests on its final frame; under `prefers-reduced-motion` only the final frame is drawn. Plates narrower than 170px (the homepage's, at 168px and below) get a label-free version. To add one: write a factory returning `{ duration, draw(ctx, W, H, t) }` that handles both the labelled and the label-free size, register it in `FIGURES`, and add its alt text to `_data/figures.yml` (read by both `bib.html` and `bib_out.html`).

### Teaser clips
A paper with `teaser={name.mp4}` in `papers.bib` shows that clip (`assets/video/name.mp4`, poster `assets/video/name.jpg`) in its thumbnail plate on the publications page and beside it in its Experience panel on the homepage, **in place of** its schematic: `bib.html` and `bib_out.html` render a `<video data-teaser>` instead of the canvas, and the script in `pub_figures.html` (`mountClip`) gives it the schematics' behaviour — plays once when it scrolls into view (in turn with the others), replays on hover or tap, stops on its last frame; under `prefers-reduced-motion` it does not play and rests on the last frame. On the homepage a clip sits in a closed panel until its logo is opened, so `about.html` also starts the panel's clips, in turn, each time it opens. Remove the `teaser` field and the paper's `figure` comes back. Alt text lives in `_data/figures.yml`, keyed by the file name. The iWSP paper's clip is cut from a slide animation (its `figure={kernel}` is kept in the entry but not shown). Every other paper has a generated clip, so all eleven papers now show a clip on the publications page and the ten with a `place` show one in their Experience panel on the homepage; the live schematics (`cloud`, `rule`, `perturb`, `suite`, `kernel`) remain in `pub_figures.html` and in the entries' `figure` / `home_figure` fields, and come back if a `teaser` field is removed. The generated ones (`coarse2026`, `plasticity2024`, `nodepert2022`, `nasbench2022`, `fgcs2022`, `bioconv2021`, `personality2020`, `personality_icdm2020`, `personality_bert2020`, `mtl2020`) are each a 640×448 HTML animation in `bin/teasers/<name>/index.html` exposing `window.DURATION` and a pure `window.renderAt(t)`, rendered frame by frame in headless Chromium and encoded by `python3 bin/teasers/render.py bin/teasers/<name> assets/video/<name>` (needs Python `playwright` and an ffmpeg with libx264; on PATH or given as `$FFMPEG`; none is installed on PATH on this machine). Their data is schematic, not the papers' results.

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

### Small screens
Checked at 320, 360, 390, 430, 600, 768 and 844px. The breakpoints, all `max-width`:
- **860px** — homepage in one column (hero, Experience panel); the navbar loses its own side padding so the name and the links stand on the page's edges (from 861 to about 1070px they still sit up to 16px inside them).
- **768px** — `--gutter` 1.5rem (2rem above), body text 1rem, footer centred with its icons as 40px targets, publication topic tags stacked under titles.
- **640px** — publications: 11.5rem clip column; research-area cards and the Code page's rows in one column (on the Code page the repeated GitHub mark goes and the grey text is larger and darker).
- **575.98px** — Bootstrap folds the nav links into the menu here (`navbar-expand-sm`), so the menu's rules start here too, not at 768: the button is 46 × 40px to the finger with its lines on the page's right edge, the bar is as tall on the homepage (no name in it) as elsewhere, and while the menu is open the bar is solid (`:has(.navbar-collapse.show)`; al-folio gives it `opacity: 0.95`). `--gutter` 1.15rem. The CV page shows page images (see "New CV"). Blog posts drop their own side padding.
- **560px** — homepage phone rules: logos three to a row, news dates above their items, tool cards stacked.
- **480px** — publications entries in one column.
- **360px** — the narrowest phones: paper titles above their clips in the Experience panels, note labels above their lines.

`html` and `body` have `overflow-x: hidden` at 768px and below, which hides a horizontal overflow instead of showing it: when checking a page, look for elements whose box passes the viewport's edge, not only at `scrollWidth`.

## Adding Content

### New Publication
1. Add the BibTeX entry **at the top** of `_bibliography/papers.bib` (file order is display order) with custom fields: `topic`, `abbr` (short venue name), `abstract`, `preview`, `place` (the Experience `id` it came out of, e.g. `jhu`, `msr`); the `place` is what lists it on the homepage, in that logo's panel, with its `teaser` clip (or, without one, its `figure` / `home_figure` schematic) beside it
2. Add its three lines to `_data/paper_notes.yml` under the entry's key
2. Add preview image to `assets/img/publication_preview/[key].jpg`
3. Valid topic values: `neuro-ai` (NeuroAI), `discovery` (Automated discovery), `personality` (Computational personality) (a new topic needs a label in `bib.html`, a colour in `pub_styles.html`, and a research-area card in `publications.md` with its own `.area-card.<id>` colour; the `.area-grid` there is three columns, one column at 640px and below)

### New CV
The CV page (`_pages/cv.md`) embeds `assets/pdf/ym_resume.pdf` in a frame. To update it, overwrite that file and keep the name, so the page and any outside links to the PDF keep working.

Phones and touch screens do not scroll a PDF inside a frame (iOS shows the first page only, Android nothing), so at 575px and below, and on any touch screen (`hover: none` and `pointer: coarse`, where a script also removes the frame before it loads the PDF), the page shows an "Open as PDF" button and one image per page instead, each a link to the PDF. The images are `assets/img/cv/page-N.jpg` and the page lists whatever `page-*` files are there, so **they must be regenerated whenever the PDF changes**, or phones show the old CV:

```bash
rm -f assets/img/cv/page-*.jpg
pdftoppm -r 110 -jpeg -jpegopt quality=78,progressive=y,optimize=y assets/pdf/ym_resume.pdf assets/img/cv/page
```

(`pdftoppm` is from poppler; 110 dpi gives 910 × 1287px for A4, which is what the `width`/`height` attributes in `cv.md` say; with ten or more pages the numbers are zero-padded, which the page's sort by path handles.)

### New News Item
Create markdown in `_news/` with format `announcement_N.md`. Use `inline: true` in frontmatter for items that render directly in the news feed.
