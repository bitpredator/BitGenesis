from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventCategory, EventType
from bitgenesis.events.event import Event

from bitgenesis.kernel.kernel import Kernel
from bitgenesis.memory.service import MemoryService


def bootstrap():
    bus = EventBus()
    kernel = Kernel(bus)

    memory_service = MemoryService(bus)

    kernel.register(
        memory_service
    )

    kernel.start()

    # 🔥 FIRST MEMORY EVENT (SYSTEM BIRTH)
    bus.publish(
        Event(
            category=EventCategory.MEMORY,
            type=EventType.MEMORY_BOOTSTRAP,
            source="bootstrap",
            payload={
                "message": "BitGenesis system initialized",
                "phase": "birth"
            }
        )
    )

    return (
        bus,
        kernel,
        memory_service.store,
    )