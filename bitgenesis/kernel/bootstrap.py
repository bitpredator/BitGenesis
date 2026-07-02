from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventCategory
from bitgenesis.events.enums import EventType

from bitgenesis.kernel.kernel import Kernel
from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.listener import MemoryListener


def bootstrap():
    bus = EventBus()
    kernel = Kernel(bus)

    # MEMORY SYSTEM
    store = MemoryStore()
    memory_listener = MemoryListener(store)

    # hook events → memory (CLEAN VERSION)
    bus.subscribe(EventCategory.PERCEPTION, memory_listener.handle)
    bus.subscribe(EventCategory.SYSTEM, memory_listener.handle)
    bus.subscribe(EventCategory.REASONING, memory_listener.handle)

    kernel.start()

    return bus, kernel, store