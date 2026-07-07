from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState


def test_cognitive_context_creation():

    context = CognitiveContext()

    assert context.state == CognitiveState.IDLE

    assert context.memories == []

    assert context.knowledge == []

    assert context.actions == []


def test_cognitive_context_state_update():

    context = CognitiveContext()

    context.update_state(CognitiveState.REASONING)

    assert context.state == CognitiveState.REASONING


def test_cognitive_context_add_data():

    context = CognitiveContext()

    context.add_memory("memory")

    context.add_knowledge("knowledge")

    context.add_action("action")

    assert context.memories == ["memory"]

    assert context.knowledge == ["knowledge"]

    assert context.actions == ["action"]