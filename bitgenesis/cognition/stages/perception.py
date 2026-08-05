from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from bitgenesis.perception import PerceptionBuilder

from .base import CognitiveStage



class PerceptionStage(CognitiveStage):
    """
    First stage of the cognitive pipeline.

    Converts external input into an internal Perception object.

    Optional language processing enriches the perception layer
    with linguistic metadata.
    """


    def __init__(
        self,
        language_processor=None,
    ):

        self._builder = PerceptionBuilder()

        self.language_processor = language_processor



    def execute(
        self,
        context: CognitiveContext,
    ) -> CognitiveContext:


        context.update_state(
            CognitiveState.PERCEIVING
        )



        # --------------------------------------------------
        # Base perception
        # --------------------------------------------------

        context.perception = self._builder.build(
            context.input_data,
        )



        # --------------------------------------------------
        # Language perception
        # --------------------------------------------------

        if (
            self.language_processor is not None
            and isinstance(
                context.input_data,
                str,
            )
        ):

            context.language_context = (
                self.language_processor.process(
                    context.input_data
                )
            )



        return context