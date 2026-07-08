from bitgenesis.cognition.context import CognitiveContext

from .base import CognitiveStage


class ExecutionStage(CognitiveStage):

    def execute(self, context: CognitiveContext) -> CognitiveContext:

        return context