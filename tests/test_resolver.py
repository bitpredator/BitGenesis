from bitgenesis.reasoning.intent_detector import IntentDetector
from bitgenesis.reasoning.resolver import Resolver


def test_resolver_returns_creator():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("Who created you?")

    result = resolver.resolve(intent)

    assert result == "Bitpredator"


def test_resolver_returns_name():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your name?")

    result = resolver.resolve(intent)

    assert result == "BitGenesis"


def test_resolver_returns_project():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your project?")

    result = resolver.resolve(intent)

    assert result == "BitGenesis"


def test_resolver_returns_version():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your version?")

    result = resolver.resolve(intent)

    assert result == "0.1.0"


def test_resolver_returns_none_for_unknown_domain():

    class FakeIntent:

        domain = "unknown"
        target = "anything"

    resolver = Resolver()

    assert resolver.resolve(FakeIntent()) is None


def test_resolver_returns_none_for_none_intent():

    resolver = Resolver()

    assert resolver.resolve(None) is None