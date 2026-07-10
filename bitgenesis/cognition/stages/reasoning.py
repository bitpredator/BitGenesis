from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class ReasoningStage(CognitiveStage):
    """
    Performs reasoning over the current cognitive context.

    The stage delegates reasoning operations to the configured
    inference/reasoning subsystem available through the context.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Executes the reasoning phase.
        """

        context.update_state(
            CognitiveState.REASONING
        )

        inference_engine = context.inference_engine

        # Reasoning subsystem not connected.
        if inference_engine is None:
            return context

        try:

            reasoning_input = {
                "input": context.input_data,
                "memory": context.working_memory,
                "knowledge": context.knowledge,
            }

            result = None

            # Preferred reasoning interface
            infer = getattr(
                inference_engine,
                "infer",
                None,
            )

            if callable(infer):

                result = infer(
                    reasoning_input
                )

            else:

                reason = getattr(
                    inference_engine,
                    "reason",
                    None,
                )

                if callable(reason):

                    result = reason(
                        reasoning_input
                    )

            if result is not None:

                context.reasoning_result = result

            return context

        except Exception:

            # Reasoning failures must not interrupt
            # the cognitive pipeline.
            return context