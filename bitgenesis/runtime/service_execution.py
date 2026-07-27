from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any

from bitgenesis.runtime.service_state import ServiceState



@dataclass(slots=True)
class ServiceExecution:
    """
    Represents runtime service execution.
    """


    service_name: str


    success: bool = True


    state: ServiceState = (
        ServiceState.CREATED
    )


    started_at: datetime | None = None


    finished_at: datetime | None = None


    duration_ms: float = 0.0


    metadata: dict[str, Any] = field(
        default_factory=dict
    )



    @property
    def failed(self) -> bool:

        return not self.success