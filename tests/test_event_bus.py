from bitgenesis.events.enums import EventCategory, EventType
from bitgenesis.events.event import Event
from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.subscriber import EventSubscriber


class DummySubscriber(EventSubscriber):
    def __init__(self):
        self.received = []

    def handle(self, event: Event) -> None:
        self.received.append(event)


def test_publish_delivers_event():
    bus = EventBus()

    subscriber = DummySubscriber()

    bus.subscribe(
        EventCategory.SYSTEM,
        subscriber,
    )

    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
    )

    bus.publish(event)

    assert len(subscriber.received) == 1
    assert subscriber.received[0] == event


def test_unsubscribe_removes_subscriber():
    bus = EventBus()

    subscriber = DummySubscriber()

    bus.subscribe(
        EventCategory.SYSTEM,
        subscriber,
    )

    bus.unsubscribe(
        EventCategory.SYSTEM,
        subscriber,
    )

    event = Event(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="pytest",
    )

    bus.publish(event)

    assert len(subscriber.received) == 0


def test_subscriber_count():
    bus = EventBus()

    bus.subscribe(
        EventCategory.SYSTEM,
        DummySubscriber(),
    )

    bus.subscribe(
        EventCategory.MEMORY,
        DummySubscriber(),
    )

    assert bus.subscriber_count() == 2


def test_clear_removes_every_subscriber():
    bus = EventBus()

    bus.subscribe(
        EventCategory.SYSTEM,
        DummySubscriber(),
    )

    bus.clear()

    assert bus.subscriber_count() == 0