from bitgenesis.reasoning.intent_detector import Intent
from bitgenesis.reasoning.resolver import Resolver



def test_resolver_returns_identity():

    resolver = Resolver()

    intent = Intent(
        domain="identity",
        action="query",
        target="name",
    )


    result = resolver.resolve(
        intent
    )


    assert result is not None

    assert result.domain == "identity"



def test_resolver_returns_unknown_response():

    resolver = Resolver()


    intent = Intent(
        domain="unknown",
        action="unknown",
        target="something",
        confidence=0.0,
    )


    result = resolver.resolve(
        intent
    )


    assert result is not None

    assert result.domain == "unknown"

    assert (
        "future learning process"
        in result.value
    )



def test_resolver_returns_none_for_none_intent():

    resolver = Resolver()


    assert resolver.resolve(
        None
    ) is None