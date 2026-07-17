from __future__ import annotations

from typing import TypeVar

from bitgenesis.kernel.service import KernelService


T = TypeVar(
    "T",
    bound=KernelService,
)


class ServiceRegistry:
    """
    Registry for Kernel services.

    Supports:
    - registration
    - lookup
    - discovery
    - backward compatibility
    """


    def __init__(self):

        self._services: dict[
            type[KernelService],
            KernelService
        ] = {}


        self._names: dict[
            str,
            KernelService
        ] = {}



    # --------------------------------------------------
    # Compatibility API
    # --------------------------------------------------

    @property
    def services(self):

        return tuple(
            self._services.values()
        )



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    def register(
        self,
        service: KernelService,
    ) -> None:


        self._services[
            type(service)
        ] = service



        name = getattr(
            service,
            "name",
            None,
        )


        if not name:

            name = type(service).__name__



        self._names[
            name
        ] = service



    def unregister(
        self,
        service: KernelService | type[KernelService],
    ) -> None:


        if isinstance(service, type):

            instance = self._services.pop(
                service,
                None,
            )

        else:

            instance = self._services.pop(
                type(service),
                None,
            )


        if instance:

            name = getattr(
                instance,
                "name",
                None,
            )


            if not name:

                name = type(instance).__name__


            self._names.pop(
                name,
                None,
            )



    def get(
        self,
        service_type: type[T],
    ) -> T | None:


        return self._services.get(
            service_type
        )



    def get_by_name(
        self,
        name: str,
    ) -> KernelService | None:


        return self._names.get(
            name
        )



    def all(self):

        return tuple(
            self._services.values()
        )



    def clear(self):

        self._services.clear()

        self._names.clear()