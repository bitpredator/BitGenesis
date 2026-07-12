from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)
from bitgenesis.events.event import Event


def test_identity_event_category_exists():

    assert EventCategory.IDENTITY.value == "identity"



def test_identity_event_types_exist():

    assert (
        EventType.IDENTITY_INITIALIZED.value
        == "identity.initialized"
    )

    assert (
        EventType.IDENTITY_UPDATED.value
        == "identity.updated"
    )

    assert (
        EventType.IDENTITY_LOADED.value
        == "identity.loaded"
    )



def test_identity_event_can_be_published():

    bus = EventBus()

    received = []


    def listener(event):

        received.append(event)


    bus.subscribe(
        EventCategory.IDENTITY,
        listener,
    )


    event = Event(
        category=EventCategory.IDENTITY,
        type=EventType.IDENTITY_INITIALIZED,
        source="identity_service",
        payload={
            "status": "ready"
        },
    )


    bus.publish(event)


    assert len(received) == 1

    assert received[0] == event



def test_identity_update_event_routing():

    bus = EventBus()

    received = []


    bus.subscribe(
        EventType.IDENTITY_UPDATED,
        received.append,
    )


    event = Event(
        category=EventCategory.IDENTITY,
        type=EventType.IDENTITY_UPDATED,
        source="identity_service",
        payload={
            "field": "name"
        },
    )


    bus.emit(event)


    assert received == [event]