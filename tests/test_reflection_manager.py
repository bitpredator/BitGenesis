from bitgenesis.reasoning.reflection_manager import ReflectionManager


class FakeRegistry:

    def __init__(self, facts=None):

        self._facts = list(facts or [])

    def all(self):

        return list(self._facts)

    def add(self, fact):

        self._facts.append(fact)


class FakeEngine:

    def __init__(self, reflections):

        self.reflections = reflections
        self.called = False

    def reflect(self, facts):

        self.called = True

        return list(self.reflections)


def test_process_empty_registry():

    registry = FakeRegistry()

    engine = FakeEngine([])

    manager = ReflectionManager(
        registry=registry,
        engine=engine,
    )

    result = manager.process()

    assert result == []
    assert engine.called is False


def test_process_uses_engine():

    registry = FakeRegistry([
        "Python"
    ])

    engine = FakeEngine([
        "Programming Languages"
    ])

    manager = ReflectionManager(
        registry=registry,
        engine=engine,
    )

    manager.process()

    assert engine.called is True


def test_process_adds_reflections():

    registry = FakeRegistry([
        "Python"
    ])

    engine = FakeEngine([
        "Programming Languages"
    ])

    manager = ReflectionManager(
        registry=registry,
        engine=engine,
    )

    manager.process()

    assert len(registry.all()) == 2
    assert "Programming Languages" in registry.all()


def test_process_returns_new_reflections():

    registry = FakeRegistry([
        "Python"
    ])

    engine = FakeEngine([
        "Programming Languages"
    ])

    manager = ReflectionManager(
        registry=registry,
        engine=engine,
    )

    result = manager.process()

    assert result == [
        "Programming Languages"
    ]


def test_process_does_not_duplicate_reflections():

    registry = FakeRegistry([
        "Python",
        "Programming Languages",
    ])

    engine = FakeEngine([
        "Programming Languages",
    ])

    manager = ReflectionManager(
        registry=registry,
        engine=engine,
    )

    result = manager.process()

    assert result == []
    assert registry.all().count(
        "Programming Languages"
    ) == 1