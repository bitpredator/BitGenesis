from __future__ import annotations

from bitgenesis.events.event import Event
from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.registry import ServiceRegistry


class Kernel:
    """
    Core orchestration layer of BitGenesis.

    The Kernel manages lifecycle of runtime services
    and coordinates system execution.
    """


    def __init__(
        self,
        event_bus: EventBus,
    ):

        self.event_bus = event_bus

        self.running = False

        self.registry = ServiceRegistry()


    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self) -> None:

        if self.running:
            return


        self.running = True


        for service in self.registry.all():

            if hasattr(service, "start"):
                service.start()


        self.event_bus.publish(
            Event(
                category=EventCategory.KERNEL,
                type=EventType.KERNEL_INITIALIZED,
                source="kernel",
                payload={
                    "services": len(self.registry.all()),
                },
            )
        )


        self.event_bus.publish(
            Event(
                category=EventCategory.SYSTEM,
                type=EventType.SYSTEM_STARTED,
                source="kernel",
                payload={
                    "status": "running",
                    "services": len(self.registry.all()),
                },
            )
        )


    def stop(self) -> None:

        if not self.running:
            return


        for service in reversed(self.registry.all()):

            if hasattr(service, "stop"):
                service.stop()


        self.running = False


        self.event_bus.publish(
            Event(
                category=EventCategory.KERNEL,
                type=EventType.KERNEL_SHUTDOWN,
                source="kernel",
                payload={
                    "status": "stopped",
                },
            )
        )


    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------

    def tick(self) -> None:

        if not self.running:
            return


        for service in self.registry.all():

            if hasattr(service, "tick"):
                service.tick()


    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def publish(
        self,
        event: Event,
    ) -> None:

        self.event_bus.publish(event)


    def emit(
        self,
        event: Event,
    ) -> None:

        self.publish(event)


    # --------------------------------------------------
    # Services
    # --------------------------------------------------

    def register(
        self,
        service: KernelService,
    ) -> None:

        self.registry.register(
            service
        )


    def unregister(
        self,
        service: KernelService,
    ) -> None:

        self.registry.unregister(
            type(service)
        )


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