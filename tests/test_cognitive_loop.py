from bitgenesis.cognition import CognitiveContext
from bitgenesis.cognition import CognitiveLoop
from bitgenesis.cognition import CognitiveState


def test_loop_execution():

    loop = CognitiveLoop()

    context = CognitiveContext()

    result = loop.execute(context)

    assert result.state == CognitiveState.COMPLETED