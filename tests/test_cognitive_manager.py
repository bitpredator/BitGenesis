from bitgenesis.cognition import CognitiveManager
from bitgenesis.cognition import CognitiveState


def test_manager_initial_state():

    manager = CognitiveManager()

    assert manager.state == CognitiveState.IDLE

    assert manager.cycles == 0

    assert manager.last_context is None


def test_manager_execute():

    manager = CognitiveManager()

    context = manager.execute("hello")

    assert context.input_data == "hello"

    assert manager.cycles == 1

    assert manager.last_context == context


def test_manager_multiple_cycles():

    manager = CognitiveManager()

    manager.execute("one")

    manager.execute("two")

    manager.execute("three")

    assert manager.cycles == 3