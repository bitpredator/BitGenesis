"""
Memory storage layer.

This component provides the public interface for memory storage.

Persistence is delegated to a configurable backend.
"""

from __future__ import annotations

from typing import List
from typing import Optional

from bitgenesis.memory.object import MemoryObject
from bitgenesis.memory.storage.backend import MemoryBackend
from bitgenesis.memory.storage.in_memory_backend import InMemoryBackend


class MemoryStore:
    """
    High-level interface for memory storage.

    The actual persistence mechanism is handled by a MemoryBackend.
    """

    def __init__(
        self,
        backend: MemoryBackend | None = None,
    ) -> None:

        self._backend = backend or InMemoryBackend()

    # ---------------------------------------------------------
    # Core CRUD operations
    # ---------------------------------------------------------

    def add(self, memory: MemoryObject) -> None:

        self._backend.save(memory)

    def get(self, memory_id: str) -> Optional[MemoryObject]:

        return self._backend.get(memory_id)

    def remove(self, memory_id: str) -> None:

        self._backend.remove(memory_id)

    def exists(self, memory_id: str) -> bool:

        return self._backend.exists(memory_id)

    # ---------------------------------------------------------
    # Bulk access
    # ---------------------------------------------------------

    def all(self) -> List[MemoryObject]:

        return self._backend.load()

    def clear(self) -> None:

        self._backend.clear()

    # ---------------------------------------------------------
    # Query operations
    # ---------------------------------------------------------

    def find_by_source(
        self,
        source: str,
    ) -> List[MemoryObject]:

        return [
            memory
            for memory in self._backend.load()
            if memory.source == source
        ]

    def find_by_tag(
        self,
        tag: str,
    ) -> List[MemoryObject]:

        return [
            memory
            for memory in self._backend.load()
            if tag in memory.tags
        ]