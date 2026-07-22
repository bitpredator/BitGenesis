"""
Kernel event bridge.

Connects kernel components with the EventBus.
"""

from __future__ import annotations


from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.factory import EventFactory



class EventBridge:
    """
    Bridge between kernel lifecycle
    and internal event system.
    """


    def __init__(
        self,
        event_bus: EventBus,
    ):

        self.event_bus = event_bus



    # --------------------------------------------------
    # Service lifecycle events
    # --------------------------------------------------


    def service_registered(
        self,
        service,
    ):

        event = EventFactory.service_registered(
            self._service_name(service)
        )

        self.event_bus.publish(
            event
        )



    def service_started(
        self,
        service,
    ):

        event = EventFactory.service_started(
            self._service_name(service)
        )

        self.event_bus.publish(
            event
        )



    def service_stopped(
        self,
        service,
    ):

        event = EventFactory.service_stopped(
            self._service_name(service)
        )

        self.event_bus.publish(
            event
        )



    def service_failed(
        self,
        service,
        error: str,
    ):

        event = EventFactory.service_failed(
            self._service_name(service),
            error,
        )

        self.event_bus.publish(
            event
        )



    # --------------------------------------------------
    # Helpers
    # --------------------------------------------------


    @staticmethod
    def _service_name(
        service,
    ):

        return (
            getattr(
                service,
                "name",
                None,
            )
            or type(service).__name__
        )