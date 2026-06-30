from dataclasses import dataclass, field
from typing import Any, Dict
import time
import uuid


@dataclass
class Memory:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: str = ""
    content: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)

    # linkage con eventi
    event_id: str = ""