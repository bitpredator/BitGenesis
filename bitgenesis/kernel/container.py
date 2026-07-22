from __future__ import annotations


import inspect
from typing import TypeVar


from bitgenesis.kernel.registry import ServiceRegistry
from bitgenesis.kernel.service import KernelService

from bitgenesis.kernel.dependency import (
    MissingDependencyError,
    CircularDependencyError,
)


from bitgenesis.kernel.exceptions import (
    ServiceNotFoundError,
)


T = TypeVar(
    "T"
)



class DependencyContainer:
    """
    Dependency Injection container.

    Supports:

    - instance registration
    - service discovery
    - lookup by type
    - lookup by name
    - automatic dependency resolution
    - singleton lifecycle
    """


    def __init__(self):

        self.registry = ServiceRegistry()

        self._instances = {}



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------


    def register(
        self,
        service: KernelService,
    ):


        self.registry.register(
            service
        )


        self._instances[
            type(service)
        ] = service



    def unregister(
        self,
        service: KernelService,
    ):


        self.registry.unregister(
            service
        )


        self._instances.pop(
            type(service),
            None,
        )



    # --------------------------------------------------
    # Lookup
    # --------------------------------------------------


    def get(
        self,
        service_type: type[T],
    ) -> T | None:


        return self.registry.get(
            service_type
        )



    def require(
        self,
        service_type: type[T],
    ) -> T:


        service = self.get(
            service_type
        )


        if service is None:

            raise ServiceNotFoundError(
                service_type
            )


        return service



    def get_by_name(
        self,
        name: str,
    ):


        return self.registry.get_by_name(
            name
        )



    def contains(
        self,
        service_type,
    ):


        return self.get(
            service_type
        ) is not None



    def discover(self):

        return self.registry.all()



    def all(self):

        return self.discover()



    # --------------------------------------------------
    # Dependency Resolution
    # --------------------------------------------------


    def resolve(
        self,
        service_type: type[T],
    ) -> T:


        return self._resolve(
            service_type,
            []
        )



    def _resolve(
        self,
        service_type,
        stack,
    ):


        if service_type in stack:

            raise CircularDependencyError(
                stack + [
                    service_type
                ]
            )



        #
        # Existing singleton
        #

        if service_type in self._instances:

            return self._instances[
                service_type
            ]



        constructor = inspect.signature(
            service_type.__init__
        )


        dependencies = {}



        for name, parameter in constructor.parameters.items():


            if name == "self":

                continue



            if parameter.kind in (
                inspect.Parameter.VAR_POSITIONAL,
                inspect.Parameter.VAR_KEYWORD,
            ):

                continue



            if parameter.annotation is inspect.Parameter.empty:

                raise MissingDependencyError(
                    name
                )



            dependencies[name] = self._resolve(
                parameter.annotation,
                stack + [
                    service_type
                ]
            )



        instance = service_type(
            **dependencies
        )



        self._instances[
            service_type
        ] = instance



        return instance



    # --------------------------------------------------
    # Maintenance
    # --------------------------------------------------


    def clear(self):

        self.registry.clear()

        self._instances.clear()