from bitgenesis.core.brain import Brain


def test_unknown_question_returns_cognitive_response():

    brain = Brain()

    response = brain.ask(
        "Tell me something about quantum engines"
    )

    assert response is not None

    assert (
        "future learning process"
        in response.content
    )