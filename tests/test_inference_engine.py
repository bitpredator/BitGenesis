from bitgenesis.knowledge.inference_engine import InferenceEngine


def test_empty_input_returns_empty_list():

    engine = InferenceEngine()

    inferred = engine.infer([])

    assert inferred == []


def test_none_input_returns_empty_list():

    engine = InferenceEngine()

    inferred = engine.infer(None)

    assert inferred == []


def test_is_a_and_likes_generates_new_fact():

    engine = InferenceEngine()

    facts = [
        "Python is_a ProgrammingLanguage",
        "User likes Python",
    ]

    inferred = engine.infer(facts)

    assert inferred == [
        "User likes ProgrammingLanguage"
    ]


def test_multiple_likes():

    engine = InferenceEngine()

    facts = [
        "Python is_a ProgrammingLanguage",
        "Alice likes Python",
        "Bob likes Python",
    ]

    inferred = engine.infer(facts)

    assert len(inferred) == 2

    assert "Alice likes ProgrammingLanguage" in inferred
    assert "Bob likes ProgrammingLanguage" in inferred


def test_multiple_is_a_relations():

    engine = InferenceEngine()

    facts = [
        "Python is_a ProgrammingLanguage",
        "Rust is_a ProgrammingLanguage",
        "User likes Python",
        "User likes Rust",
    ]

    inferred = engine.infer(facts)

    assert len(inferred) == 1

    assert inferred[0] == (
        "User likes ProgrammingLanguage"
    )


def test_existing_fact_is_not_duplicated():

    engine = InferenceEngine()

    facts = [
        "Python is_a ProgrammingLanguage",
        "User likes Python",
        "User likes ProgrammingLanguage",
    ]

    inferred = engine.infer(facts)

    assert inferred == []


def test_invalid_fact_is_ignored():

    engine = InferenceEngine()

    facts = [
        "Python",
        "Something invalid",
        "User likes Python",
    ]

    inferred = engine.infer(facts)

    assert inferred == []


def test_duplicate_input_does_not_duplicate_output():

    engine = InferenceEngine()

    facts = [
        "Python is_a ProgrammingLanguage",
        "Python is_a ProgrammingLanguage",
        "User likes Python",
        "User likes Python",
    ]

    inferred = engine.infer(facts)

    assert inferred == [
        "User likes ProgrammingLanguage"
    ]


def test_unrelated_facts_produce_no_inference():

    engine = InferenceEngine()

    facts = [
        "Car is_a Vehicle",
        "User likes Pizza",
    ]

    inferred = engine.infer(facts)

    assert inferred == []