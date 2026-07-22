from bitgenesis.kernel.provider import (
    ServiceProvider,
    ProviderRegistry,
)

from bitgenesis.kernel.container import (
    DependencyContainer,
)

from bitgenesis.kernel.service_manager import (
    ServiceManager,
)



class TestProvider(ServiceProvider):


    def __init__(self):

        self.registered = False
        self.booted = False



    def register(
        self,
        container,
    ):

        self.registered = True



    def boot(
        self,
        container,
        manager,
    ):

        self.booted = True



def test_provider_registration():

    registry = ProviderRegistry()

    provider = TestProvider()


    registry.register(
        provider
    )


    registry.boot(
        DependencyContainer(),
        ServiceManager(),
    )


    assert provider.registered is True

    assert provider.booted is True



def test_provider_storage():

    registry = ProviderRegistry()

    provider = TestProvider()


    registry.register(
        provider
    )


    assert registry.all() == (
        provider,
    )