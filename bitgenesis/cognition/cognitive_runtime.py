from __future__ import annotations


from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.loop import CognitiveLoop
from bitgenesis.cognition.state import CognitiveState

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.runtime.runtime_status import RuntimeState

from bitgenesis.learning.experience import Experience



class CognitiveRuntime:
    """
    Coordinates the execution of the BitGenesis cognitive pipeline.

    Runtime responsibilities:

    - create cognitive contexts
    - inject cognitive subsystems
    - process language input
    - execute cognitive cycles
    - track execution state
    - emit cognitive lifecycle events
    - create learning experiences
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
        # Runtime state
        # --------------------------------------------------

        self.state = CognitiveState.IDLE

        self.runtime_state = RuntimeState()



        # --------------------------------------------------
        # Statistics
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

        self.learning_engine = learning_engine

        self.language_processor = language_processor

        self.planner = planner

        self.executor = executor

        self.event_bus = event_bus



        # --------------------------------------------------
        # Cognitive pipeline
        # --------------------------------------------------

        self._loop = CognitiveLoop(
            language_processor=self.language_processor,
        )



    # ======================================================
    # Properties
    # ======================================================


    @property
    def loop(
        self,
    ) -> CognitiveLoop:

        return self._loop



    @property
    def is_running(
        self,
    ) -> bool:

        return self.state != CognitiveState.IDLE



    @property
    def cycle_count(
        self,
    ) -> int:

        return self._cycle_counter



    @property
    def last_context(
        self,
    ) -> CognitiveContext | None:

        return self._last_context



    # ======================================================
    # Events
    # ======================================================


    def _emit(
        self,
        event_type,
        payload=None,
    ):


        if self.event_bus is None:

            return


        self.event_bus.emit(
            Event(
                category=EventCategory.COGNITION,
                type=event_type,
                source="cognitive_runtime",
                payload=payload or {},
            )
        )



    # ======================================================
    # Lifecycle
    # ======================================================


    def start(
        self,
    ):

        self.state = CognitiveState.INITIALIZING

        self.runtime_state.mark_started()


        self._emit(
            EventType.COGNITIVE_RUNTIME_STARTED,
        )



    def stop(
        self,
    ):

        self.state = CognitiveState.IDLE

        self.runtime_state.mark_stopped()


        self._emit(
            EventType.COGNITIVE_RUNTIME_STOPPED,
        )



    # ======================================================
    # Language processing
    # ======================================================


    def _process_language(
        self,
        context: CognitiveContext,
    ):


        if self.language_processor is None:

            return


        if not isinstance(
            context.input_data,
            str,
        ):

            return


        context.language_context = (
            self.language_processor.process(
                context.input_data
            )
        )



    # ======================================================
    # Learning
    # ======================================================


    def _create_experience(
        self,
        context,
    ):


        if self.learning_engine is None:

            return



        language = None


        if getattr(
            context,
            "language_context",
            None,
        ) is not None:

            language = (
                context.language_context.language.value
            )



        experience = Experience(

            input_data=context.input_data,

            output_data=context.response,

            context={

                "language": language,

                "cycle_id": context.cycle_id,

            },

            metadata={

                "stages":
                    len(context.stage_history),

            },

        )


        self.learning_engine.learn(
            experience
        )



    # ======================================================
    # Execution
    # ======================================================


    def run(
        self,
        input_data=None,
    ) -> CognitiveContext:


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

            learning_engine=self.learning_engine,


            planner=self.planner,

            executor=self.executor,

            event_bus=self.event_bus,

        )



        try:


            self._process_language(
                context
            )


            self._emit(
                EventType.COGNITIVE_CYCLE_STARTED,
                {
                    "input": str(input_data),
                },
            )



            context = self._loop.execute(
                context
            )



            self._cycle_counter += 1


            self._last_context = context



            self.runtime_state.update_cycle(
                cycle=self._cycle_counter
            )



            self._create_experience(
                context
            )



            self._emit(
                EventType.COGNITIVE_CYCLE_COMPLETED,
                {
                    "cycle": self._cycle_counter,
                },
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


            self._emit(
                EventType.COGNITIVE_CYCLE_FAILED,
                {
                    "error": str(exc),
                },
            )


            raise



        finally:

            self.stop()



    # ======================================================
    # Persistence
    # ======================================================


    def export_state(
        self,
    ) -> dict:

        return self.runtime_state.to_dict()



    def import_state(
        self,
        data: dict,
    ):

        self.runtime_state.from_dict(
            data
        )



    # ======================================================
    # Utilities
    # ======================================================


    def reset_statistics(
        self,
    ):

        self._cycle_counter = 0

        self._last_context = None

        self.runtime_state.reset()