from __future__ import annotations

from typing import Any

from bitgenesis.kernel.service import KernelService
from bitgenesis.memory.store import MemoryStore


class MemoryService(KernelService):
    """
    Core memory service.

    Gestisce il backend di memoria di BitGenesis.
    """

    version = "2.0.0"

    def __init__(
        self,
        event_bus=None,
        store: MemoryStore | None = None,
    ):

        super().__init__("memory")

        self.event_bus = event_bus
        self.store = store or MemoryStore()

    def start(self):
        """
        Avvio servizio memoria.
        """

        return None

    def stop(self):
        """
        Arresto servizio memoria.
        """

        return None

    def tick(self):
        """
        Ciclo runtime memoria.
        """

        return None

    def remember(
        self,
        key: str,
        value: Any,
    ):
        """
        Salva un ricordo.
        """

        if self.store is None:
            return

        if hasattr(self.store, "set"):
            self.store.set(key, value)

    def recall(
        self,
        key: str,
        default=None,
    ):
        """
        Recupera un ricordo.
        """

        if self.store is None:
            return default

        if hasattr(self.store, "get"):
            return self.store.get(key, default)

        return default

    def metadata(self):

        return {
            "name": self.name,
            "version": self.version,
            "enabled": True,
            "type": "memory",
        }