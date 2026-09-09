"""Executable checks against a real local MCP server; no model or API keys."""

import asyncio
import json
import sys
from datetime import datetime, timezone
from importlib.metadata import version
from pathlib import Path

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from client import WorkflowFailed, unpack, wait_for_result


async def main():
    checks = []
    observations = {}
    parameters = StdioServerParameters(
        command=sys.executable,
        args=[str(Path(__file__).with_name("server.py"))],
        env={"OTEL_SDK_DISABLED": "true"},
    )
    async with stdio_client(parameters) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            cases = [
                ("valid input", "sku,quantity\nSAMPLE-A,2\n", True),
                ("negative quantity", "sku,quantity\nSAMPLE-A,-2\n", False),
                ("missing SKU", "sku,quantity\n,2\n", False),
                ("missing column", "sku,quantity\nSAMPLE-A\n", False),
                ("extra column", "sku,quantity\nSAMPLE-A,2,3\n", False),
                ("header only", "sku,quantity\n", False),
                ("malformed header quotes", '"sku,quantity\n', False),
                ("malformed row quotes", 'sku,quantity\n"SAMPLE-A,2\n', False),
                ("row limit", "sku,quantity\n" + "SAMPLE-A,2\n" * 101, False),
                ("size limit", "x" * 10001, False),
            ]
            for label, csv_text, accepted in cases:
                result = unpack(await session.call_tool("validate_now", {"csv_text": csv_text}))
                assert result["accepted"] is accepted, (label, result)
                assert bool(result["errors"]) is not accepted, (label, result)
                checks.append(label)

            for label, csv_text, accepted in [cases[0], cases[1]]:
                handle = unpack(await session.call_tool("validate_later", {"csv_text": csv_text}))
                assert "run_id" in handle and "accepted" not in handle, handle
                result = await wait_for_result(session, handle["run_id"])
                assert result["accepted"] is accepted, result
                status = unpack(await session.call_tool("workflows-get_status", {"run_id": handle["run_id"]}))
                assert status["status"] == "completed", status
                observations[label] = {"handle": handle, "terminal": status}
                checks.append("async lifecycle: " + label)

            handle = unpack(await session.call_tool("validate_later", {"csv_text": cases[0][1], "simulate_failure": True}))
            try:
                await wait_for_result(session, handle["run_id"])
            except WorkflowFailed as error:
                assert "Simulated worker failure" in str(error), str(error)
            else:
                raise AssertionError("A failed worker must not be reported as success")
            raw = await session.call_tool("workflows-get_status", {"run_id": handle["run_id"]})
            assert raw.isError is False and unpack(raw)["status"] == "error"
            observations["worker failure"] = {"mcp_is_error": raw.isError, "terminal": unpack(raw)}
            checks.append("worker failure despite successful MCP status call")

            handle = unpack(await session.call_tool("validate_later", {"csv_text": cases[0][1]}))
            try:
                await wait_for_result(session, handle["run_id"], timeout=.01)
            except TimeoutError:
                checks.append("bounded client deadline")
            else:
                raise AssertionError("The deliberately slow job must exceed the short deadline")
            # A timeout ends observation, not execution. Drain this run before closing stdio.
            result = await wait_for_result(session, handle["run_id"])
            assert result["accepted"] is True
            checks.append("same run can complete after client deadline")

    report = {
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "python": sys.version.split()[0],
        "mcp_agent": version("mcp-agent"),
        "mcp": version("mcp"),
        "checks_passed": checks,
        "observations": observations,
        "limits": "Local asyncio/stdio sample with fictional CSV; no LLM, cloud durability, production integration or paid-client validation.",
    }
    Path(__file__).with_name("observed-results.json").write_text(json.dumps(report, indent=2) + "\n")
    print(f"PASS: {len(checks)} checks against the real local MCP server")


if __name__ == "__main__":
    asyncio.run(main())
