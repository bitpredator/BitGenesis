"""
Memory object definition.
"""

from dataclasses import dataclass, field
from typing import Any

from bitgenesis.core.cognitive_object import CognitiveObject


@dataclass(slots=True, kw_only=True)
class MemoryObject(CognitiveObject):
    source: str
    content: Any
    links: list[str] = field(default_factory=list)

    def add_link(self, memory_id: str) -> None:
        if memory_id not in self.links:
            self.links.append(memory_id)
            self.touch()

    def remove_link(self, memory_id: str) -> None:
        if memory_id in self.links:
            self.links.remove(memory_id)
            self.touch()

    def is_linked_to(self, memory_id: str) -> bool:
        return memory_id in self.links

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags