from bitgenesis.reasoning.intent_detector import IntentDetector
from bitgenesis.reasoning.resolver import Resolver


def test_resolver_returns_creator():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("Who created you?")

    resolution = resolver.resolve(intent)

    assert resolution.domain == "identity"
    assert resolution.target == "creator"
    assert resolution.value == "Bitpredator"
    assert resolution.success is True


def test_resolver_returns_name():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your name?")

    resolution = resolver.resolve(intent)

    assert resolution.value == "BitGenesis"


def test_resolver_returns_project():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your project?")

    resolution = resolver.resolve(intent)

    assert resolution.value == "BitGenesis"


def test_resolver_returns_version():

    detector = IntentDetector()
    resolver = Resolver()

    intent = detector.detect("What is your version?")

    resolution = resolver.resolve(intent)

    assert resolution.value == "0.1.0"


def test_resolver_returns_none_for_unknown_domain():

    class FakeIntent:
        domain = "unknown"
        target = "anything"

    resolver = Resolver()

    resolution = resolver.resolve(FakeIntent())

    assert resolution is None


def test_resolver_returns_none_for_none_intent():

    resolver = Resolver()

    assert resolver.resolve(None) is None