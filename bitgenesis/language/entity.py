from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from enum import Enum
from typing import Any


class EntityType(Enum):
    """
    Supported entity types.

    Entity extraction begins with a small set of
    generic concepts and can be expanded over time.
    """

    UNKNOWN = "unknown"

    PERSON = "person"

    PROJECT = "project"

    ORGANIZATION = "organization"

    PLACE = "place"

    LANGUAGE = "language"

    SERVICE = "service"

    FILE = "file"

    MEMORY = "memory"

    KNOWLEDGE = "knowledge"

    TOOL = "tool"

    VERSION = "version"

    DATE = "date"

    TIME = "time"

    NUMBER = "number"


@dataclass(slots=True)
class Entity:
    """
    Represents one semantic entity extracted
    from natural language.

    Future versions may include:

    - character offsets
    - aliases
    - ontology identifiers
    - knowledge graph links
    - embeddings
    """

    type: EntityType

    value: str

    confidence: float = 1.0

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def to_dict(self) -> dict[str, Any]:
        """
        Returns a serializable representation.
        """

        return {
            "type": self.type.value,
            "value": self.value,
            "confidence": self.confidence,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
        }

    def __str__(self) -> str:
        return self.value