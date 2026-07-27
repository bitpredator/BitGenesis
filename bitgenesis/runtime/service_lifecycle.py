from __future__ import annotations


from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.events.event_bus import EventBus



class ServiceLifecycleManager:
    """
    Handles service lifecycle events.

    Responsibilities:

    - emit lifecycle events
    - isolate lifecycle failures
    - provide common lifecycle handling
    """



    def __init__(
        self,
        event_bus: EventBus | None = None,
    ):

        self.event_bus = event_bus



    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def _emit(
        self,
        event_type: EventType,
        service,
        payload: dict | None = None,
    ):

        if self.event_bus is None:
            return


        data = {
            "service": (
                type(service).__name__
            )
        }


        if payload:

            data.update(
                payload
            )


        self.event_bus.emit(
            Event(
                category=EventCategory.RUNTIME,
                type=event_type,
                source="service_lifecycle",
                payload=data,
            )
        )



    # --------------------------------------------------
    # Start lifecycle
    # --------------------------------------------------

    def start(
        self,
        service,
        context,
    ):

        self._emit(
            EventType.SERVICE_STARTING,
            service,
        )


        try:

            start = getattr(
                service,
                "start",
                None,
            )


            if start:

                start(
                    context
                )


            self._emit(
                EventType.SERVICE_STARTED,
                service,
            )


            self._emit(
                EventType.SERVICE_READY,
                service,
            )


            return True



        except Exception as exc:


            self._emit(
                EventType.SERVICE_FAILED,
                service,
                {
                    "error": str(exc),
                    "phase": "start",
                },
            )


            return False



    # --------------------------------------------------
    # Stop lifecycle
    # --------------------------------------------------

    def stop(
        self,
        service,
        context,
    ):

        self._emit(
            EventType.SERVICE_STOPPING,
            service,
        )


        try:

            stop = getattr(
                service,
                "stop",
                None,
            )


            if stop:

                stop(
                    context
                )


            self._emit(
                EventType.SERVICE_STOPPED,
                service,
            )


            return True



        except Exception as exc:


            self._emit(
                EventType.SERVICE_FAILED,
                service,
                {
                    "error": str(exc),
                    "phase": "stop",
                },
            )


            return False