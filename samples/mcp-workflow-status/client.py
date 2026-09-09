"""A local MCP client that distinguishes dispatch, completion, and validation."""

import asyncio
import json


class WorkflowFailed(RuntimeError):
    pass


def unpack(response):
    if response.isError:
        raise RuntimeError("MCP tool returned an error")
    if response.structuredContent is not None:
        return response.structuredContent["result"]
    return json.loads(next(item.text for item in response.content if item.type == "text"))


async def wait_for_result(session, run_id, *, timeout=3.0):
    """Observe a specific run within a deadline; timeout does not cancel it."""
    async with asyncio.timeout(timeout):
        while True:
            status = unpack(await session.call_tool("workflows-get_status", {"run_id": run_id}))
            if status.get("run_id") != run_id:
                raise RuntimeError("Status response does not identify the requested run")
            if status["status"] == "completed":
                if not status.get("completed") or status.get("error"):
                    raise RuntimeError("Inconsistent completed workflow state")
                return status["result"]["value"]
            if status["status"] in {"error", "cancelled", "canceled"}:
                raise WorkflowFailed(status.get("error") or status["status"])
            if status["status"] not in {"pending", "running", "initialized"}:
                raise RuntimeError(f"Unexpected workflow state: {status['status']}")
            await asyncio.sleep(.05)
