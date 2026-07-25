from __future__ import annotations

from typing import Any

from bitgenesis.runtime.execution_plan import ExecutionPlan
from bitgenesis.runtime.execution_step import ExecutionStep
from bitgenesis.runtime.planner_result import PlannerResult



class CognitiveExecutionPlanner:
    """
    Converts cognitive decisions into executable runtime plans.

    The planner does not execute actions.
    It only creates an ordered execution plan.
    """


    def create_plan(
        self,
        decision: Any,
    ) -> PlannerResult:
        """
        Create an execution plan from a cognitive decision.
        """


        if decision is None:

            return PlannerResult(
                success=False,
                plan=ExecutionPlan(),
                reason="missing decision",
            )



        action = getattr(
            decision,
            "action",
            None,
        )


        if not action:

            return PlannerResult(
                success=False,
                plan=ExecutionPlan(),
                reason="missing action",
            )



        plan = ExecutionPlan()


        plan.add(
            ExecutionStep(
                action=action,
            )
        )



        return PlannerResult(
            success=True,
            plan=plan,
        )