from bitgenesis.knowledge.entity_node import EntityNode


def test_node_has_id():
    node = EntityNode()

    assert node.id is not None


def test_node_name_is_stored():
    node = EntityNode(name="BitGenesis")

    assert node.name == "BitGenesis"


def test_node_attributes_are_stored():
    node = EntityNode(
        name="BitGenesis",
        attributes={"creator": "BitPredator"},
    )

    assert node.attributes["creator"] == "BitPredator"