from bitgenesis.knowledge.entity_node import EntityNode
from bitgenesis.knowledge.knowledge_graph import KnowledgeGraph
from bitgenesis.knowledge.relation import Relation


def test_add_node():
    graph = KnowledgeGraph()

    node = EntityNode(name="BitGenesis")

    graph.add_node(node)

    assert graph.get_node(node.id) == node


def test_all_nodes():
    graph = KnowledgeGraph()

    graph.add_node(EntityNode(name="A"))
    graph.add_node(EntityNode(name="B"))

    assert len(graph.all_nodes()) == 2


def test_add_relation():
    graph = KnowledgeGraph()

    a = graph.add_node(EntityNode(name="A"))
    b = graph.add_node(EntityNode(name="B"))

    relation = Relation(
        source=a.id,
        target=b.id,
        relation_type="connected_to",
    )

    graph.add_relation(relation)

    assert len(graph.all_relations()) == 1


def test_neighbors_returns_connected_nodes():
    graph = KnowledgeGraph()

    a = graph.add_node(EntityNode(name="A"))
    b = graph.add_node(EntityNode(name="B"))

    graph.add_relation(
        Relation(
            source=a.id,
            target=b.id,
            relation_type="linked",
        )
    )

    neighbors = graph.neighbors(a.id)

    assert len(neighbors) == 1
    assert neighbors[0].name == "B"


def test_neighbors_empty_when_no_relations():
    graph = KnowledgeGraph()

    node = graph.add_node(EntityNode(name="Solo"))

    assert graph.neighbors(node.id) == []


def test_unknown_node_returns_none():
    graph = KnowledgeGraph()

    node = EntityNode()

    assert graph.get_node(node.id) is None


def test_all_relations_initially_empty():
    graph = KnowledgeGraph()

    assert graph.all_relations() == []