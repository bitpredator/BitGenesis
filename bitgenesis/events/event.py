"""
Core event object.
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any

from bitgenesis.core.identifiers import generate_id

from .enums import EventCategory
from .enums import EventPriority
from .enums import EventType


@dataclass(slots=True, frozen=True, kw_only=True)
class Event:
    """
    Immutable event exchanged across the BitGenesis architecture.
    """

    category: EventCategory
    type: EventType
    source: str

    payload: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)

    priority: EventPriority = EventPriority.NORMAL

    id: str = field(default_factory=generate_id)

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )