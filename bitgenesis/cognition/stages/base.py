from abc import ABC, abstractmethod

from bitgenesis.cognition.context import CognitiveContext


class CognitiveStage(ABC):
    """
    Base class for all cognitive pipeline stages.
    """

    @abstractmethod
    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Executes the stage and returns the updated context.
        """
        raise NotImplementedError