from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class PerceptionStage(CognitiveStage):
    """
    Processes the initial input of a cognitive cycle.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:

        context.update_state(CognitiveState.PERCEIVING)

        return context