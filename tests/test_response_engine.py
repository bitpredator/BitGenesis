from bitgenesis.dialogue.response_engine import ResponseEngine


def test_response_engine_returns_creator():

    engine = ResponseEngine()

    response = engine.respond("Who created you?")

    assert response == "My creator is Bitpredator."


def test_response_engine_returns_name():

    engine = ResponseEngine()

    response = engine.respond("What is your name?")

    assert response == "I am BitGenesis."


def test_response_engine_returns_project():

    engine = ResponseEngine()

    response = engine.respond("What is your project?")

    assert response == "My project is BitGenesis."


def test_response_engine_returns_version():

    engine = ResponseEngine()

    response = engine.respond("What is your version?")

    assert response == "I am currently running version 0.1.0."


def test_response_engine_returns_description():

    engine = ResponseEngine()

    response = engine.respond("Describe yourself")

    assert response is not None
    assert "modular cognitive ai framework" in response.lower()


def test_response_engine_returns_none_for_unknown_question():

    engine = ResponseEngine()

    response = engine.respond("How is the weather today?")

    assert response is None


def test_response_engine_returns_none_for_empty_question():

    engine = ResponseEngine()

    response = engine.respond("")

    assert response is None