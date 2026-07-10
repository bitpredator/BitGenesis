from bitgenesis.events.event import Event
from bitgenesis.memory.importance import MemoryImportance
from bitgenesis.memory.object import MemoryObject

from uuid import uuid4


class MemoryFactory:

    @staticmethod
    def from_event(event: Event) -> MemoryObject:

        content = {
            "payload": event.payload,
            "event": {
                "id": event.id,
                "type": event.type.value,
                "category": event.category.value,
                "source": event.source,
            },
        }

        evaluator = MemoryImportance()

        temporary_memory = MemoryObject(
            id=event.id,
            source=event.source,
            content=content,
            metadata={},
            importance=0.0,
            confidence=1.0,
            tags=[],
        )

        importance = evaluator.score(
            temporary_memory
        )

        return MemoryObject(
            id=event.id,
            source=event.source,
            content=content,
            metadata={
                "event_id": event.id,
                "event_type": event.type.value,
                "event_category": event.category.value,
                "priority": event.priority.value,
                "timestamp": event.timestamp,
            },
            importance=importance,
            confidence=1.0,
            tags=[
                event.category.value,
                event.type.value,
            ],
        )


    @staticmethod
    def from_consolidation(data: dict) -> MemoryObject:
        """
        Creates a memory object from a cognitive consolidation cycle.
        """

        memory_id = str(uuid4())

        content = {
            "consolidation": data,
        }

        evaluator = MemoryImportance()

        temporary_memory = MemoryObject(
            id=memory_id,
            source="cognitive_cycle",
            content=content,
            metadata={},
            importance=0.0,
            confidence=1.0,
            tags=[],
        )

        importance = evaluator.score(
            temporary_memory
        )

        return MemoryObject(
            id=memory_id,
            source="cognitive_cycle",
            content=content,
            metadata={
                "type": "consolidation",
            },
            importance=importance,
            confidence=1.0,
            tags=[
                "cognition",
                "consolidated",
            ],
        )