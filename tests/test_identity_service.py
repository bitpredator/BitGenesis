from bitgenesis.events.event_bus import EventBus

from bitgenesis.kernel.kernel import Kernel

from bitgenesis.identity.service import IdentityService


def test_identity_service_can_be_created():

    bus = EventBus()

    service = IdentityService(
        bus
    )

    assert service is not None



def test_identity_service_can_be_registered_in_kernel():

    bus = EventBus()

    kernel = Kernel(bus)

    service = IdentityService(
        bus
    )

    kernel.register(
        service
    )

    assert service in kernel.services



def test_identity_service_starts_with_kernel():

    bus = EventBus()

    kernel = Kernel(bus)

    service = IdentityService(
        bus
    )

    kernel.register(
        service
    )

    kernel.start()

    assert service.running is True



def test_identity_service_stops_with_kernel():

    bus = EventBus()

    kernel = Kernel(bus)

    service = IdentityService(
        bus
    )

    kernel.register(
        service
    )

    kernel.start()

    kernel.stop()

    assert service.running is False



def test_identity_service_exposes_identity_manager():

    bus = EventBus()

    service = IdentityService(
        bus
    )

    assert service.manager is not None
    
    
def test_identity_service_exposes_persistent_identity():

    service = IdentityService(
        event_bus=EventBus()
    )

    assert service.identity.name == "BitGenesis"
    assert service.identity.version == "0.2.0"    