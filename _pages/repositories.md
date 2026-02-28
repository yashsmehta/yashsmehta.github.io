---
layout: page
permalink: /repositories/
title: Code
description: Open-source research code and tools
nav: true
nav_order: 3
---

<style>
  /* ── Page header ── */
  .post .post-title {
    font-family: "factoria", sans-serif;
    font-weight: 700;
    font-style: normal !important;
    color: #002D72;
    font-size: 2.2rem;
    margin-bottom: 0.5rem;
  }
  .post .post-description {
    font-family: "proxima-nova", sans-serif;
    font-weight: 300;
    font-size: 0.95em;
    color: #6b7c8d;
    margin-top: 0.15rem;
  }
  .post .post-header {
    margin-bottom: 1rem;
  }

  /* ── GitHub Profile Card ── */
  .gh-profile {
    display: flex;
    align-items: center;
    gap: 1.25rem;
    padding: 1.1rem 1.4rem;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.55);
    border: 1px solid rgba(104, 172, 229, 0.15);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    text-decoration: none;
    color: #2c3e50;
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    margin-bottom: 0.3rem;
  }
  .gh-profile:hover {
    transform: translateY(-1px);
    border-color: rgba(104, 172, 229, 0.3);
    box-shadow: 0 6px 20px rgba(0, 45, 114, 0.07);
    background: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    color: #2c3e50;
  }
  .gh-profile-avatar {
    width: 64px;
    height: 64px;
    border-radius: 50%;
    border: 2px solid rgba(104, 172, 229, 0.2);
    flex-shrink: 0;
  }
  .gh-profile-info {
    flex: 1;
    min-width: 0;
  }
  .gh-profile-name {
    font-family: "factoria", sans-serif;
    font-weight: 700;
    font-size: 1.1em;
    color: #002D72;
    line-height: 1.2;
  }
  .gh-profile-username {
    font-family: "proxima-nova", sans-serif;
    font-weight: 300;
    font-size: 0.82em;
    color: #68ACE5;
    margin-top: 0.1rem;
  }
  .gh-profile-bio {
    font-family: "proxima-nova", sans-serif;
    font-weight: 300;
    font-size: 0.78em;
    color: #6b7c8d;
    line-height: 1.4;
    margin-top: 0.25rem;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  .gh-profile-stats {
    display: flex;
    gap: 1rem;
    flex-shrink: 0;
    align-items: flex-start;
  }
  .gh-stat {
    text-align: center;
  }
  .gh-stat-num {
    font-family: "factoria", sans-serif;
    font-weight: 700;
    font-size: 1.15em;
    color: #002D72;
    line-height: 1;
  }
  .gh-stat-label {
    font-family: "proxima-nova", sans-serif;
    font-weight: 300;
    font-size: 0.65em;
    color: #8a9bac;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-top: 0.2rem;
  }

  /* ── Section divider ── */
  .repositories-page .section-divider {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(104, 172, 229, 0.18), transparent);
    margin: 1.2rem 0;
  }

  /* ── Section headings ── */
  .repositories-page h2 {
    font-family: "factoria", sans-serif;
    font-weight: 500;
    font-size: 1.15em;
    color: #002D72;
    letter-spacing: -0.01em;
    margin-top: 0;
    margin-bottom: 0.8rem;
    padding-bottom: 0.3rem;
    border-bottom: 1.5px solid rgba(104, 172, 229, 0.2);
    display: inline-block;
  }

  /* ── Compact Repository List ── */
  .repo-list {
    display: flex;
    flex-direction: column;
    gap: 0.45rem;
  }
  .repo-row {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 0.7rem 1rem;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.45);
    border: 1px solid rgba(104, 172, 229, 0.12);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    text-decoration: none;
    color: #2c3e50;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    position: relative;
    overflow: hidden;
  }
  .repo-row::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2.5px;
    background: linear-gradient(180deg, #002D72, #68ACE5);
    border-radius: 0 2px 2px 0;
    opacity: 0;
    transition: opacity 0.25s ease;
  }
  .repo-row:hover {
    transform: translateY(-1px);
    border-color: rgba(104, 172, 229, 0.3);
    box-shadow: 0 4px 14px rgba(0, 45, 114, 0.06);
    background: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    color: #2c3e50;
  }
  .repo-row:hover::before {
    opacity: 1;
  }

  .repo-row .repo-icon {
    color: #68ACE5;
    font-size: 0.95rem;
    flex-shrink: 0;
    opacity: 0.6;
    transition: opacity 0.2s ease;
  }
  .repo-row:hover .repo-icon {
    opacity: 1;
  }

  .repo-row-main {
    flex: 1;
    min-width: 0;
    display: flex;
    align-items: baseline;
    gap: 0.5rem;
    flex-wrap: wrap;
  }
  .repo-row .repo-name {
    font-family: "factoria", sans-serif;
    font-weight: 700;
    font-size: 0.9em;
    color: #002D72;
    white-space: nowrap;
  }
  .repo-row .repo-owner {
    font-weight: 300;
    color: #8a9bac;
    font-size: 0.88em;
  }
  .repo-row .repo-slash {
    color: #c8d6e0;
    font-weight: 300;
    margin: 0 0.05em;
  }
  .repo-row .repo-desc {
    font-family: "proxima-nova", sans-serif;
    font-weight: 300;
    font-size: 0.78em;
    color: #9baab8;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    flex: 1;
    min-width: 60px;
    max-width: 280px;
  }

  .repo-row-meta {
    display: flex;
    align-items: center;
    gap: 0.8rem;
    flex-shrink: 0;
  }
  .repo-stat {
    display: flex;
    align-items: center;
    gap: 0.2rem;
    font-family: "proxima-nova", sans-serif;
    font-weight: 500;
    font-size: 0.75em;
    color: #6b7c8d;
  }
  .repo-stat i, .repo-stat svg {
    font-size: 0.85em;
  }
  .repo-stat .star-icon {
    color: #d4a017;
  }
  .repo-stat .fork-icon {
    color: #8a9bac;
  }
  .repo-lang {
    display: flex;
    align-items: center;
    gap: 0.3rem;
    font-family: "proxima-nova", sans-serif;
    font-weight: 400;
    font-size: 0.72em;
    color: #8a9bac;
  }
  .repo-lang-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    flex-shrink: 0;
  }
  .repo-row .repo-arrow {
    font-size: 0.8rem;
    color: #68ACE5;
    opacity: 0;
    transform: translateX(-3px);
    transition: opacity 0.2s ease, transform 0.2s ease;
    flex-shrink: 0;
  }
  .repo-row:hover .repo-arrow {
    opacity: 1;
    transform: translateX(0);
  }

  /* ── Loading state ── */
  .loading-placeholder {
    font-family: "proxima-nova", sans-serif;
    font-weight: 300;
    font-size: 0.85em;
    color: #b0bec5;
    padding: 0.5rem 0;
  }

  /* ── Mobile ── */
  @media screen and (max-width: 768px) {
    .post .post-title { font-size: 1.8rem; }

    .gh-profile {
      flex-direction: column;
      text-align: center;
      gap: 0.8rem;
      padding: 1rem;
    }
    .gh-profile-stats {
      justify-content: center;
    }

    .repo-row {
      flex-wrap: wrap;
      padding: 0.65rem 0.85rem;
      gap: 0.3rem 0.6rem;
    }
    .repo-row-main {
      width: 100%;
      flex-wrap: wrap;
    }
    .repo-row .repo-desc {
      width: 100%;
      flex-basis: 100%;
      white-space: normal;
      max-width: none;
      margin-top: 0.1rem;
      font-size: 0.78em;
    }
    .repo-row-meta {
      width: 100%;
      margin-top: 0.2rem;
      gap: 0.7rem;
    }
    .repo-row .repo-arrow { display: none; }
  }
