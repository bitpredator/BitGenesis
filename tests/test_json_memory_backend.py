"""
Tests for JSON memory persistence backend.
"""

from bitgenesis.memory.object import MemoryObject
from bitgenesis.memory.storage.json_backend import JsonMemoryBackend


def create_memory() -> MemoryObject:

    return MemoryObject(
        source="test",
        content={
            "message": "hello world"
        },
        metadata={
            "type": "test"
        },
        tags=[
            "testing"
        ],
    )


def test_json_backend_creates_file(tmp_path):

    path = tmp_path / "memories.json"

    JsonMemoryBackend(path)

    assert path.exists()



def test_json_backend_save_and_exists(tmp_path):

    path = tmp_path / "memories.json"

    backend = JsonMemoryBackend(path)

    memory = create_memory()

    backend.save(memory)

    assert backend.exists(
        str(memory.id)
    )



def test_json_backend_get_memory(tmp_path):

    path = tmp_path / "memories.json"

    backend = JsonMemoryBackend(path)

    memory = create_memory()

    backend.save(memory)

    loaded = backend.get(
        str(memory.id)
    )

    assert loaded is not None

    assert loaded.id == memory.id

    assert loaded.content == memory.content



def test_json_backend_persistence_between_instances(tmp_path):

    path = tmp_path / "memories.json"

    backend1 = JsonMemoryBackend(path)

    memory = create_memory()

    backend1.save(memory)


    backend2 = JsonMemoryBackend(path)

    loaded = backend2.get(
        str(memory.id)
    )


    assert loaded is not None

    assert loaded.id == memory.id

    assert loaded.source == "test"



def test_json_backend_remove(tmp_path):

    path = tmp_path / "memories.json"

    backend = JsonMemoryBackend(path)

    memory = create_memory()

    backend.save(memory)

    backend.remove(
        str(memory.id)
    )


    assert not backend.exists(
        str(memory.id)
    )



def test_json_backend_clear(tmp_path):

    path = tmp_path / "memories.json"

    backend = JsonMemoryBackend(path)

    memory = create_memory()

    backend.save(memory)

    backend.clear()


    assert backend.load() == []