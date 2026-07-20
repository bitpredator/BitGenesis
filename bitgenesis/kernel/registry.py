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
    - multiple instances of the same service type
    - lookup by type
    - lookup by logical name
    - backward compatibility
    """


    def __init__(self):

        self._services: list[KernelService] = []

        self._names: dict[str, KernelService] = {}


    # --------------------------------------------------
    # Compatibility API
    # --------------------------------------------------

    @property
    def services(self):

        return tuple(
            self._services
        )


    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------

    @staticmethod
    def _service_name(
        service,
    ) -> str:

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


        if service not in self._services:

            self._services.append(
                service
            )


        self._names[
            self._service_name(service)
        ] = service



    def unregister(
        self,
        service: KernelService | type[KernelService],
    ) -> None:


        if isinstance(
            service,
            type,
        ):

            matches = [
                item
                for item in self._services
                if isinstance(
                    item,
                    service,
                )
            ]

            for item in matches:

                self.unregister(
                    item
                )

            return



        if service in self._services:

            self._services.remove(
                service
            )


        self._names.pop(
            self._service_name(service),
            None,
        )



    # --------------------------------------------------
    # Lookup
    # --------------------------------------------------

    def get(
        self,
        service_type: type[T],
    ) -> T | None:


        for service in self._services:

            if isinstance(
                service,
                service_type,
            ):

                return service


        return None



    def get_all(
        self,
        service_type: type[T],
    ) -> tuple[T, ...]:

        return tuple(
            service
            for service in self._services
            if isinstance(
                service,
                service_type,
            )
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
            self._services
        )



    def clear(self):

        self._services.clear()

        self._names.clear()