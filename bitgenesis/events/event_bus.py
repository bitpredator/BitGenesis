"""
Core EventBus implementation.
"""

from collections import defaultdict
from collections.abc import Callable

from .enums import EventCategory
from .event import Event


class EventBus:
    """
    Central publish/subscribe event bus.

    The EventBus is responsible only for distributing events to
    registered subscribers. It does not contain business logic,
    persistence, or event processing.
    """

    def __init__(self) -> None:
        self._subscribers: dict[
            EventCategory,
            list[Callable[[Event], None]]
        ] = defaultdict(list)

    def subscribe(
        self,
        category: EventCategory,
        callback: Callable[[Event], None],
    ) -> None:
        """
        Register a subscriber for a specific event category.
        """
        self._subscribers[category].append(callback)

    def unsubscribe(
        self,
        category: EventCategory,
        callback: Callable[[Event], None],
    ) -> None:
        """
        Remove a previously registered subscriber.
        """
        if callback in self._subscribers[category]:
            self._subscribers[category].remove(callback)

    def publish(self, event: Event) -> None:
        """
        Publish an event to all subscribers of its category.
        """
        for callback in self._subscribers[event.category]:
            callback(event)

    def clear(self) -> None:
        """
        Remove every registered subscriber.
        """
        self._subscribers.clear()

    def subscriber_count(self) -> int:
        """
        Return the total number of registered subscribers.
        """
        return sum(
            len(callbacks)
            for callbacks in self._subscribers.values()
        )