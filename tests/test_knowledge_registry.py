from bitgenesis.knowledge.registry import KnowledgeRegistry


def test_create_entity():

    registry = KnowledgeRegistry()

    entity = registry.get_or_create("BitGenesis")

    assert entity.name == "BitGenesis"


def test_same_entity_is_reused():

    registry = KnowledgeRegistry()

    first = registry.get_or_create("BitPredator")
    second = registry.get_or_create("BitPredator")

    assert first is second


def test_case_is_ignored():

    registry = KnowledgeRegistry()

    a = registry.get_or_create("Python")
    b = registry.get_or_create("python")
    c = registry.get_or_create("PYTHON")

    assert a is b
    assert b is c


def test_exists():

    registry = KnowledgeRegistry()

    registry.get_or_create("BitGenesis")

    assert registry.exists("BitGenesis")
    assert registry.exists("bitgenesis")


def test_count():

    registry = KnowledgeRegistry()

    registry.get_or_create("A")
    registry.get_or_create("B")
    registry.get_or_create("A")

    assert registry.count() == 2


def test_all():

    registry = KnowledgeRegistry()

    registry.get_or_create("One")
    registry.get_or_create("Two")

    assert len(registry.all()) == 2


def test_clear():

    registry = KnowledgeRegistry()

    registry.get_or_create("Entity")

    registry.clear()

    assert registry.count() == 0


def test_get_returns_none():

    registry = KnowledgeRegistry()

    assert registry.get("Unknown") is None