</style>

<div class="repositories-page">

<!-- GitHub Profile — populated by JS -->
<div id="gh-profile-container">
  <p class="loading-placeholder">Loading GitHub profile...</p>
</div>

<hr class="section-divider">

<div style="display: flex; align-items: baseline; gap: 0.6rem; margin-bottom: 0.8rem;">
  <h2 style="margin-bottom: 0;"><i class="fas fa-code-branch" style="font-size: 0.85em; margin-right: 0.3em; color: #68ACE5;"></i>Repositories</h2>
  <span id="total-stars" style="font-family: 'proxima-nova', sans-serif; font-weight: 300; font-size: 0.78em; color: #8a9bac;"></span>
</div>

<div id="repo-list-container" class="repo-list">
  <p class="loading-placeholder">Loading repositories...</p>
</div>

</div>

<script>
(function() {
  const GITHUB_USER = 'yashsmehta';
  const REPOS = [
    'automl/awesome-transformer-search',
    'countzerozzz/nodepert',
    'yashsmehta/MetaLearnPlasticity',
    'yashsmehta/archvision',
    'automl/NASLib',
    'yashsmehta/personality-prediction'
  ];

  // Language colors (GitHub convention)
  const LANG_COLORS = {
    'Python': '#3572A5',
    'Jupyter Notebook': '#DA5B0B',
    'JavaScript': '#f1e05a',
    'TypeScript': '#3178c6',
    'HTML': '#e34c26',
    'CSS': '#563d7c',
    'Shell': '#89e051',
    'TeX': '#3D6117',
    'Makefile': '#427819',
    'C++': '#f34b7d',
    'C': '#555555',
    'Rust': '#dea584',
    'Go': '#00ADD8',
    'Java': '#b07219',
    'Ruby': '#701516',
    null: '#8b949e'
  };

  // Fetch GitHub profile
  fetch('https://api.github.com/users/' + GITHUB_USER)
    .then(r => r.json())
    .then(user => {
      document.getElementById('gh-profile-container').innerHTML =
        '<a href="' + user.html_url + '" class="gh-profile" target="_blank" rel="noopener">' +
          '<img src="' + user.avatar_url + '" alt="' + GITHUB_USER + '" class="gh-profile-avatar">' +
          '<div class="gh-profile-info">' +
            '<div class="gh-profile-name">' + (user.name || GITHUB_USER) + '</div>' +
            '<div class="gh-profile-username">@' + user.login + '</div>' +
            (user.bio ? '<div class="gh-profile-bio">' + user.bio + '</div>' : '') +
          '</div>' +
          '<div class="gh-profile-stats">' +
            '<div class="gh-stat"><div class="gh-stat-num">' + user.public_repos + '</div><div class="gh-stat-label">Repos</div></div>' +
            '<div class="gh-stat"><div class="gh-stat-num">' + user.followers + '</div><div class="gh-stat-label">Followers</div></div>' +
            '<div class="gh-stat"><div class="gh-stat-num">' + user.following + '</div><div class="gh-stat-label">Following</div></div>' +
          '</div>' +
        '</a>';
    })
    .catch(function() {
      document.getElementById('gh-profile-container').innerHTML =
        '<a href="https://github.com/' + GITHUB_USER + '" class="gh-profile" target="_blank" rel="noopener">' +
          '<i class="fab fa-github" style="font-size:2rem;color:#68ACE5;"></i>' +
          '<div class="gh-profile-info">' +
            '<div class="gh-profile-name">' + GITHUB_USER + '</div>' +
            '<div class="gh-profile-username">View on GitHub</div>' +
          '</div>' +
        '</a>';
    });

  // Fetch all repos in parallel
  Promise.all(REPOS.map(function(repo) {
    return fetch('https://api.github.com/repos/' + repo)
      .then(r => r.json())
      .catch(function() { return null; });
  })).then(function(results) {
    // Sort by star count descending
    var indexed = results.map(function(d, i) { return { data: d, idx: i }; });
    indexed.sort(function(a, b) {
      var sa = (a.data && a.data.stargazers_count) || 0;
      var sb = (b.data && b.data.stargazers_count) || 0;
      return sb - sa;
    });

    var container = document.getElementById('repo-list-container');
    var html = '';

    indexed.forEach(function(item) {
      var data = item.data;
      var i = item.idx;
      if (!data || data.message) {
        // Fallback for failed fetch
        var parts = REPOS[i].split('/');
        html += '<a href="https://github.com/' + REPOS[i] + '" class="repo-row" target="_blank" rel="noopener">' +
          '<i class="fab fa-github repo-icon"></i>' +
          '<div class="repo-row-main">' +
            '<span class="repo-name"><span class="repo-owner">' + parts[0] + '</span><span class="repo-slash">/</span>' + parts[1] + '</span>' +
          '</div>' +
          '<span class="repo-arrow">&rarr;</span>' +
        '</a>';
        return;
      }

      var owner = data.owner ? data.owner.login : REPOS[i].split('/')[0];
      var langColor = LANG_COLORS[data.language] || LANG_COLORS[null];

      html += '<a href="' + data.html_url + '" class="repo-row" target="_blank" rel="noopener">' +
        '<i class="fab fa-github repo-icon"></i>' +
        '<div class="repo-row-main">' +
          '<span class="repo-name"><span class="repo-owner">' + owner + '</span><span class="repo-slash">/</span>' + data.name + '</span>' +
          (data.description ? '<span class="repo-desc">' + data.description + '</span>' : '') +
        '</div>' +
        '<div class="repo-row-meta">' +
          (data.language ? '<span class="repo-lang"><span class="repo-lang-dot" style="background:' + langColor + ';"></span>' + data.language + '</span>' : '') +
          '<span class="repo-stat"><i class="fas fa-star star-icon"></i>' + data.stargazers_count + '</span>' +
          '<span class="repo-stat"><i class="fas fa-code-branch fork-icon"></i>' + data.forks_count + '</span>' +
        '</div>' +
        '<span class="repo-arrow">&rarr;</span>' +
      '</a>';
    });

    container.innerHTML = html;

    // Show total stars
    var totalStars = results.reduce(function(sum, d) {
      return sum + ((d && d.stargazers_count) || 0);
    }, 0);
    var starsEl = document.getElementById('total-stars');
    if (starsEl && totalStars > 0) {
      starsEl.innerHTML = '<i class="fas fa-star" style="color:#d4a017;font-size:0.85em;"></i> ' + totalStars.toLocaleString() + ' total stars';
    }
  });
})();
</script>
