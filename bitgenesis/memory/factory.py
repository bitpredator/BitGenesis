"""
Memory object factory.

Converts events into MemoryObject instances.
"""

from bitgenesis.events.event import Event
from bitgenesis.memory.object import MemoryObject


class MemoryFactory:
    """
    Factory responsible for creating MemoryObject instances
    from incoming events.
    """

    @staticmethod
    def from_event(event: Event) -> MemoryObject:
        """
        Create a MemoryObject from an Event.
        """

        return MemoryObject(
            source=event.source,
            content=event.payload,
            metadata={
                "event_id": event.id,
                "event_type": event.type.value,
                "event_category": event.category.value,
                "timestamp": event.timestamp,
                "priority": event.priority.name,
            },
            importance=0.5,
            confidence=1.0,
            tags=[
                event.category.value,
                event.type.value,
            ],
        )