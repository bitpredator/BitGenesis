from dataclasses import dataclass

from bitgenesis.runtime.action_registry import ActionRegistry

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventType



class DummyAction:

    def execute(self, context):

        return DummyResult()



class DummyResult:

    success = True



@dataclass
class Context:

    value: str = "test"



def test_action_registry_emits_action_events():

    bus = EventBus()

    received = []


    bus.subscribe(
        EventType.ACTION_STARTED,
        received.append,
    )

    bus.subscribe(
        EventType.ACTION_COMPLETED,
        received.append,
    )


    registry = ActionRegistry(
        event_bus=bus
    )


    registry.register(
        "dummy",
        DummyAction,
    )


    registry.execute(
        "dummy",
        Context(),
    )


    assert len(received) == 2


    assert received[0].type == (
        EventType.ACTION_STARTED
    )

    assert received[1].type == (
        EventType.ACTION_COMPLETED
    )



def test_action_registry_emits_failure_event():

    bus = EventBus()

    received = []


    bus.subscribe(
        EventType.ACTION_FAILED,
        received.append,
    )


    class BrokenAction:

        def execute(self, context):

            raise RuntimeError(
                "boom"
            )


    registry = ActionRegistry(
        event_bus=bus
    )


    registry.register(
        "broken",
        BrokenAction,
    )


    try:

        registry.execute(
            "broken",
            Context(),
        )

    except RuntimeError:
        pass


    assert len(received) == 1

    assert received[0].type == (
        EventType.ACTION_FAILED
    )