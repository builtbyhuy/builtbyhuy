# Portfolio validation

Checked locally on 22 October 2026. Preview: `http://127.0.0.1:8874/` while the task's local preview server is running.

## Rendered review

- Home and all three case pages inspected at a 1440 CSS-pixel desktop width.
- Home, all three case pages and the Vietnamese guide rendered at 390 CSS pixels. No horizontal document overflow was observed. The local Manrope font loaded and all displayed images loaded.
- The final full-page mobile captures were opened and visually inspected. Case labels, headings, summaries, actions, captions, diagrams and footer links remain readable in a single column.
- The initial IAB device-emulation capture squeezed content even though DOM widths were normal. That evidence was rejected and replaced after resetting emulation and setting the screen/viewport consistently. Final inspected captures are in `evidence/`; they do not show the rejected state.
- The 1200 × 628 original portfolio cover was captured and opened; the saved PNG is in `assets/portfolio-featured.png`.

## Used interactions

- Before button: switches to the actual before screenshot, updates the live caption and `aria-pressed` states.
- After button, activated with Enter: switches back to the actual after screenshot and updates the pressed state.
- Native technical disclosure activated with Enter: opens its evidence and limits.
- Keyboard Tab reaches a visible skip link; Enter moves focus to `main`.
- Emulated `prefers-reduced-motion: reduce` changes computed document scroll behavior to `auto`.
- Local HTML links, fragment IDs and CSS asset references checked against the delivered files; see `evidence/local-link-check.json` for the actual result.

## Evidence

`evidence/browser-checks.json` records page widths, loaded images and font checks. `evidence/interaction-checks.json` records the observed keyboard and comparison states. PNG captures show the final rendered desktop and mobile views.

## Limits

This validates the local static hub, not a publication or LinkedIn update. The new Web Reference Design brief-composer URL is an integration dependency owned by the parallel product task; verify its deployed route before publishing the hub. The hub makes no live bot, customer adoption, production performance or business-impact claim. No private operational records are included.

This is a practical render and interaction review, not a full accessibility conformance audit or a claim of usability testing with outside participants.

## Readable sources route follow-up

Added `sources.html` using the same local visual system, and updated the five public footer links to use it. The editable `DESIGN-NOTES.md` is retained unchanged. Every non-title note line was checked against the HTML text to preserve source, licensing and provenance details. All internal HTML links, anchors and CSS assets were rechecked; the result is in `evidence/sources-check.json`.

The local `/sources.html` route was opened and visually inspected in Chrome at its ordinary 1920-pixel viewport. Its four content sections and eleven reference links rendered; no horizontal overflow was observed. `evidence/sources-desktop.png` records the view. This follow-up does not publish the changed files.
