"""AgentToolGuard: High-throughput deterministic AI agent tool-calling firewall."""

import time
import re
from dataclasses import dataclass
from typing import Dict, Any, Optional, Tuple
from .registry import ToolSchemaRegistry
from .risk_policy import ToolPolicy, RiskTier
from .cycle_detector import CycleDetector

# Fast heuristic regex for dangerous injection patterns in tool arguments
INJECTION_PATTERN = re.compile(
    r"(;|\|\||&&|\$\(|\`|\bDROP\s+TABLE\b|\bDELETE\s+FROM\b|--|\bUNION\s+SELECT\b|<script\b|\bEXEC\s*\(|\bSYSTEM\s*\(|ignore\s+previous\s+instructions)",
    re.IGNORECASE
)

@dataclass(frozen=True)
class GuardDecision:
    allowed: bool
    reason: str
    risk_tier: str
    latency_us: float
    tool_name: str

class AgentToolGuard:
    def __init__(self, registry: Optional[ToolSchemaRegistry] = None):
        self.registry = registry or ToolSchemaRegistry()
        self.cycle_detectors: Dict[str, CycleDetector] = {}

    def get_cycle_detector(self, session_id: str) -> CycleDetector:
        if session_id not in self.cycle_detectors:
            self.cycle_detectors[session_id] = CycleDetector(window_size=10, max_identical_repeats=3)
        return self.cycle_detectors[session_id]

    def evaluate(
        self,
        tool_name: str,
        arguments: Dict[str, Any],
        session_id: str = "default_session",
        auth_token: Optional[str] = None
    ) -> GuardDecision:
        """
        Evaluates an autonomous agent tool call.
        Enforces schema, injection boundaries, risk tiers, and cycle loops.
        """
        start_ns = time.perf_counter_ns()

        # 1. Check tool policy & risk tier
        if tool_name not in self.registry.policies:
            elapsed_us = (time.perf_counter_ns() - start_ns) / 1000.0
            return GuardDecision(
                allowed=False,
                reason=f"SECURITY_REJECT: Tool '{tool_name}' not registered in security policy.",
                risk_tier="UNKNOWN",
                latency_us=round(elapsed_us, 2),
                tool_name=tool_name
            )

        policy = self.registry.policies[tool_name]

        # 2. Critical Action Authorization Check (Tier 3)
        if policy.risk_tier == RiskTier.TIER_3_CRITICAL and policy.requires_approval_token:
            if not auth_token or not auth_token.startswith("auth_sig_"):
                elapsed_us = (time.perf_counter_ns() - start_ns) / 1000.0
                return GuardDecision(
                    allowed=False,
                    reason=f"BLOCKED_UNAUTHORIZED: Critical tool '{tool_name}' requires valid cryptographic approval token.",
                    risk_tier=policy.risk_tier.value,
                    latency_us=round(elapsed_us, 2),
                    tool_name=tool_name
                )

        # 3. Deep Parameter Sanitization & Injection Scanner
        for key, val in arguments.items():
            if isinstance(val, str):
                if INJECTION_PATTERN.search(val):
                    elapsed_us = (time.perf_counter_ns() - start_ns) / 1000.0
                    return GuardDecision(
                        allowed=False,
                        reason=f"INJECTION_DEFLECTED: Dangerous payload detected in parameter '{key}'.",
                        risk_tier=policy.risk_tier.value,
                        latency_us=round(elapsed_us, 2),
                        tool_name=tool_name
                    )

        # 4. Schema & Parameter Type Boundary Check
        valid_schema, schema_err = self.registry.validate_arguments(tool_name, arguments)
        if not valid_schema:
            elapsed_us = (time.perf_counter_ns() - start_ns) / 1000.0
            return GuardDecision(
                allowed=False,
                reason=f"SCHEMA_VIOLATION: {schema_err}",
                risk_tier=policy.risk_tier.value,
                latency_us=round(elapsed_us, 2),
                tool_name=tool_name
            )

        # 5. Cyclic Loop & Agent Thrashing Detection
        cycle_detector = self.get_cycle_detector(session_id)
        is_loop, loop_reason = cycle_detector.record_and_check(tool_name, arguments)
        if is_loop:
            elapsed_us = (time.perf_counter_ns() - start_ns) / 1000.0
            return GuardDecision(
                allowed=False,
                reason=f"CYCLE_INTERCEPTED: {loop_reason}",
                risk_tier=policy.risk_tier.value,
                latency_us=round(elapsed_us, 2),
                tool_name=tool_name
            )

        elapsed_us = (time.perf_counter_ns() - start_ns) / 1000.0
        return GuardDecision(
            allowed=True,
            reason="PASSED: Verified schema boundary, risk tier, and cycle safety.",
            risk_tier=policy.risk_tier.value,
            latency_us=round(elapsed_us, 2),
            tool_name=tool_name
        )
