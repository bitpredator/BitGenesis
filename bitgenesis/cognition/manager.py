from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.cognitive_runtime import CognitiveRuntime
from bitgenesis.cognition.state import CognitiveState


class CognitiveManager:
    """
    Manages cognitive runtime instances.

    The manager is responsible for creating and supervising
    cognitive execution cycles without implementing cognitive logic.
    """

    def __init__(self):

        self._runtime: CognitiveRuntime | None = None

        self._last_context: CognitiveContext | None = None

        self._cycles = 0

    @property
    def state(self) -> CognitiveState:

        if self._runtime is None:

            return CognitiveState.IDLE

        return self._runtime.state

    @property
    def last_context(self) -> CognitiveContext | None:

        return self._last_context

    @property
    def cycles(self) -> int:

        return self._cycles

    def execute(self, input_data=None) -> CognitiveContext:
        """
        Executes a new cognitive cycle.
        """

        runtime = CognitiveRuntime()

        self._runtime = runtime

        context = runtime.run(input_data)

        self._last_context = context

        self._cycles += 1

        return context