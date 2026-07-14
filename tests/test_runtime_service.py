from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.runtime.service import RuntimeService


def test_runtime_service_starts():

    bus = EventBus()

    service = RuntimeService(
        bus
    )

    service.start()

    assert service.running is True



def test_runtime_service_stops():

    bus = EventBus()

    service = RuntimeService(
        bus
    )

    service.start()
    service.stop()

    assert service.running is False



def test_runtime_service_start_event():

    bus = EventBus()

    received = []

    bus.subscribe(
        EventType.RUNTIME_STARTED,
        received.append,
    )


    service = RuntimeService(
        bus
    )

    service.start()


    assert len(received) == 1

    event = received[0]

    assert event.category == EventCategory.RUNTIME

    assert event.type == EventType.RUNTIME_STARTED



def test_runtime_service_stop_event():

    bus = EventBus()

    received = []

    bus.subscribe(
        EventType.RUNTIME_STOPPED,
        received.append,
    )


    service = RuntimeService(
        bus
    )

    service.start()
    service.stop()


    assert len(received) == 1

    event = received[0]

    assert event.category == EventCategory.RUNTIME

    assert event.type == EventType.RUNTIME_STOPPED



def test_runtime_service_start_is_idempotent():

    bus = EventBus()

    received = []

    bus.subscribe(
        EventType.RUNTIME_STARTED,
        received.append,
    )


    service = RuntimeService(
        bus
    )

    service.start()
    service.start()


    assert service.running is True

    assert len(received) == 1