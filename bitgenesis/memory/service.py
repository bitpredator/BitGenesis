from __future__ import annotations

from bitgenesis.kernel.service import KernelService

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventCategory

from bitgenesis.memory.store import MemoryStore
from bitgenesis.memory.listener import MemoryListener


class MemoryService(KernelService):
    """
    Kernel service responsible for memory lifecycle.

    Handles:
    - MemoryStore ownership
    - EventBus subscription
    - Memory event processing
    """


    def __init__(
        self,
        event_bus: EventBus,
        store: MemoryStore | None = None,
    ):

        self.event_bus = event_bus

        self.store = store or MemoryStore()

        self.listener = MemoryListener(
            self.store
        )

        self.running = False


    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self) -> None:

        if self.running:
            return

        self.event_bus.subscribe(
            EventCategory.MEMORY,
            self.listener.handle,
        )

        self.running = True


    def stop(self) -> None:

        if not self.running:
            return

        self.event_bus.unsubscribe(
            EventCategory.MEMORY,
            self.listener.handle,
        )

        self.running = False


    def tick(self) -> None:
        """
        Reserved for future memory maintenance.

        Examples:
        - decay
        - consolidation
        - cleanup
        """
        pass