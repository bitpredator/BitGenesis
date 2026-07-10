from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class ExecutionStage(CognitiveStage):
    """
    Executes the generated cognitive plan.

    The stage delegates execution to the configured executor
    available through the CognitiveContext.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Executes the current cognitive plan.
        """

        context.update_state(
            CognitiveState.EXECUTING
        )

        executor = context.executor

        # No execution subsystem connected.
        if executor is None:
            return context

        try:

            execution_input = {
                "input": context.input_data,
                "plan": context.plan,
                "reasoning": context.reasoning_result,
                "memory": context.working_memory,
                "knowledge": context.knowledge,
            }

            result = None

            # Preferred execution interface
            if hasattr(executor, "execute"):

                result = executor.execute(
                    execution_input
                )

            # Alternative interface
            elif hasattr(executor, "run"):

                result = executor.run(
                    execution_input
                )

            # Generic callable executor
            elif callable(executor):

                result = executor(
                    execution_input
                )

            if result is not None:

                context.response = result

            return context

        except Exception:

            # Execution failures are isolated.
            # The cognitive cycle can continue.
            return context