from __future__ import annotations

from typing import Type

from bitgenesis.kernel.exceptions import ServiceNotFoundError
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor
from bitgenesis.kernel.service_entry import ServiceEntry


class ServiceRegistry:
    """
    Registry for Kernel services.

    Supports multiple instances of the same service type.
    """


    def __init__(self):

        self._entries: list[ServiceEntry] = []

        self._type_index: dict[
            Type[KernelService],
            list[ServiceEntry],
        ] = {}


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
                name=(
                    getattr(
                        service,
                        "name",
                        None,
                    )
                    or type(service).__name__
                ),
            )


        entry = ServiceEntry(
            service=service,
            descriptor=descriptor,
        )


        self._entries.append(
            entry
        )


        self._type_index.setdefault(
            type(service),
            [],
        ).append(
            entry
        )


    def unregister(
        self,
        service: KernelService,
    ):

        entries = self._type_index.get(
            type(service),
            [],
        )


        for entry in list(entries):

            if entry.service is service:

                entries.remove(
                    entry
                )

                self._entries.remove(
                    entry
                )

                break


        if not entries:

            self._type_index.pop(
                type(service),
                None,
            )


    # --------------------------------------------------
    # Lookup
    # --------------------------------------------------

    def get(
        self,
        service_type,
    ):

        entries = self._type_index.get(
            service_type,
            [],
        )


        if not entries:
            return None


        return entries[0].service



    def get_all(
        self,
        service_type,
    ):

        return tuple(
            entry.service
            for entry in self._type_index.get(
                service_type,
                [],
            )
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
                service_type
            )


        return service



    def contains(
        self,
        service_type,
    ):

        return bool(
            self._type_index.get(
                service_type
            )
        )



    def get_by_name(
        self,
        name: str,
    ):

        for entry in self._entries:

            if entry.descriptor.name == name:
                return entry.service


        return None


    # --------------------------------------------------
    # Discovery
    # --------------------------------------------------

    def all(self):

        return tuple(
            entry.service
            for entry in self._entries
        )



    def entries(self):

        return tuple(
            self._entries
        )



    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    def descriptor(
        self,
        service,
    ):

        for entry in self._entries:

            if entry.service is service:

                return entry.descriptor


        return None



    # --------------------------------------------------
    # Utility
    # --------------------------------------------------

    def clear(self):

        self._entries.clear()

        self._type_index.clear()