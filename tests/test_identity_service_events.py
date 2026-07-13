from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.identity.service import IdentityService


def test_identity_service_emits_initialized_event():

    bus = EventBus()

    received = []

    bus.subscribe(
        EventCategory.IDENTITY,
        received.append,
    )

    service = IdentityService(
        bus
    )

    service.start()

    assert len(received) == 1

    event = received[0]

    assert event.category == EventCategory.IDENTITY

    assert event.type == EventType.IDENTITY_INITIALIZED

    assert event.source == "identity_service"