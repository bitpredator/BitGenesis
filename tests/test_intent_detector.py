from bitgenesis.reasoning.intent_detector import IntentDetector


def test_detect_identity_name():

    detector = IntentDetector()

    intent = detector.detect(
        "Who are you?"
    )

    assert intent is not None

    assert intent.domain == "identity"

    assert intent.target == "name"



def test_detect_creator():

    detector = IntentDetector()

    intent = detector.detect(
        "Who created you?"
    )

    assert intent.domain == "identity"

    assert intent.target == "creator"



def test_detect_memory_query():

    detector = IntentDetector()

    intent = detector.detect(
        "What do you remember?"
    )

    assert intent is not None

    assert intent.domain == "memory"



def test_detect_returns_unknown_for_unknown_input():

    detector = IntentDetector()

    intent = detector.detect(
        "What is the weather today?"
    )

    assert intent is not None

    assert intent.domain == "unknown"

    assert intent.confidence == 0.0



def test_detect_returns_none_for_empty_string():

    detector = IntentDetector()

    assert detector.detect(
        ""
    ) is None



def test_detect_returns_none_for_whitespace():

    detector = IntentDetector()

    assert detector.detect(
        "   "
    ) is None