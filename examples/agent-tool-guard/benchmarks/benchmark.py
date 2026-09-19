"""Empirical benchmark suite for AgentToolGuard."""

import time
import statistics
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from tool_guard import AgentToolGuard, ToolSchemaRegistry, ToolPolicy, RiskTier

def run_benchmark(iterations: int = 50_000):
    registry = ToolSchemaRegistry()
    registry.register_tool(
        name="query_vector_db",
        parameters={
            "collection": {"type": "string"},
            "top_k": {"type": "integer", "min": 1, "max": 100},
            "filter_tag": {"type": "string"}
        },
        required_fields=["collection", "top_k"],
        policy=ToolPolicy(name="query_vector_db", risk_tier=RiskTier.TIER_1_READ)
    )

    guard = AgentToolGuard(registry)

    # 1. Throughput & Latency Benchmark for Valid Calls
    latencies_us = []
    start_total = time.perf_counter()

    for i in range(iterations):
        # vary session to avoid artificial loop tripping in clean throughput test
        sess = f"session_{i % 5000}"
        decision = guard.evaluate(
            "query_vector_db",
            {"collection": "knowledge_prod", "top_k": (i % 50) + 1, "filter_tag": "docs"},
            session_id=sess
        )
        latencies_us.append(decision.latency_us)

    total_time = time.perf_counter() - start_total
    throughput = iterations / total_time

    p50 = statistics.median(latencies_us)
    p95 = statistics.quantiles(latencies_us, n=20)[18]
    p99 = statistics.quantiles(latencies_us, n=100)[98]

    # 2. Benchmark Injection Deflection Speed
    injection_start = time.perf_counter()
    injection_iters = 20_000
    for i in range(injection_iters):
        guard.evaluate(
            "query_vector_db",
            {"collection": "'; DROP TABLE embeddings; --", "top_k": 5},
            session_id=f"inj_{i}"
        )
    inj_time = time.perf_counter() - injection_start
    inj_throughput = injection_iters / inj_time

    print("=" * 60)
    print("      AGENT TOOL GUARD EMPIRICAL BENCHMARK RESULTS")
    print("=" * 60)
    print(f"Iterations:              {iterations:,}")
    print(f"Total Evaluation Time:   {total_time:.4f} s")
    print(f"Throughput:              {throughput:,.0f} evaluations/sec")
    print(f"Latency p50:             {p50:.2f} µs")
    print(f"Latency p95:             {p95:.2f} µs")
    print(f"Latency p99:             {p99:.2f} µs")
    print(f"Injection Deflection:    {inj_throughput:,.0f} attacks/sec")
    print("=" * 60)

if __name__ == "__main__":
    run_benchmark(50_000)
