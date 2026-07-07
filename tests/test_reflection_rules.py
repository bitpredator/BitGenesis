from bitgenesis.reasoning.reflection_rules import ReflectionRules


def test_empty_input_returns_empty_list():

    rules = ReflectionRules()

    reflections = rules.apply([])

    assert reflections == []


def test_detect_programming_languages():

    rules = ReflectionRules()

    facts = [
        "User likes Python",
        "User likes Rust",
        "User likes C++",
    ]

    reflections = rules.apply(facts)

    assert len(reflections) == 1
    assert reflections[0] == (
        "The user enjoys programming languages."
    )


def test_detect_planner():

    rules = ReflectionRules()

    facts = [
        "Planner initialized",
        "Planner executed",
    ]

    reflections = rules.apply(facts)

    assert len(reflections) == 1
    assert reflections[0] == (
        "Planner subsystem is operational."
    )


def test_detect_memory():

    rules = ReflectionRules()

    facts = [
        "Memory stored",
        "Memory queried",
    ]

    reflections = rules.apply(facts)

    assert len(reflections) == 1
    assert reflections[0] == (
        "Memory subsystem is functioning correctly."
    )


def test_multiple_reflections():

    rules = ReflectionRules()

    facts = [
        "Python",
        "Rust",
        "C++",
        "Planner initialized",
        "Memory stored",
    ]

    reflections = rules.apply(facts)

    assert len(reflections) == 3