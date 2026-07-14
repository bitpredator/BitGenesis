from bitgenesis.kernel.bootstrap import bootstrap

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventType


def test_bootstrap_emits_kernel_events():

    bus = EventBus()

    received = []


    def listener(event):

        received.append(event)


    bus.subscribe(
        EventType.KERNEL_INITIALIZED,
        listener,
    )

    bus.subscribe(
        EventType.SYSTEM_STARTED,
        listener,
    )


    bootstrap(
        bus=bus
    )


    types = [
        event.type
        for event in received
    ]


    assert EventType.KERNEL_INITIALIZED in types

    assert EventType.SYSTEM_STARTED in types