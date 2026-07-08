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

    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Executes a complete cognitive cycle.
        """

        for stage in self._stages:

            context = stage.execute(context)

        return context