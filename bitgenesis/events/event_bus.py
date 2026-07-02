from collections import defaultdict
from typing import Callable, Dict, List, Union

from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventCategory, EventType


class EventBus:
    """
    Central event dispatcher.
    """

    def __init__(self):
        self._by_category: Dict[EventCategory, List] = defaultdict(list)
        self._by_type: Dict[EventType, List] = defaultdict(list)

    # -------------------------
    # Subscription
    # -------------------------

    def subscribe(self, key: Union[EventCategory, EventType], subscriber):
        if isinstance(key, EventCategory):
            self._by_category[key].append(subscriber)
        elif isinstance(key, EventType):
            self._by_type[key].append(subscriber)
        else:
            raise TypeError("Invalid subscription key")

    def unsubscribe(self, key: Union[EventCategory, EventType], subscriber):
        if isinstance(key, EventCategory):
            if subscriber in self._by_category[key]:
                self._by_category[key].remove(subscriber)
        elif isinstance(key, EventType):
            if subscriber in self._by_type[key]:
                self._by_type[key].remove(subscriber)

    def clear(self):
        self._by_category.clear()
        self._by_type.clear()

    def subscriber_count(self) -> int:
        return (
            sum(len(v) for v in self._by_category.values()) +
            sum(len(v) for v in self._by_type.values())
        )

    # -------------------------
    # Publish / Emit
    # -------------------------

    def publish(self, event: Event):
        self._dispatch(event)

    def emit(self, event: Event):
        """Alias for compatibility"""
        self._dispatch(event)

    def _dispatch(self, event: Event):
        for sub in self._by_category.get(event.category, []):
            self._call(sub, event)

        for sub in self._by_type.get(event.type, []):
            self._call(sub, event)

    def _call(self, subscriber, event: Event):
        """
        Supports:
        - callable(event)
        - object with handle(event)
        """
        if callable(subscriber):
            subscriber(event)
        elif hasattr(subscriber, "handle"):
            subscriber.handle(event)
        else:
            raise TypeError("Subscriber must be callable or have handle(event)")