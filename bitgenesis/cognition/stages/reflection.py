from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class ReflectionStage(CognitiveStage):
    """
    Evaluates the result of the cognitive cycle.

    Reflection is delegated to the configured reflection engine
    available through the CognitiveContext.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Executes the reflection phase.
        """

        context.update_state(
            CognitiveState.REFLECTING
        )

        reflection_engine = context.reflection_engine

        # Reflection subsystem not connected.
        if reflection_engine is None:
            return context

        try:

            reflection_input = {
                "input": context.input_data,
                "memory": context.working_memory,
                "knowledge": context.knowledge,
                "reasoning": context.reasoning_result,
                "plan": context.plan,
                "response": context.response,
            }

            reflection = None

            # Preferred interface
            if hasattr(reflection_engine, "reflect"):

                reflection = reflection_engine.reflect(
                    reflection_input
                )

            # Alternative interface
            elif hasattr(reflection_engine, "evaluate"):

                reflection = reflection_engine.evaluate(
                    reflection_input
                )

            # Generic callable engine
            elif callable(reflection_engine):

                reflection = reflection_engine(
                    reflection_input
                )

            if reflection is not None:

                context.reflection = reflection

            return context

        except Exception:

            # Reflection failures must not break
            # the cognitive execution cycle.
            return context