from datetime import UTC, datetime

from bitgenesis.core.entity import Entity


def test_entity_generates_unique_identifier():
    entity1 = Entity()
    entity2 = Entity()

    assert entity1.id != entity2.id


def test_entity_has_creation_timestamp():
    entity = Entity()

    assert isinstance(entity.created_at, datetime)
    assert entity.created_at.tzinfo == UTC


def test_entity_has_update_timestamp():
    entity = Entity()

    assert isinstance(entity.updated_at, datetime)
    assert entity.updated_at.tzinfo == UTC


def test_touch_updates_timestamp():
    entity = Entity()

    previous_timestamp = entity.updated_at

    entity.touch()

    assert entity.updated_at > previous_timestamp