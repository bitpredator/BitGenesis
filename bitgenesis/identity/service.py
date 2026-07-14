from __future__ import annotations

from bitgenesis.events.event import Event
from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.identity.manager import IdentityManager
from bitgenesis.kernel.service import KernelService


class IdentityService(KernelService):
    """
    Runtime service responsible for identity lifecycle.

    Handles:
    - IdentityManager ownership
    - Identity lifecycle events
    - Runtime integration with Kernel
    """


    def __init__(
        self,
        event_bus: EventBus,
        manager: IdentityManager | None = None,
    ) -> None:

        self.event_bus = event_bus

        self.manager = manager or IdentityManager()

        self.running = False


    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self) -> None:

        if self.running:
            return


        self.running = True


        self.event_bus.publish(
            Event(
                category=EventCategory.IDENTITY,
                type=EventType.IDENTITY_INITIALIZED,
                source="identity_service",
                payload={
                    "message": "Identity subsystem initialized",
                    "identity": self.manager.as_dict(),
                },
            )
        )


    def stop(self) -> None:

        if not self.running:
            return


        self.running = False


    def tick(self) -> None:

        if not self.running:
            return


    # --------------------------------------------------
    # Identity access
    # --------------------------------------------------

    @property
    def identity(self):

        return self.manager.profile