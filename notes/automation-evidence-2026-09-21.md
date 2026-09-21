# Automation project evidence — 21 September 2026

This pack accompanies my entry-level automation/implementation applications. It uses public project code and synthetic inputs. It does not expose customer data, invoke live services, or claim commercial outcomes.

## 1. Merged Python contribution

**[python-docx-ng PR #131](https://github.com/toxicphreAK/python-docx-ng/pull/131)** was submitted by `builtbyhuy` and merged on 4 August 2026. Merge commit: `0935865a2a245ffa3354a4be671d01c2d60f1228`.

The patch binds style names/IDs as XPath variables, forwards them through the XML wrapper and adds regression tests. The repository is `toxicphreAK/python-docx-ng`, not another similarly named package.

A small independent reproducer shows why binding matters:

```bash
# Requires Python and lxml. Run from this profile repository.
python samples/xpath-binding-demo.py
```

[Reproducer source](../samples/xpath-binding-demo.py)

Observed in Python 3.13.5:

```text
Plain Style: interpolated=MATCH; bound=MATCH
O'Brien: interpolated=MATCH; bound=MATCH
He said "hello": interpolated=XPathError; bound=MATCH
He said "it's fine" [today]: interpolated=XPathError; bound=MATCH
Result: 4/4 bound-variable cases passed.
```

**Boundary:** this is a focused synthetic XML reproducer. It is not a rerun of the upstream suite or a claim that all document APIs were tested in this session.

## 2. Telegram vehicle-tracking project

**[Project repository](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi)**. The source contains Telegram webhook handling, vehicle recognition integration and spreadsheet reporting.

The offline sample extracts three pure helpers from `src/utils.js`: `normalizePlate`, `isValidVietnamPlate` and `parseMessage`. Source blob reviewed: `25aee5a21f2882934fa1f678aba2851f984a66d3`. Formatting is simplified; helper logic is unchanged.

```bash
# Requires Node.js; no npm install or credentials.
node samples/vehicle-boundary-demo.cjs
```

[Runnable sample](../samples/vehicle-boundary-demo.cjs)

Observed on Node.js v22.16.0:

```text
PASS: normalizes synthetic plate text
PASS: keeps normalized synthetic plate stable
PASS: handles empty text
PASS: rejects clearly invalid plate format
PASS: parses manual exit command
PASS: parses Vietnamese-accented inventory command
PASS: does not invent a command from unknown text
PASS: documents parser/validator boundary
Result: 8/8 focused checks passed.
```

One useful limit: `parseMessage('RA nonsense')` produces a manual-exit action, but the resulting plate fails `isValidVietnamPlate`. Parsing is not final validation. The downstream handler must be inspected before concluding whether the full application rejects or accepts that input.

**Not exercised:** photo recognition, Telegram message delivery, live database behavior, Google Sheets/Excel writes, or the complete application's test suite. This is not a recording of the live bot.

## 3. Additional integration sample

The **[webhook-to-CRM sample](https://github.com/builtbyhuy/webhook-crm-reliability-sample)** documents signature, duplicate/conflict and bounded retry behavior using a simulated CRM. Its existing repository tests were not rerun for this pack.

## Review sequence

Open the merged PR and inspect the changed files. Run the XPath reproducer. Run the vehicle-helper sample and discuss the parser/validation boundary. For the full bot, use an authorized test environment and synthetic photographs before making any claim about live integrations.

Prepared with AI assistance. These commands let reviewers reproduce the limited checks; they do not claim production performance, paid-client delivery or unaided proficiency.
