from bitgenesis.knowledge.builder import KnowledgeBuilder
from bitgenesis.knowledge.graph import KnowledgeGraph
from bitgenesis.knowledge.registry import KnowledgeRegistry
from bitgenesis.memory.object import MemoryObject


def create_memory(payload):

    return MemoryObject(
        source="pytest",
        content={
            "payload": payload,
        },
    )


def test_builder_creates_entities():

    registry = KnowledgeRegistry()
    graph = KnowledgeGraph()

    builder = KnowledgeBuilder(registry, graph)

    memory = create_memory(
        {
            "creator": "BitPredator",
            "project": "BitGenesis",
        }
    )

    entities = builder.process(memory)

    assert len(entities) == 2

    assert registry.count() == 2


def test_builder_reuses_existing_entities():

    registry = KnowledgeRegistry()
    graph = KnowledgeGraph()

    builder = KnowledgeBuilder(registry, graph)

    builder.process(
        create_memory(
            {
                "creator": "BitPredator",
            }
        )
    )

    builder.process(
        create_memory(
            {
                "creator": "BitPredator",
            }
        )
    )

    assert registry.count() == 1


def test_builder_creates_graph_relations():

    registry = KnowledgeRegistry()
    graph = KnowledgeGraph()

    builder = KnowledgeBuilder(registry, graph)

    builder.process(
        create_memory(
            {
                "creator": "BitPredator",
                "project": "BitGenesis",
            }
        )
    )

    assert len(graph.edges) == 1


def test_empty_memory():

    registry = KnowledgeRegistry()
    graph = KnowledgeGraph()

    builder = KnowledgeBuilder(registry, graph)

    entities = builder.process(create_memory({}))

    assert entities == []

    assert registry.count() == 0