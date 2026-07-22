from __future__ import annotations


from bitgenesis.kernel.registry import ServiceRegistry
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor

from bitgenesis.events.bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)


class ServiceManager:
    """
    Manages Kernel service lifecycle.
    """

    def __init__(
        self,
        registry: ServiceRegistry | None = None,
        event_bus: EventBus | None = None,
    ):

        self.registry = (
            registry
            or ServiceRegistry()
        )

        self.event_bus = event_bus


    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def _emit(
        self,
        event_type: EventType,
        service: KernelService,
    ):

        if self.event_bus is None:
            return


        self.event_bus.publish(
            Event(
                category=EventCategory.KERNEL,
                type=event_type,
                source=type(self).__name__,
                payload={
                    "service": type(service).__name__
                },
            )
        )


    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register(
        self,
        service: KernelService,
        descriptor: ServiceDescriptor | None = None,
    ):

        if descriptor is None:

            descriptor = ServiceDescriptor(
                name=type(service).__name__,
            )


        self.registry.register(
            service,
            descriptor,
        )


        self._emit(
            EventType.SERVICE_REGISTERED,
            service,
        )


    def unregister(
        self,
        service: KernelService,
    ):

        self.registry.unregister(
            service
        )


        self._emit(
            EventType.SERVICE_UNREGISTERED,
            service,
        )


    # --------------------------------------------------
    # Discovery
    # --------------------------------------------------

    def get(
        self,
        service_type,
    ):

        return self.registry.get(
            service_type
        )


    def get_all(
        self,
        service_type,
    ):

        return self.registry.get_all(
            service_type
        )


    def require(
        self,
        service_type,
    ):

        return self.registry.require(
            service_type
        )


    def contains(
        self,
        service_type,
    ):

        return self.registry.contains(
            service_type
        )


    def get_by_name(
        self,
        name,
    ):

        return self.registry.get_by_name(
            name
        )


    def discover(self):

        return self.registry.all()


    def all(self):

        return self.discover()


    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    def descriptor(
        self,
        service,
    ):

        # support class lookup
        if isinstance(
            service,
            type,
        ):

            service = self.registry.get(
                service
            )


            if service is None:
                return None


        return self.registry.descriptor(
            service
        )


    # --------------------------------------------------
    # Ordering
    # --------------------------------------------------

    def _ordered_entries(self):

        return sorted(
            self.registry.entries(),
            key=lambda entry:
                entry.descriptor.priority,
        )


    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start_all(self):

        for entry in self._ordered_entries():

            if not entry.descriptor.auto_start:
                continue


            entry.service.start()


            self._emit(
                EventType.SERVICE_STARTED,
                entry.service,
            )


    def stop_all(self):

        for entry in reversed(
            self._ordered_entries()
        ):

            entry.service.stop()


            self._emit(
                EventType.SERVICE_STOPPED,
                entry.service,
            )


    def tick_all(self):

        for entry in self.registry.entries():

            entry.service.tick()


            self._emit(
                EventType.SERVICE_TICKED,
                entry.service,
            )