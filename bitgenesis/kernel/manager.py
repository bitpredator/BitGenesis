from __future__ import annotations


from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventType,
    EventCategory,
)


class ServiceManager:
    """
    Central lifecycle manager for BitGenesis services.

    Responsible for:
    - service registration
    - service discovery
    - lifecycle execution
    - runtime ticking
    - lifecycle events emission

    The Kernel delegates service operations here.
    """


    def __init__(
        self,
        registry,
        bus,
    ):

        self.registry = registry

        self.bus = bus



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------


    def register(
        self,
        service,
    ):

        self.registry.register(
            service
        )


        self._emit(
            EventType.SERVICE_REGISTERED,
            service,
        )



    def unregister(
        self,
        service,
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



    def get_by_name(
        self,
        name,
    ):

        return self.registry.get_by_name(
            name
        )



    def all(self):

        return self.registry.all()



    @property
    def count(self):

        return len(
            self.registry.all()
        )



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------


    def start_all(self):


        for service in self.registry.all():

            self._start_service(
                service
            )



    def stop_all(self):


        for service in reversed(
            self.registry.all()
        ):

            self._stop_service(
                service
            )



    def tick_all(self):


        for service in self.registry.all():

            self._tick_service(
                service
            )



    # --------------------------------------------------
    # Internal lifecycle
    # --------------------------------------------------


    def _start_service(
        self,
        service,
    ):


        service.start()


        self._emit(
            EventType.SERVICE_STARTED,
            service,
        )



    def _stop_service(
        self,
        service,
    ):


        service.stop()


        self._emit(
            EventType.SERVICE_STOPPED,
            service,
        )



    def _tick_service(
        self,
        service,
    ):


        service.tick()


        self._emit(
            EventType.SERVICE_TICKED,
            service,
        )



    # --------------------------------------------------
    # Events
    # --------------------------------------------------


    def _emit(
        self,
        event_type,
        service,
    ):


        self.bus.emit(
            Event(
                category=EventCategory.KERNEL,
                type=event_type,
                source="service_manager",
                payload={
                    "service": type(service).__name__,
                    **self._metadata(service),
                },
            )
        )



    # --------------------------------------------------
    # Metadata compatibility
    # --------------------------------------------------


    def _metadata(
        self,
        service,
    ) -> dict:

        if hasattr(
            service,
            "metadata",
        ):

            return service.metadata()


        return {

            "name": getattr(
                service,
                "name",
                type(service).__name__,
            ),

            "version": getattr(
                service,
                "version",
                "0.0.0",
            ),

            "type": type(service).__name__,
        }