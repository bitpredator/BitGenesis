from dataclasses import dataclass
from typing import Any


@dataclass
class PlanStep:
    action: str
    target: Any = None
    metadata: dict = None


@dataclass
class ExecutionPlan:
    steps: list
    intent: str
    confidence: float


class Planner:

    def build(self, decision, context=None):

        steps = []

        # --------------------------
        # MEMORY ACTIONS
        # --------------------------
        if decision.action == "use_memory":

            steps.append(
                PlanStep(
                    action="retrieve_memory_items",
                    target=decision.data,
                    metadata={"source": "memory"}
                )
            )

        # --------------------------
        # KNOWLEDGE ACTIONS
        # --------------------------
        elif decision.action == "use_knowledge":

            steps.append(
                PlanStep(
                    action="query_knowledge_graph",
                    target=decision.data,
                    metadata={"source": "knowledge"}
                )
            )

        # --------------------------
        # STORE / PERCEPTION
        # --------------------------
        elif decision.action == "store_information":

            steps.append(
                PlanStep(
                    action="store_memory",
                    target=decision.data,
                    metadata={"source": "event"}
                )
            )

        # --------------------------
        # DEFAULT FALLBACK
        # --------------------------
        else:

            steps.append(
                PlanStep(
                    action="no_op",
                    metadata={"reason": decision.explanation}
                )
            )

        return ExecutionPlan(
            steps=steps,
            intent=decision.action,
            confidence=decision.confidence,
        )