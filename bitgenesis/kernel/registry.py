from __future__ import annotations

from typing import Type, TypeVar

from bitgenesis.kernel.service import KernelService


T = TypeVar(
    "T",
    bound=KernelService,
)


class ServiceRegistry:
    """
    Registry for Kernel services.
    """

    def __init__(self):

        self._services: dict[type[KernelService], KernelService] = {}


    def register(
        self,
        service: KernelService,
    ) -> None:

        self._services[type(service)] = service


    def unregister(
        self,
        service_type: type[KernelService],
    ) -> None:

        self._services.pop(
            service_type,
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