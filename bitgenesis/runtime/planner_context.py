from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class PlannerContext:
    """
    Context provided to the execution planner.
    """

    decision: Any