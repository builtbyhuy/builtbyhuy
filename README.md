# Hồ Khắc Huy

**From idea to working tool.**
Hanoi, Vietnam · English / Vietnamese

I use AI to build web tools, connect data workflows and fix software problems. Try a website-brief builder, trace a vehicle-recording workflow, or inspect a Python fix reviewed and merged by its maintainer. My background in import/export documentation shapes my focus on missing information, exceptions and traceability.

**[Explore my portfolio](https://builtbyhuy.github.io/builtbyhuy/)** · [LinkedIn](https://www.linkedin.com/in/builtbyhuy/) · [Email](mailto:hohuyblon@gmail.com)

## Web Reference Design

**For people planning a website with an AI coding tool.** Answer guided questions to create an editable brief, then use companion instructions and working examples to carry requirements and references through implementation and review.

- **[Create a website brief](https://builtbyhuy.github.io/web-reference-design/brief/):** customize a brief, download it and use it in your own coding agent. The browser tool prepares the instructions; your agent does the implementation.
- **[Explore the worked examples](https://builtbyhuy.github.io/web-reference-design/):** inspect desktop/mobile results and try the form interactions. The examples are fictional and create local previews.
- **[Install the skill or inspect the source](https://github.com/builtbyhuy/web-reference-design):** use the workflow on your own project, with resource attribution and license notes included.

The brief keeps the audience, page action, preserved behavior and checks together instead of scattered across chat messages. The browser composer organizes the request; your own AI coding tool implements the page.

<details>
<summary>Reviewed contribution and engineering cases</summary>

### A document-formatting bug, fixed and accepted upstream

A valid style containing quotation marks could be created but fail when retrieved. I contributed the maintainer-described correction to python-docx-ng with regression coverage. The maintainer reviewed and merged it.

[Reviewed PR #131](https://github.com/toxicphreAK/python-docx-ng/pull/131) · [Original issue and diagnosis](https://github.com/toxicphreAK/python-docx-ng/issues/121)

### Vehicle entry/exit records

A workflow connects Telegram photo intake, PostgreSQL records and a Google Sheets reporting view. Its concurrency case reproduces simultaneous requests creating duplicate active records and checks the correction with real database connections.

[Case and reproduction](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi/blob/9f05f77547a33a82f644c2ea60a63ae9e0fb8cbb/docs/CASE-CONCURRENT-FIRST-ENTRY.md) · [Source](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi)

### Codex Plugin Check

A CLI and GitHub Action record what specified released Codex versions discover from a plugin checkout. Structured results distinguish observed discovery from capabilities that are only declared.

[Source, checks and scope](https://github.com/builtbyhuy/codex-plugin-check)

</details>

<details>
<summary>Other interactive experiments</summary>

- **[QuoteLens](https://builtbyhuy.github.io/quotelens-review-workbench/):** compare supplier-offer costs and keep a local review linked to its inputs. [Source](https://github.com/builtbyhuy/quotelens-review-workbench)
- **[PourLab](https://builtbyhuy.github.io/pourlab-puzzle-studio/):** create a water-sort puzzle, play it and inspect a checked solution. [Source](https://github.com/builtbyhuy/pourlab-puzzle-studio)

These are independent projects; working demos are available for inspection.

</details>
