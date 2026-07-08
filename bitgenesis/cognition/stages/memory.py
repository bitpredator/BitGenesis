from bitgenesis.cognition.context import CognitiveContext

from .base import CognitiveStage


class MemoryStage(CognitiveStage):

    def execute(self, context: CognitiveContext) -> CognitiveContext:

        return context