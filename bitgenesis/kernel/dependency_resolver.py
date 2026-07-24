from __future__ import annotations

from typing import Dict, Type

from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.exceptions import ServiceNotFoundError


class DependencyResolver:
    """
    Resolves dependencies between kernel services.

    This component builds the dependency order
    required for service initialization.
    """


    def __init__(
        self,
        service_manager,
    ):

        self.service_manager = service_manager

        self._dependencies: Dict[
            Type[KernelService],
            list[Type[KernelService]]
        ] = {}



    # -------------------------------------------------
    # REGISTRATION
    # -------------------------------------------------

    def add_dependency(
        self,
        service_type: Type[KernelService],
        dependency_type: Type[KernelService],
    ):

        if service_type not in self._dependencies:

            self._dependencies[service_type] = []


        self._dependencies[
            service_type
        ].append(
            dependency_type
        )



    # -------------------------------------------------
    # RESOLUTION
    # -------------------------------------------------

    def resolve(
        self,
        service_type: Type[KernelService],
    ):

        if not self.service_manager.contains(
            service_type
        ):
            raise ServiceNotFoundError(
                service_type.__name__
            )


        resolved = []

        visited = set()


        self._resolve_recursive(
            service_type,
            resolved,
            visited,
        )


        return resolved



    def _resolve_recursive(
        self,
        service_type,
        resolved,
        visited,
    ):

        if service_type in visited:
            return


        visited.add(
            service_type
        )


        dependencies = self._dependencies.get(
            service_type,
            []
        )


        for dependency in dependencies:

            self._resolve_recursive(
                dependency,
                resolved,
                visited,
            )


        service = self.service_manager.get(
            service_type
        )


        if service is not None:

            resolved.append(
                service
            )



    # -------------------------------------------------
    # BULK RESOLUTION
    # -------------------------------------------------

    def resolve_all(self):

        result = []

        visited = set()


        for service_type in self._dependencies:

            self._resolve_recursive(
                service_type,
                result,
                visited,
            )


        return result