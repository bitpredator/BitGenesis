from bitgenesis.events.event_bus import EventBus
from bitgenesis.kernel.kernel import Kernel
from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.listener import MemoryListener


def bootstrap():
    bus = EventBus()
    kernel = Kernel(bus)

    # MEMORY SYSTEM
    store = MemoryStore()
    memory_listener = MemoryListener(store)

    # hook eventi → memoria
    bus.subscribe("perception.event", memory_listener.handle)
    bus.subscribe("system.event", memory_listener.handle)
    bus.subscribe("reasoning.event", memory_listener.handle)

    kernel.start()

    return bus, kernel, store