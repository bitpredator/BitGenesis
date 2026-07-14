from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class ActionResult:
    """
    Result returned by runtime actions.
    """


    success: bool

    data: Any = None

    error: str | None = None


    @classmethod
    def ok(
        cls,
        data: Any = None,
    ) -> "ActionResult":

        return cls(
            success=True,
            data=data,
        )


    @classmethod
    def fail(
        cls,
        error: str,
    ) -> "ActionResult":

        return cls(
            success=False,
            error=error,
        )