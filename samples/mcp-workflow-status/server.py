"""Deterministic CSV validation exposed through real mcp-agent tools."""

import asyncio
import csv
import io

from mcp_agent.app import MCPApp
from mcp_agent.config import Settings
from mcp_agent.server.app_server import create_mcp_server_for_app


app = MCPApp(
    name="csv_status_sample",
    settings=Settings(
        _env_file=None,
        execution_engine="asyncio",
        usage_telemetry={"enabled": False},
        otel={"enabled": False},
        logger={"type": "none", "transports": ["none"], "progress_display": False, "level": "error"},
    ),
)


def inspect_csv(csv_text: str) -> dict:
    """Validate a small fictional inventory upload without storing it."""
    if len(csv_text) > 10_000:
        return {"accepted": False, "rows": 0, "errors": ["Input exceeds 10000 characters"]}
    errors = []
    count = 0
    try:
        reader = csv.DictReader(io.StringIO(csv_text), strict=True)
        if reader.fieldnames != ["sku", "quantity"]:
            return {"accepted": False, "rows": 0, "errors": ["Expected header sku,quantity"]}
        for count, row in enumerate(reader, 1):
            if count > 100:
                errors.append("Input exceeds 100 rows")
                break
            if None in row or any(v is None for v in row.values()):
                errors.append(f"Row {count}: expected exactly two fields")
                continue
            if not row["sku"].strip():
                errors.append(f"Row {count}: SKU is empty")
            try:
                quantity = int(row["quantity"])
                if quantity < 0:
                    raise ValueError
            except ValueError:
                errors.append(f"Row {count}: quantity must be a nonnegative integer")
    except csv.Error:
        errors.append("Malformed CSV quoting")
    if count == 0:
        errors.append("At least one inventory row is required")
    return {"accepted": not errors, "rows": count, "errors": errors}


@app.tool(name="validate_now")
async def validate_now(csv_text: str) -> dict:
    """Return the final validation result in this call."""
    return inspect_csv(csv_text)


@app.async_tool(name="validate_later")
async def validate_later(csv_text: str, simulate_failure: bool = False) -> dict:
    """Start deterministic validation; poll the returned workflow handle."""
    # A short simulated processing delay makes the running state observable.
    await asyncio.sleep(0.2)
    if simulate_failure:
        raise RuntimeError("Simulated worker failure; no inventory was changed")
    return inspect_csv(csv_text)


async def main():
    async with app.run():
        server = create_mcp_server_for_app(app)
        await server.run_stdio_async()


if __name__ == "__main__":
    asyncio.run(main())
