from bitgenesis.core.brain import Brain
from bitgenesis.cognition import CognitiveContext
from bitgenesis.core.lifecycle import BrainState
from bitgenesis.cognition.state import CognitiveState


def test_brain_think_returns_context():

    brain = Brain()

    context = brain.think(
        "hello"
    )

    assert isinstance(
        context,
        CognitiveContext
    )


def test_brain_think_updates_context():

    brain = Brain()

    context = brain.think(
        "hello"
    )

    assert context.input_data == "hello"

    assert context.state == CognitiveState.COMPLETED


def test_brain_exposes_last_cognitive_context():

    brain = Brain()

    brain.think(
        "memory test"
    )

    assert brain.cognitive_context is not None

    assert brain.cognitive_context.input_data == "memory test"


def test_brain_returns_to_idle_after_thinking():

    brain = Brain()

    brain.think(
        "cycle"
    )

    assert brain.state == BrainState.IDLE