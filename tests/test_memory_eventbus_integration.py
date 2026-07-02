from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventCategory, EventType, EventPriority

from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.listener import MemoryListener


def test_eventbus_triggers_memory_listener():
    store = MemoryStore()
    listener = MemoryListener(store)

    bus = EventBus()

    # subscribe listener to ALL events (wildcard style via explicit types for now)
    bus.subscribe(EventType.SYSTEM_STARTED, listener.handle)

    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="test",
        payload={"x": 123},
        priority=EventPriority.NORMAL,
    )

    bus.emit(event)

    memory = store.get(event.id)

    assert memory is not None
    assert memory.content["payload"]["x"] == 123