from __future__ import annotations

from typing import Dict, Optional, Type

from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor
from bitgenesis.kernel.service_state import ServiceState
from bitgenesis.kernel.exceptions import ServiceNotFoundError
from bitgenesis.kernel.dependency_resolver import DependencyResolver

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)


class ServiceManager:


    def __init__(
        self,
        event_bus=None,
    ):

        self.event_bus = event_bus

        self._services: Dict[str, KernelService] = {}

        self._descriptors: Dict[str, ServiceDescriptor] = {}

        self._states: Dict[str, ServiceState] = {}

        self._type_index: Dict[
            Type[KernelService],
            list[str]
        ] = {}

        self._registration_order = 0


        self.dependency_resolver = DependencyResolver(
            self
        )



    # =================================================
    # EVENTS
    # =================================================


    def _emit(
        self,
        event_type,
        payload,
    ):

        if self.event_bus is None:
            return


        self.event_bus.publish(
            Event(
                category=EventCategory.KERNEL,
                type=event_type,
                source="service_manager",
                payload={
                    "service": payload
                },
            )
        )



    # =================================================
    # REGISTRATION
    # =================================================


    def register(
        self,
        service: KernelService,
        descriptor: Optional[ServiceDescriptor] = None,
    ):

        service_type = type(service)


        if descriptor is None:

            descriptor = ServiceDescriptor(
                name=service.name
            )


        descriptor._registration_order = (
            self._registration_order
        )

        self._registration_order += 1


        name = descriptor.name


        self._services[name] = service

        self._descriptors[name] = descriptor

        self._states[name] = ServiceState.CREATED



        if service_type not in self._type_index:

            self._type_index[service_type] = []


        self._type_index[service_type].append(
            name
        )


        self._emit(
            EventType.SERVICE_REGISTERED,
            name,
        )


        return service



    def unregister(
        self,
        service: KernelService,
    ):


        service_type = type(service)


        names = self._type_index.get(
            service_type,
            []
        )


        if not names:
            return


        name = names[0]


        del self._services[name]

        del self._descriptors[name]

        del self._states[name]


        names.remove(name)


        if not names:

            del self._type_index[service_type]



        self._emit(
            EventType.SERVICE_UNREGISTERED,
            name,
        )



    # =================================================
    # DISCOVERY
    # =================================================


    def get(
        self,
        service_type,
    ):


        names = self._type_index.get(
            service_type,
            []
        )


        if not names:

            return None


        return self._services.get(
            names[0]
        )



    def require(
        self,
        service_type,
    ):


        service = self.get(
            service_type
        )


        if service is None:

            raise ServiceNotFoundError(
                service_type.__name__
            )


        return service



    def get_by_name(
        self,
        name: str,
    ):

        return self._services.get(
            name
        )



    def contains(
        self,
        service_type,
    ):

        return service_type in self._type_index



    def discover(self):

        return tuple(
            self._services.values()
        )



    def all(self):

        return tuple(
            self._services.values()
        )



    def descriptor(
        self,
        service_type,
    ):


        names = self._type_index.get(
            service_type,
            []
        )


        if not names:

            return None


        return self._descriptors.get(
            names[0]
        )



    # =================================================
    # STATE
    # =================================================


    def state(
        self,
        service_type,
    ):


        names = self._type_index.get(
            service_type,
            []
        )


        if not names:

            return ServiceState.CREATED


        return self._states.get(
            names[0],
            ServiceState.CREATED,
        )



    def running_services(self):

        return tuple(
            service
            for name, service in self._services.items()
            if self._states.get(name)
            == ServiceState.RUNNING
        )



    # =================================================
    # LIFECYCLE
    # =================================================


    def start_all(self):


        ordered = sorted(
            self._services.items(),
            key=lambda item:
                self._descriptors[item[0]].priority
        )


        for name, service in ordered:


            descriptor = self._descriptors[name]


            if not descriptor.auto_start:

                continue


            try:

                self._states[name] = (
                    ServiceState.STARTING
                )


                service.start()


                self._states[name] = (
                    ServiceState.RUNNING
                )


            except Exception:


                self._states[name] = (
                    ServiceState.FAILED
                )

                raise



            self._emit(
                EventType.SERVICE_STARTED,
                name,
            )



    def stop_all(self):


        ordered = sorted(
            self._services.items(),
            key=lambda item:
                (
                    -self._descriptors[item[0]].priority,
                    -getattr(
                        self._descriptors[item[0]],
                        "_registration_order",
                        0,
                    ),
                ),
        )


        for name, service in ordered:


            try:

                self._states[name] = (
                    ServiceState.STOPPING
                )


                service.stop()


                self._states[name] = (
                    ServiceState.STOPPED
                )


            except Exception:


                self._states[name] = (
                    ServiceState.FAILED
                )



            self._emit(
                EventType.SERVICE_STOPPED,
                name,
            )



    def tick_all(self):


        for name, service in self._services.items():


            service.tick()


            self._emit(
                EventType.SERVICE_TICKED,
                name,
            )