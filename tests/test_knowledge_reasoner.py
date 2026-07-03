from bitgenesis.knowledge.entity_node import EntityNode
from bitgenesis.knowledge.graph import KnowledgeGraph
from bitgenesis.reasoning.knowledge_reasoner import KnowledgeReasoner


def build_graph():

    graph = KnowledgeGraph()

    creator = EntityNode(
        name="BitPredator",
        entity_type="creator",
    )

    project = EntityNode(
        name="BitGenesis",
        entity_type="project",
    )

    language = EntityNode(
        name="Python",
        entity_type="language",
    )

    graph.add_relation(
        creator,
        "creator_of",
        project,
    )

    graph.add_relation(
        project,
        "written_in",
        language,
    )

    return graph


def test_has_knowledge_true():

    reasoner = KnowledgeReasoner(build_graph())

    assert reasoner.has_knowledge("BitGenesis")


def test_has_knowledge_false():

    reasoner = KnowledgeReasoner(build_graph())

    assert not reasoner.has_knowledge("Unknown")


def test_answer_unknown():

    reasoner = KnowledgeReasoner(build_graph())

    assert reasoner.answer("Unknown") is None


def test_creator_answer():

    reasoner = KnowledgeReasoner(build_graph())

    answer = reasoner.answer("BitPredator")

    assert len(answer) == 1
    assert answer[0]["relation"] == "creator_of"
    assert answer[0]["target"] == "BitGenesis"


def test_project_answer():

    reasoner = KnowledgeReasoner(build_graph())

    answer = reasoner.answer("BitGenesis")

    assert len(answer) == 2

    relations = {item["relation"] for item in answer}

    assert "creator_of" in relations
    assert "written_in" in relations


def test_language_answer():

    reasoner = KnowledgeReasoner(build_graph())

    answer = reasoner.answer("Python")

    assert len(answer) == 1
    assert answer[0]["relation"] == "written_in"
    assert answer[0]["target"] == "BitGenesis"