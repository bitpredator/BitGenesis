from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Resolution:
    """
    Represents the result produced by the reasoning layer.

    A Resolution is the canonical object exchanged between
    reasoning and dialogue.

    It is intentionally domain-agnostic and can represent
    identity, memory, knowledge, goals, tools or future modules.
    """

    domain: str
    target: str
    value: Any

    confidence: float = 1.0
    metadata: dict = field(default_factory=dict)

    @property
    def success(self) -> bool:
        return self.value is not None