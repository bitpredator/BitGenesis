"""
Memory processing pipeline.

Responsible for enriching MemoryObject instances before
they are persisted inside the MemoryStore.
"""

from bitgenesis.memory.object import MemoryObject


class MemoryProcessor:
    """
    Enriches newly created memories.

    Future versions will perform semantic analysis,
    embedding generation, knowledge extraction,
    duplicate detection and consolidation.
    """

    def process(self, memory: MemoryObject) -> MemoryObject:
        """
        Process and enrich a memory object.

        Parameters
        ----------
        memory:
            The memory to process.

        Returns
        -------
        MemoryObject
            The processed memory.
        """

        self._normalize_importance(memory)
        self._normalize_confidence(memory)
        self._ensure_system_tags(memory)
        self._mark_processed(memory)

        return memory

    def _normalize_importance(self, memory: MemoryObject) -> None:
        """
        Clamp importance between 0.0 and 1.0.
        """

        memory.importance = max(0.0, min(1.0, memory.importance))

    def _normalize_confidence(self, memory: MemoryObject) -> None:
        """
        Clamp confidence between 0.0 and 1.0.
        """

        memory.confidence = max(0.0, min(1.0, memory.confidence))

    def _ensure_system_tags(self, memory: MemoryObject) -> None:
        """
        Ensure internal tags always exist.
        """

        if "memory" not in memory.tags:
            memory.add_tag("memory")

        if "processed" not in memory.tags:
            memory.add_tag("processed")

    def _mark_processed(self, memory: MemoryObject) -> None:
        """
        Mark memory as processed.
        """

        memory.metadata["processed"] = True