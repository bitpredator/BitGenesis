from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from bitgenesis.runtime.result import ActionResult


@dataclass(slots=True)
class ExecutionResult:
    """
    Result produced by runtime execution.
    """

    success: bool = True

    results: list[ActionResult] = field(
        default_factory=list
    )

    actions_executed: int = 0

    started_at: datetime | None = None

    finished_at: datetime | None = None

    duration_ms: float = 0.0


    @property
    def failed_actions(self) -> int:

        return sum(
            1
            for result in self.results
            if not result.success
        )


    @property
    def successful_actions(self) -> int:

        return sum(
            1
            for result in self.results
            if result.success
        )