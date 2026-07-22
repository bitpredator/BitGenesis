from __future__ import annotations


from abc import ABC, abstractmethod


from bitgenesis.kernel.container import DependencyContainer
from bitgenesis.kernel.service_manager import ServiceManager



class ServiceProvider(ABC):
    """
    Base class for service providers.

    A provider is responsible for:

    - registering dependencies
    - bootstrapping services
    - extending the kernel
    """


    @abstractmethod
    def register(
        self,
        container: DependencyContainer,
    ) -> None:
        """
        Register services and dependencies.
        """

        raise NotImplementedError



    def boot(
        self,
        container: DependencyContainer,
        manager: ServiceManager,
    ) -> None:
        """
        Optional boot phase.

        Executed after all providers
        have registered their services.
        """

        pass
    
class ProviderRegistry:
    """
    Stores and manages service providers.
    """


    def __init__(self):

        self._providers: list[ServiceProvider] = []



    def register(
        self,
        provider: ServiceProvider,
    ) -> None:

        self._providers.append(
            provider
        )



    def boot(
        self,
        container: DependencyContainer,
        manager: ServiceManager,
    ) -> None:


        #
        # Registration phase
        #

        for provider in self._providers:

            provider.register(
                container
            )


        #
        # Boot phase
        #

        for provider in self._providers:

            provider.boot(
                container,
                manager,
            )



    def all(self):

        return tuple(
            self._providers
        )



    def clear(self):

        self._providers.clear()    