from __future__ import annotations

from typing import Iterable

from bitgenesis.reasoning.decision import Decision


class DecisionRanker:
    """
    Selects the best decision from a collection of candidates.

    The ranking strategy is intentionally simple for v0.2.0.
    Future versions may include:
    - emotional weighting
    - long-term goals
    - identity constraints
    - attention score
    - urgency
    - reinforcement learning
    """

    def rank(
        self,
        candidates: Iterable[Decision],
    ) -> Decision:

        candidates = list(candidates)

        if not candidates:
            raise ValueError(
                "No decision candidates available."
            )

        return max(
            candidates,
            key=self._score,
        )

    # --------------------------------------------------
    # Internal scoring
    # --------------------------------------------------

    def _score(
        self,
        decision: Decision,
    ) -> float:
        """
        Computes the ranking score.

        Current formula:

            confidence + priority

        This method is intentionally isolated because it will
        become much more sophisticated in future releases.
        """

        return (
            decision.confidence
            + decision.priority
        )