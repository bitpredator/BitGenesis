from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventCategory, EventType, EventPriority


def create_event():
    return Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="test-source",
        payload={"hello": "world"},
        priority=EventPriority.NORMAL,
    )


def test_factory_creates_memory_object():
    event = create_event()

    memory = MemoryFactory.from_event(event)

    assert memory is not None
    assert memory.id == event.id
    assert memory.source == event.source


def test_factory_maps_event_content():
    event = create_event()

    memory = MemoryFactory.from_event(event)

    # content = payload puro
    assert memory.content == event.payload


def test_factory_preserves_event_payload_structure():
    event = create_event()

    memory = MemoryFactory.from_event(event)

    assert isinstance(memory.content, dict)
    assert memory.content["hello"] == "world"


def test_factory_metadata_contains_event_info():
    event = create_event()

    memory = MemoryFactory.from_event(event)

    assert memory.metadata["event_id"] == event.id
    assert memory.metadata["event_type"] == event.type.value
    assert memory.metadata["event_category"] == event.category.value

    # coerente con factory: .name
    assert memory.metadata["priority"] == event.priority.name


def test_factory_tags_are_correct():
    event = create_event()

    memory = MemoryFactory.from_event(event)

    assert event.category.value in memory.tags
    assert event.type.value in memory.tags