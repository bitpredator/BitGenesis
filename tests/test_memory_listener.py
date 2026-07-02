from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)

from bitgenesis.memory.listener import MemoryListener
from bitgenesis.memory.store import MemoryStore


def test_event_is_converted_processed_and_stored():
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

    # Factory
    assert memory.source == event.source
    assert memory.content == event.payload

    assert memory.metadata["event_id"] == event.id
    assert memory.metadata["event_type"] == event.type.value
    assert memory.metadata["event_category"] == event.category.value
    assert memory.metadata["priority"] == event.priority.name

    # Processor
    assert "memory" in memory.tags
    assert "processed" in memory.tags

    assert memory.metadata["processed"] is True

    assert 0.0 <= memory.importance <= 1.0
    assert 0.0 <= memory.confidence <= 1.0


def test_memory_listener_stores_multiple_processed_events():
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

    memories = store.all()

    assert len(memories) == len(events)
    assert {m.metadata["event_id"] for m in memories} == {e.id for e in events}

    for memory in memories:
        assert "memory" in memory.tags
        assert "processed" in memory.tags
        assert memory.metadata["processed"] is True

        assert 0.0 <= memory.importance <= 1.0
        assert 0.0 <= memory.confidence <= 1.0