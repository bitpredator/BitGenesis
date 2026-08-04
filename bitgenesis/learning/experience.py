from __future__ import annotations


from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any
from uuid import uuid4



@dataclass(slots=True)
class Experience:
    """
    Represents a single cognitive experience.

    An experience is generated from:

    - perception
    - reasoning
    - execution
    - feedback

    It is the fundamental learning unit
    consumed by the LearningEngine.
    """


    # --------------------------------------------------
    # Identity
    # --------------------------------------------------

    id: str = field(
        default_factory=lambda: str(uuid4())
    )


    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )



    # --------------------------------------------------
    # Experience data
    # --------------------------------------------------

    input_data: Any = None

    output_data: Any = None


    context: dict[str, Any] = field(
        default_factory=dict
    )



    # --------------------------------------------------
    # Learning signals
    # --------------------------------------------------

    success: bool = False

    feedback: Any = None


    importance: float = 0.5



    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    source: str = "cognitive_runtime"


    metadata: dict[str, Any] = field(
        default_factory=dict
    )



    # --------------------------------------------------
    # Reward
    # --------------------------------------------------

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



    # --------------------------------------------------
    # Serialization
    # --------------------------------------------------

    def to_dict(
        self,
    ) -> dict[str, Any]:
        """
        Converts experience into serializable data.
        """


        return {

            "id": self.id,

            "created_at": (
                self.created_at.isoformat()
            ),

            "input_data": self.input_data,

            "output_data": self.output_data,

            "context": self.context,

            "success": self.success,

            "feedback": self.feedback,

            "importance": self.importance,

            "source": self.source,

            "metadata": self.metadata,

            "reward": self.reward(),

        }