from bitgenesis.memory.memory_similarity import MemorySimilarity


def test_returns_zero_for_non_dict_payload():
    assert MemorySimilarity.score(None, {}) == 0.0
    assert MemorySimilarity.score({}, None) == 0.0
    assert MemorySimilarity.score([], {}) == 0.0
    assert MemorySimilarity.score({}, []) == 0.0


def test_returns_zero_for_empty_payloads():
    assert MemorySimilarity.score({}, {}) == 0.0


def test_scores_matching_key_only():
    payload1 = {
        "creator": "BitPredator",
    }

    payload2 = {
        "creator": "SomeoneElse",
    }

    assert MemorySimilarity.score(payload1, payload2) == 1.0


def test_scores_matching_key_and_value():
    payload1 = {
        "creator": "BitPredator",
    }

    payload2 = {
        "creator": "BitPredator",
    }

    assert MemorySimilarity.score(payload1, payload2) == 3.0


def test_scores_multiple_matching_fields():
    payload1 = {
        "creator": "BitPredator",
        "language": "Python",
    }

    payload2 = {
        "creator": "BitPredator",
        "language": "Rust",
    }

    # creator -> +3
    # language -> +1
    assert MemorySimilarity.score(payload1, payload2) == 4.0


def test_ignores_non_matching_keys():
    payload1 = {
        "creator": "BitPredator",
    }

    payload2 = {
        "version": "0.1",
    }

    assert MemorySimilarity.score(payload1, payload2) == 0.0