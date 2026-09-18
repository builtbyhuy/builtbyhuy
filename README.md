# Hi, I'm Hồ Khắc Huy.

**Senior Software Engineer · Distributed Systems, Webhook Reliability & Applied AI**

I build high-throughput backend systems, crash-resilient data pipelines, and security proxies for production applications. My primary engineering stack is **Python (FastAPI, asyncio), TypeScript (Node.js), and Systems Programming (Binary Protocols, WAL, SQLite/PostgreSQL)**.

Hanoi, Vietnam (UTC+7) · Available for Senior Engineering & Contract Roles  
[Email Huy](mailto:hohuyblon@gmail.com) · [LinkedIn](https://www.linkedin.com/in/builtbyhuy/) · [GitHub](https://github.com/builtbyhuy)

---

## 🏛️ Flagship Systems & Verified Open Source

### 1. [python-docx-ng](https://github.com/toxicphreAK/python-docx-ng/pull/131) — Quote-Safe XPath Bugfix `Merged Upstream`
* **Problem**: Word document style names containing single quotes broke XPath query evaluation across document trees.
* **Contribution**: Replaced raw string interpolation with bound variable parameter lookups; authored full regression test matrix against quotation injection. Independently reviewed and merged into upstream release.
* **Links**: [Merged Upstream PR #131](https://github.com/toxicphreAK/python-docx-ng/pull/131) · [Reproduction Notes](notes/2026-09-06-xpath-variables.md)

### 2. [HookSentinel](https://github.com/builtbyhuy/webhook-gateway) — Distributed Ingestion & Dead-Letter Broker
* **Problem**: Third-party webhook retry storms (Stripe, GitHub, Shopify) causing duplicate database writes, double-billing, and unhandled signature tampering.
* **Architecture**: Multi-provider HMAC-SHA256 verification (constant-time digest), distributed idempotency ledger (`provider:sha256(raw_body)`), exponential backoff jitter, and Dead-Letter Queue (DLQ).
* **Empirical Benchmark**: **6,661 req/s** ingest throughput (0.58ms p99), **11,904 checks/s** duplicate replay suppression, **78/78 automated tests passing**.
* **Links**: [GitHub Repository](https://github.com/builtbyhuy/webhook-gateway) · [Interactive Chaos Playground ↗](https://builtbyhuy.github.io/webhook-gateway/)

### 3. [PromptShield](https://github.com/builtbyhuy/ai-guard-gateway) — Enterprise LLM Security Proxy & Fallback Router
* **Problem**: OWASP LLM01 Prompt Injections (DAN jailbreaks, delimiter hijacking, system overrides) and expensive duplicate LLM API token queries.
* **Architecture**: Real-time heuristic threat scanner, in-memory token-bucket rate limiter, deterministic SHA-256 exact-hash semantic cache (<1µs), and automated multi-provider circuit breaker (OpenAI ↔ Anthropic failover).
* **Empirical Benchmark**: **1,641,261 scans/s** threat detection (0.4µs latency), **690,222 reads/s** cache throughput with 100% token cost elimination, **7/7 tests passing**.
* **Links**: [GitHub Repository](https://github.com/builtbyhuy/ai-guard-gateway) · [Interactive Security Radar ↗](https://builtbyhuy.github.io/ai-guard-gateway/)

### 4. [ResilientDAG](https://github.com/builtbyhuy/streamline-engine) — Fault-Tolerant DAG Data Pipeline Engine
* **Problem**: Long-running ETL pipelines failing mid-flight requiring complete 100% re-execution from scratch, wasting compute and API budget.
* **Architecture**: Directed Acyclic Graph dependency solver using Kahn's algorithm, strict Zod runtime schema boundaries, parallel concurrency tiers, and durable disk checkpoints for zero-re-run crash recovery.
* **Empirical Benchmark**: **179,421 graph solutions/s** (4.2µs p50), **115,767 checks/s** deadlock cycle interception, **0% upstream compute loss on restart**, **10/10 tests passing**.
* **Links**: [GitHub Repository](https://github.com/builtbyhuy/streamline-engine) · [Interactive Pipeline Sandbox ↗](https://builtbyhuy.github.io/streamline-engine/)

### 5. [CrashProofWAL](https://github.com/builtbyhuy/wal-kv-ledger) — Crash-Resilient Write-Ahead Log Key-Value Store
* **Problem**: Storage corruption and bit rot caused by sudden kernel panics, power loss, or `kill -9` during append-heavy workloads.
* **Architecture**: Compact binary block protocol, hardware CRC32 block checksums, automatic corrupted-tail truncation on recovery, O(1) in-memory index, and SHA-256 Merkle tree state proofs.
* **Empirical Benchmark**: **847,449 writes/s (72.4 MB/s)**, **2.7M reads/s** index lookups, **15.03 ms surgical crash truncation** with 0 bytes committed data lost, **5/5 tests passing**.
* **Links**: [GitHub Repository](https://github.com/builtbyhuy/wal-kv-ledger) · [Interactive Defrag & Recovery Cockpit ↗](https://builtbyhuy.github.io/wal-kv-ledger/)

---

## 💼 Commercial & Client Engineering Work

* **60-Second Lead Capture Engine**: Architected high-reliability lead ingestion pipeline (Node.js/Express, token bucket rate limiting, Telegram webhook dispatch, write-ahead failover logging) delivering sub-minute response times and zero lead loss.
* **Automotive Workforce Attendance System**: Built operations web application for an automotive manufacturing facility in Vietnam, translating shift scheduling and punch-in rules into validated data models.
* **ERP Data Reconciliation Pipeline**: Engineered automated ETL reconciliation scripts extracting transaction records from Odoo ERP and spreadsheets into audited multi-format reports (Excel, HTML, PDF).
* **SkillArena**: Full-stack interactive simulation platform built with Next.js, React, TypeScript, and Supabase, featuring strict Zod schema validation and Playwright end-to-end test suites.

---

## 📬 Contact & Availability

* **Email**: [hohuyblon@gmail.com](mailto:hohuyblon@gmail.com)
* **LinkedIn**: [linkedin.com/in/builtbyhuy](https://www.linkedin.com/in/builtbyhuy/)
* **Location**: Hanoi, Vietnam (Remote Worldwide)
