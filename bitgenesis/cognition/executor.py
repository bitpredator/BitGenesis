from __future__ import annotations


class CognitiveExecutor:
    """
    Executes cognitive plans.

    At this stage the cognitive executor is a
    lightweight abstraction layer.

    Future versions will connect this component
    with reasoning, learning and reflection systems.
    """


    def execute(
        self,
        plan,
    ):
        """
        Execute a cognitive plan.

        Currently execution is symbolic:
        the received plan is returned unchanged.

        This keeps the cognitive pipeline testable
        while leaving room for future execution logic.
        """

        return plan