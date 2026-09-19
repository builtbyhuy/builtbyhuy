"""Real-time cyclic loop and thrashing detector for autonomous agent tool executions."""

import hashlib
import json
from collections import deque
from typing import Tuple, List

class CycleDetector:
    def __init__(self, window_size: int = 10, max_identical_repeats: int = 3):
        self.window_size = window_size
        self.max_identical_repeats = max_identical_repeats
        self.history: deque = deque(maxlen=window_size)
        self.hash_counts: dict = {}

    def _hash_call(self, tool_name: str, arguments: dict) -> str:
        serialized = json.dumps(arguments, sort_keys=True, default=str)
        payload = f"{tool_name}:{serialized}"
        return hashlib.sha256(payload.encode("utf-8")).hexdigest()[:16]

    def record_and_check(self, tool_name: str, arguments: dict) -> Tuple[bool, str]:
        """
        Records the tool call and checks for infinite loops.
        Returns: (is_loop_detected, reason)
        """
        call_hash = self._hash_call(tool_name, arguments)

        # 1. Check direct consecutive repetition
        consecutive_count = 0
        for past_hash in reversed(self.history):
            if past_hash == call_hash:
                consecutive_count += 1
            else:
                break

        if consecutive_count >= self.max_identical_repeats - 1:
            return True, f"Agent thrashing detected: {tool_name} invoked {consecutive_count + 1} consecutive times with identical parameters."

        # 2. Check alternating 2-cycle loop (A -> B -> A -> B)
        if len(self.history) >= 3:
            h_list = list(self.history)
            if h_list[-2] == call_hash and h_list[-1] == h_list[-3]:
                return True, f"Oscillating 2-cycle loop detected for tool {tool_name}."

        # 3. Check frequency overflow in sliding window
        current_freq = self.hash_counts.get(call_hash, 0) + 1
        if current_freq > 4:
            return True, f"Excessive identical call frequency in sliding window ({current_freq} times)."

        # Update sliding window state
        if len(self.history) == self.window_size:
            oldest = self.history[0]
            if oldest in self.hash_counts:
                self.hash_counts[oldest] -= 1
                if self.hash_counts[oldest] <= 0:
                    del self.hash_counts[oldest]

        self.history.append(call_hash)
        self.hash_counts[call_hash] = self.hash_counts.get(call_hash, 0) + 1

        return False, "OK"
