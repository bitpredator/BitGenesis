from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.loop import CognitiveLoop
from bitgenesis.cognition.state import CognitiveState


class CognitiveRuntime:
    """
    Coordinates the execution of a single cognitive cycle.

    The runtime is responsible for creating the execution context,
    invoking the cognitive loop, and managing the runtime state.

    Cognitive processing is delegated to pipeline stages.
    The runtime only coordinates execution flow and dependency injection.
    """

    def __init__(
        self,
        *,
        memory_store=None,
        knowledge_registry=None,
        inference_engine=None,
        reflection_engine=None,
    ):

        self.state = CognitiveState.IDLE

        # Cognitive subsystem references
        self.memory_store = memory_store

        self.knowledge_registry = knowledge_registry

        self.inference_engine = inference_engine

        self.reflection_engine = reflection_engine

        self._loop = CognitiveLoop()

    @property
    def is_running(self) -> bool:
        """
        Indicates whether a cognitive cycle is currently executing.
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
        Executes a complete cognitive cycle.

        Parameters
        ----------
        input_data:
            Initial input passed to the cognitive pipeline.

        Returns
        -------
        CognitiveContext
            The updated cognitive context produced by the pipeline.
        """

        context = CognitiveContext(
            state=CognitiveState.INITIALIZING,
            input_data=input_data,

            memory_store=self.memory_store,

            knowledge_registry=self.knowledge_registry,

            inference_engine=self.inference_engine,

            reflection_engine=self.reflection_engine,
        )

        self.state = CognitiveState.INITIALIZING

        try:

            context = self._loop.execute(context)

            return context

        except Exception:

            context.update_state(CognitiveState.FAILED)

            raise

        finally:

            self.state = CognitiveState.IDLE