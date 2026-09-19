"""Tool schema registry with zero-copy microsecond constraint validation."""

import re
from typing import Dict, Any, Optional, List, Tuple
from .risk_policy import ToolPolicy, RiskTier

class ToolSchemaRegistry:
    def __init__(self):
        self.schemas: Dict[str, Dict[str, Any]] = {}
        self.policies: Dict[str, ToolPolicy] = {}

    def register_tool(
        self,
        name: str,
        parameters: Dict[str, Dict[str, Any]],
        required_fields: List[str],
        policy: ToolPolicy
    ):
        self.schemas[name] = {
            "parameters": parameters,
            "required": set(required_fields)
        }
        self.policies[name] = policy

    def validate_arguments(self, tool_name: str, args: Dict[str, Any]) -> Tuple[bool, str]:
        if tool_name not in self.schemas:
            return False, f"Unregistered tool: '{tool_name}' is not in the safe schema registry."

        schema = self.schemas[tool_name]
        required = schema["required"]

        # Check required keys
        for req in required:
            if req not in args:
                return False, f"Missing required parameter '{req}' for tool '{tool_name}'."

        # Check types and constraints
        param_defs = schema["parameters"]
        for key, val in args.items():
            if key not in param_defs:
                return False, f"Unexpected parameter '{key}' passed to tool '{tool_name}'."

            expected_type = param_defs[key].get("type")
            if expected_type == "string" and not isinstance(val, str):
                return False, f"Parameter '{key}' must be string, got {type(val).__name__}."
            elif expected_type == "integer" and (not isinstance(val, int) or isinstance(val, bool)):
                return False, f"Parameter '{key}' must be integer, got {type(val).__name__}."
            elif expected_type == "number" and not isinstance(val, (int, float)):
                return False, f"Parameter '{key}' must be number, got {type(val).__name__}."
            elif expected_type == "boolean" and not isinstance(val, bool):
                return False, f"Parameter '{key}' must be boolean, got {type(val).__name__}."

            # Regex boundary validation
            regex_pat = param_defs[key].get("pattern")
            if regex_pat and isinstance(val, str):
                if not re.match(regex_pat, val):
                    return False, f"Parameter '{key}' failed pattern check: '{val}' does not match '{regex_pat}'."

            # Numeric range validation
            if isinstance(val, (int, float)):
                min_val = param_defs[key].get("min")
                max_val = param_defs[key].get("max")
                if min_val is not None and val < min_val:
                    return False, f"Parameter '{key}' value {val} below minimum {min_val}."
                if max_val is not None and val > max_val:
                    return False, f"Parameter '{key}' value {val} exceeds maximum {max_val}."

        return True, "OK"
