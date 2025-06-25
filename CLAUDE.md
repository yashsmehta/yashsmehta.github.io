# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Jekyll-based academic portfolio website using the al-folio theme. The site showcases academic work including publications, projects, teaching experience, and research.

## Key Technologies

- **Jekyll** - Static site generator (Ruby-based)
- **Jekyll Scholar** - For managing academic publications with BibTeX
- **Bootstrap 4.6.1** - CSS framework
- **GitHub Pages** - Hosting platform with automated deployment

## Development Commands

```bash
# Install dependencies (run first)
bundle install

# Development server with live reload
bundle exec jekyll serve --livereload

# Build for production
JEKYLL_ENV=production bundle exec jekyll build

# Clean build artifacts
bundle exec jekyll clean

# Alternative: Use Docker
./bin/docker_run.sh  # Serves on port 8080
```

## Project Structure

### Content Directories
- `_pages/` - Main website pages (about.md, publications.md, projects.md, teaching.md, cv.md)
- `_news/` - News/announcement items (markdown files with dates)
- `_projects/` - Individual project descriptions
- `_bibliography/papers.bib` - BibTeX file for all publications

### Theme Structure
- `_layouts/` - Page templates (about.html, bib.html, page.html, post.html)
- `_includes/` - Reusable components (header.html, footer.html, news.html, projects.html)
- `_sass/` - SCSS stylesheets with custom variables and themes
- `assets/` - Images, PDFs, JavaScript, and compiled CSS

## Key Customizations

### About Page
- Custom JHU color scheme (Heritage Blue #002D72, Spirit Blue #68ACE5)
- Animated network background on all pages
- Institution logos section
- Integrated news feed

### Publications Page
- Topic-based filtering system (bio-learning, NAS, personality)
- Interactive abstract popups
- Publication preview images
- Custom bibliography formatting

### Styling
- Custom fonts: Factoria and Proxima Nova
- Glassmorphism effects with backdrop blur
- Mobile-responsive design

## Deployment

The site automatically deploys to GitHub Pages when pushing to the `master` branch via GitHub Actions. Manual deployment is available with `./bin/deploy`.

## Adding Content

### New Publication
1. Add BibTeX entry to `_bibliography/papers.bib`
2. Add preview image to `assets/img/publication_preview/[paper-key].jpg`
3. Include `selected={true}` in BibTeX for featured papers

### New Project
Create a markdown file in `_projects/` with frontmatter:
```yaml
---
layout: page
title: Project Title
description: Brief description
img: assets/img/project-thumbnail.jpg
importance: 1
category: research
---
```

### New News Item
Create a markdown file in `_news/` with the filename format `YYYY-MM-DD-announcement.md`.

## Configuration

Main settings are in `_config.yml`:
- Site metadata and URLs
- Social media profiles
- Theme colors and settings
- Plugin configurations
- Jekyll Scholar settings