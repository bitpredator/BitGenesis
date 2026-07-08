from bitgenesis.cognition.context import CognitiveContext

from .base import CognitiveStage


class KnowledgeStage(CognitiveStage):
    """
    Integrates knowledge relevant to the current cognitive context.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:

        return context