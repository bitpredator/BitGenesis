from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventCategory, EventType
from bitgenesis.events.event import Event

from bitgenesis.kernel.kernel import Kernel
from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.listener import MemoryListener


def bootstrap():
    bus = EventBus()
    kernel = Kernel(bus)

    store = MemoryStore()
    memory_listener = MemoryListener(store)

    # memory listens to system events
    bus.subscribe(EventCategory.SYSTEM, memory_listener.handle)

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

    return bus, kernel, store