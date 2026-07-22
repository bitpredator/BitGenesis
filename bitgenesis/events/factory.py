"""
Event factory utilities.

Centralized event creation for the BitGenesis event system.
"""

from __future__ import annotations

from typing import Any

from .event import Event
from .enums import (
    EventCategory,
    EventPriority,
    EventType,
)



class EventFactory:
    """
    Creates standardized BitGenesis events.
    """

    SOURCE = "bitgenesis"



    # ======================================================
    # Generic
    # ======================================================


    @staticmethod
    def create(
        *,
        category: EventCategory,
        type: EventType,
        source: str = SOURCE,
        payload: dict[str, Any] | None = None,
        metadata: dict[str, Any] | None = None,
        priority: EventPriority = EventPriority.NORMAL,
    ) -> Event:
        """
        Create a generic event.
        """

        return Event(
            category=category,
            type=type,
            source=source,
            payload=payload or {},
            metadata=metadata or {},
            priority=priority,
        )



    # ======================================================
    # Service lifecycle
    # ======================================================


    @classmethod
    def service_registered(
        cls,
        service_name: str,
        *,
        source: str = "service_manager",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_REGISTERED,
            source=source,
            payload={
                "service": service_name,
            },
        )



    @classmethod
    def service_unregistered(
        cls,
        service_name: str,
        *,
        source: str = "service_manager",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_UNREGISTERED,
            source=source,
            payload={
                "service": service_name,
            },
        )



    @classmethod
    def service_discovered(
        cls,
        service_name: str,
        *,
        source: str = "service_manager",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_DISCOVERED,
            source=source,
            payload={
                "service": service_name,
            },
        )



    @classmethod
    def service_started(
        cls,
        service_name: str,
        *,
        source: str = "service_manager",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_STARTED,
            source=source,
            payload={
                "service": service_name,
            },
            priority=EventPriority.HIGH,
        )



    @classmethod
    def service_stopped(
        cls,
        service_name: str,
        *,
        source: str = "service_manager",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_STOPPED,
            source=source,
            payload={
                "service": service_name,
            },
            priority=EventPriority.HIGH,
        )



    @classmethod
    def service_failed(
        cls,
        service_name: str,
        error: str,
        *,
        source: str = "service_manager",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.SERVICE_FAILED,
            source=source,
            payload={
                "service": service_name,
                "error": error,
            },
            priority=EventPriority.CRITICAL,
        )



    @classmethod
    def service_ticked(
        cls,
        service_name: str,
        *,
        source: str = "service_manager",
    ) -> Event:

        return cls.create(
            category=EventCategory.RUNTIME,
            type=EventType.SERVICE_TICKED,
            source=source,
            payload={
                "service": service_name,
            },
        )



    # ======================================================
    # Kernel lifecycle
    # ======================================================


    @classmethod
    def kernel_initialized(
        cls,
        *,
        source: str = "kernel",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.KERNEL_INITIALIZED,
            source=source,
            priority=EventPriority.HIGH,
        )



    @classmethod
    def kernel_ready(
        cls,
        *,
        source: str = "kernel",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.KERNEL_READY,
            source=source,
            priority=EventPriority.HIGH,
        )



    @classmethod
    def kernel_shutdown(
        cls,
        *,
        source: str = "kernel",
    ) -> Event:

        return cls.create(
            category=EventCategory.KERNEL,
            type=EventType.KERNEL_SHUTDOWN,
            source=source,
            priority=EventPriority.HIGH,
        )