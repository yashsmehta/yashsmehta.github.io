---
layout: page
permalink: /publications/
title: Publications
nav: true
nav_order: 1
---

<style>
.publications {
  margin-top: 2rem;
  display: grid;
  gap: 1.5rem;
}

.publication-item {
  display: flex;
  padding: 0.8rem;
  border-radius: 12px;
  transition: all 0.3s ease;
  font-size: 0.95rem;
  border-left: 4px solid transparent;
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.04);
  height: 140px;
  overflow: hidden;
}

.publication-item:hover {
  box-shadow: 0 4px 8px rgba(0,0,0,0.08);
  transform: translateY(-2px);
}

.pub-image {
  width: 160px;
  min-width: 160px;
  margin-right: 1.2rem;
  aspect-ratio: 16/9;
}

.pub-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.preview-placeholder {
  width: 100%;
  height: 100%;
  background: #f5f5f5;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.preview-placeholder::after {
  content: '📄';
  font-size: 2.5rem;
  color: #ddd;
}

.pub-content {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.title-row {
  display: flex;
  align-items: flex-start;
  gap: 0.8rem;
  margin-bottom: 0.15rem;
}

.title-row .title {
  font-weight: 600;
  color: #2c3e50;
  font-size: 1rem;
  line-height: 1.2;
  flex: 1;
}

.topic-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 1.6rem;
  height: 1.6rem;
  border-radius: 50%;
  font-size: 0.9rem;
  flex-shrink: 0;
}

.pub-content .author {
  color: #666;
  margin-bottom: 0.3rem;
  font-size: 0.9rem;
  line-height: 1.2;
}

.pub-content .periodical {
  margin-top: 0.1rem;
  font-size: 0.9rem;
  margin-bottom: 0.3rem;
  line-height: 1.3;
  display: flex;
  align-items: center;
  gap: 0.4rem;
  flex-wrap: wrap;
}

.pub-content .periodical .venue {
  color: #0366d6;
}

.pub-content .periodical .venue em {
  font-style: normal;
  font-weight: 500;
}

.pub-content .periodical .year {
  color: #666;
  font-weight: 600;
}

.pub-links {
  display: flex;
  flex-wrap: wrap;
  gap: 0.4rem;
  margin-top: auto;
  padding-bottom: 0.2rem;
}

.pub-links a, .abstract-toggle {
  display: inline-flex;
  align-items: center;
  padding: 0.2rem 0.6rem;
  border-radius: 4px;
  color: #666;
  text-decoration: none;
  font-size: 0.85rem;
  background: rgba(0,0,0,0.05);
  transition: all 0.2s ease;
  height: 24px;
}

.pub-links a:hover {
  background: rgba(0,0,0,0.08);
  transform: translateY(-1px);
  color: #333;
}

.pub-links i {
  margin-right: 0.3rem;
  font-size: 0.9rem;
}

.abstract-toggle {
  cursor: pointer;
  user-select: none;
}

.abstract-content {
  display: none;
}

body.modal-open {
  overflow: hidden;
}

/* Topic colors and filters */
.topic-filters {
  margin-bottom: 2rem;
  display: flex;
  gap: 0.6rem;
  flex-wrap: wrap;
}

.topic-filter {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.4rem 1rem;
  border-radius: 30px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
  border: 2px solid transparent;
  user-select: none;
}

.topic-filter i {
  font-size: 1rem;
}

/* Bio-learning theme */
.topic-filter.bio-learning,
.topic-bio-learning .topic-icon {
  color: #e74694;
}

.topic-filter.bio-learning {
  background: rgba(231, 70, 148, 0.1);
  border-color: rgba(231, 70, 148, 0.2);
}

.topic-filter.bio-learning.active {
  color: #d11b71;  /* Bolder pink */
  background: rgba(231, 70, 148, 0.15);
  border-color: #d11b71;
  font-weight: 600;
}

/* NAS theme */
.topic-filter.nas,
.topic-nas .topic-icon {
  color: #3b82f6;
}

.topic-filter.nas {
  background: rgba(59, 130, 246, 0.1);
  border-color: rgba(59, 130, 246, 0.2);
}

.topic-filter.nas.active {
  color: #1d4ed8;  /* Bolder blue */
  background: rgba(59, 130, 246, 0.15);
  border-color: #1d4ed8;
  font-weight: 600;
}

/* Personality theme */
.topic-filter.personality,
.topic-personality .topic-icon {
  color: #10b981;
}

.topic-filter.personality {
  background: rgba(16, 185, 129, 0.1);
  border-color: rgba(16, 185, 129, 0.2);
}

.topic-filter.personality.active {
  color: #047857;  /* Bolder green */
  background: rgba(16, 185, 129, 0.15);
  border-color: #047857;
  font-weight: 600;
}

/* Remove the general active state that was making everything white */
.topic-filter.active {
  background: rgba(0,0,0,0.03);
}

.publication-item.topic-bio-learning {
  border-left-color: #e74694;
}

.publication-item.topic-nas {
  border-left-color: #3b82f6;
}

.publication-item.topic-personality {
  border-left-color: #10b981;
}

.topic-filter.active {
  background: currentColor;
  border-color: currentColor;
  color: white;
}

.publication-item.hidden {
  display: none;
}

@media (max-width: 768px) {
  .publication-item {
    flex-direction: column;
    height: auto;
  }
  
  .pub-image {
    width: 160px;
    margin: 0 auto 1rem auto;
  }
}

/* Modal styles */
.modal-overlay {
  display: none;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 1000;
}

