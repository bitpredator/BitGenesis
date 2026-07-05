from bitgenesis.dialogue.formatter import ResponseFormatter
from bitgenesis.reasoning.intent_detector import Intent
from bitgenesis.reasoning.resolution import Resolution


def test_formatter_creator():

    formatter = ResponseFormatter()

    intent = Intent(domain="identity", action="query", target="creator")

    resolution = Resolution(
        domain="identity",
        target="creator",
        value="Bitpredator",
    )

    response = formatter.format(resolution)

    assert response == "My creator is Bitpredator."


def test_formatter_name():

    formatter = ResponseFormatter()

    resolution = Resolution(
        domain="identity",
        target="name",
        value="BitGenesis",
    )

    response = formatter.format(resolution)

    assert response == "I am BitGenesis."


def test_formatter_project():

    formatter = ResponseFormatter()

    resolution = Resolution(
        domain="identity",
        target="project",
        value="BitGenesis",
    )

    response = formatter.format(resolution)

    assert response == "My project is BitGenesis."


def test_formatter_version():

    formatter = ResponseFormatter()

    resolution = Resolution(
        domain="identity",
        target="version",
        value="0.1.0",
    )

    response = formatter.format(resolution)

    assert response == "I am currently running version 0.1.0."


def test_formatter_description():

    formatter = ResponseFormatter()

    resolution = Resolution(
        domain="identity",
        target="description",
        value="A modular cognitive AI framework.",
    )

    response = formatter.format(resolution)

    assert response == "A modular cognitive AI framework."


def test_formatter_unknown_identity_target():

    formatter = ResponseFormatter()

    resolution = Resolution(
        domain="identity",
        target="unknown",
        value="value",
    )

    response = formatter.format(resolution)

    assert response == "value"


def test_formatter_unknown_domain():

    formatter = ResponseFormatter()

    resolution = Resolution(
        domain="memory",
        target="anything",
        value="memory value",
    )

    response = formatter.format(resolution)

    assert response == "memory value"


def test_formatter_none_value():

    formatter = ResponseFormatter()

    resolution = Resolution(
        domain="identity",
        target="creator",
        value=None,
    )

    response = formatter.format(resolution)

    assert response == "I don't know."


def test_formatter_none_resolution():

    formatter = ResponseFormatter()

    assert formatter.format(None) is None