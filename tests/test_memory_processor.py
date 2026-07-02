from bitgenesis.memory.object import MemoryObject
from bitgenesis.memory.processor import MemoryProcessor


def create_memory(**kwargs) -> MemoryObject:
    """
    Create a MemoryObject with sensible defaults.
    """
    defaults = {
        "source": "pytest",
        "content": {"message": "hello"},
    }
    defaults.update(kwargs)
    return MemoryObject(**defaults)


def test_process_returns_same_instance():
    processor = MemoryProcessor()

    memory = create_memory()

    processed = processor.process(memory)

    assert processed is memory


def test_importance_is_clamped_to_zero():
    processor = MemoryProcessor()

    memory = create_memory(importance=-10)

    processor.process(memory)

    assert memory.importance == 0.0


def test_importance_is_clamped_to_one():
    processor = MemoryProcessor()

    memory = create_memory(importance=5)

    processor.process(memory)

    assert memory.importance == 1.0


def test_confidence_is_clamped_to_zero():
    processor = MemoryProcessor()

    memory = create_memory(confidence=-2)

    processor.process(memory)

    assert memory.confidence == 0.0


def test_confidence_is_clamped_to_one():
    processor = MemoryProcessor()

    memory = create_memory(confidence=8)

    processor.process(memory)

    assert memory.confidence == 1.0


def test_memory_tag_is_added():
    processor = MemoryProcessor()

    memory = create_memory()

    processor.process(memory)

    assert "memory" in memory.tags


def test_processed_tag_is_added():
    processor = MemoryProcessor()

    memory = create_memory()

    processor.process(memory)

    assert "processed" in memory.tags


def test_existing_tags_are_preserved():
    processor = MemoryProcessor()

    memory = create_memory(tags=["important"])

    processor.process(memory)

    assert "important" in memory.tags
    assert "memory" in memory.tags
    assert "processed" in memory.tags


def test_processed_metadata_is_set():
    processor = MemoryProcessor()

    memory = create_memory()

    processor.process(memory)

    assert memory.metadata["processed"] is True


def test_processing_is_idempotent():
    processor = MemoryProcessor()

    memory = create_memory()

    processor.process(memory)
    processor.process(memory)

    assert memory.tags.count("memory") == 1
    assert memory.tags.count("processed") == 1