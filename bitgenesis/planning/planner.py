from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


# --------------------------------------------------
# Planning objects
# --------------------------------------------------

@dataclass(slots=True)
class PlanStep:
    """
    Single executable planning step.
    """

    action: str

    target: Any = None

    metadata: dict = field(
        default_factory=dict
    )


@dataclass(slots=True)
class ExecutionPlan:
    """
    Runtime execution plan.

    A plan is an ordered list of executable steps.
    """

    steps: list[PlanStep]

    intent: str

    confidence: float

    metadata: dict = field(
        default_factory=dict
    )


# --------------------------------------------------
# Planner
# --------------------------------------------------

class Planner:
    """
    Converts a reasoning decision into an execution plan.

    Future versions will support:
    - multi-step plans
    - conditional branches
    - retries
    - dynamic planning
    """

    def build(
        self,
        decision,
        context=None,
    ) -> ExecutionPlan:

        steps: list[PlanStep] = []

        action = decision.action

        if action == "use_memory":

            steps.extend(
                self._plan_memory(
                    decision
                )
            )

        elif action == "use_knowledge":

            steps.extend(
                self._plan_knowledge(
                    decision
                )
            )

        elif action == "store_information":

            steps.extend(
                self._plan_storage(
                    decision
                )
            )

        else:

            steps.append(
                PlanStep(
                    action="no_op",
                    metadata={
                        "reason": getattr(
                            decision,
                            "explanation",
                            "",
                        )
                    },
                )
            )

        return ExecutionPlan(
            steps=steps,
            intent=action,
            confidence=decision.confidence,
            metadata={
                "planner": "default",
            },
        )

    # --------------------------------------------------
    # Planning strategies
    # --------------------------------------------------

    def _plan_memory(
        self,
        decision,
    ) -> list[PlanStep]:

        return [
            PlanStep(
                action="retrieve_memory_items",
                target=decision.data,
                metadata={
                    "source": "memory",
                },
            )
        ]

    def _plan_knowledge(
        self,
        decision,
    ) -> list[PlanStep]:

        return [
            PlanStep(
                action="query_knowledge_graph",
                target=decision.data,
                metadata={
                    "source": "knowledge",
                },
            )
        ]

    def _plan_storage(
        self,
        decision,
    ) -> list[PlanStep]:

        return [
            PlanStep(
                action="store_memory",
                target=decision.data,
                metadata={
                    "source": "event",
                },
            )
        ]