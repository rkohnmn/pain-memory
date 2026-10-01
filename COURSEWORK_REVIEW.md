# Coursework Review & Portfolio Audit Report

**Author:** Robert Kohn  
**Institution:** Muhlenberg College  
**Course:** COM 256 — Interactive Web Design (Spring 2026)  
**Project:** *Pain and Memory: Memory-Shaped Affective Accumulation*  
**Date of Audit:** October 2026  

---

## Executive Summary

A comprehensive recursive audit was conducted on the HTML and web development coursework folder. The coursework comprises a large-scale, multi-tiered interactive hypermedia art installation titled ***Pain and Memory: Memory-Shaped Affective Accumulation***. 

The original folder contained a mixture of student-authored core work, early structural drafts, instructor starter templates, legacy stylesheets, and third-party libraries. A dedicated clean directory, [`github-html-coursework/`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/github-html-coursework/), was constructed containing **only** verified student-authored work, third-party libraries under open-source licenses, and clean documentation. The original source directory remains completely untouched.

---

## Best Work to Publish

The coursework components are ranked qualitatively below from most impactful to supporting modules:

### 1. Title & Experience Gateway (`index.html`)
- **Original File:** [`index.html`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/index.html) (647 lines)
- **Proposed Portfolio Role:** Flagship project landing page and interactive entry gateway
- **Why It Is Valuable:** Demonstrates extraordinary aesthetic polish and frontend sophistication. Pairs high-craft editorial serif typography (*Cinzel*, *Cormorant Garamond*, *EB Garamond*) with a custom dark-mode atmospheric theme.
- **Skills Demonstrated:**
  - Procedural 2D Canvas particle simulation with velocity decay, boundary wrapping, and opacity fade.
  - Multi-tier mouse-following parallax depth layers (`.parallax-layer` with configurable data depths).
  - Ambient radial illumination drift animations using CSS keyframes.
  - Fluid responsive typography with CSS `clamp()`.
  - SVG fractal noise grain overlay.
  - Cross-window launcher with dynamic screen centering calculations.
- **Cleanup Performed:** Verified link targets, relative paths, and script integrity. Preserved all original physics and aesthetic choices.
- **Remaining Improvements:** Add keyboard focus indicators for the main "Enter" button; add a `prefers-reduced-motion` media query to respect users with vestibular sensitivities.

### 2. The Navigation Portal (`portal.html`)
- **Original File:** [`portal.html`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/portal.html) (540 lines)
- **Proposed Portfolio Role:** Spatial hub and hypermedia threshold
- **Why It Is Valuable:** Solves complex layout and UX challenges by combining two 6-cell image ribbons with a centered typographic threshold card. Demonstrates sophisticated event-driven JavaScript state management.
- **Skills Demonstrated:**
  - CSS Grid with responsive column collapse (6 columns desktop $\rightarrow$ 4 columns tablet $\rightarrow$ 3 columns mobile).
  - Hover states with grayscale-to-color filter transitions and cell scaling.
  - Automated 15-second inactivity countdown timer linked to a visual CSS transition bar that resets on `mousemove`, `keydown`, and `click`.
  - Custom CSS corner-bracketed frame architecture (`.threshold-card`).
- **Cleanup Performed:** Normalized image filenames (resolved `Snow.jpg` vs `snow.jpg` casing). Verified return links and navigation flow.
- **Remaining Improvements:** Add accessible ARIA live region notifications for the countdown bar; ensure cells are keyboard-navigable via standard tab order.

### 3. Phase 2: Beta Advanced Hypertext & Typographic Kernels (`beta/`)
- **Original Folder:** [`beta/`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/beta/) (`image/`, `imagine/`, `text/`)
- **Proposed Portfolio Role:** The advanced philosophical and typographic tier of the installation
- **Why It Is Valuable:** Represents the conceptual and stylistic peak of the coursework. Completely discards boxed container structures in favor of ethereal, floating text kernels styled via [`beta-text-design.css`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/github-html-coursework/beta/text/beta-text-design.css).
- **Skills Demonstrated:**
  - Design systems: multi-tier typography hierarchy (`.emph`, `.emph-more`) and a 6-tier muted chromatic scale (`.color-1` to `.color-6`).
  - Fixed-stage viewport containment (`.stage` 1200×900) hosting 3600×2700 original photography.
  - Layered text shadows providing legibility directly over photography without opaque card containers.
