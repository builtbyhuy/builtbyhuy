# Hi, I'm Huy.

**I build web features, connect APIs and fix Python workflows.**

I can take a defined feature or defect from reproduction to a tested implementation
and clear handover. My preferred stack is **TypeScript, React/Next.js and Python**,
with SQL, webhooks, n8n, Make and Airtable.

Hanoi, Vietnam (UTC+7) · 10–20 hours/week for remote project work

[Discuss a project](mailto:hohuyblon@gmail.com) · [LinkedIn](https://www.linkedin.com/in/builtbyhuy/)

## Work you can inspect

### 1. A Python bug fix accepted by an upstream maintainer

**Problem:** a document style containing quotes could be created but could not
be looked up correctly.

**My contribution:** changed the affected XPath lookups to use bound variables,
passed them through the XML wrapper, and added regression coverage for quoted
names and injection-like input. The maintainer reviewed the edge cases and
merged the change.

[Review merged PR #131](https://github.com/toxicphreAK/python-docx-ng/pull/131) ·
[Read the reproduction and fix](notes/2026-09-06-xpath-variables.md)

**Relevant work:** Python debugging, document processing and regression tests.
*Open-source contribution.*

### 2. Proofline — a web interface with a working recovery flow

**Problem modeled:** a reviewer needs to see which requirements have evidence
and which still block a release.

**My contribution:** built the HTML/CSS/JavaScript interface, the acceptance
evaluator and its tests. The UI includes ready, loading, empty and error states.
A keyboard-focus fix keeps Retry from leaving focus on a hidden control.

**Try it:** [open the live interface](https://builtbyhuy.github.io/proofline-release-review/),
select **Error**, then **Retry**. Inspect the loading state and continue navigating
with the keyboard.

[Source and verification](https://github.com/builtbyhuy/proofline-release-review)

**Relevant work:** frontend features, internal tools and accessible error recovery.
*Independent technical sample with fictional release data; no backend or live deployment control.*

### 3. Webhook-to-CRM — duplicates, failures and retries made visible

**Problem modeled:** a repeated event or temporary API failure should not silently
create conflicting records or trigger unlimited retries.

**My contribution:** built the Python/SQLite processing boundary, signature
validation, duplicate/conflict checks, bounded retries and regression tests.
The local CLI preserves event identity across restarts and requires explicit
recovery after exhausted retries.

**Inspect it:** [read the one-page walkthrough and seven recorded runs](samples/webhook-walkthrough/),
or [follow the runnable scenarios](https://github.com/builtbyhuy/webhook-crm-reliability-sample#quick-start)
to compare a successful event, a duplicate and an exhausted retry.

**Relevant work:** API integrations, automation debugging and data validation.
*Independent sample with synthetic events and a simulated CRM. The preview API's
ledger is scoped to one request; it does not provide cross-request durability.*

### 4. A contractor website with a local request preview

**Problem modeled:** a homeowner needs to choose a service and explain the work without a long form.

[Try the page](https://builtbyhuy.github.io/contractor-site-sample/): choose a service,
preview a request using fictional details, then edit it. The responsive page includes
inline error messages, keyboard focus and an original house illustration.

[Source and sample boundaries](https://github.com/builtbyhuy/contractor-site-sample)

**Relevant work:** service landing pages and accessible frontend forms.
*Independent, Codex-assisted sample for a fictional company. No message is sent,
no request is booked, and no customer or conversion result is claimed.*

### 4. Practical Tools — ten local workflows with inspectable results

**Problem modeled:** everyday data and file tasks need useful outputs, clear review steps,
and predictable behavior when input is malformed or work is repeated.

**Implementation:** a Python/Flask workbench with receipt OCR, inventory review, CSV cleanup,
file organization, note search, application tracking, recall cards, image preparation,
data profiling and a local webhook delivery simulator.

[Explore the collection](https://github.com/builtbyhuy/practical-tools) ·
[Review the checks and limits](https://github.com/builtbyhuy/practical-tools/blob/main/docs/VERIFICATION.md)

**Relevant work:** Python, SQLite, form recovery, safe file operations, image processing,
idempotency and bounded retries.
*Independent, Codex-assisted portfolio collection with fictional examples. Local single-user
applications; no customer deployment or business result is claimed.*

## Other engineering work

- **SkillArena — independent product.** Built a Next.js, React and TypeScript
  sales-practice application with scenario simulation, transcript-backed
  debriefs, drills and rematches. Private implementation.
- **Workforce attendance — private business project.** Built an attendance
  application for a Vietnamese automotive operation.
- **Management reporting — private business work.** Built repeatable reporting
  from Odoo and spreadsheet data, with source tracking, validation and
  Excel/HTML/PDF outputs.

These descriptions identify my work; private project details and business
results are not presented as public case studies. My independent software and
automation work began in August 2023.

## A practical first assignment

A first milestone can be **one web feature, one failing API path or one reporting
workflow**. Once we agree the brief, I return the implementation, the checks used
to verify it, and handover notes covering remaining limits and recovery.

Send the current behavior, the result you need and the relevant stack.
I'll identify the missing inputs and propose a scope, acceptance checks, price
and delivery schedule for your review.

I use Codex-assisted implementation, testing and writing. We agree tooling and
data requirements before sharing private project material. Working hours and
the implementation start date are agreed for each engagement.

[Email Huy](mailto:hohuyblon@gmail.com)

## More technical work

- [MCP workflow status](samples/mcp-workflow-status/) — distinguish dispatch,
  completion, rejected input and worker failure in a runnable local example.
  Fictional CSV data.
- [Codex Plugin Check](https://github.com/builtbyhuy/codex-plugin-check) —
  experimental CLI and GitHub Action for skills/hooks discovery against a pinned
  Codex release. Strict isolation is Linux-only; discovery is not a security certification.
- **HandoffLab** — a local, unreleased failure-replay prototype extending the
  webhook sample.
- [Editable workshop presentation](samples/workshop-presentation/) —
  an independent presentation concept using fictional data.
