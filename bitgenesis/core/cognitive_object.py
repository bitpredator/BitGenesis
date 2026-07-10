"""
Base cognitive object for BitGenesis.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID

from bitgenesis.core.entity import Entity


def _serialize_value(value):
    """
    Convert complex Python objects into JSON compatible values.
    """

    if isinstance(value, UUID):
        return str(value)

    if isinstance(value, datetime):
        return value.isoformat()

    if isinstance(value, dict):
        return {
            key: _serialize_value(item)
            for key, item in value.items()
        }

    if isinstance(value, list):
        return [
            _serialize_value(item)
            for item in value
        ]

    if isinstance(value, tuple):
        return [
            _serialize_value(item)
            for item in value
        ]

    return value


@dataclass(slots=True, kw_only=True)
class CognitiveObject(Entity):
    """
    Base class for every cognitive object managed by BitGenesis.
    """

    metadata: dict[str, object] = field(default_factory=dict)

    importance: float = 0.5

    confidence: float = 1.0

    tags: list[str] = field(default_factory=list)


    def add_tag(self, tag: str) -> None:

        if tag not in self.tags:
            self.tags.append(tag)
            self.touch()


    def remove_tag(self, tag: str) -> None:

        if tag in self.tags:
            self.tags.remove(tag)
            self.touch()


    def to_dict(self) -> dict:
        """
        Serialize cognitive object into JSON-safe data.
        """

        data = super().to_dict()

        data.update(
            {
                "metadata": _serialize_value(
                    self.metadata
                ),
                "importance": self.importance,
                "confidence": self.confidence,
                "tags": list(self.tags),
            }
        )

        return data