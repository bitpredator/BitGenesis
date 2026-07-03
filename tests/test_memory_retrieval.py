from bitgenesis.memory.memory_retrieval import MemoryRetrieval
from bitgenesis.memory.object import MemoryObject
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
    EventPriority,
)


def create_event():
    return Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="kernel",
        payload={},
        priority=EventPriority.NORMAL,
    )


def create_memory(
    event_type="system.started",
    category="system",
    source="kernel",
    importance=0.5,
    confidence=1.0,
):

    return MemoryObject(
        source=source,
        content={},
        importance=importance,
        confidence=confidence,
        metadata={
            "event_type": event_type,
            "event_category": category,
        },
    )


def test_retrieve_returns_list():

    event = create_event()

    memories = [
        create_memory(),
        create_memory(),
    ]

    result = MemoryRetrieval.retrieve(event, memories)

    assert isinstance(result, list)


def test_retrieve_respects_top_k():

    event = create_event()

    memories = [create_memory() for _ in range(20)]

    result = MemoryRetrieval.retrieve(event, memories, top_k=5)

    assert len(result) == 5


def test_matching_memory_is_ranked_first():

    event = create_event()

    matching = create_memory(
        event_type="system.started",
        category="system",
        source="kernel",
    )

    other = create_memory(
        event_type="user.login",
        category="user",
        source="client",
    )

    result = MemoryRetrieval.retrieve(event, [other, matching])

    assert result[0] is matching


def test_empty_memory_returns_empty_list():

    event = create_event()

    result = MemoryRetrieval.retrieve(event, [])

    assert result == []


def test_importance_affects_ranking():

    event = create_event()

    low = create_memory(importance=0.2)

    high = create_memory(importance=1.0)

    result = MemoryRetrieval.retrieve(event, [low, high])

    assert result[0] is high