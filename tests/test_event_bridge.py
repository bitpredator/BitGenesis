from bitgenesis.kernel.event_bridge import EventBridge
from bitgenesis.events.bus import EventBus
from bitgenesis.events.enums import (
    EventType,
    EventCategory,
)


class FakeService:
    """
    Simple test service.
    """

    name = "FakeService"



def test_bridge_creation():

    bus = EventBus()

    bridge = EventBridge(
        bus
    )

    assert bridge.event_bus is bus



def test_publish_service_registered_event():

    bus = EventBus()

    received = []


    bus.subscribe(
        EventType.SERVICE_REGISTERED,
        lambda event: received.append(event),
    )


    bridge = EventBridge(
        bus
    )


    bridge.service_registered(
        FakeService()
    )


    assert len(received) == 1

    event = received[0]

    assert (
        event.type
        ==
        EventType.SERVICE_REGISTERED
    )

    assert (
        event.category
        ==
        EventCategory.KERNEL
    )

    assert (
        event.payload["service"]
        ==
        "FakeService"
    )



def test_publish_service_started_event():

    bus = EventBus()

    received = []


    bus.subscribe(
        EventType.SERVICE_STARTED,
        lambda event: received.append(event),
    )


    bridge = EventBridge(
        bus
    )


    bridge.service_started(
        FakeService()
    )


    assert len(received) == 1

    assert (
        received[0].type
        ==
        EventType.SERVICE_STARTED
    )



def test_publish_service_stopped_event():

    bus = EventBus()

    received = []


    bus.subscribe(
        EventType.SERVICE_STOPPED,
        lambda event: received.append(event),
    )


    bridge = EventBridge(
        bus
    )


    bridge.service_stopped(
        FakeService()
    )


    assert len(received) == 1

    assert (
        received[0].type
        ==
        EventType.SERVICE_STOPPED
    )



def test_bridge_without_listener_does_not_fail():

    bus = EventBus()

    bridge = EventBridge(
        bus
    )


    bridge.service_registered(
        FakeService()
    )


    bridge.service_started(
        FakeService()
    )


    bridge.service_stopped(
        FakeService()
    )