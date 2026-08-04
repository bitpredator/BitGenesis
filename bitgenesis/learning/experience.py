from __future__ import annotations


from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass(slots=True)
class Experience:
    """
    Represents a single cognitive experience.

    An experience is generated from:
    - perception
    - reasoning
    - execution
    - feedback

    It is the fundamental unit consumed
    by the learning subsystem.
    """


    input_data: Any = None

    output_data: Any = None

    context: dict[str, Any] = field(
        default_factory=dict
    )


    success: bool = False

    feedback: Any = None


    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )


    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    def reward(
        self,
    ) -> float:
        """
        Calculates a simple reward signal.

        Future versions may replace this with:
        - reinforcement learning signals
        - emotional weighting
        - utility evaluation
        """

        if self.success:
            return 1.0

        return 0.0