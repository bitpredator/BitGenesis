from uuid import uuid4

from bitgenesis.knowledge.relation import Relation


def test_relation_has_id():
    relation = Relation()

    assert relation.id is not None


def test_relation_stores_source_target():
    source = uuid4()
    target = uuid4()

    relation = Relation(
        source=source,
        target=target,
    )

    assert relation.source == source
    assert relation.target == target


def test_relation_type_is_stored():
    relation = Relation(
        relation_type="creator_of",
    )

    assert relation.relation_type == "creator_of"