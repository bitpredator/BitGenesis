from dataclasses import dataclass

from bitgenesis.events.types import Event
from bitgenesis.memory.store import MemoryStore


@dataclass
class ReasoningContext:

    # Evento che ha attivato il ragionamento
    event: Event

    # Accesso alla memoria completa
    memory_store: MemoryStore

    # Contesto costruito da MemoryContext
    memory_context: dict | None = None