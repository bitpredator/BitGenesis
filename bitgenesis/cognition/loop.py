from bitgenesis.cognition.context import CognitiveContext

from bitgenesis.cognition.stages import (
    ConsolidationStage,
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
    Executes the cognitive pipeline by orchestrating
    the registered cognitive stages.

    Stages are injected with shared dependencies through
    the CognitiveContext.
    """

    def __init__(self, stages=None):

        self._stages = stages or [
            PerceptionStage(),
            MemoryStage(),
            KnowledgeStage(),
            ReasoningStage(),
            PlanningStage(),
            ExecutionStage(),
            ReflectionStage(),
            ConsolidationStage(),
        ]


    @property
    def stages(self):

        return tuple(self._stages)


    def execute(
        self,
        context: CognitiveContext
    ) -> CognitiveContext:
        """
        Executes a complete cognitive cycle.
        """

        try:

            for stage in self._stages:

                stage_name = (
                    stage.__class__.__name__
                )

                execution = (
                    context.start_stage(
                        stage_name
                    )
                )

                try:

                    context = stage.execute(
                        context
                    )

                    context.complete_stage(
                        execution
                    )

                except Exception as exc:

                    context.fail_stage(
                        execution,
                        exc
                    )

                    raise


            context.complete_cycle()

            return context


        except Exception as exc:

            context.errors.append(
                str(exc)
            )

            raise