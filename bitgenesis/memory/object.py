"""
Memory object definition.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import UUID

from bitgenesis.core.cognitive_object import CognitiveObject


@dataclass(slots=True, kw_only=True)
class MemoryObject(CognitiveObject):
    """
    Persistent cognitive memory object.

    Represents a single stored memory inside BitGenesis.
    """

    source: str

    content: Any

    links: list[str] = field(
        default_factory=list
    )


    # ---------------------------------------------------------
    # Link management
    # ---------------------------------------------------------

    def add_link(
        self,
        memory_id: str,
    ) -> None:

        if memory_id not in self.links:

            self.links.append(
                memory_id
            )

            self.touch()


    def remove_link(
        self,
        memory_id: str,
    ) -> None:

        if memory_id in self.links:

            self.links.remove(
                memory_id
            )

            self.touch()


    def is_linked_to(
        self,
        memory_id: str,
    ) -> bool:

        return memory_id in self.links


    def has_tag(
        self,
        tag: str,
    ) -> bool:

        return tag in self.tags


    # ---------------------------------------------------------
    # Serialization
    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        """
        Serialize memory object.
        """

        data = super().to_dict()

        data.update(
            {
                "source": self.source,
                "content": self.content,
                "links": list(self.links),
            }
        )

        return data


    @classmethod
    def from_dict(
        cls,
        data: dict,
    ) -> "MemoryObject":
        """
        Restore memory object from serialized data.
        """

        return cls(

            id=UUID(
                data["id"]
            ),

            created_at=datetime.fromisoformat(
                data["created_at"]
            ),

            updated_at=datetime.fromisoformat(
                data["updated_at"]
            ),

            metadata=data.get(
                "metadata",
                {},
            ),

            importance=data.get(
                "importance",
                0.5,
            ),

            confidence=data.get(
                "confidence",
                1.0,
            ),

            tags=data.get(
                "tags",
                [],
            ),

            source=data.get(
                "source",
                "unknown",
            ),

            content=data.get(
                "content",
                {},
            ),

            links=data.get(
                "links",
                [],
            ),
        )