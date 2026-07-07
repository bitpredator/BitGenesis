from bitgenesis.cognition.state import CognitiveState


def test_cognitive_state_values():

    assert CognitiveState.IDLE.value == "idle"

    assert CognitiveState.REASONING.value == "reasoning"

    assert CognitiveState.COMPLETED.value == "completed"