.modal {
  display: none;
  position: absolute;
  background: white;
  padding: 1.2rem;
  border-radius: 12px;
  max-width: 600px;
  width: auto;
  max-height: 150px;
  overflow-y: auto;
  box-shadow: 0 4px 12px rgba(0,0,0,0.15);
  z-index: 1001;
  transform-origin: top left;
}

.modal.show {
  display: block;
  animation: popIn 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}

@keyframes popIn {
  from {
    opacity: 0;
    transform: scale(0.6);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.modal::before {
  content: '';
  position: absolute;
  top: -8px;
  left: 20px;
  width: 16px;
  height: 16px;
  background: white;
  transform: rotate(45deg);
  box-shadow: -2px -2px 5px rgba(0,0,0,0.06);
}

.modal-title {
  display: none;
}

.modal-body {
  font-size: 0.9rem;
  line-height: 1.5;
  color: #4a5568;
  padding-right: 0.5rem;
  padding-top: 0.2rem;
}

.modal-close {
  position: absolute;
  top: 0.5rem;
  right: 0.5rem;
  width: 1.5rem;
  height: 1.5rem;
  border: none;
  background: none;
  color: #94a3b8;
  font-size: 1.2rem;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: color 0.2s ease;
}

.modal-close:hover {
  color: #475569;
}

/* Add smooth scrollbar for the modal */
.modal::-webkit-scrollbar {
  width: 8px;
}

.modal::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 4px;
}

.modal::-webkit-scrollbar-thumb {
  background: #ccc;
  border-radius: 4px;
}

.modal::-webkit-scrollbar-thumb:hover {
  background: #bbb;
}
</style>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">

<div class="topic-filters">
  <div class="topic-filter bio-learning" data-topic="bio-learning">
    <i class="fas fa-brain"></i>
    <span>Biologically inspired learning</span>
  </div>
  <div class="topic-filter nas" data-topic="nas">
    <i class="fas fa-search"></i>
    <span>Neural architecture search</span>
  </div>
  <div class="topic-filter personality" data-topic="personality">
    <i class="fas fa-robot"></i>
    <span>Computational personality</span>
  </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
  const modal = document.createElement('div');
  modal.className = 'modal';
  modal.innerHTML = `
    <button class="modal-close">&times;</button>
    <div class="modal-body"></div>
  `;
  document.body.appendChild(modal);

  let currentToggle = null;
  let globalClickHandler = null;

  // Handle abstract toggles
  document.querySelectorAll('.abstract-toggle').forEach(toggle => {
    toggle.addEventListener('click', function(e) {
      e.preventDefault();
      e.stopPropagation();
      
      // If clicking the same toggle that's already open, close it
      if (currentToggle === this && modal.classList.contains('show')) {
        closeModal();
        return;
      }
      
      currentToggle = this;
      const paper = this.closest('.publication-item');
      const abstract = paper.querySelector('.abstract-content').textContent.trim();
      
      // Get click coordinates
      const clickX = e.clientX;
      const clickY = e.clientY + window.scrollY;
      
      // Position modal relative to click, but ensure it stays in viewport
      const modalWidth = 600;
      const viewportWidth = window.innerWidth;
      
      // Calculate left position
      let leftPos = clickX - 20;
      if (leftPos + modalWidth > viewportWidth) {
        leftPos = viewportWidth - modalWidth - 20;
      }
      leftPos = Math.max(20, leftPos);
      
      // Set position and transform origin
      modal.style.left = `${leftPos}px`;
      modal.style.top = `${clickY + 10}px`;
      modal.style.transformOrigin = `${clickX - leftPos}px 0`;
      
      modal.querySelector('.modal-body').textContent = abstract;
      
      // Remove existing click handler if any
      if (globalClickHandler) {
        document.removeEventListener('click', globalClickHandler);
      }
      
      // Add new click handler
      globalClickHandler = function(e) {
        if (!modal.contains(e.target) && e.target !== currentToggle) {
          closeModal();
        }
      };
      
      // Show modal and add click handler with delay
      modal.classList.add('show');
      setTimeout(() => {
        document.addEventListener('click', globalClickHandler);
      }, 0);
    });
  });

  // Close button handler
  modal.querySelector('.modal-close').addEventListener('click', function(e) {
    e.stopPropagation();
    closeModal();
  });

  // Close on escape key
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && modal.classList.contains('show')) {
      closeModal();
    }
  });

  function closeModal() {
    modal.classList.remove('show');
    if (globalClickHandler) {
      document.removeEventListener('click', globalClickHandler);
      globalClickHandler = null;
    }
    currentToggle = null;
  }

  // Topic filtering functionality
  const filters = document.querySelectorAll('.topic-filter');
  const papers = document.querySelectorAll('.publication-item');
  let activeFilters = new Set();

  filters.forEach(filter => {
    filter.addEventListener('click', function() {
      const topic = this.dataset.topic;
      this.classList.toggle('active');
      
      if (this.classList.contains('active')) {
        activeFilters.add(topic);
      } else {
        activeFilters.delete(topic);
      }

      papers.forEach(paper => {
        if (activeFilters.size === 0) {
          paper.classList.remove('hidden');
        } else {
          const shouldShow = Array.from(activeFilters).some(filter => 
            paper.classList.contains(`topic-${filter}`)
          );
          paper.classList.toggle('hidden', !shouldShow);
        }
      });
    });
  });
});
</script>

<div class="modal-overlay">
  <div class="modal">
    <div class="modal-header">
      <h3 class="modal-title"></h3>
      <button class="modal-close">×</button>
    </div>
    <div class="modal-body"></div>
  </div>
</div>

<div class="publications">
{% bibliography --file papers --sort_by year --order descending %}
</div>
