# Hồ Khắc Huy

**Automation & implementation · seeking an entry-level role**  
Hanoi, Vietnam · English / Vietnamese

I enjoy turning a manual workflow into a small, understandable system: capture the input, validate it, produce a useful result, and make failures visible.

My academic background is Human Resource Management at RMIT University Vietnam. I have finished my coursework and am awaiting final results. I currently work in import/export documentation at MAX, an automotive-parts business, and am moving toward automation and implementation work.

**Contact:** [huy@wove.agency](mailto:huy@wove.agency) · alternate: [hohuyblon@gmail.com](mailto:hohuyblon@gmail.com)  
**[Current CV](CV.md)** · **[Project evidence and runnable examples](notes/automation-evidence-2026-09-21.md)**

## Application case study

### Keyloop Software Engineer — service-event proof of value

I built a six-slide, job-specific demo that connects a real automotive service-workshop workflow to a proposed, testable service-event design. It separates real evidence from role adaptation and links the technical boundary to my independent webhook reliability sample.

**[Read the case study and download the deck](case-studies/keyloop-software-engineer-demo/README.md)**

## Selected work

### Python style-lookup fix — merged open-source contribution

**[python-docx-ng PR #131](https://github.com/toxicphreAK/python-docx-ng/pull/131)** · merged 4 August 2026

Replaced string-interpolated XPath lookups with bound variables so style names and IDs containing quotes can be looked up correctly. The change forwards variables through the XML wrapper while preserving namespace handling, and adds regression tests.

Contributed to `toxicphreAK/python-docx-ng`. A [small runnable reproducer](samples/xpath-binding-demo.py) demonstrates the binding mechanism using synthetic XML.

### Telegram vehicle entry/exit tracking — personal project

**[Source](https://github.com/builtbyhuy/xuong-vinfast-phuc-loi)** · **[Offline helper checks](samples/vehicle-boundary-demo.cjs)**

A workflow for vehicle photographs and entry/exit commands: Telegram input, license-plate recognition, notifications and spreadsheet tracking. The repository contains Node.js webhook handling, Google Cloud Vision integration, Google Sheets records and Excel report generation.

The offline example exercises plate normalization and command parsing, including the boundary between parsing and validation. It does not invoke photo recognition or live Telegram/Google services.

### Webhook-to-CRM reliability boundary — independent technical sample

**[Source and reproduction instructions](https://github.com/builtbyhuy/webhook-crm-reliability-sample)**

A Python sample demonstrating signature checks, SQLite-backed duplicate/conflict handling and bounded retry behavior. The repository documents test commands, failure cases and production gaps. It uses fictional inputs and a simulated CRM.

## How I work

I use AI-assisted development for implementation, research and documentation. I am building practical experience in workflow analysis, Python/JavaScript project work, API integrations, testing and clear handoff documentation.

I am seeking an entry-level automation, implementation or application-support role with defined tasks and technical guidance. Start date and work schedule are to be agreed with the employer.

## Scope of the portfolio

These examples are open-source contributions, personal projects and independent samples—not paid-client delivery case studies. Live recognition accuracy, production reliability and commercial outcomes are not claimed. The linked CV is the current version of my application profile.
