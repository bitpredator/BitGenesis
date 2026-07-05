from bitgenesis.memory.query import MemoryQuery
from bitgenesis.memory.factory import MemoryFactory
from bitgenesis.memory.store import MemoryStore

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)


def create_memory(message: str):

    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
        payload={"message": message},
        priority=EventPriority.NORMAL,
    )

    return MemoryFactory.from_event(event)


def test_memory_query_all():

    store = MemoryStore()

    m1 = create_memory("First")
    m2 = create_memory("Second")

    store.add(m1)
    store.add(m2)

    query = MemoryQuery(store)

    result = query.all()

    assert len(result) == 2
    assert m1 in result
    assert m2 in result


def test_memory_query_latest():

    store = MemoryStore()

    m1 = create_memory("First")
    m2 = create_memory("Second")

    store.add(m1)
    store.add(m2)

    query = MemoryQuery(store)

    latest = query.latest()

    assert latest == m2


def test_memory_query_recent():

    store = MemoryStore()

    for i in range(10):
        store.add(create_memory(f"Memory {i}"))

    query = MemoryQuery(store)

    recent = query.recent(limit=3)

    assert len(recent) == 3

    assert recent[0].content["payload"]["message"] == "Memory 7"
    assert recent[1].content["payload"]["message"] == "Memory 8"
    assert recent[2].content["payload"]["message"] == "Memory 9"


def test_memory_query_search():

    store = MemoryStore()

    store.add(create_memory("Python"))
    store.add(create_memory("Rust"))
    store.add(create_memory("C++"))

    query = MemoryQuery(store)

    result = query.search(
        lambda memory: memory.content["payload"]["message"] == "Rust"
    )

    assert len(result) == 1

    assert result[0].content["payload"]["message"] == "Rust"


def test_memory_query_latest_empty():

    query = MemoryQuery(MemoryStore())

    assert query.latest() is None


def test_memory_query_recent_empty():

    query = MemoryQuery(MemoryStore())

    assert query.recent() == []


def test_memory_query_all_empty():

    query = MemoryQuery(MemoryStore())

    assert query.all() == []


def test_memory_query_search_empty():

    store = MemoryStore()

    store.add(create_memory("Python"))

    query = MemoryQuery(store)

    result = query.search(
        lambda memory: memory.content["payload"]["message"] == "Java"
    )

    assert result == []