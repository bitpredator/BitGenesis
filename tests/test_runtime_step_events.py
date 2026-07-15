from dataclasses import dataclass

from bitgenesis.runtime.executor import Executor
from bitgenesis.runtime.action_registry import ActionRegistry

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventType


@dataclass
class Step:

    action: str



class Plan:

    def __init__(self):

        self.steps = [
            Step(
                action="test_action"
            )
        ]



def test_executor_emits_step_events():

    bus = EventBus()

    received = []


    bus.subscribe(
        EventType.STEP_STARTED,
        received.append,
    )

    bus.subscribe(
        EventType.STEP_COMPLETED,
        received.append,
    )


    registry = ActionRegistry()


    registry.register(
        "test_action",
        lambda ctx: DummyResult()
    )


    executor = Executor(
        registry=registry,
        event_bus=bus,
    )


    executor.execute(
        Plan()
    )


    assert len(received) == 2


    assert received[0].type == (
        EventType.STEP_STARTED
    )

    assert received[1].type == (
        EventType.STEP_COMPLETED
    )



class DummyResult:

    success = True