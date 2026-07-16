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

    Stores and manages kernel-level services.
    Provides backward compatible access through
    the services property.
    """


    def __init__(self):

        self._services: dict[type[KernelService], KernelService] = {}


    # --------------------------------------------------
    # Compatibility API
    # --------------------------------------------------

    @property
    def services(self):
        """
        Backward compatible service collection access.

        Allows:
            registry.services

        while keeping internal storage private.
        """

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

        self._services[type(service)] = service


    def unregister(
        self,
        service: KernelService | type[KernelService],
    ) -> None:

        if isinstance(service, type):

            self._services.pop(
                service,
                None,
            )

        else:

            self._services.pop(
                type(service),
                None,
            )


    def get(
        self,
        service_type: type[T],
    ) -> T | None:

        return self._services.get(
            service_type
        )


    def all(self):

        return tuple(
            self._services.values()
        )


    def clear(self):

        self._services.clear()