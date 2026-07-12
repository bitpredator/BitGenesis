from __future__ import annotations

from bitgenesis.events.event import Event
from bitgenesis.events.event_bus import EventBus
from bitgenesis.kernel.service import KernelService


class Kernel:
    """
    Core orchestration layer of BitGenesis.

    The Kernel is responsible for managing the system
    lifecycle and coordinating all runtime services.
    """

    def __init__(self, event_bus: EventBus):

        self.event_bus = event_bus

        self.running = False

        self._services: list[KernelService] = []


    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self) -> None:

        if self.running:
            return

        self.running = True

        for service in self._services:
            service.start()


    def stop(self) -> None:

        if not self.running:
            return

        for service in reversed(self._services):
            service.stop()

        self.running = False


    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------

    def tick(self) -> None:

        if not self.running:
            return

        for service in self._services:
            service.tick()


    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def publish(self, event: Event) -> None:

        self.event_bus.publish(event)


    def emit(self, event: Event) -> None:

        self.publish(event)


    # --------------------------------------------------
    # Services
    # --------------------------------------------------

    def register(
        self,
        service: KernelService,
    ) -> None:
        if service not in self._services:
            self._services.append(service)

    def unregister(self, service: KernelService) -> None:

        if service in self._services:
            self._services.remove(service)


    @property
    def services(self):

        return tuple(self._services)