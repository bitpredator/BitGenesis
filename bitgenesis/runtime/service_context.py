from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from bitgenesis.events.event_bus import EventBus



@dataclass(slots=True)
class ServiceContext:
    """
    Context provided to runtime services during orchestration.

    Contains shared runtime dependencies without coupling
    services directly to RuntimeManager.
    """


    event_bus: EventBus | None = None

    memory_store: Any = None

    graph: Any = None

    runtime_state: Any = None


    metadata: dict[str, Any] = field(
        default_factory=dict
    )



    def with_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Add contextual metadata.
        """

        self.metadata[key] = value