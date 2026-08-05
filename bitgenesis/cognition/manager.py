from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.cognitive_runtime import CognitiveRuntime
from bitgenesis.cognition.state import CognitiveState



class CognitiveManager:
    """
    Creates and supervises cognitive execution cycles.

    The manager owns the runtime configuration but delegates
    all cognitive processing to the CognitiveRuntime.
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
        learning_engine=None,
        language_processor=None,
        planner=None,
        executor=None,
        event_bus=None,
    ):


        # --------------------------------------------------
        # Cognitive subsystems
        # --------------------------------------------------

        self.memory_store = memory_store

        self.memory_factory = memory_factory

        self.knowledge_registry = knowledge_registry

        self.inference_engine = inference_engine

        self.reflection_engine = reflection_engine

        self.response_engine = response_engine

        self.learning_engine = learning_engine


        # --------------------------------------------------
        # Language subsystem
        # --------------------------------------------------

        self.language_processor = language_processor



        # --------------------------------------------------
        # Runtime services
        # --------------------------------------------------

        self.planner = planner

        self.executor = executor

        self.event_bus = event_bus



        # --------------------------------------------------
        # Runtime tracking
        # --------------------------------------------------

        self._runtime: CognitiveRuntime | None = None

        self._last_context: CognitiveContext | None = None

        self._cycles = 0



    # ======================================================
    # Properties
    # ======================================================

    @property
    def state(
        self,
    ) -> CognitiveState:


        if self._runtime is None:

            return CognitiveState.IDLE


        return self._runtime.state



    @property
    def last_context(
        self,
    ) -> CognitiveContext | None:


        return self._last_context



    @property
    def cycles(
        self,
    ) -> int:


        return self._cycles



    # ======================================================
    # Execution
    # ======================================================

    def execute(
        self,
        input_data=None,
    ) -> CognitiveContext:
        """
        Executes one cognitive cycle.
        """



        runtime = CognitiveRuntime(


            memory_store=self.memory_store,


            memory_factory=self.memory_factory,


            knowledge_registry=self.knowledge_registry,


            inference_engine=self.inference_engine,


            reflection_engine=self.reflection_engine,


            response_engine=self.response_engine,


            learning_engine=self.learning_engine,


            language_processor=self.language_processor,


            planner=self.planner,


            executor=self.executor,


            event_bus=self.event_bus,

        )



        self._runtime = runtime



        context = runtime.run(
            input_data
        )



        self._last_context = context



        self._cycles += 1



        return context