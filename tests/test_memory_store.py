from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.object import MemoryObject


def create_sample_memory(memory_id: str, source: str = "user", content: str = "data"):
    memory = MemoryObject(
        id=memory_id,
        source=source,
        content=content,
    )
    return memory


def test_add_and_get_memory():
    store = MemoryStore()

    memory = create_sample_memory("m1")

    store.add(memory)

    result = store.get("m1")

    assert result is not None
    assert result.id == "m1"
    assert result.content == "data"


def test_get_non_existing_memory():
    store = MemoryStore()

    result = store.get("missing")

    assert result is None


def test_exists_true():
    store = MemoryStore()

    memory = create_sample_memory("m1")

    store.add(memory)

    assert store.exists("m1") is True


def test_exists_false():
    store = MemoryStore()

    assert store.exists("unknown") is False


def test_remove_memory():
    store = MemoryStore()

    memory = create_sample_memory("m1")

    store.add(memory)

    store.remove("m1")

    assert store.exists("m1") is False


def test_all_returns_all_memories():
    store = MemoryStore()

    m1 = create_sample_memory("m1")
    m2 = create_sample_memory("m2")

    store.add(m1)
    store.add(m2)

    all_memories = store.all()

    assert len(all_memories) == 2
    assert {m.id for m in all_memories} == {"m1", "m2"}


def test_find_by_source():
    store = MemoryStore()

    m1 = create_sample_memory("m1", source="user")
    m2 = create_sample_memory("m2", source="system")
    m3 = create_sample_memory("m3", source="user")

    store.add(m1)
    store.add(m2)
    store.add(m3)

    results = store.find_by_source("user")

    assert len(results) == 2
    assert {m.id for m in results} == {"m1", "m3"}


def test_find_by_tag():
    store = MemoryStore()

    m1 = create_sample_memory("m1")
    m2 = create_sample_memory("m2")
    m3 = create_sample_memory("m3")

    m1.add_tag("important")
    m2.add_tag("important")
    m3.add_tag("irrelevant")

    store.add(m1)
    store.add(m2)
    store.add(m3)

    results = store.find_by_tag("important")

    assert len(results) == 2
    assert {m.id for m in results} == {"m1", "m2"}