from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class ConsolidationStage(CognitiveStage):
    """
    Finalizes the cognitive cycle.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:

        context.update_state(CognitiveState.CONSOLIDATING)

        # Future versions will consolidate memories,
        # update long-term knowledge and finalize statistics.

        context.update_state(CognitiveState.COMPLETED)

        return context