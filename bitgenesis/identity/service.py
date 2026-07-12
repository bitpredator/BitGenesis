from __future__ import annotations

from bitgenesis.events.event_bus import EventBus

from bitgenesis.kernel.service import KernelService

from bitgenesis.identity.manager import IdentityManager


class IdentityService(KernelService):
    """
    Kernel service responsible for identity management.

    Handles identity lifecycle and exposes the
    IdentityManager to the cognitive system.
    """


    def __init__(
        self,
        event_bus: EventBus,
    ) -> None:

        self.event_bus = event_bus

        self.manager = IdentityManager()

        self.running = False


    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self) -> None:

        if self.running:
            return

        self.running = True


    def stop(self) -> None:

        if not self.running:
            return

        self.running = False


    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------

    def tick(self) -> None:

        if not self.running:
            return


    # --------------------------------------------------
    # Identity access
    # --------------------------------------------------

    @property
    def profile(self):

        return self.manager.profile