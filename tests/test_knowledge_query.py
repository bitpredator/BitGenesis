from bitgenesis.knowledge.entity_node import EntityNode
from bitgenesis.knowledge.graph import KnowledgeGraph
from bitgenesis.knowledge.knowledge_query import KnowledgeQuery


def test_find_existing_node():

    graph = KnowledgeGraph()

    node = EntityNode(
        name="BitGenesis",
        entity_type="project",
    )

    graph.add_node(node)

    query = KnowledgeQuery(graph)

    assert query.find_by_name("BitGenesis") == node


def test_find_missing_node():

    graph = KnowledgeGraph()

    query = KnowledgeQuery(graph)

    assert query.find_by_name("Unknown") is None


def test_exists_returns_true():

    graph = KnowledgeGraph()

    node = EntityNode(
        name="Python",
        entity_type="language",
    )

    graph.add_node(node)

    query = KnowledgeQuery(graph)

    assert query.exists("Python")


def test_exists_returns_false():

    graph = KnowledgeGraph()

    query = KnowledgeQuery(graph)

    assert not query.exists("Java")


def test_neighbors_returns_relations():

    graph = KnowledgeGraph()

    creator = EntityNode(
        name="BitPredator",
        entity_type="creator",
    )

    project = EntityNode(
        name="BitGenesis",
        entity_type="project",
    )

    graph.add_relation(
        creator,
        "creator_of",
        project,
    )

    query = KnowledgeQuery(graph)

    neighbors = query.neighbors(creator)

    assert len(neighbors) == 1
    assert neighbors[0][0] == "creator_of"
    assert neighbors[0][1] == project


def test_relations_of():

    graph = KnowledgeGraph()

    creator = EntityNode(
        name="BitPredator",
        entity_type="creator",
    )

    project = EntityNode(
        name="BitGenesis",
        entity_type="project",
    )

    graph.add_relation(
        creator,
        "creator_of",
        project,
    )

    query = KnowledgeQuery(graph)

    relations = query.relations_of("BitPredator")

    assert len(relations) == 1
    assert relations[0][0] == "creator_of"
    assert relations[0][1] == project


def test_relations_of_unknown_node():

    graph = KnowledgeGraph()

    query = KnowledgeQuery(graph)

    assert query.relations_of("Unknown") == []