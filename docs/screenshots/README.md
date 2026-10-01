# Project Screenshots Manifest

This directory contains high-resolution renders of the ***Pain and Memory*** interactive hypermedia web installation. All screenshots were captured directly from the live static pages running in Microsoft Edge (Chromium engine) via Puppeteer Core at a 2× device pixel ratio for retina-quality sharpness.

## Screenshot Index

| File | Screen / Feature | Viewport | Scale | Purpose |
| :--- | :--- | :--- | :--- | :--- |
| [`01-overview.png`](01-overview.png) | Title & Experience Gateway (`index.html`) | 1440×900 | 2× (2880×1800) | Primary visual identity and aesthetic overview: serif typography (*Cinzel*, *Cormorant Garamond*), live HTML5 Canvas particle physics, ambient radial illumination, and the "Enter" portal launch trigger. |
| [`02-main-workflow.png`](02-main-workflow.png) | Navigation Portal Interface (`portal.html`) | 1440×900 | 2× (2880×1800) | The central navigation threshold: dual 6-cell image ribbons (12 spatial cells), corner-bracketed "Threshold: Absence without Resolution" typography, and the 15-second inactivity countdown timer bar. |
| [`03-spatial-hypermedia.png`](03-spatial-hypermedia.png) | Spatial Text Overlay Scene (`alpha/imagine/1103.html`) | 1440×900 | 2× (2880×1800) | Core hypermedia output: photographic scene with radial vignette contrast and spatially placed glassmorphic text containers exploring absence and memory artifacts. |
| [`04-typographic-design-system.png`](04-typographic-design-system.png) | Ethereal Text Kernels (`beta/text/archive_self.html`) | 1440×900 | 2× (2880×1800) | Advanced typography-first design system (`beta-text-design.css`): floating text phrases directly superimposed on photographic space with multi-tier font weight emphasis (`.emph`, `.emph-more`), layered drop shadows, and a 6-tone muted chromatic palette. |
| [`05-mobile-responsive.png`](05-mobile-responsive.png) | Mobile Viewport Collapse (`portal.html`) | 390×844 | 2× (780×1688) | Demonstrates mobile-responsive CSS Grid behavior: the 6-column image ribbons smoothly collapse to 3 columns, preserving legible touch targets and central threshold framing on smartphone screens. |
| [`06-layout-archetype.png`](06-layout-archetype.png) | Consolidated Layout Engine (`alpha/text/11103.html`) | 1440×900 | 2× (2880×1800) | Demonstrates CSS consolidation: the "Scattered Drift" layout archetype from the refactored [`alpha/text/design.css`](../../alpha/text/design.css), showing how 10 repetitive stylesheets were unified into a DRY 7-class architectural engine. |

## Regeneration Instructions

To regenerate these screenshots:

1. Ensure Node.js (v18+) is installed.
2. Install `puppeteer-core` in your execution environment (`npm install puppeteer-core`).
3. Run the automated capture script pointing to Microsoft Edge or Google Chrome:
   ```bash
   node scratch/generate_docs_screenshots.js
   ```
4. Note on Timers & Animations:
   - `index.html` requires a delay of at least 3,000ms to allow the particle field and rise keyframes to settle into their equilibrium states.
   - `portal.html` requires a delay of ~2,000ms to capture the staggered ribbon cell fade-in.
