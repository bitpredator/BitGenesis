from __future__ import annotations

from datetime import datetime

from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.loop import CognitiveLoop
from bitgenesis.cognition.state import CognitiveState

from bitgenesis.runtime.runtime_status import RuntimeState


class CognitiveRuntime:
    """
    Coordinates the execution of the BitGenesis cognitive pipeline.

    Runtime responsibilities:

    - create cognitive contexts
    - inject cognitive subsystems
    - execute cognitive cycles
    - track execution state
    - persist runtime metadata

    Designed for future:
    - continuous execution
    - scheduling
    - pause/resume
    - external stimuli
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

        # --------------------------------------------------
        # Runtime state
        # --------------------------------------------------

        self.state = CognitiveState.IDLE

        self.runtime_state = RuntimeState()

        # --------------------------------------------------
        # Runtime statistics
        # --------------------------------------------------

        self._cycle_counter = 0
        self._last_context = None


        # --------------------------------------------------
        # Cognitive subsystems
        # --------------------------------------------------

        self.memory_store = memory_store
        self.memory_factory = memory_factory

        self.knowledge_registry = knowledge_registry
        self.inference_engine = inference_engine

        self.reflection_engine = reflection_engine
        self.response_engine = response_engine

        self.planner = planner
        self.executor = executor

        self.event_bus = event_bus


        # --------------------------------------------------
        # Pipeline
        # --------------------------------------------------

        self._loop = CognitiveLoop()


    # ======================================================
    # Properties
    # ======================================================

    @property
    def loop(self) -> CognitiveLoop:
        return self._loop


    @property
    def is_running(self) -> bool:
        return self.state != CognitiveState.IDLE


    @property
    def cycle_count(self) -> int:
        return self._cycle_counter


    @property
    def last_context(self) -> CognitiveContext | None:
        return self._last_context


    # ======================================================
    # Runtime lifecycle
    # ======================================================

    def start(self):
        """
        Starts runtime execution.
        """

        self.state = CognitiveState.INITIALIZING

        self.runtime_state.mark_started()


    def stop(self):
        """
        Stops runtime execution.
        """

        self.state = CognitiveState.IDLE

        self.runtime_state.mark_stopped()



    # ======================================================
    # Execution
    # ======================================================

    def run(
        self,
        input_data=None,
    ) -> CognitiveContext:
        """
        Executes one cognitive cycle.
        """

        self.start()


        context = CognitiveContext(
            state=CognitiveState.INITIALIZING,

            input_data=input_data,


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

            context = self._loop.execute(
                context
            )


            self._cycle_counter += 1

            self._last_context = context


            self.runtime_state.update_cycle(
                cycle=self._cycle_counter
            )


            return context



        except Exception as exc:


            context.update_state(
                CognitiveState.FAILED
            )


            self._last_context = context


            self.runtime_state.register_error(
                str(exc)
            )


            raise



        finally:

            self.stop()



    # ======================================================
    # Persistence helpers
    # ======================================================

    def export_state(self) -> dict:
        """
        Returns serializable runtime state.
        """

        return self.runtime_state.to_dict()



    def import_state(
        self,
        data: dict,
    ):
        """
        Restores runtime state.
        """

        self.runtime_state.from_dict(
            data
        )


    # ======================================================
    # Utilities
    # ======================================================

    def reset_statistics(self):
        """
        Reset runtime counters.
        """

        self._cycle_counter = 0

        self._last_context = None

        self.runtime_state.reset()