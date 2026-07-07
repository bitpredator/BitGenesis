from bitgenesis.reasoning.reflection_engine import ReflectionEngine


class FakeRules:

    def apply(self, facts):

        return ["reflection"]


def test_engine_uses_rules():

    engine = ReflectionEngine(
        rules=FakeRules(),
    )

    reflections = engine.reflect(
        ["fact"]
    )

    assert reflections == ["reflection"]


def test_engine_returns_empty_for_empty_input():

    engine = ReflectionEngine()

    reflections = engine.reflect([])

    assert reflections == []


def test_engine_returns_list():

    engine = ReflectionEngine(
        rules=FakeRules(),
    )

    reflections = engine.reflect(
        ["anything"]
    )

    assert isinstance(reflections, list)