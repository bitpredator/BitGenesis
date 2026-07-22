from bitgenesis.events.factory import EventFactory
from bitgenesis.events.enums import (
    EventCategory,
    EventPriority,
    EventType,
)


def test_create_generic_event():

    event = EventFactory.create(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
        source="test",
        payload={
            "value": 123,
        },
    )


    assert event.category == EventCategory.SYSTEM
    assert event.type == EventType.SYSTEM_STARTED
    assert event.source == "test"
    assert event.payload["value"] == 123



def test_service_registered_event():

    event = EventFactory.service_registered(
        "MemoryService",
    )


    assert event.type == EventType.SERVICE_REGISTERED
    assert event.category == EventCategory.KERNEL
    assert event.payload["service"] == "MemoryService"



def test_service_started_event():

    event = EventFactory.service_started(
        "RuntimeService",
    )


    assert event.type == EventType.SERVICE_STARTED
    assert event.priority == EventPriority.HIGH
    assert event.payload["service"] == "RuntimeService"



def test_service_failed_event():

    event = EventFactory.service_failed(
        "DatabaseService",
        "connection failed",
    )


    assert event.type == EventType.SERVICE_FAILED
    assert event.priority == EventPriority.CRITICAL

    assert (
        event.payload["error"]
        ==
        "connection failed"
    )



def test_service_stopped_event():

    event = EventFactory.service_stopped(
        "MemoryService",
    )


    assert event.type == EventType.SERVICE_STOPPED
    assert event.payload["service"] == "MemoryService"



def test_kernel_initialized_event():

    event = EventFactory.kernel_initialized()


    assert event.type == EventType.KERNEL_INITIALIZED
    assert event.category == EventCategory.KERNEL



def test_kernel_ready_event():

    event = EventFactory.kernel_ready()


    assert event.type == EventType.KERNEL_READY



def test_event_unique_identifier():

    first = EventFactory.create(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
    )

    second = EventFactory.create(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
    )


    assert first.id != second.id



def test_default_payload_is_empty():

    event = EventFactory.create(
        category=EventCategory.SYSTEM,
        type=EventType.SYSTEM_STARTED,
    )


    assert event.payload == {}
    assert event.metadata == {}