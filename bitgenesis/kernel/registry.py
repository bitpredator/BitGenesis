from __future__ import annotations


from typing import Type


from bitgenesis.kernel.exceptions import ServiceNotFoundError
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor
from bitgenesis.kernel.service_entry import ServiceEntry



class ServiceRegistry:
    """
    Registry for Kernel services.

    Supports:
    - multiple instances of the same service type
    - descriptor metadata
    - service discovery
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
                )
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
        service_type: Type[KernelService],
    ) -> KernelService | None:


        entries = self._type_index.get(
            service_type,
            [],
        )


        if not entries:

            return None



        return entries[0].service



    def get_all(
        self,
        service_type: Type[KernelService],
    ) -> tuple[KernelService, ...]:


        return tuple(
            entry.service
            for entry in self._type_index.get(
                service_type,
                [],
            )
        )



    def require(
        self,
        service_type: Type[KernelService],
    ) -> KernelService:


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
        service_type: Type[KernelService],
    ) -> bool:


        return bool(
            self._type_index.get(
                service_type
            )
        )



    def get_by_name(
        self,
        name: str,
    ) -> KernelService | None:


        for entry in self._entries:


            if entry.descriptor.name == name:

                return entry.service



        return None



    # --------------------------------------------------
    # Discovery
    # --------------------------------------------------


    def all(
        self,
    ) -> tuple[KernelService, ...]:


        return tuple(
            entry.service
            for entry in self._entries
        )



    def entries(
        self,
    ) -> tuple[ServiceEntry, ...]:


        return tuple(
            self._entries
        )



    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------


    def descriptor(
        self,
        service_or_type,
    ) -> ServiceDescriptor | None:


        # Support:
        # descriptor(instance)
        # descriptor(ServiceClass)

        if isinstance(
            service_or_type,
            type,
        ):


            entries = self._type_index.get(
                service_or_type,
                [],
            )


            if not entries:

                return None



            return entries[0].descriptor



        else:


            for entry in self._entries:


                if entry.service is service_or_type:

                    return entry.descriptor



        return None



    # --------------------------------------------------
    # Utility
    # --------------------------------------------------


    def clear(
        self,
    ):


        self._entries.clear()

        self._type_index.clear()