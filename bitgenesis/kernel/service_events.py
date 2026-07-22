"""
Kernel service lifecycle events.

Provides immutable Event factories for service operations.
"""

from __future__ import annotations

from typing import Any

from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)


class ServiceEvents:
    """
    Factory for kernel service events.
    """

    SOURCE = "kernel.service"


    @staticmethod
    def _payload(
        service,
        **extra: Any,
    ) -> dict[str, Any]:

        return {
            "service": type(service).__name__,
            "name": getattr(
                service,
                "name",
                type(service).__name__,
            ),
            **extra,
        }


    # --------------------------------------------------
    # Registration
    # --------------------------------------------------

    @classmethod
    def registered(
        cls,
        service,
    ) -> Event:

        return Event(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_REGISTERED,
            source=cls.SOURCE,
            payload=cls._payload(
                service
            ),
        )


    @classmethod
    def unregistered(
        cls,
        service,
    ) -> Event:

        return Event(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_UNREGISTERED,
            source=cls.SOURCE,
            payload=cls._payload(
                service
            ),
        )


    # --------------------------------------------------
    # Discovery
    # --------------------------------------------------

    @classmethod
    def discovered(
        cls,
        service,
    ) -> Event:

        return Event(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_DISCOVERED,
            source=cls.SOURCE,
            payload=cls._payload(
                service
            ),
        )


    @classmethod
    def ready(
        cls,
        service,
    ) -> Event:

        return Event(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_READY,
            source=cls.SOURCE,
            payload=cls._payload(
                service
            ),
        )


    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    @classmethod
    def started(
        cls,
        service,
    ) -> Event:

        return Event(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_STARTED,
            source=cls.SOURCE,
            payload=cls._payload(
                service
            ),
        )


    @classmethod
    def stopped(
        cls,
        service,
    ) -> Event:

        return Event(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_STOPPED,
            source=cls.SOURCE,
            payload=cls._payload(
                service
            ),
        )


    @classmethod
    def ticked(
        cls,
        service,
    ) -> Event:

        return Event(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_TICKED,
            source=cls.SOURCE,
            payload=cls._payload(
                service
            ),
        )


    # --------------------------------------------------
    # Errors
    # --------------------------------------------------

    @classmethod
    def failed(
        cls,
        service,
        error: Exception,
    ) -> Event:

        return Event(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_FAILED,
            source=cls.SOURCE,
            payload=cls._payload(
                service,
                error=str(error),
                exception=type(error).__name__,
            ),
        )