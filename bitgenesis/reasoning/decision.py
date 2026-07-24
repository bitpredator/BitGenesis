from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Decision:
    """
    Represents a cognitive decision.

    A Decision is produced by the reasoning layer and may
    later receive planning and execution results attached
    during the cognitive pipeline.
    """

    action: str

    confidence: float

    explanation: str

    data: Any = None

    # --------------------------------------------------
    # Decision ranking support
    # --------------------------------------------------

    priority: float = 0.0

    # --------------------------------------------------
    # Pipeline runtime attachments
    # --------------------------------------------------

    plan: Any = None

    execution: Any = None