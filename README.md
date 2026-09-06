# Hi, I'm Huy.

I build Python and JavaScript tools for the parts that fail quietly: webhooks,
plugin discovery, and release handoffs.

My favorite demo is the one that breaks on purpose.

## Start here

### [Webhook reliability boundary](https://github.com/builtbyhuy/webhook-crm-reliability-sample)

A signed-webhook simulation with SQLite-backed duplicate/conflict detection and
bounded retries. Event identity survives restarts; exhausted retries require
explicit recovery instead of quietly trying again.

**Python · SQLite · HMAC · unittest** — independent sample; synthetic events,
simulated CRM, no customer traffic.

### [Codex Plugin Check](https://github.com/builtbyhuy/codex-plugin-check)

A zero-dependency CLI and GitHub Action that verifies skills and hooks against
a pinned Codex release. Declared capabilities and observed discovery stay
separate; installation alone is not proof that a plugin works.

**JavaScript · Node.js · GitHub Actions · Docker** — experimental; strict
isolation is Linux-only, and discovery is not a security certification.

### [Proofline](https://github.com/builtbyhuy/proofline-release-review) · [try the interface](https://builtbyhuy.github.io/proofline-release-review/)

A release-review interface with an executable acceptance model. Missing
evidence keeps the fictional release blocked; unit and browser tests cover the
decision rules, state transitions, and keyboard-focus recovery.

**HTML/CSS · JavaScript · Playwright** — independent frontend sample, not a
deployment controller.

## Field notes

[When a saved document style cannot be read back](notes/2026-09-06-xpath-variables.md)
— a walkthrough of a merged Python fix, XPath variable binding, and the public
round-trip test that kept the repair honest. Includes a runnable reproduction.

## Reviewed outside my own repos

In [python-docx-ng PR #131](https://github.com/toxicphreAK/python-docx-ng/pull/131),
I fixed quote-sensitive style lookups by binding XPath variables and adding
regression coverage. The maintainer reviewed the edge cases and merged it.
One open-source contribution, not a client case study.

## On my bench

I'm extending the webhook sample into **HandoffLab**: a failure-replay matrix
that checks downstream side effects and records the operator's recovery
decision. The local prototype is tested; it is not released yet.

## Say hello

For a focused software project or open-source collaboration:
[email me](mailto:hohuyblon@gmail.com) or [find me on LinkedIn](https://www.linkedin.com/in/builtbyhuy/).
