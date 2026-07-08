from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.cognitive_runtime import CognitiveRuntime
from bitgenesis.cognition.state import CognitiveState


class CognitiveManager:
    """
    Manages cognitive runtime instances.

    The manager coordinates runtime creation and provides
    shared cognitive subsystem dependencies.
    """

    def __init__(
        self,
        *,
        memory_store=None,
        knowledge_registry=None,
        inference_engine=None,
        reflection_engine=None,
        response_engine=None,
        planner=None,
        event_bus=None,
    ):

        self.memory_store = memory_store

        self.knowledge_registry = knowledge_registry

        self.inference_engine = inference_engine

        self.reflection_engine = reflection_engine

        self.response_engine = response_engine

        self.planner = planner

        self.event_bus = event_bus

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

        runtime = CognitiveRuntime(
            memory_store=self.memory_store,
            knowledge_registry=self.knowledge_registry,
            inference_engine=self.inference_engine,
            reflection_engine=self.reflection_engine,
            response_engine=self.response_engine,
            planner=self.planner,
            event_bus=self.event_bus,
        )

        self._runtime = runtime

        context = runtime.run(input_data)

        self._last_context = context

        self._cycles += 1

        return context