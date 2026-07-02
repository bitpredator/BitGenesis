from bitgenesis.events.event import Event
from bitgenesis.memory.object import MemoryObject


class MemoryFactory:

    @staticmethod
    def from_event(event: Event) -> MemoryObject:

        return MemoryObject(
            id=event.id,
            source=event.source,

            content={
                "payload": event.payload,
                "event": {
                    "id": event.id,
                    "type": event.type.value,
                    "category": event.category.value,
                    "source": event.source,
                }
            },

            metadata={
                "event_id": event.id,
                "event_type": event.type.value,
                "event_category": event.category.value,
                "priority": event.priority.value,
                "timestamp": event.timestamp,
            },

            importance=0.5,
            confidence=1.0,

            tags=[
                event.category.value,
                event.type.value,
            ],
        )