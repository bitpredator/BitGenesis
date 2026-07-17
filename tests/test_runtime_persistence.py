from __future__ import annotations

import pytest

from bitgenesis.cognition.cognitive_runtime import CognitiveRuntime
from bitgenesis.cognition.state import CognitiveState
from bitgenesis.runtime.runtime_status import RuntimeState


# --------------------------------------------------
# Helpers
# --------------------------------------------------

class DummyStage:

    def __init__(self):
        self.executed = False


    def execute(self, context):

        self.executed = True

        return context



# --------------------------------------------------
# Initial state
# --------------------------------------------------

def test_runtime_initial_state():

    runtime = CognitiveRuntime()

    assert runtime.state == CognitiveState.IDLE

    assert runtime.cycle_count == 0

    assert runtime.last_context is None



# --------------------------------------------------
# Cycle persistence
# --------------------------------------------------

def test_runtime_cycle_counter_persistence():

    runtime = CognitiveRuntime()


    runtime.run()

    runtime.run()

    runtime.run()


    assert runtime.cycle_count == 3



# --------------------------------------------------
# Last context persistence
# --------------------------------------------------

def test_runtime_last_context_persistence():

    runtime = CognitiveRuntime()


    context = runtime.run(
        input_data="hello"
    )


    assert runtime.last_context is context

    assert context.input_data == "hello"



# --------------------------------------------------
# Reset statistics
# --------------------------------------------------

def test_runtime_reset_statistics():

    runtime = CognitiveRuntime()


    runtime.run()


    assert runtime.cycle_count == 1


    runtime.reset_statistics()


    assert runtime.cycle_count == 0

    assert runtime.last_context is None



# --------------------------------------------------
# Runtime returns to idle
# --------------------------------------------------

def test_runtime_returns_idle_after_execution():

    runtime = CognitiveRuntime()


    runtime.run()


    assert runtime.state == CognitiveState.IDLE



# --------------------------------------------------
# Runtime failure persistence
# --------------------------------------------------

def test_runtime_failure_persists_context():

    class BrokenLoop:


        def execute(self, context):

            raise RuntimeError(
                "runtime failure"
            )


    runtime = CognitiveRuntime()

    runtime._loop = BrokenLoop()


    with pytest.raises(RuntimeError):

        runtime.run(
            input_data="failure"
        )


    assert runtime.last_context is not None

    assert runtime.last_context.state == CognitiveState.FAILED



# --------------------------------------------------
# Multiple runtime instances isolation
# --------------------------------------------------

def test_runtime_instances_are_isolated():

    runtime_a = CognitiveRuntime()

    runtime_b = CognitiveRuntime()


    runtime_a.run()


    assert runtime_a.cycle_count == 1

    assert runtime_b.cycle_count == 0



# --------------------------------------------------
# Runtime state enum availability
# --------------------------------------------------

def test_runtime_state_exists():

    assert RuntimeState is not None

    assert hasattr(
        RuntimeState,
        "IDLE"
    )