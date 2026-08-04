from __future__ import annotations

from bitgenesis.cognition.context import CognitiveContext

from bitgenesis.learning.experience import Experience

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.cognition.stages import (
    ConsolidationStage,
    DialogueStage,
    ExecutionStage,
    KnowledgeStage,
    MemoryStage,
    PerceptionStage,
    PlanningStage,
    ReasoningStage,
    ReflectionStage,
)


class CognitiveLoop:
    """
    Executes a single cognitive pipeline.

    The CognitiveLoop orchestrates cognitive stages
    and emits lifecycle events through EventBus.

    After a successful cognitive cycle, the loop can
    generate an Experience and forward it to the
    LearningEngine.
    """


    def __init__(
        self,
        stages=None,
    ):

        self._stages = stages or [
            PerceptionStage(),
            MemoryStage(),
            KnowledgeStage(),
            ReasoningStage(),
            PlanningStage(),
            ExecutionStage(),
            DialogueStage(),
            ReflectionStage(),
            ConsolidationStage(),
        ]

        self._execution_count = 0


    @property
    def stages(self):

        return tuple(self._stages)


    @property
    def execution_count(self) -> int:

        return self._execution_count



    # --------------------------------------------------
    # Event helper
    # --------------------------------------------------

    def _emit(
        self,
        context,
        event_type,
        payload=None,
    ):

        if context.event_bus is None:
            return


        context.event_bus.emit(
            Event(
                category=EventCategory.COGNITION,
                type=event_type,
                source="cognitive_loop",
                payload=payload or {},
            )
        )



    # --------------------------------------------------
    # Learning integration
    # --------------------------------------------------

    def create_experience(
        self,
        context: CognitiveContext,
    ):
        """
        Converts a completed cognitive cycle
        into a learning experience.
        """

        return Experience(

            input_data=context.input_data,

            output_data=context.response,

            context={
                "cycle_id": context.cycle_id,

                "stages": [
                    item["stage"]
                    for item in context.stage_history
                ],
            },

            success=(
                len(context.errors) == 0
            ),

            metadata={
                "state": context.state.value,
            },
        )


    def process_learning(
        self,
        context: CognitiveContext,
    ):
        """
        Sends the completed experience
        to the LearningEngine.
        """

        learning_engine = (
            context.learning_engine
        )


        if learning_engine is None:

            return


        experience = self.create_experience(
            context
        )


        learning_engine.learn(
            experience
        )


        self._emit(
            context,
            EventType.LEARNING_COMPLETED,
            {
                "cycle_id": context.cycle_id,
            },
        )



    # --------------------------------------------------
    # Hooks
    # --------------------------------------------------

    def before_cycle(
        self,
        context,
    ):

        self._emit(
            context,
            EventType.COGNITIVE_CYCLE_STARTED,
        )



    def after_cycle(
        self,
        context,
    ):

        self.process_learning(
            context
        )


        self._emit(
            context,
            EventType.COGNITIVE_CYCLE_COMPLETED,
            {
                "execution_count": self._execution_count,
            },
        )



    def before_stage(
        self,
        stage,
        context,
    ):

        self._emit(
            context,
            EventType.COGNITIVE_STAGE_STARTED,
            {
                "stage": stage.__class__.__name__,
            },
        )



    def after_stage(
        self,
        stage,
        context,
    ):

        self._emit(
            context,
            EventType.COGNITIVE_STAGE_COMPLETED,
            {
                "stage": stage.__class__.__name__,
            },
        )



    def on_stage_failed(
        self,
        stage,
        context,
        exception,
    ):

        if context.event_bus is None:

            return


        context.event_bus.emit(
            Event(
                category=EventCategory.COGNITION,
                type=EventType.COGNITIVE_CYCLE_FAILED,
                source="cognitive_loop",
                payload={
                    "stage": stage.__class__.__name__,
                    "error": str(exception),
                },
            )
        )



    # --------------------------------------------------
    # Pipeline execution
    # --------------------------------------------------

    def execute(
        self,
        context: CognitiveContext,
    ) -> CognitiveContext:
        """
        Executes one complete cognitive cycle.
        """

        self.before_cycle(
            context
        )


        try:

            for stage in self._stages:


                self.before_stage(
                    stage,
                    context,
                )


                stage_name = (
                    stage.__class__.__name__
                )


                execution = context.start_stage(
                    stage_name
                )


                try:

                    context = stage.execute(
                        context
                    )


                    context.complete_stage(
                        execution
                    )


                    self.after_stage(
                        stage,
                        context,
                    )


                except Exception as exc:


                    context.fail_stage(
                        execution,
                        exc,
                    )


                    self.on_stage_failed(
                        stage,
                        context,
                        exc,
                    )

                    raise



            context.complete_cycle()


            self._execution_count += 1


            self.after_cycle(
                context
            )


            return context



        except Exception as exc:


            context.errors.append(
                str(exc)
            )

            raise