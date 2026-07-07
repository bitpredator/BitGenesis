from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventCategory, EventType, EventPriority


def create_event(payload=None):
    return Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="test-source",
        payload=payload or {"hello": "world"},
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

    assert memory.content["payload"] == event.payload
    assert memory.content["event"]["type"] == event.type.value
    assert memory.content["event"]["source"] == event.source
    assert memory.content["event"]["category"] == event.category.value


def test_factory_preserves_event_payload_structure():
    event = create_event()

    memory = MemoryFactory.from_event(event)

    assert isinstance(memory.content["payload"], dict)
    assert memory.content["payload"]["hello"] == "world"


def test_factory_metadata_contains_event_info():
    event = create_event()

    memory = MemoryFactory.from_event(event)

    assert memory.metadata["event_id"] == event.id
    assert memory.metadata["event_type"] == event.type.value
    assert memory.metadata["event_category"] == event.category.value
    assert memory.metadata["priority"] == event.priority.value


def test_factory_tags_are_correct():
    event = create_event()

    memory = MemoryFactory.from_event(event)

    assert event.category.value in memory.tags
    assert event.type.value in memory.tags


def test_factory_calculates_importance_for_user_memory():
    event = create_event(
        {"message": "User likes Python"}
    )

    memory = MemoryFactory.from_event(event)

    assert memory.importance == 0.95


def test_factory_calculates_importance_for_planner_memory():
    event = create_event(
        {"message": "Planner initialized"}
    )

    memory = MemoryFactory.from_event(event)

    assert memory.importance == 0.70


def test_factory_calculates_importance_for_system_memory():
    event = create_event(
        {"message": "System started"}
    )

    memory = MemoryFactory.from_event(event)

    assert memory.importance == 0.40


def test_factory_calculates_default_importance():
    event = create_event(
        {"message": "Hello world"}
    )

    memory = MemoryFactory.from_event(event)

    assert memory.importance == 0.20