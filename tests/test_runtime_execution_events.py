from bitgenesis.runtime.runtime_manager import RuntimeManager
from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventType


class DummyPlan:
    steps = []


def test_runtime_execution_started_event():

    bus = EventBus()

    received = []

    bus.subscribe(
        EventType.EXECUTION_STARTED,
        received.append,
    )


    manager = RuntimeManager(
        event_bus=bus
    )


    manager.execute(
        DummyPlan()
    )


    assert len(received) == 1

    assert received[0].type == (
        EventType.EXECUTION_STARTED
    )



def test_runtime_execution_completed_event():

    bus = EventBus()

    received = []

    bus.subscribe(
        EventType.EXECUTION_COMPLETED,
        received.append,
    )


    manager = RuntimeManager(
        event_bus=bus
    )


    manager.execute(
        DummyPlan()
    )


    assert len(received) == 1

    assert received[0].type == (
        EventType.EXECUTION_COMPLETED
    )