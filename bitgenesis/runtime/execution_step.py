from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True)
class ExecutionStep:

    action: str

    payload: dict[str, Any] = field(
        default_factory=dict
    )

    priority: int = 0

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


    def execute_name(self) -> str:

        return self.action