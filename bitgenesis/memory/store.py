"""
Memory storage layer.

This component is responsible for storing and retrieving MemoryObject instances.
It does NOT perform reasoning or intelligence operations.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from bitgenesis.memory.object import MemoryObject


class MemoryStore:
    """
    Simple in-memory storage for MemoryObject instances.
    """

    def __init__(self) -> None:
        self._store: Dict[str, MemoryObject] = {}

    # -------------------------
    # Core CRUD operations
    # -------------------------

    def add(self, memory: MemoryObject) -> None:
        """
        Add or overwrite a memory in the store.
        """
        self._store[memory.id] = memory

    def get(self, memory_id: str) -> Optional[MemoryObject]:
        """
        Retrieve a memory by its ID.
        """
        return self._store.get(memory_id)

    def remove(self, memory_id: str) -> None:
        """
        Remove a memory from the store if it exists.
        """
        self._store.pop(memory_id, None)

    def exists(self, memory_id: str) -> bool:
        """
        Check whether a memory exists in the store.
        """
        return memory_id in self._store

    # -------------------------
    # Bulk access
    # -------------------------

    def all(self) -> List[MemoryObject]:
        """
        Return all stored memories.
        """
        return list(self._store.values())

    # -------------------------
    # Query operations
    # -------------------------

    def find_by_source(self, source: str) -> List[MemoryObject]:
        return [
            memory
            for memory in self._store.values()
            if memory.source == source
        ]

    def find_by_tag(self, tag: str) -> List[MemoryObject]:
        return [
            memory
            for memory in self._store.values()
            if tag in memory.tags
        ]