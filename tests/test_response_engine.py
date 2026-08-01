from bitgenesis.dialogue.response_engine import ResponseEngine



def test_response_engine_returns_creator():

    engine = ResponseEngine()


    response = engine.respond(
        "Who created you?"
    )


    assert response is not None

    assert (
        "Bitpredator"
        in response.content
    )



def test_response_engine_returns_name():

    engine = ResponseEngine()


    response = engine.respond(
        "Who are you?"
    )


    assert response is not None

    assert (
        "BitGenesis"
        in response.content
    )



def test_response_engine_returns_project():

    engine = ResponseEngine()


    response = engine.respond(
        "What is your project?"
    )


    assert response is not None

    assert (
        "BitGenesis"
        in response.content
    )



def test_response_engine_returns_unknown_question():

    engine = ResponseEngine()


    response = engine.respond(
        "What is the weather today?"
    )


    assert response is not None


    assert (
        "future learning process"
        in response.content
    )



def test_response_engine_returns_none_for_empty_question():

    engine = ResponseEngine()


    response = engine.respond(
        ""
    )


    assert response is None