from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from bitgenesis.perception import PerceptionBuilder

from .base import CognitiveStage


class PerceptionStage(CognitiveStage):
    """
    First stage of the cognitive pipeline.

    Converts the external input into an internal Perception object
    that can be processed by the remaining cognitive stages.
    """

    def __init__(self):

        self._builder = PerceptionBuilder()

    def execute(self, context: CognitiveContext) -> CognitiveContext:

        context.update_state(CognitiveState.PERCEIVING)

        context.perception = self._builder.build(
            context.input_data,
        )

        return context