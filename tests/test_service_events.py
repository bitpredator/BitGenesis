from bitgenesis.events.event import Event
from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)
from bitgenesis.kernel.kernel import Kernel
from bitgenesis.kernel.service import KernelService


class DummyService(KernelService):

    def start(self):
        pass

    def stop(self):
        pass

    def tick(self):
        pass


def test_service_registered_event():

    bus = EventBus()

    received = []

    bus.subscribe(
        EventType.SERVICE_REGISTERED,
        received.append,
    )

    kernel = Kernel(bus)

    service = DummyService()

    kernel.register(service)

    assert len(received) == 1

    event = received[0]

    assert event.category == EventCategory.KERNEL
    assert event.type == EventType.SERVICE_REGISTERED
    assert event.payload["service"] == "DummyService"


def test_service_unregistered_event():

    bus = EventBus()

    received = []

    bus.subscribe(
        EventType.SERVICE_UNREGISTERED,
        received.append,
    )

    kernel = Kernel(bus)

    service = DummyService()

    kernel.register(service)

    kernel.unregister(service)

    assert len(received) == 1

    event = received[0]

    assert event.category == EventCategory.KERNEL
    assert event.type == EventType.SERVICE_UNREGISTERED
    assert event.payload["service"] == "DummyService"