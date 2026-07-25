from __future__ import annotations

from dataclasses import dataclass

from bitgenesis.runtime.execution_plan import ExecutionPlan



@dataclass(frozen=True)
class PlannerResult:
    """
    Result returned by the cognitive execution planner.
    """


    success: bool

    plan: ExecutionPlan

    reason: str | None = None