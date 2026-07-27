from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class ServiceExecution:
    """
    Represents the execution of a runtime service.

    Each runtime service executed by the orchestrator
    produces one ServiceExecution instance.
    """

    service_name: str

    success: bool = True

    started_at: datetime | None = None

    finished_at: datetime | None = None

    duration_ms: float = 0.0

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )

    @property
    def executed(self) -> bool:
        """
        True if the service has been executed.
        """

        return (
            self.started_at is not None
            and self.finished_at is not None
        )

    @property
    def failed(self) -> bool:
        """
        Convenience property.
        """

        return not self.success