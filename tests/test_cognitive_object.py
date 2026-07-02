from datetime import datetime

from bitgenesis.core.cognitive_object import CognitiveObject
from bitgenesis.core.entity import Entity


def test_cognitive_object_is_entity():
    cognitive_object = CognitiveObject()

    assert isinstance(cognitive_object, Entity)


def test_metadata_is_empty_by_default():
    cognitive_object = CognitiveObject()

    assert cognitive_object.metadata == {}


def test_tags_are_empty_by_default():
    cognitive_object = CognitiveObject()

    assert cognitive_object.tags == []


def test_default_importance():
    cognitive_object = CognitiveObject()

    assert cognitive_object.importance == 0.5


def test_default_confidence():
    cognitive_object = CognitiveObject()

    assert cognitive_object.confidence == 1.0


def test_add_tag():
    cognitive_object = CognitiveObject()

    cognitive_object.add_tag("memory")

    assert "memory" in cognitive_object.tags


def test_add_tag_avoids_duplicates():
    cognitive_object = CognitiveObject()

    cognitive_object.add_tag("memory")
    cognitive_object.add_tag("memory")

    assert cognitive_object.tags == ["memory"]


def test_remove_tag():
    cognitive_object = CognitiveObject()

    cognitive_object.add_tag("memory")
    cognitive_object.remove_tag("memory")

    assert cognitive_object.tags == []


def test_add_tag_updates_timestamp():
    cognitive_object = CognitiveObject()

    previous_timestamp = cognitive_object.updated_at

    cognitive_object.add_tag("memory")

    assert cognitive_object.updated_at > previous_timestamp


def test_remove_tag_updates_timestamp():
    cognitive_object = CognitiveObject()

    cognitive_object.add_tag("memory")

    previous_timestamp = cognitive_object.updated_at

    cognitive_object.remove_tag("memory")

    assert cognitive_object.updated_at > previous_timestamp