- **Cleanup Performed:** Excluded instructor starter templates; repaired broken relative links; redirected orphaned "return" links from the removed template back to the portal; normalized image casing.
- **Remaining Improvements:** Group floating text links into semantic `<nav>` or `<ul>` structures for improved screen-reader discoverability.

### 4. Phase 1: Alpha Spatial & Layout Studies (`alpha/`)
- **Original Folder:** [`alpha/`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/alpha/) (`image/`, `imagine/`, `text/`)
- **Proposed Portfolio Role:** Foundation hypermedia layer and CSS refactoring demonstration
- **Why It Is Valuable:** Shows tangible evidence of software engineering growth and code cleanup. In `alpha/text/`, Robert refactored 10 repetitive, single-file stylesheets into a single unified 7-class layout system ([`design.css`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/github-html-coursework/alpha/text/design.css)).
- **Skills Demonstrated:**
  - Complex polygon coordinate mapping on HTML `<map>` elements.
  - CSS code consolidation and DRY (Don't Repeat Yourself) architecture.
  - Seven layout archetypes: scattered drift, corridor perspective, spiral echo, diagonal descent, cognitive loop, door hinge arc, and default containers.
  - Glassmorphic styling with `backdrop-filter: blur(2px)` and fluid sizing via `clamp()`.
- **Cleanup Performed:** Completed the truncated gallery index ([`image/index.html`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/github-html-coursework/alpha/image/index.html)) with the missing 10th fragment (`tf.html`), return navigation, and closing tags; fixed broken relative links to `doorr.html` and `oculuss.html`.
- **Remaining Improvements:** Modernize image maps by augmenting them with SVG overlay polygons for superior resolution independence.

### 5. Architectural Hypertext Link Matrix (`kohn_EMATRIX.csv`)
- **Original File:** [`kohn_EMATRIX.csv`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/kohn_EMATRIX.csv)
- **Proposed Portfolio Role:** Technical system architecture and graph routing specification
- **Why It Is Valuable:** Proves intentional structural engineering behind the user experience. Demonstrates how a quantitative/mathematical mindset (graph theory, node degree, state machines) informs interactive web architecture.
- **Skills Demonstrated:**
  - Hypermedia graph planning: exactly 5 outbound destinations per node across 40+ system nodes.
  - Cross-quadrant routing balancing visual spatial nodes and philosophical text nodes.
- **Cleanup Performed:** Audited and cross-checked against HTML link targets.

### 6. Academic Bibliography & Media Theory (`credits.html`)
- **Original File:** [`credits.html`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/credits.html)
- **Proposed Portfolio Role:** Research context and thematic grounding
- **Why It Is Valuable:** Demonstrates intellectual depth and media literacy by grounding the web installation in narrative analyses of memory, grief, and identity across 10 media texts.
- **Skills Demonstrated:** Responsive CSS list formatting, animated underline hover interactions, external link security (`rel="noopener noreferrer"`).
- **Cleanup Performed:** Audited for privacy; confirmed no phone numbers, student IDs, or private data exist.

---

## Included Files

The following files were copied, cleaned, and verified inside [`github-html-coursework/`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/github-html-coursework/):

```
github-html-coursework/
├── .gitignore
├── README.md
├── COURSEWORK_REVIEW.md
├── index.html
├── portal.html
├── credits.html
├── kohn_EMATRIX.csv
├── alpha/
│   ├── README.md
│   ├── image/
│   │   ├── 1103.html, 2201.html, corn.html, door.html, hall.html
│   │   ├── ldr.html, oculus.html, snow.html, snowman.html, tf.html
│   │   ├── index.html (Completed gallery index)
│   │   ├── jQuery-rwdImageMaps-master/ (Matt Stow MIT library)
│   │   ├── js/ (imageMapResizer.min.js, ios-orientationchange-fix.min.js)
│   │   └── media/ (10 normalized 1200x900 photographs)
│   ├── imagine/
│   │   └── 1103.html, 2201.html, corn.html, door.html, hall.html
│   │       ldr.html, oculus.html, snow.html, snowman.html, tf.html
│   └── text/
│       ├── 11103.html, 22201.html, coorn.html, doorr.html, halll.html
│       ├── ldrr.html, oculuss.html, snoww.html, snowwoman.html, tff.html
│       └── design.css (Refactored consolidated 7-class stylesheet)
└── beta/
    ├── README.md
    ├── image/
    │   ├── 1103.html, 2201.html, corn.html, door.html, hall.html
    │   ├── ldr.html, oculus.html, snow.html, snowman.html, tf.html
    │   ├── jQuery-rwdImageMaps-master/ (Matt Stow MIT library)
    │   ├── js/ (imageMapResizer.min.js, ios-orientationchange-fix.min.js)
    │   └── media/ (10 normalized 3600x2700 original photographs)
    ├── imagine/
    │   └── 1103.html, 2201.html, corn.html, door.html, hall.html
    │       ldr.html, oculus.html, snow.html, snowman.html, tf.html
    └── text/
        ├── archive_self.html, caregiving_labor.html, endurance_survival.html
        ├── ethical_repetition.html, friendship_decay.html, memory_tyranny.html
        ├── pain_expression.html, relational_pain.html, sensory_memory.html
        ├── temporal_dissonance.html
        └── beta-text-design.css (Typography-first design system)
```

---

## Excluded Instructor Material

The following files were identified as instructor/course-provided starter code or templates and were **completely excluded** from the portfolio:

| Excluded File | Identifying Evidence | Rationale |
| :--- | :--- | :--- |
| `alpha/text/index.html` | Contains instructor comments: `<!-- Do no forget the </div> at the end of the document, which must be uncommented when you use the image as a template... -->` and `<div class="overlay-text">Your Text Here</div>` | Starter template provided to students for the text assignment. |
| `beta/image/index.html` | Contains placeholder `<img src="media/xxx.jpg" width="1200" height="900" usemap="#abc" />`, dummy links `xxx.html`, and coordinate comment `coords="x1,y1,x2,y2,x3,y3"` | Boilerplate image map template provided by instructor. |
| `beta/imagine/index.html` | Identical boilerplate image map template with dummy links to `xxx.html` and placeholder comments. | Starter template provided by instructor. |
| `beta/text/index.html` | Identical boilerplate template with placeholder `xxx.jpg` and `xxx.html`. | Starter template provided by instructor. |
| `beta/textold/index.html` | Identical boilerplate template with placeholder `xxx.jpg`. | Starter template provided by instructor. |
| `beta/textold/template.html` | Contains placeholder `<div id="container"><a href="">word</a></div>` and commented-out `xxx.jpg`. | Starter template provided by instructor. |
| `alpha/image/media/index.html` | 87-byte empty document (`<title>index</title><body></body>`) dated 2019. | Blank server-directory protection file supplied with course materials. |
| `alpha/text/media/index.html` | 87-byte empty document dated 2019. | Blank placeholder file. |
| `beta/image/media/index.html` | 87-byte empty document dated 2019. | Blank placeholder file. |
| `beta/textold/media/index.html` | 87-byte empty document dated 2019. | Blank placeholder file. |

---

## Excluded Low-Value Work & Obsolete Drafts

The following student-authored directories were excluded because they represent superseded development iterations:

1. **`alpha/text/OLD/` (10 CSS files):**
   - Files: `11103.css`, `22201.css`, `corn.css`, `doorr.css`, `halll.css`, `ldrr.css`, `oculuss.css`, `snoww.css`, `snowwman.css`, `tff.css`.
   - Rationale: Robert successfully refactored and consolidated all 10 of these individual stylesheets into [`alpha/text/design.css`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/github-html-coursework/alpha/text/design.css). Publishing the un-refactored copies would dilute the clean architecture of the repository.
2. **`beta/textold/` (13 HTML and CSS files):**
   - Files: Early iterations of `archive_self.html`, `caregiving_labor.html`, etc.
   - Rationale: These files used unstyled `box0` containers and dead links to speculative files (`identity_spatial.html`, `distributed_archive.html`). They were completely superseded by the final, polished versions in `beta/text/` that utilize `beta-text-design.css`.

---

## Uncertain Authorship

- **None.** All files retained in the portfolio have clear authorship:
  - Custom HTML, CSS, JavaScript, interactive logic, copy, and layout: Robert Kohn.
  - Photography: Robert Kohn (original photography of campus spaces, landscape, and interiors).
  - External plugins: Clearly attributed open-source libraries (Matt Stow, David J. Bradshaw).

---

## Third-Party Material & Attribution

The portfolio incorporates the following third-party dependencies, all permitted under standard open-source licenses:

1. **jQuery 1.10.2** (CDN reference):
   - Hosted via Google Hosted Libraries CDN (`https://ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js`).
   - Standard MIT License.
2. **jQuery-rwdImageMaps** (Matt Stow):
   - Stored in `alpha/image/jQuery-rwdImageMaps-master/` and `beta/image/jQuery-rwdImageMaps-master/`.
   - Used to recalculate polygonal coordinates dynamically upon viewport resize.
   - MIT License preserved in local directory (`LICENSE` and `README.md` intact).
3. **imageMapResizer.min.js** (David J. Bradshaw):
   - Stored in `js/` directories.
   - MIT License.
4. **ios-orientationchange-fix.min.js**:
   - Viewport orientation fix for legacy mobile browsers. Public Domain / MIT.
5. **Google Fonts**:
   - *Cinzel* (OFL - Open Font License)
   - *Cormorant Garamond* (OFL)
   - *EB Garamond* (OFL)

---

## Privacy & Security Findings

A regex security audit was executed across all coursework files searching for credentials, tokens, phone numbers, private emails, and student ID numbers:
- **Zero Secrets / API Keys / Passwords:** No authentication keys or sensitive tokens exist.
- **Personal Information:** Robert Kohn's public LinkedIn URL is present in `credits.html` and repository documentation. No home addresses, personal phone numbers, or student ID numbers were found.
- **Instructor Privacy:** The instructor is identified by name (`David Tafler`) as course faculty. No private instructor email, phone number, office location, grading rubric, or private feedback is exposed.

---

## Accessibility Findings

### Strengths
- **Document Structure:** All pages specify `<!DOCTYPE html>`, `lang="en"`, character encoding (`UTF-8`), and proper viewport meta tags.
- **Fluid Typography:** Consistent use of CSS `clamp()` prevents text truncation and preserves readability across screen widths.
- **Contrast Ratios:** Text in `alpha/imagine` and `index.html` utilizes semi-transparent dark backdrops (`rgba(22, 20, 28, 0.82)`) and radial gradient overlays to ensure sufficient contrast against photographic backgrounds.
- **External Links:** Links opening in new tabs in `credits.html` include `rel="noopener noreferrer"`.

### Areas for Improvement
- **Image Maps Keyboard Accessibility:** HTML `<area>` elements can be difficult to navigate via keyboard tabs. In a future iteration, augmenting these with SVG overlay paths with visible `:focus` outlines would enhance accessibility.
- **Alternative Text:** Several `<area>` tags use brief or functional alt labels (`alt="door"`, `alt="wall"`). Descriptive alt text explaining the destination or visual context would improve screen-reader utility.
- **Motion Sensitivity:** The landing page features a continuous canvas particle system and mouse parallax. Adding `@media (prefers-reduced-motion: reduce)` would ensure compliance for users sensitive to vestibular motion.

---

## Recommended High-Impact Improvements

If you wish to polish this portfolio further before sharing it with recruiters or interviewers, consider these high-impact enhancements:

1. **Add `prefers-reduced-motion` in [`index.html`](file:///c:/Users/RobTop/Downloads/project%20-%20kohn%20robbie-20261001T003143Z-1-001/project%20-%20kohn%20robbie/github-html-coursework/index.html):**
   ```css
   @media (prefers-reduced-motion: reduce) {
       #particles { display: none; }
       .ambient { animation: none; }
       .parallax-layer { transform: none !important; }
   }
   ```
2. **Add a Visual Preview / Hero Screenshot:**
   Take a high-resolution screenshot of `index.html` and `portal.html`, place them in an `assets/` directory, and embed them in the master repository `README.md`.
3. **Keyboard Focus Highlights:**
   Add explicit `:focus-visible` styles to the `.enter-btn` in `index.html` and the `.strip-item` buttons in `portal.html` to guarantee full keyboard navigability.
4. **Deploy as GitHub Pages (Optional):**
   When you decide to publish the repository to GitHub, enable GitHub Pages pointing to the `main` branch. Because all paths and image casings have been strictly normalized, the entire installation will run live on the web with zero additional configuration.
