from __future__ import annotations

from bitgenesis.events.event import Event
from bitgenesis.events.event_bus import EventBus
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.registry import ServiceRegistry


class Kernel:
    """
    Core orchestration layer of BitGenesis.

    The Kernel is responsible for managing the system
    lifecycle and coordinating all runtime services.
    """

    def __init__(self, event_bus: EventBus):

        self.event_bus = event_bus

        self.running = False

        self.registry = ServiceRegistry()
        self._services: list[KernelService] = []


    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self) -> None:

        if self.running:
            return

        self.running = True

        for service in self.registry.all():
            service.start()


    def stop(self) -> None:

        if not self.running:
            return

        for service in reversed(self.registry.all()):
            service.stop()

        self.running = False


    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------

    def tick(self) -> None:

        if not self.running:
            return

        for service in self.registry.all():
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
        self.registry.register(service)
        self._services.append(service)

    def unregister(self, service: KernelService) -> None:

        self.registry.unregister(type(service))
        self._services.remove(service)


    @property
    def services(self):
    
        return self.registry.all()
    
    def get_service(
        self,
        service_type: type[KernelService],
    ):
        return self.registry.get(
            service_type
        )