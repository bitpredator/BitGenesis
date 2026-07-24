from __future__ import annotations

from typing import Dict, Optional, Type

from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor
from bitgenesis.kernel.service_state import ServiceState
from bitgenesis.kernel.exceptions import ServiceNotFoundError

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

        self._type_index: Dict[Type[KernelService], list[str]] = {}

        self._registration_order = 0


    # -------------------------------------------------
    # EVENTS
    # -------------------------------------------------

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
                    "service": payload,
                },
            )
        )


    # -------------------------------------------------
    # REGISTRATION
    # -------------------------------------------------

    def register(
        self,
        service: KernelService,
        descriptor: Optional[ServiceDescriptor] = None,
    ):

        service_type = type(service)

        if descriptor is None:

            descriptor = ServiceDescriptor(
                name=service_type.__name__,
            )


        service_name = descriptor.name


        self._services[service_name] = service

        self._descriptors[service_name] = descriptor

        self._states[service_name] = ServiceState.CREATED


        self._registration_order += 1

        descriptor._registration_order = (
            self._registration_order
        )


        if service_type not in self._type_index:

            self._type_index[service_type] = []


        self._type_index[service_type].append(
            service_name
        )


        self._emit(
            EventType.SERVICE_REGISTERED,
            service_name,
        )


        return service



    def unregister(
        self,
        service: KernelService,
    ):

        service_type = type(service)

        service_names = self._type_index.get(
            service_type,
            [],
        )


        if not service_names:
            return


        service_name = service_names[0]


        descriptor = self._descriptors.get(
            service_name
        )


        del self._services[service_name]

        del self._descriptors[service_name]

        del self._states[service_name]


        self._type_index[service_type].remove(
            service_name
        )


        if not self._type_index[service_type]:

            del self._type_index[service_type]


        self._emit(
            EventType.SERVICE_UNREGISTERED,
            descriptor.name if descriptor else service_name,
        )


    # -------------------------------------------------
    # DISCOVERY
    # -------------------------------------------------

    def get(
        self,
        service_type,
    ):

        services = self._type_index.get(
            service_type,
            [],
        )


        if not services:
            return None


        return self._services.get(
            services[0]
        )


    def get_by_name(
        self,
        name: str,
    ):

        return self._services.get(
            name
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

        services = self._type_index.get(
            service_type,
            [],
        )


        if not services:
            return None


        return self._descriptors.get(
            services[0]
        )


    # -------------------------------------------------
    # STATE
    # -------------------------------------------------

    def state(
        self,
        service_type,
    ):

        services = self._type_index.get(
            service_type,
            [],
        )


        if not services:
            return ServiceState.CREATED


        return self._states.get(
            services[0],
            ServiceState.CREATED,
        )



    def running_services(self):

        return tuple(
            service
            for name, service in self._services.items()
            if self._states.get(name)
            == ServiceState.RUNNING
        )


    # -------------------------------------------------
    # LIFECYCLE
    # -------------------------------------------------

    def start_all(self):

        services = sorted(
            self._services.items(),
            key=lambda item:
                self._descriptors[item[0]].priority,
        )


        for service_name, service in services:

            descriptor = self._descriptors[
                service_name
            ]


            if not descriptor.auto_start:
                continue


            try:

                self._states[
                    service_name
                ] = ServiceState.STARTING


                service.start()


                self._states[
                    service_name
                ] = ServiceState.RUNNING


            except Exception:

                self._states[
                    service_name
                ] = ServiceState.FAILED

                self._emit(
                    EventType.SERVICE_FAILED,
                    descriptor.name,
                )

                raise



            self._emit(
                EventType.SERVICE_STARTED,
                descriptor.name,
            )



    def stop_all(self):

        services = sorted(
            self._services.items(),
            key=lambda item: (
                -self._descriptors[item[0]].priority,
                -getattr(
                    self._descriptors[item[0]],
                    "_registration_order",
                    0,
                ),
            ),
        )


        for service_name, service in services:

            descriptor = self._descriptors[
                service_name
            ]


            try:

                self._states[
                    service_name
                ] = ServiceState.STOPPING


                service.stop()


                self._states[
                    service_name
                ] = ServiceState.STOPPED


            except Exception:

                self._states[
                    service_name
                ] = ServiceState.FAILED



            self._emit(
                EventType.SERVICE_STOPPED,
                descriptor.name,
            )


    # -------------------------------------------------
    # TICK
    # -------------------------------------------------

    def tick_all(self):

        for service_name, service in tuple(
            self._services.items()
        ):

            descriptor = self._descriptors.get(
                service_name
            )


            try:

                service.tick()


                self._emit(
                    EventType.SERVICE_TICKED,
                    descriptor.name
                    if descriptor
                    else service_name,
                )


            except Exception:

                self._states[
                    service_name
                ] = ServiceState.FAILED


                self._emit(
                    EventType.SERVICE_FAILED,
                    descriptor.name
                    if descriptor
                    else service_name,
                )


                raise