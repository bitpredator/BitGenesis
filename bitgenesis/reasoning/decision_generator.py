from __future__ import annotations

from typing import List

from bitgenesis.reasoning.decision import Decision


class DecisionGenerator:
    """
    Generates all candidate decisions for the current cognitive context.

    This component does NOT decide which action should be executed.
    It only produces possible candidates that will later be evaluated
    by the DecisionRanker.
    """

    def generate(
        self,
        context,
    ) -> List[Decision]:

        candidates: List[Decision] = []

        event = context.unified.event
        memory = context.unified.memory_context or {}
        knowledge = context.unified.knowledge_context or {}

        # --------------------------------------------------
        # Perception events should always be remembered
        # --------------------------------------------------

        if getattr(event, "type", None) == "perception.event":

            candidates.append(
                Decision(
                    action="store_information",
                    confidence=1.0,
                    explanation="Perception events should be stored.",
                    data=event.payload,
                )
            )

        # --------------------------------------------------
        # Memory retrieval
        # --------------------------------------------------

        memory_items = memory.get("items") or []

        if memory_items:

            candidates.append(
                Decision(
                    action="use_memory",
                    confidence=0.80,
                    explanation="Relevant memories are available.",
                    data=memory_items,
                )
            )

        # --------------------------------------------------
        # Knowledge reasoning
        # --------------------------------------------------

        relations = knowledge.get("relations") if knowledge else None

        if relations:

            candidates.append(
                Decision(
                    action="use_knowledge",
                    confidence=0.80,
                    explanation="Relevant knowledge is available.",
                    data=relations,
                )
            )

        # --------------------------------------------------
        # Fallback
        # --------------------------------------------------

        if not candidates:

            candidates.append(
                Decision(
                    action="ignore",
                    confidence=0.50,
                    explanation="No relevant cognitive signal detected.",
                )
            )

        return candidates