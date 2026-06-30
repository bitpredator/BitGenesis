from dataclasses import dataclass, field
from typing import Any, Dict
import time
import uuid


@dataclass
class Event:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: str = ""
    source: str = "unknown"
    payload: Dict[str, Any] = field(default_factory=dict)
    timestamp: float = field(default_factory=time.time)

    # tracing fields
    trace_id: str = ""
    parent_id: str = ""