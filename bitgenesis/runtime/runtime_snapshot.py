from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from bitgenesis.runtime.runtime_statistics import RuntimeStatistics


@dataclass(frozen=True, slots=True)
class RuntimeSnapshot:
    """
    Immutable snapshot of the runtime state.

    A snapshot captures the runtime statistics at a specific
    instant and can safely be stored, logged or exported.
    """

    created_at: datetime

    statistics: RuntimeStatistics

    # --------------------------------------------------
    # Export
    # --------------------------------------------------

    def to_dict(self) -> dict:

        return {
            "created_at": self.created_at.isoformat(),
            "statistics": self.statistics.to_dict(),
        }

    # --------------------------------------------------
    # Representation
    # --------------------------------------------------

    def __str__(self) -> str:

        stats = self.statistics

        return (
            "RuntimeSnapshot("
            f"ticks={stats.total_ticks}, "
            f"executions={stats.total_executions}, "
            f"services={stats.services_executed}, "
            f"success_rate={stats.execution_success_rate:.2%}"
            ")"
        )