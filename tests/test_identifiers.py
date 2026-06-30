from bitgenesis.core.identifiers import generate_id


def test_generate_id():
    assert generate_id() is not None