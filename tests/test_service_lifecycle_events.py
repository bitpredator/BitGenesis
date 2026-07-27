from __future__ import annotations


from bitgenesis.runtime.service_lifecycle import (
    ServiceLifecycleManager,
)

from bitgenesis.events.enums import (
    EventType,
)



class DummyService:
    """
    Simple lifecycle test service.
    """

    def __init__(self):

        self.started = False
        self.stopped = False



    def start(
        self,
        context,
    ):

        self.started = True



    def stop(
        self,
        context,
    ):

        self.stopped = True





class FailingService:
    """
    Service that fails during start.
    """

    def start(
        self,
        context,
    ):

        raise RuntimeError(
            "startup failed"
        )





class FakeEventBus:
    """
    Captures emitted events.
    """

    def __init__(self):

        self.events = []



    def emit(
        self,
        event,
    ):

        self.events.append(
            event
        )





def test_service_start_lifecycle_events():

    bus = FakeEventBus()

    lifecycle = ServiceLifecycleManager(
        event_bus=bus
    )


    service = DummyService()


    result = lifecycle.start(
        service,
        None,
    )


    assert result is True

    assert service.started is True


    types = [
        event.type
        for event in bus.events
    ]


    assert EventType.SERVICE_STARTING in types

    assert EventType.SERVICE_STARTED in types

    assert EventType.SERVICE_READY in types





def test_service_stop_lifecycle_events():

    bus = FakeEventBus()

    lifecycle = ServiceLifecycleManager(
        event_bus=bus
    )


    service = DummyService()


    result = lifecycle.stop(
        service,
        None,
    )


    assert result is True

    assert service.stopped is True


    types = [
        event.type
        for event in bus.events
    ]


    assert EventType.SERVICE_STOPPING in types

    assert EventType.SERVICE_STOPPED in types





def test_service_failure_emits_failed_event():

    bus = FakeEventBus()

    lifecycle = ServiceLifecycleManager(
        event_bus=bus
    )


    service = FailingService()


    result = lifecycle.start(
        service,
        None,
    )


    assert result is False


    types = [
        event.type
        for event in bus.events
    ]


    assert EventType.SERVICE_FAILED in types