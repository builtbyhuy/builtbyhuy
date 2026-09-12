# One event. Two deliveries. One simulated write.

[Open the one-page walkthrough](webhook-delivery-walkthrough.pdf)

This is an original, AI-assisted explanation of my existing [webhook reliability sample](https://github.com/builtbyhuy/webhook-crm-reliability-sample). The contact data is fictional and the CRM is simulated. These are recorded executions, not screenshots of client activity.

## What happened

I ran each row below in a separate Python process on 12 September 2026. Runs 1–3 share a SQLite ledger. Runs 4–6 share a second ledger. Run 7 uses an incorrect signature and stops before event processing.

| Run | Input or action | Observed result | Simulated CRM attempts |
|---|---|---|---:|
| 1 | First valid delivery | `would_write` | 1 |
| 2 | Same event and data, new process | `duplicate_suppressed` | 0 |
| 3 | Same event ID, changed company | `idempotency_conflict` | 0 |
| 4 | Repeated simulated HTTP 500 | `retry_exhausted` | 3 |
| 5 | Restart without replay permission | `retry_exhausted` | 0 |
| 6 | Explicit replay of the original event | `would_write` | 1 |
| 7 | Incorrect HMAC signature | `invalid_signature` | 0 |

The important distinction is between **a new process** and **permission to retry**. Restarting did not reset the exhausted event. Only the explicit replay restarted processing.

## Inspect or reproduce

The numbered JSON files preserve the complete outputs and exit codes. [Run summary](run-summary.json), [original input](event.json), and [conflicting input](conflict.json) are included. The changed fixture reuses the same event ID but changes the fictional company name.

Source: [webhook sample at `ff1672b466c3`](https://github.com/builtbyhuy/webhook-crm-reliability-sample/tree/ff1672b466c3d3be48ab02d3a92b6b234c005739). Its [quick start and scenarios](https://github.com/builtbyhuy/webhook-crm-reliability-sample/blob/ff1672b466c3d3be48ab02d3a92b6b234c005739/README.md#quick-start) describe signing the exact input bytes, supplying a SQLite ledger, setting the simulated failure scenario, and using `--replay-exhausted`. Changing input bytes also requires a new signature. Use a demo-only signing key, never a production credential.

## Limits

No request was sent to a CRM. Retry delays were recorded, not slept. These restart results apply to the **local CLI**; the separately deployed preview API uses a ledger scoped to one request. The runs do not establish distributed-worker safety, a real CRM integration, production reliability, avoided losses, customer acceptance or earnings.
