# AgentToolGuard — Deterministic AI Agent Tool-Call Firewall

Deterministic parameter schema validation, injection deflection, risk tiering, and sliding-window cyclic loop interception for autonomous LLM agents (GPT-4o, Claude 3.5 Sonnet).

## 📊 Empirical Benchmarks (Apple M-Series / Python 3.14)

* **Throughput**: **102,516 evaluations/sec**
* **Latency p50**: **5.33 µs**
* **Latency p95**: **15.88 µs**
* **Latency p99**: **41.17 µs**
* **Injection Deflection Speed**: **435,640 attacks/sec**
* **Cycle Interception**: 100% sliding-window loop detection (consecutive & 2-cycle oscillation)
* **Test Suite**: 10/10 automated tests passing (`python3 -m unittest discover tests`)

## 🏛️ Architecture

1. **Schema Boundary Registry**: Zero-copy parameter validation enforcing type boundaries, regex constraints, and value ranges in microsecond time.
2. **Deep Parameter Sanitizer**: Heuristic regex scanning intercepting SQL fragments (`'; DROP TABLE`, `UNION SELECT`), shell escapes, and prompt override attempts inside tool arguments.
3. **Risk Tier & Blast Radius Limiter**:
   - `Tier 1 (Read-Only)`: Idempotent data fetches (`search_kb`, `get_status`).
   - `Tier 2 (Bounded Mutation)`: Non-destructive updates.
   - `Tier 3 (Critical Destructive)`: High-cost/irreversible actions (`delete_account`, `refund_order`) requiring cryptographic authorization tokens.
4. **Sliding-Window Cycle Detector**: In-memory hash chain tracking call history to intercept agent thrashing and alternating oscillating loops.

## 🚀 Running Tests & Benchmarks

```bash
# Run unit test suite
python3 -m unittest discover tests -p "test_*.py" -v

# Run 50,000-iteration empirical benchmark
python3 benchmarks/benchmark.py
```
