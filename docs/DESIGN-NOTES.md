# Portfolio design and sources

Prepared 22 October 2026. This is a static portfolio for readers who need to understand a practical problem and inspect the work before reading code. No analytics, external font CDN or third-party runtime is included.

## Inspected professional references

- [Brittany Chiang](https://brittanychiang.com/), opened live and screenshot inspected on 22 October 2026. Useful mechanism: a concise personal introduction beside readable, evidence-linked project descriptions; capabilities appear with actual work. This portfolio keeps direct links to the reviewed contribution and reproduction evidence. It does not copy the site's artwork, dark theme, cursor effect or personal claims.
- [Seán Halpin](https://www.seanhalpin.xyz/), opened live and screenshot inspected on 22 October 2026. Useful mechanism: large type, generous spacing and project presentation that leads with an understandable product. This portfolio uses a large editorial opening and one dominant real product image, then quieter case rows. It does not reuse his illustrations, project graphics, colors or animations.
- [Brittany Chiang v4 source](https://github.com/bchiang7/v4): its [MIT license](https://raw.githubusercontent.com/bchiang7/v4/main/LICENSE) was checked. The Gatsby/styled-components template would add an unnecessary build/runtime for this small static hub. No code or assets from it were incorporated.

## Incorporated supply and licenses

- The existing [Web Reference Design showcase](https://github.com/builtbyhuy/web-reference-design) supplies the permissively licensed static structure and baseline CSS idioms: local font loading, a bounded page width, visible keyboard focus, a skip link, responsive project presentation and reduced-motion handling. [Its MIT license](https://github.com/builtbyhuy/web-reference-design/blob/main/LICENSE) was checked live; the copyright notice is retained in `LICENSE`. The hub is an adaptation with a new content hierarchy and cream/ink/cobalt editorial system.
- `assets/manrope-variable.ttf` and `assets/manrope-OFL.txt` are copied from that existing project. The [official Google Fonts Manrope license](https://github.com/google/fonts/blob/main/ofl/manrope/OFL.txt) was checked on 22 October 2026. Manrope uses SIL OFL 1.1. The full notice is retained alongside the font. The typeface is self-hosted and supports the English and Vietnamese copy in this hub.
- `assets/fieldnote-after.png`, `assets/fieldnote-before.png` and `assets/fieldnote-mobile.png` are actual existing screenshots of Huy's Web Reference Design example, copied from its local `examples/fieldnote/evidence/` folder. The screenshot includes its AI-generated courtyard study. [Project provenance](https://github.com/builtbyhuy/web-reference-design/blob/main/PROVENANCE.md) records the example and assets. FIELDNOTE is a fictional studio and the before page is a deliberately flawed fixture. That boundary appears in captions. The image is not evidence of architectural/client work.
- Georgia is used only as a locally available system-font fallback for a small display role. No font file is redistributed for it.
- No external gallery artwork, client logos, stock photography, paid template or specialist service is used. Original diagrams on the vehicle page explain actual source behavior; the numeric panel is labeled as local synthetic regression evidence.
- `assets/portfolio-featured.png` is an inspected 1200 × 628 browser capture of the original `cover.html` in this folder. `assets/wrd-featured.png` is an inspected 1200 × 628 unmodified browser capture of the public [Web Reference Design homepage](https://builtbyhuy.github.io/web-reference-design/), captured on 22 October 2026. Both are ready image files, not placeholder thumbnails. The product homepage capture predates the new brief-composer integration.

## Specific adaptation decisions

- **First viewport:** name/navigation above “From idea. To working tool.” A short explanation presents Huy's ability to direct AI through research, implementation, testing, iteration and usable delivery. The large product example follows immediately rather than a generic feature-card grid.
- **Hierarchy:** one usable product first, then two bounded cases. QuoteLens and PourLab remain optional experiments in a native disclosure.
- **Typography:** Manrope for functional text, restrained Georgia italic for the editorial title. Headings use tight tracking; body text has a comfortable reading measure.
- **Palette:** warm paper `#f6f5ef`, ink `#202722`, muted text `#5c655d`, cobalt `#274ad8`. Cobalt indicates product identity and selected emphasis; primary buttons use ink.
- **Media:** an actual FIELDNOTE capture is framed in plain browser chrome. Its caption explains what it is. No fake dashboard is used for a source-only workflow.
- **Interaction:** native links and disclosures. Before/After buttons update the real captured example, their `aria-pressed` state and a live caption; keyboard operation is native. No carousel, scroll hijacking or continuous decorative animation.
- **Mobile:** the introduction and product become one column. Content precedes its action; row summaries sit below titles; workflow nodes stack. The header keeps only the essential local navigation.
- **Motion:** only smooth in-page scrolling, disabled with `prefers-reduced-motion: reduce`. No content depends on animation.

## Content provenance and limits

- [Vehicle workflow and its pinned case](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi/blob/9f05f77547a33a82f644c2ea60a63ae9e0fb8cbb/docs/CASE-CONCURRENT-FIRST-ENTRY.md): local PostgreSQL regression evidence, not production usage. The hub does not expose workshop records or account credentials.
- [python-docx-ng PR #131](https://github.com/toxicphreAK/python-docx-ng/pull/131): merged upstream contribution. The issue/diagnosis came from upstream. The hub credits the correction and regression contribution without claiming independent discovery or employment.
- AI is presented as a working capability: Huy defines goals and constraints, directs the build, evaluates the result and guides revisions. The portfolio demonstrates this through usable tools, recorded checks and handover instructions. Detailed cases retain relevant implementation provenance; personal technical skills are described only through the work actually shown.

The portfolio was produced locally. Publication status and any LinkedIn changes are separate from these files.

## AI capability positioning revision — 22 October 2026

Reframed the introduction and case copy around directing AI to produce useful tools: define the task, guide implementation, evaluate results, refine and hand over. Replaced repeated support disclaimers with concrete contribution and outcome descriptions. Kept the selected visual direction and factual example/data boundaries.

Applied ui-ux-pro-max to this copy revision, including its Heading Line Balance guidance and body-text readability checks. Inspected the revised homepage on desktop and at a 390-pixel mobile width. Checked 320, 390, 1280 and 1440-pixel layouts: no horizontal overflow, local Manrope loaded, body line-height 1.65. Recreated and inspected the 1200 × 628 Featured cover from cover.html. This was a focused content and layout review; the earlier interaction evidence still refers to the unchanged controls and product behavior.