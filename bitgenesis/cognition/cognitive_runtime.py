from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.loop import CognitiveLoop
from bitgenesis.cognition.state import CognitiveState


class CognitiveRuntime:
    """
    Coordinates the execution of a single cognitive cycle.

    The runtime is responsible for creating the execution context,
    injecting shared subsystem references and executing the cognitive
    pipeline through the CognitiveLoop.

    Individual cognitive operations are delegated entirely to the
    pipeline stages.
    """

    def __init__(
        self,
        *,
        memory_store=None,
        memory_factory=None,
        knowledge_registry=None,
        inference_engine=None,
        reflection_engine=None,
        response_engine=None,
        planner=None,
        executor=None,
        event_bus=None,
    ):

        self.state = CognitiveState.IDLE

        # Shared cognitive subsystems

        self.memory_store = memory_store

        self.memory_factory = memory_factory

        self.knowledge_registry = knowledge_registry

        self.inference_engine = inference_engine

        self.reflection_engine = reflection_engine

        self.response_engine = response_engine

        self.planner = planner

        self.executor = executor

        self.event_bus = event_bus

        # Cognitive pipeline

        self._loop = CognitiveLoop()

    @property
    def is_running(self) -> bool:
        """
        Returns True while a cognitive cycle is executing.
        """

        return self.state != CognitiveState.IDLE

    @property
    def loop(self) -> CognitiveLoop:
        """
        Returns the cognitive execution loop.
        """

        return self._loop

    def run(self, input_data=None) -> CognitiveContext:
        """
        Executes one complete cognitive cycle.
        """

        self.state = CognitiveState.INITIALIZING

        context = CognitiveContext(
            state=CognitiveState.INITIALIZING,
            input_data=input_data,

            # Shared subsystem injection

            memory_store=self.memory_store,

            memory_factory=self.memory_factory,

            knowledge_registry=self.knowledge_registry,

            inference_engine=self.inference_engine,

            reflection_engine=self.reflection_engine,

            response_engine=self.response_engine,

            planner=self.planner,

            executor=self.executor,

            event_bus=self.event_bus,
        )

        try:

            return self._loop.execute(context)

        except Exception:

            context.update_state(
                CognitiveState.FAILED
            )

            raise

        finally:

            self.state = CognitiveState.IDLE