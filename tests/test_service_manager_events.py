from bitgenesis.kernel.service_manager import ServiceManager
from bitgenesis.kernel.service import KernelService

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import EventType


# ======================================================
# Test Services
# ======================================================


class ExampleService(KernelService):

    def __init__(self):
        self.started = False
        self.stopped = False


    def start(self):
        self.started = True


    def stop(self):
        self.stopped = True



# ======================================================
# Helpers
# ======================================================


def create_manager():

    bus = EventBus()

    manager = ServiceManager(
        event_bus=bus,
    )

    return manager, bus



# ======================================================
# Tests
# ======================================================


def test_service_registration_emits_event():

    manager, bus = create_manager()

    received = []


    def listener(event: Event):
        received.append(event)


    bus.subscribe(
        EventType.SERVICE_REGISTERED,
        listener,
    )


    service = ExampleService()


    manager.register(
        service,
    )


    assert len(received) == 1

    assert (
        received[0].type
        == EventType.SERVICE_REGISTERED
    )



def test_service_start_emits_event():

    manager, bus = create_manager()

    received = []


    bus.subscribe(
        EventType.SERVICE_STARTED,
        lambda event:
            received.append(event),
    )


    service = ExampleService()


    manager.register(
        service,
    )


    manager.start_all()


    assert service.started is True

    assert len(received) == 1

    assert (
        received[0].type
        == EventType.SERVICE_STARTED
    )



def test_service_stop_emits_event():

    manager, bus = create_manager()

    received = []


    bus.subscribe(
        EventType.SERVICE_STOPPED,
        lambda event:
            received.append(event),
    )


    service = ExampleService()


    manager.register(
        service,
    )


    manager.stop_all()


    assert service.stopped is True

    assert len(received) == 1

    assert (
        received[0].type
        == EventType.SERVICE_STOPPED
    )



def test_service_tick_emits_event():

    manager, bus = create_manager()

    received = []


    bus.subscribe(
        EventType.SERVICE_TICKED,
        lambda event:
            received.append(event),
    )


    service = ExampleService()


    manager.register(
        service,
    )


    manager.tick_all()


    assert len(received) == 1

    assert (
        received[0].type
        == EventType.SERVICE_TICKED
    )