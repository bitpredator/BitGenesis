from dataclasses import dataclass
from typing import Any


@dataclass
class Decision:
    action: str
    confidence: float
    explanation: str
    data: Any = None