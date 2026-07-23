from __future__ import annotations

from collections import defaultdict
from typing import Callable

from bitgenesis.events.event import Event


class EventBus:
    """
    Central event dispatcher.

    Supports:

    - publish(Event)
    - publish(EventType, payload)
    - emit(Event)
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

        listeners = self._listeners.get(
            event_type,
            []
        )

        if callback in listeners:

            listeners.remove(
                callback
            )


    # --------------------------------------------------
    # Publish
    # --------------------------------------------------

    def publish(
        self,
        event_or_type,
        payload=None,
    ):
        """
        Publish event.

        Supports:

        publish(Event)

        publish(EventType, payload)
        """


        # ------------------------------
        # Native Event
        # ------------------------------

        if isinstance(
            event_or_type,
            Event,
        ):

            event = event_or_type


        # ------------------------------
        # Compatibility API
        # ------------------------------

        else:

            from bitgenesis.events.enums import EventCategory

            event = Event(
                category=EventCategory.SYSTEM,
                type=event_or_type,
                source="event_bus",
                payload=payload or {},
            )


        targets = []


        # EventType listeners

        targets.extend(
            self._listeners.get(
                event.type,
                []
            )
        )


        # Category listeners

        if event.category:

            targets.extend(
                self._listeners.get(
                    event.category,
                    []
                )
            )


        for callback in list(targets):

            if callable(callback):

                callback(event)

            elif hasattr(
                callback,
                "handle",
            ):

                callback.handle(
                    event
                )


    # --------------------------------------------------
    # Compatibility
    # --------------------------------------------------

    def emit(
        self,
        event_or_type,
        payload=None,
    ):

        return self.publish(
            event_or_type,
            payload,
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