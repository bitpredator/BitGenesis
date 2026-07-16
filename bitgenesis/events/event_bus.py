from __future__ import annotations

from collections import defaultdict
from typing import Callable

from bitgenesis.events.event import Event


class EventBus:
    """
    Central event dispatcher.

    Supports:
    - publish(Event)
    - emit(EventType, payload)
    - subscribe()
    - unsubscribe()
    """

    def __init__(self):

        self._listeners = defaultdict(list)


    # --------------------------------------------------
    # Subscribe
    # --------------------------------------------------

    def subscribe(
        self,
        event_type,
        callback: Callable,
    ):

        self._listeners[event_type].append(
            callback
        )


    def unsubscribe(
        self,
        event_type,
        callback,
    ):

        if callback in self._listeners.get(event_type, []):

            self._listeners[event_type].remove(
                callback
            )


    # --------------------------------------------------
    # New API
    # --------------------------------------------------

    def publish(
        self,
        event: Event,
    ):

        targets = []


        targets.extend(
            self._listeners.get(
                event.type,
                []
            )
        )


        targets.extend(
            self._listeners.get(
                event.category,
                []
            )
        )


        for callback in targets:

            if callable(callback):

                callback(event)

            elif hasattr(callback, "handle"):

                callback.handle(event)



    # --------------------------------------------------
    # Compatibility API
    # --------------------------------------------------

    def emit(
        self,
        event_or_type,
        payload=None,
    ):

        # New style:
        # emit(Event(...))

        if isinstance(event_or_type, Event):

            return self.publish(
                event_or_type
            )


        # Old style:
        # emit(EventType.X, payload)

        from bitgenesis.events.enums import EventCategory


        event = Event(
            category=EventCategory.SYSTEM,
            type=event_or_type,
            source="event_bus",
            payload=payload,
        )


        self.publish(
            event
        )


    # --------------------------------------------------
    # Utilities
    # --------------------------------------------------

    def subscriber_count(
        self,
        event_type=None,
    ):

        if event_type:

            return len(
                self._listeners.get(
                    event_type,
                    []
                )
            )


        return sum(
            len(x)
            for x in self._listeners.values()
        )


    def clear(self):

        self._listeners.clear()