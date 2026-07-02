"""
Memory event listener.

This component connects the Event System with the MemoryStore,
allowing automatic memory creation from system events.
"""

from typing import Any

from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventType
from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.object import MemoryObject


class MemoryListener:
    """
    Listens to system events and converts them into MemoryObjects.
    """

    def __init__(self, store: MemoryStore) -> None:
        self.store = store

    def handle(self, event: Event) -> None:
        """
        Handle incoming events and store relevant ones as memory.
        """

        memory = self._convert_event_to_memory(event)

        self.store.add(memory)

    def _convert_event_to_memory(self, event: Event) -> MemoryObject:
        """
        Convert an Event into a MemoryObject.
        """

        return MemoryObject(
            id=event.id,
            source=event.category.value,
            content={
                "type": event.type.value,
                "payload": event.payload,
                "metadata": event.metadata,
                "priority": event.priority.value,
                "timestamp": event.timestamp.isoformat(),
            },
        )