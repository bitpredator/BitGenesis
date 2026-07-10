from bitgenesis.cognition.context import CognitiveContext
from bitgenesis.cognition.state import CognitiveState

from .base import CognitiveStage


class PlanningStage(CognitiveStage):
    """
    Generates an execution plan from the current cognitive state.

    The stage delegates planning logic to the configured planner
    available through the CognitiveContext.
    """

    def execute(self, context: CognitiveContext) -> CognitiveContext:
        """
        Executes the planning phase.
        """

        context.update_state(
            CognitiveState.PLANNING
        )

        planner = context.planner

        # Planning subsystem not connected.
        if planner is None:
            return context

        try:

            planning_input = {
                "input": context.input_data,
                "reasoning": context.reasoning_result,
                "knowledge": context.knowledge,
                "memory": context.working_memory,
            }

            plan = None

            # Preferred interface
            if hasattr(planner, "create_plan"):

                plan = planner.create_plan(
                    planning_input
                )

            # Alternative interface
            elif hasattr(planner, "plan"):

                plan = planner.plan(
                    planning_input
                )

            # Generic callable planner
            elif callable(planner):

                plan = planner(
                    planning_input
                )

            if plan is not None:

                context.plan = plan

                context.update_state(
                    CognitiveState.PLANNED
                )

            return context

        except Exception:

            # Planning errors are isolated.
            # The cognitive cycle can continue.
            return context