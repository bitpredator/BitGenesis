from bitgenesis.dialogue.formatter import ResponseFormatter
from bitgenesis.reasoning.intent_detector import Intent


def test_formatter_creator():

    formatter = ResponseFormatter()

    intent = Intent(
        domain="identity",
        action="query",
        target="creator",
    )

    response = formatter.format(intent, "Bitpredator")

    assert response == "My creator is Bitpredator."


def test_formatter_name():

    formatter = ResponseFormatter()

    intent = Intent(
        domain="identity",
        action="query",
        target="name",
    )

    response = formatter.format(intent, "BitGenesis")

    assert response == "I am BitGenesis."


def test_formatter_project():

    formatter = ResponseFormatter()

    intent = Intent(
        domain="identity",
        action="query",
        target="project",
    )

    response = formatter.format(intent, "BitGenesis")

    assert response == "My project is BitGenesis."


def test_formatter_version():

    formatter = ResponseFormatter()

    intent = Intent(
        domain="identity",
        action="query",
        target="version",
    )

    response = formatter.format(intent, "0.1.0")

    assert response == "I am currently running version 0.1.0."


def test_formatter_description():

    formatter = ResponseFormatter()

    intent = Intent(
        domain="identity",
        action="query",
        target="description",
    )

    response = formatter.format(
        intent,
        "A modular cognitive AI framework."
    )

    assert response == "A modular cognitive AI framework."


def test_formatter_unknown_identity_target():

    formatter = ResponseFormatter()

    intent = Intent(
        domain="identity",
        action="query",
        target="unknown",
    )

    response = formatter.format(intent, "value")

    assert response == "value"


def test_formatter_unknown_domain():

    formatter = ResponseFormatter()

    intent = Intent(
        domain="memory",
        action="query",
        target="anything",
    )

    response = formatter.format(intent, "memory value")

    assert response == "memory value"


def test_formatter_none_value():

    formatter = ResponseFormatter()

    intent = Intent(
        domain="identity",
        action="query",
        target="creator",
    )

    response = formatter.format(intent, None)

    assert response == "I don't know."


def test_formatter_none_intent():

    formatter = ResponseFormatter()

    assert formatter.format(None, "anything") is None