from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)
from bitgenesis.events.event import Event

from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.memory.object import MemoryObject


def test_factory_returns_memory_object():
    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
    )

    memory = MemoryFactory.from_event(event)

    assert isinstance(memory, MemoryObject)


def test_factory_copies_source():
    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="kernel",
    )

    memory = MemoryFactory.from_event(event)

    assert memory.source == "kernel"


def test_factory_copies_payload():
    payload = {
        "message": "hello",
        "value": 42,
    }

    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
        payload=payload,
    )

    memory = MemoryFactory.from_event(event)

    assert memory.content == payload


def test_factory_generates_metadata():
    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
    )

    memory = MemoryFactory.from_event(event)

    assert memory.metadata["event_id"] == event.id
    assert memory.metadata["event_type"] == event.type.value
    assert memory.metadata["event_category"] == event.category.value


def test_factory_sets_default_scores():
    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
    )

    memory = MemoryFactory.from_event(event)

    assert memory.importance == 0.5
    assert memory.confidence == 1.0


def test_factory_generates_tags():
    event = Event(
        category=EventCategory.MEMORY,
        type=EventType.MEMORY_CREATED,
        source="pytest",
    )

    memory = MemoryFactory.from_event(event)

    assert EventCategory.MEMORY.value in memory.tags
    assert EventType.MEMORY_CREATED.value in memory.tags


def test_factory_preserves_timestamp():
    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
    )

    memory = MemoryFactory.from_event(event)

    assert memory.metadata["timestamp"] == event.timestamp


def test_factory_preserves_priority():
    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
        priority=EventPriority.CRITICAL,
    )

    memory = MemoryFactory.from_event(event)

    assert memory.metadata["priority"] == "CRITICAL"