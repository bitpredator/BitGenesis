"""
Base cognitive object for BitGenesis.
"""

from dataclasses import dataclass, field

from bitgenesis.core.entity import Entity


@dataclass(slots=True, kw_only=True)
class CognitiveObject(Entity):
    """
    Base class for every cognitive object managed by BitGenesis.

    It extends Entity with common cognitive properties shared
    by memories, knowledge, goals, plans and other domain objects.
    """

    metadata: dict[str, object] = field(default_factory=dict)

    importance: float = 0.5

    confidence: float = 1.0

    tags: list[str] = field(default_factory=list)

    def add_tag(self, tag: str) -> None:
        """
        Add a tag if it is not already present.
        """
        if tag not in self.tags:
            self.tags.append(tag)
            self.touch()

    def remove_tag(self, tag: str) -> None:
        """
        Remove an existing tag.
        """
        if tag in self.tags:
            self.tags.remove(tag)
            self.touch()

    def to_dict(self) -> dict:
        """
        Serialize cognitive object.
        """

        data = super().to_dict()

        data.update(
            {
                "metadata": self.metadata,
                "importance": self.importance,
                "confidence": self.confidence,
                "tags": list(self.tags),
            }
        )

        return data        