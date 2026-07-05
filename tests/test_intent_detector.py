from bitgenesis.reasoning.intent_detector import (
    Intent,
    IntentDetector,
)


def test_detect_creator_intent():

    detector = IntentDetector()

    intent = detector.detect("Who created you?")

    assert isinstance(intent, Intent)
    assert intent.domain == "identity"
    assert intent.action == "query"
    assert intent.target == "creator"
    assert intent.confidence == 1.0


def test_detect_name_intent():

    detector = IntentDetector()

    intent = detector.detect("What is your name?")

    assert intent is not None
    assert intent.target == "name"


def test_detect_project_intent():

    detector = IntentDetector()

    intent = detector.detect("What is your project?")

    assert intent is not None
    assert intent.target == "project"


def test_detect_version_intent():

    detector = IntentDetector()

    intent = detector.detect("What is your version?")

    assert intent is not None
    assert intent.target == "version"


def test_detect_description_intent():

    detector = IntentDetector()

    intent = detector.detect("Describe yourself")

    assert intent is not None
    assert intent.target == "description"


def test_detect_is_case_insensitive():

    detector = IntentDetector()

    intent = detector.detect("WHO CREATED YOU?")

    assert intent is not None
    assert intent.target == "creator"


def test_detect_returns_none_for_unknown_input():

    detector = IntentDetector()

    intent = detector.detect("What is the weather today?")

    assert intent is None


def test_detect_returns_none_for_empty_string():

    detector = IntentDetector()

    assert detector.detect("") is None


def test_detect_returns_none_for_whitespace():

    detector = IntentDetector()

    assert detector.detect("     ") is None