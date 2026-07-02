from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventCategory, EventType, EventPriority

from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.listener import MemoryListener


def test_event_is_converted_to_memory():
    store = MemoryStore()
    listener = MemoryListener(store)

    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="test",
        payload={"key": "value"},
        priority=EventPriority.NORMAL,
    )

    listener.handle(event)

    memory = store.get(event.id)

    assert memory is not None
    assert memory.id == event.id
    assert memory.source == EventCategory.SYSTEM.value
    assert memory.content["type"] == EventType.SYSTEM_STARTED.value


def test_memory_listener_stores_multiple_events():
    store = MemoryStore()
    listener = MemoryListener(store)

    events = [
        Event(
            category=EventCategory.MEMORY,
            type=EventType.MEMORY_CREATED,
            source="test",
            payload={"a": 1},
            priority=EventPriority.NORMAL,
        ),
        Event(
            category=EventCategory.REASONING,
            type=EventType.REASONING_STARTED,
            source="test",
            payload={"b": 2},
            priority=EventPriority.HIGH,
        ),
    ]

    for event in events:
        listener.handle(event)

    assert len(store.all()) == 2
    assert {m.id for m in store.all()} == {e.id for e in events}