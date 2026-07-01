"""
Core EventBus implementation.
"""

from collections import defaultdict

from .enums import EventCategory
from .event import Event
from .subscriber import EventSubscriber


class EventBus:
    """
    Central publish/subscribe event bus.

    The EventBus is responsible only for distributing events to
    registered subscribers.
    """

    def __init__(self) -> None:
        self._subscribers: dict[
            EventCategory,
            list[EventSubscriber],
        ] = defaultdict(list)

    def subscribe(
        self,
        category: EventCategory,
        subscriber: EventSubscriber,
    ) -> None:
        """
        Register a subscriber for a specific event category.
        """
        self._subscribers[category].append(subscriber)

    def unsubscribe(
        self,
        category: EventCategory,
        subscriber: EventSubscriber,
    ) -> None:
        """
        Remove a subscriber.
        """
        if subscriber in self._subscribers[category]:
            self._subscribers[category].remove(subscriber)

    def publish(self, event: Event) -> None:
        """
        Publish an event to all subscribers.
        """
        for subscriber in self._subscribers[event.category]:
            subscriber.handle(event)

    def clear(self) -> None:
        """
        Remove all subscribers.
        """
        self._subscribers.clear()

    def subscriber_count(self) -> int:
        """
        Return the total number of registered subscribers.
        """
        return sum(
            len(subscribers)
            for subscribers in self._subscribers.values()
        )