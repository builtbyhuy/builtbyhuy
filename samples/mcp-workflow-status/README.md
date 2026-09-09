# An async tool started. Did it finish?

A runnable example of three different outcomes in `mcp-agent`: a tool call
returns a workflow handle; the workflow completes or fails; the completed
workflow accepts or rejects the input.

Imagine an inventory import that displays a green check as soon as a worker
returns a run ID. A malformed upload could still be processing, rejected, or
headed for a worker error. This sample makes those states observable using a
fictional CSV upload, a real MCP server over stdio, and deterministic Python.

## Run the sample

Tested on macOS with Python 3.12.13, `mcp-agent` 0.2.6, and `mcp` 1.30.0.
Install into a fresh environment from this directory:

```sh
python3.12 -m venv .venv
.venv/bin/python -m pip install -r requirements.lock
.venv/bin/python check_sample.py
```

The check starts and closes its own local MCP server. No model provider,
API key, paid service, or customer account is needed. The server disables
usage telemetry and OpenTelemetry. Package installation requires internet.

Expected final line:

```text
PASS: 15 checks against the real local MCP server
```

The deliberately failed worker also emits error logs. That is an exercised
failure path; the final PASS appears only after the client handles it and all
assertions finish. `observed-results.json` contains the latest local run's
versions, timestamp, passed checks, and actual response payloads. Running the
check replaces that report.

## What the client must distinguish

| Observation | What it establishes | Next action |
| --- | --- | --- |
| `validate_now` returns `accepted` | The synchronous validation result is available | Inspect `accepted` and `errors` |
| `validate_later` returns `run_id` | Work was dispatched | Poll this run, without dispatching another one |
| Status is `running` | There is no final result yet | Continue within the client's deadline |
| Status is `completed`, result has `accepted: false` | The worker finished, but rejected the CSV | Show the validation errors |
| Status is `error` | The worker failed | Surface the failure; do not show a successful import |
| The client reaches its deadline | This client stopped waiting | Preserve the run ID; timeout does not establish cancellation |

The failure case is easy to misread: the MCP call to `workflows-get_status`
returned `isError: false` while its payload reported `status: "error"`.
The status query itself succeeded. The worker did not. The sample checks both
layers rather than using the MCP flag as a workflow-success signal.

`client.py` unwraps the actual response shapes observed in the pinned versions:
the start handle arrives as JSON text, while status has a structured `result`
wrapper. It checks the returned run ID, waits for a terminal state, raises on
worker failure, and bounds the entire polling operation with `asyncio.timeout`.

## What was checked

Ten synchronous cases cover valid input, negative quantities, a missing SKU,
missing and extra columns, a header without rows, malformed header and row
quotes, and the input's row and character limits. Two async cases confirm that
both accepted and rejected CSVs can complete successfully as workflows. Three
further checks cover an actual worker exception, a client deadline, and the
same workflow completing after that deadline. The client drains that run before
closing stdio instead of mistaking an observation timeout for a cancelled job.

The server accepts only the exact `sku,quantity` header and nonnegative integer
quantities. It inspects at most 101 rows to detect the 100-row limit; the `rows`
field counts rows encountered, not accepted inventory records. It stores
nothing, and it does not implement an inventory import.

## One setup failure encountered

Installing `mcp-agent==0.2.6` alone in this environment initially resolved
`mcp==2.2.0`. Importing the framework failed because it still imported
`mcp.server.fastmcp`, which that MCP SDK version did not provide. Pinning
`mcp==1.30.0` allowed this sample to start. The lock file records the tested
combination; this is one observed compatibility failure, not a claim about all
versions or environments. The checks also passed after syncing the
environment exactly to that lock file.

## Scope and attribution

This is an independent, Codex-assisted implementation and writing sample.
Its evidence is a local asyncio/stdio execution with fictional input. It does
not establish restart durability, distributed execution, cancellation,
authorization, production scalability, or a paid client result. It uses no
LLM agents. Publishing it does not imply endorsement by LastMile AI.

The implementation follows the public
[workflow concepts](https://docs.mcp-agent.com/concepts/workflows) and
[MCP server concepts](https://docs.mcp-agent.com/concepts/mcp-servers).
The tested package release is listed on
[PyPI](https://pypi.org/project/mcp-agent/0.2.6/).
