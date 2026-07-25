from __future__ import annotations


from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventType,
    EventCategory,
)


from bitgenesis.kernel.registry import ServiceRegistry
from bitgenesis.kernel.dependency_resolver import DependencyResolver

from bitgenesis.kernel.service_state import ServiceState
from bitgenesis.kernel.descriptor import ServiceDescriptor



class ServiceManager:
    """
    Central service orchestration layer.

    Responsibilities:
    - service registration
    - service discovery
    - dependency resolution
    - lifecycle execution
    - runtime ticking
    - state tracking
    - lifecycle events
    """


    def __init__(
        self,
        event_bus=None,
    ):


        self.event_bus = event_bus


        self.registry = ServiceRegistry()


        self.dependency_resolver = DependencyResolver(
            self.registry
        )


        self._states = {}



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------


    def register(
        self,
        service,
        descriptor: ServiceDescriptor | None = None,
    ):


        self.registry.register(
            service,
            descriptor,
        )


        self._states[type(service)] = (
            ServiceState.CREATED
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


        self._states.pop(
            type(service),
            None,
        )


        self._emit(
            EventType.SERVICE_UNREGISTERED,
            service,
        )



    # --------------------------------------------------
    # Discovery
    # --------------------------------------------------


    def contains(
        self,
        service_type,
    ):


        return self.registry.contains(
            service_type
        )



    def get(
        self,
        service_type,
    ):


        return self.registry.get(
            service_type
        )



    def require(
        self,
        service_type,
    ):


        return self.registry.require(
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



    def discover(self):


        return self.registry.all()



    @property
    def count(self):


        return len(
            self.registry.all()
        )



    def descriptor(
        self,
        service,
    ):


        return self.registry.descriptor(
            service
        )



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------


    def start_all(self):


        entries = sorted(
            self.registry.entries(),
            key=lambda entry: (
                entry.descriptor.priority
                if entry.descriptor
                else 0
            ),
        )


        for entry in entries:


            if entry.descriptor:

                if not entry.descriptor.auto_start:
                    continue


            self._start_service(
                entry.service
            )



    def stop_all(self):


        entries = list(
            reversed(
                self.registry.entries()
            )
        )


        for entry in entries:


            self._stop_service(
                entry.service
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


        service_type = type(service)


        try:


            self._states[service_type] = (
                ServiceState.STARTING
            )


            service.start()



            self._states[service_type] = (
                ServiceState.RUNNING
            )



            self._emit(
                EventType.SERVICE_STARTED,
                service,
            )


        except Exception:


            self._states[service_type] = (
                ServiceState.FAILED
            )



    def _stop_service(
        self,
        service,
    ):


        service_type = type(service)


        try:


            self._states[service_type] = (
                ServiceState.STOPPING
            )


            service.stop()



            self._states[service_type] = (
                ServiceState.STOPPED
            )



            self._emit(
                EventType.SERVICE_STOPPED,
                service,
            )


        except Exception:


            self._states[service_type] = (
                ServiceState.FAILED
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
    # State
    # --------------------------------------------------


    def state(
        self,
        service_type,
    ):


        return self._states.get(
            service_type,
            ServiceState.CREATED,
        )



    def running_services(self):


        return tuple(
            service
            for service in self.registry.all()
            if self.state(type(service))
            == ServiceState.RUNNING
        )



    # --------------------------------------------------
    # Events
    # --------------------------------------------------


    def _emit(
        self,
        event_type,
        service,
    ):


        if self.event_bus is None:
            return



        self.event_bus.emit(
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
    # Metadata
    # --------------------------------------------------


    def _metadata(
        self,
        service,
    ):


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