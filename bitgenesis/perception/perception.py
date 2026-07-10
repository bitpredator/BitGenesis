from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass(slots=True)
class Perception:
    """
    Internal representation of a perceived input.

    Every external stimulus entering the cognitive pipeline is
    converted into a Perception object before being processed by
    the remaining cognitive stages.
    """

    raw_input: Any

    modality: str = "text"

    language: str | None = None

    source: str | None = None

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    metadata: dict[str, Any] = field(
        default_factory=dict
    )