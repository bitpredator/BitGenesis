from __future__ import annotations

from typing import Type

from bitgenesis.kernel.service import KernelService



class DependencyResolver:


    def __init__(
        self,
        service_manager,
    ):

        self.service_manager = service_manager

        self._dependencies: dict[
            Type[KernelService],
            list[Type[KernelService]]
        ] = {}



    # =================================================
    # MANUAL DEPENDENCIES
    # =================================================


    def add_dependency(
        self,
        service_type: Type[KernelService],
        dependency_type: Type[KernelService],
    ):

        if service_type not in self._dependencies:

            self._dependencies[service_type] = []


        self._dependencies[service_type].append(
            dependency_type
        )



    # =================================================
    # RESOLUTION
    # =================================================


    def resolve(
        self,
        service_type: Type[KernelService],
    ):


        resolved = []

        visited = set()


        self._resolve(
            service_type,
            resolved,
            visited,
        )


        return resolved



    def _resolve(
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



        dependencies = []



        # -----------------------------
        # Descriptor dependencies
        # -----------------------------

        descriptor = self.service_manager.descriptor(
            service_type
        )


        if descriptor is not None:

            dependencies.extend(
                getattr(
                    descriptor,
                    "dependencies",
                    (),
                )
            )



        # -----------------------------
        # Runtime dependencies
        # -----------------------------

        dependencies.extend(
            self._dependencies.get(
                service_type,
                [],
            )
        )



        # -----------------------------
        # Resolve children
        # -----------------------------

        for dependency in dependencies:

            self._resolve(
                dependency,
                resolved,
                visited,
            )



        # -----------------------------
        # Add service
        # -----------------------------

        service = self.service_manager.get(
            service_type
        )


        if service is not None:

            resolved.append(
                service
            )