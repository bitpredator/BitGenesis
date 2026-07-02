from bitgenesis.core.cognitive_object import CognitiveObject
from bitgenesis.memory.object import MemoryObject


def test_memory_object_is_cognitive_object():
    memory = MemoryObject(
        source="user",
        content="Hello BitGenesis"
    )

    assert isinstance(memory, CognitiveObject)


def test_source_is_stored():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    assert memory.source == "user"


def test_content_is_stored():
    memory = MemoryObject(
        source="user",
        content="Hello BitGenesis"
    )

    assert memory.content == "Hello BitGenesis"


def test_links_are_empty_by_default():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    assert memory.links == []


def test_add_link():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    memory.add_link("memory-001")

    assert memory.links == ["memory-001"]


def test_add_link_avoids_duplicates():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    memory.add_link("memory-001")
    memory.add_link("memory-001")

    assert memory.links == ["memory-001"]


def test_remove_link():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    memory.add_link("memory-001")
    memory.remove_link("memory-001")

    assert memory.links == []


def test_is_linked_to():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    memory.add_link("memory-001")

    assert memory.is_linked_to("memory-001")


def test_is_not_linked_to():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    assert not memory.is_linked_to("memory-001")


def test_has_tag():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    memory.add_tag("important")

    assert memory.has_tag("important")


def test_has_tag_returns_false_when_missing():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    assert not memory.has_tag("important")


def test_add_link_updates_timestamp():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    previous_timestamp = memory.updated_at

    memory.add_link("memory-001")

    assert memory.updated_at > previous_timestamp


def test_remove_link_updates_timestamp():
    memory = MemoryObject(
        source="user",
        content="Hello"
    )

    memory.add_link("memory-001")

    previous_timestamp = memory.updated_at

    memory.remove_link("memory-001")

    assert memory.updated_at > previous_timestamp