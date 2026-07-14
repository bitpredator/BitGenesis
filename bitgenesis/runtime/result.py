from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class ActionResult:
    """
    Result returned by runtime actions.

    Represents the outcome of a single runtime action execution.
    """

    success: bool

    action: str | None = None

    data: Any = None

    error: str | None = None


    # --------------------------------------------------
    # Factory helpers
    # --------------------------------------------------

    @classmethod
    def ok(
        cls,
        data: Any = None,
        action: str | None = None,
    ) -> "ActionResult":

        return cls(
            success=True,
            action=action,
            data=data,
        )


    @classmethod
    def fail(
        cls,
        error: str,
        action: str | None = None,
    ) -> "ActionResult":

        return cls(
            success=False,
            action=action,
            error=error,
        )