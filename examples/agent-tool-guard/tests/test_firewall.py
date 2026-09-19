"""Comprehensive test suite for AgentToolGuard (compatible with unittest & pytest)."""

import unittest
import sys
import os

# Add src to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from tool_guard import AgentToolGuard, ToolSchemaRegistry, ToolPolicy, RiskTier

class TestAgentToolGuard(unittest.TestCase):
    def setUp(self):
        self.registry = ToolSchemaRegistry()

        # Tool 1: Safe query tool (Tier 1)
        self.registry.register_tool(
            name="search_kb",
            parameters={
                "query": {"type": "string", "pattern": r"^[a-zA-Z0-9\s\?.,_-]{1,100}$"},
                "limit": {"type": "integer", "min": 1, "max": 50}
            },
            required_fields=["query"],
            policy=ToolPolicy(name="search_kb", risk_tier=RiskTier.TIER_1_READ)
        )

        # Tool 2: Mutation tool (Tier 2)
        self.registry.register_tool(
            name="update_user_tag",
            parameters={
                "user_id": {"type": "string"},
                "tag": {"type": "string"}
            },
            required_fields=["user_id", "tag"],
            policy=ToolPolicy(name="update_user_tag", risk_tier=RiskTier.TIER_2_MUTATION)
        )

        # Tool 3: Critical destructive tool (Tier 3)
        self.registry.register_tool(
            name="delete_account",
            parameters={
                "account_id": {"type": "string"},
                "reason": {"type": "string"}
            },
            required_fields=["account_id"],
            policy=ToolPolicy(
                name="delete_account",
                risk_tier=RiskTier.TIER_3_CRITICAL,
                requires_approval_token=True
            )
        )

        self.guard = AgentToolGuard(self.registry)

    def test_valid_tool_call_passes(self):
        decision = self.guard.evaluate("search_kb", {"query": "how to reset password", "limit": 10})
        self.assertTrue(decision.allowed)
        self.assertIn("PASSED", decision.reason)
        self.assertEqual(decision.risk_tier, "TIER_1_READ")
        self.assertLess(decision.latency_us, 1000.0)

    def test_missing_required_param_rejected(self):
        decision = self.guard.evaluate("search_kb", {"limit": 10})
        self.assertFalse(decision.allowed)
        self.assertIn("SCHEMA_VIOLATION", decision.reason)
        self.assertIn("Missing required parameter 'query'", decision.reason)

    def test_type_mismatch_rejected(self):
        decision = self.guard.evaluate("search_kb", {"query": 12345})
        self.assertFalse(decision.allowed)
        self.assertIn("SCHEMA_VIOLATION", decision.reason)
        self.assertIn("must be string", decision.reason)

    def test_numeric_boundary_rejected(self):
        decision = self.guard.evaluate("search_kb", {"query": "test query", "limit": 500})
        self.assertFalse(decision.allowed)
        self.assertIn("SCHEMA_VIOLATION", decision.reason)
        self.assertIn("exceeds maximum 50", decision.reason)

    def test_injection_payload_deflected(self):
        malicious_payload = "'; DROP TABLE users; --"
        decision = self.guard.evaluate("search_kb", {"query": malicious_payload})
        self.assertFalse(decision.allowed)
        self.assertIn("INJECTION_DEFLECTED", decision.reason)

    def test_unauthorized_tier3_blocked(self):
        decision = self.guard.evaluate("delete_account", {"account_id": "acc_99"}, auth_token=None)
        self.assertFalse(decision.allowed)
        self.assertIn("BLOCKED_UNAUTHORIZED", decision.reason)

    def test_authorized_tier3_passes(self):
        decision = self.guard.evaluate(
            "delete_account",
            {"account_id": "acc_99"},
            auth_token="auth_sig_valid_cryptographic_token"
        )
        self.assertTrue(decision.allowed)
        self.assertEqual(decision.risk_tier, "TIER_3_CRITICAL")

    def test_agent_thrashing_cycle_intercepted(self):
        session = "loop_test_session"
        d1 = self.guard.evaluate("search_kb", {"query": "loop query"}, session_id=session)
        self.assertTrue(d1.allowed)
        d2 = self.guard.evaluate("search_kb", {"query": "loop query"}, session_id=session)
        self.assertTrue(d2.allowed)
        d3 = self.guard.evaluate("search_kb", {"query": "loop query"}, session_id=session)
        self.assertFalse(d3.allowed)
        self.assertIn("CYCLE_INTERCEPTED", d3.reason)

    def test_oscillating_cycle_intercepted(self):
        session = "oscillate_session"
        self.guard.evaluate("search_kb", {"query": "alpha"}, session_id=session)
        self.guard.evaluate("search_kb", {"query": "beta"}, session_id=session)
        self.guard.evaluate("search_kb", {"query": "alpha"}, session_id=session)
        d4 = self.guard.evaluate("search_kb", {"query": "beta"}, session_id=session)
        self.assertFalse(d4.allowed)
        self.assertIn("CYCLE_INTERCEPTED", d4.reason)
        self.assertIn("Oscillating 2-cycle", d4.reason)

    def test_unregistered_tool_rejected(self):
        decision = self.guard.evaluate("dangerous_eval", {"code": "rm -rf /"})
        self.assertFalse(decision.allowed)
        self.assertIn("SECURITY_REJECT", decision.reason)

if __name__ == "__main__":
    unittest.main()
