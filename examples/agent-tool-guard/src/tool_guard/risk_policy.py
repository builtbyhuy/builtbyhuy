"""Risk classification and blast-radius policy for AI Agent tool executions."""

from enum import Enum
from dataclasses import dataclass
from typing import Optional, Set

class RiskTier(str, Enum):
    TIER_1_READ = "TIER_1_READ"              # Safe, idempotent read operations (e.g. search, get)
    TIER_2_MUTATION = "TIER_2_MUTATION"      # State changes with bounded blast radius (e.g. update_tag)
    TIER_3_CRITICAL = "TIER_3_CRITICAL"      # Irreversible/high-cost actions (e.g. delete_db, refund)

@dataclass(frozen=True)
class ToolPolicy:
    name: str
    risk_tier: RiskTier
    max_calls_per_session: int = 50
    requires_approval_token: bool = False
    forbidden_patterns: Optional[Set[str]] = None
