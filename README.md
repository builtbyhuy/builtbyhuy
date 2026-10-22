# Hồ Khắc Huy

**Software implementation · Python & JavaScript · Workflow automation**  
Hanoi, Vietnam · English / Vietnamese

I build tools around the details that make a workflow reliable: valid inputs,
correct calculations, clear failure states and decisions that can be checked.
My background in import/export documentation shapes that focus on information,
exceptions and traceability.

## Reviewed upstream

### [python-docx-ng — fixing a style that could be created but not retrieved](https://github.com/toxicphreAK/python-docx-ng/pull/131)

A valid style name containing quotation marks could break its XPath lookup.
I contributed the correction across style-name, style-ID and latent-style
lookups, using bound variables while preserving custom namespaces. Regression
cases cover the shared wrapper and public style API.

The upstream maintainer checked mixed quotes, save/load and namespace behavior,
then merged the change on 4 August 2026.

[Issue and original diagnosis](https://github.com/toxicphreAK/python-docx-ng/issues/121) ·
[Diff and regression tests](https://github.com/toxicphreAK/python-docx-ng/pull/131/files) ·
[Maintainer review](https://github.com/toxicphreAK/python-docx-ng/pull/131#issuecomment-5180241589)

## Engineering work

### [Vehicle workflow — separate operational records from reporting](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi)

A Node.js workflow connects Telegram photo intake, plate extraction, vehicle
entry/exit records and Google Sheets reporting. The March 2026 migration moves
vehicle-state decisions into a PostgreSQL function and keeps Sheets as an
asynchronous reporting mirror. Database and mirror-failure tests sit alongside
the implementation.

The design separates the source of truth from its reporting view, so a failed
spreadsheet refresh is logged without blocking the database operation. A later
concurrency case reproduces two first-entry requests creating two active records,
then moves the transaction lock before lookup. It checks the real PostgreSQL
behavior, migration path, rollback and independent plates.

[Concurrency case](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi/blob/9f05f77547a33a82f644c2ea60a63ae9e0fb8cbb/docs/CASE-CONCURRENT-FIRST-ENTRY.md) ·
[Migration and tests](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi/commit/e38b44ce4fe0cc6d56f0654ae5cd4a33cd948e4d) ·
[Database contract](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi/blob/e38b44ce4fe0cc6d56f0654ae5cd4a33cd948e4d/supabase/schema.sql) ·
[Reporting mirror](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi/blob/e38b44ce4fe0cc6d56f0654ae5cd4a33cd948e4d/src/sheets-sync.js)

### [Codex Plugin Check — check what a released binary actually discovers](https://github.com/builtbyhuy/codex-plugin-check)

An experimental Node.js CLI and GitHub Action that reconciles plugin installation
and discovery responses into a structured receipt. It checks the requested
checkout against installed identity and distinguishes discovered skills,
untrusted hooks and declared integrations.

The key decision: a declared capability is not evidence that it ran. The strict
Linux/Docker probe uses a read-only checkout, denied network access and temporary
state; diagnostic mode has a separate contract. Archived receipts cover ten pinned
public-plugin fixtures on Codex 0.146.1 and 0.147.0. Ordinary tests and installed-package
checks run on both Windows and Linux in CI.

[Source and run instructions](https://github.com/builtbyhuy/codex-plugin-check) ·
[Fixture inputs and receipts](https://github.com/builtbyhuy/codex-plugin-check/blob/main/docs/evidence/public-fixture-matrix.md) ·
[Receipt contract](https://github.com/builtbyhuy/codex-plugin-check/blob/main/docs/receipt.schema.json)

### [QuoteLens — keep a quote comparison attached to its source](https://builtbyhuy.github.io/quotelens-review-workbench/)

A browser workbench for entering a purchase request, importing CSV offers and
comparing whole-pack costs, minimum orders and entered delivery fees. Source-row
references make a selection inspectable. Changing a decision input invalidates
its review, even when the total stays the same.

This independent engineering project focuses on exact money, revision state and
portable records. Try a new request rather than only the included synthetic example.

[Working app](https://builtbyhuy.github.io/quotelens-review-workbench/) ·
[Case study](https://builtbyhuy.github.io/quotelens-review-workbench/case-study.html) ·
[Source and checks](https://github.com/builtbyhuy/quotelens-review-workbench)

### [PourLab — edit a puzzle, play it, inspect a checked solution](https://builtbyhuy.github.io/pourlab-puzzle-studio/)

A browser water-sort studio with custom levels, legal manual play, Undo and exact
search in a worker. Solutions are checked through the move rules before replay.
A search budget ending produces an unresolved result; it does not declare the
puzzle impossible. The solver evaluation includes a separate BFS oracle.

This independent engineering project connects rules, editor state, search,
storage recovery and an interactive 3D board with a complete 2D fallback.

[Working studio](https://builtbyhuy.github.io/pourlab-puzzle-studio/) ·
[Guide and case study](https://builtbyhuy.github.io/pourlab-puzzle-studio/about.html) ·
[Source and checks](https://github.com/builtbyhuy/pourlab-puzzle-studio)

## Working with AI

I use Codex extensively for research, implementation, debugging, tests and
documentation. The repositories make the resulting code, technical decisions and
reproduction steps available for review.

Interested in software implementation, Python utilities and workflow automation.

[CV](https://github.com/builtbyhuy/builtbyhuy/blob/main/CV.md) ·
[LinkedIn](https://www.linkedin.com/in/builtbyhuy/) ·
[Email](mailto:hohuyblon@gmail.com)
