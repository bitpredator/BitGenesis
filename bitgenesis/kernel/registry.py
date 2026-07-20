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

    Stores services by both type and logical name while
    remaining backward compatible with legacy services.
    """

    def __init__(self):

        self._services: dict[type[KernelService], KernelService] = {}

        self._names: dict[str, KernelService] = {}

    # --------------------------------------------------
    # Compatibility API
    # --------------------------------------------------

    @property
    def services(self):

        return tuple(
            self._services.values()
        )

    # --------------------------------------------------
    # Internal helpers
    # --------------------------------------------------

    @staticmethod
    def _service_name(service) -> str:
        """
        Returns the logical service name.

        Priority:

        1. service.service_name
        2. service.name
        3. ClassName
        """

        return getattr(
            service,
            "service_name",
            getattr(
                service,
                "name",
                type(service).__name__,
            ),
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

        self._names[
            self._service_name(service)
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

            if instance is None:
                return

        else:

            instance = service

            self._services.pop(
                type(service),
                None,
            )

        self._names.pop(
            self._service_name(instance),
            None,
        )

    # --------------------------------------------------
    # Lookup
    # --------------------------------------------------

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

    # --------------------------------------------------
    # Utilities
    # --------------------------------------------------

    def all(self):

        return tuple(
            self._services.values()
        )

    def clear(self):

        self._services.clear()

        self._names.clear()