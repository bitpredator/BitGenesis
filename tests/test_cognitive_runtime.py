from bitgenesis.cognition import CognitiveRuntime
from bitgenesis.cognition import CognitiveState


def test_runtime_initial_state():

    runtime = CognitiveRuntime()

    assert runtime.state == CognitiveState.IDLE

    assert runtime.is_running is False


def test_runtime_execution():

    runtime = CognitiveRuntime()

    context = runtime.run("hello")

    assert context.input_data == "hello"

    assert context.state == CognitiveState.COMPLETED

    assert runtime.state == CognitiveState.IDLE


def test_runtime_multiple_runs():

    runtime = CognitiveRuntime()

    runtime.run("one")

    runtime.run("two")

    assert runtime.state == CognitiveState.IDLE