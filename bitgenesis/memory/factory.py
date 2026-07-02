from bitgenesis.events.event import Event
from bitgenesis.memory.object import MemoryObject


class MemoryFactory:

    @staticmethod
    def from_event(event: Event) -> MemoryObject:

        return MemoryObject(
            id=event.id,

            source=event.source,

            # ✅ SOLO payload (OBBLIGATORIO per listener test)
            content=event.payload,

            metadata={
                "event_id": event.id,
                "event_type": event.type.value,
                "event_category": event.category.value,
                "event_source": event.source,
                "priority": event.priority.name,
                "timestamp": event.timestamp,
            },

            importance=0.5,
            confidence=1.0,

            tags=[
                event.category.value,
                event.type.value,
            ],
        )