from bitgenesis.knowledge.extractor import KnowledgeExtractor
from bitgenesis.memory.object import MemoryObject


def create_memory(payload):

    return MemoryObject(
        source="pytest",
        content={
            "payload": payload,
        },
    )


def test_extract_single_entity():

    memory = create_memory(
        {
            "creator": "BitPredator",
        }
    )

    entities = KnowledgeExtractor.extract(memory)

    assert len(entities) == 1

    assert entities[0].name == "BitPredator"

    assert entities[0].entity_type == "creator"


def test_extract_multiple_entities():

    memory = create_memory(
        {
            "creator": "BitPredator",
            "project": "BitGenesis",
            "language": "Python",
        }
    )

    entities = KnowledgeExtractor.extract(memory)

    assert len(entities) == 3


def test_ignore_non_string_values():

    memory = create_memory(
        {
            "creator": "BitPredator",
            "version": 1,
            "enabled": True,
        }
    )

    entities = KnowledgeExtractor.extract(memory)

    assert len(entities) == 1

    assert entities[0].name == "BitPredator"


def test_empty_payload_returns_empty_list():

    memory = create_memory({})

    assert KnowledgeExtractor.extract(memory) == []


def test_missing_payload_returns_empty_list():

    memory = MemoryObject(
        source="pytest",
        content={},
    )

    assert KnowledgeExtractor.extract(memory) == []


def test_none_content_returns_empty_list():

    memory = MemoryObject(
        source="pytest",
        content=None,
    )

    assert KnowledgeExtractor.extract(memory) == []