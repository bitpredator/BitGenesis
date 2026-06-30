from dataclasses import dataclass
from typing import Any

from bitgenesis.events.types import Event
from bitgenesis.memory.store import MemoryStore


@dataclass
class ReasoningContext:
    event: Event
    memory: MemoryStore