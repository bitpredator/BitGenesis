from bitgenesis.events.enums import EventType


def test_action_lifecycle_events_exist():

    assert EventType.ACTION_STARTED.value == (
        "runtime.action.started"
    )

    assert EventType.ACTION_COMPLETED.value == (
        "runtime.action.completed"
    )

    assert EventType.ACTION_FAILED.value == (
        "runtime.action.failed"
    )


def test_execution_lifecycle_events_exist():

    assert EventType.EXECUTION_STARTED.value == (
        "runtime.execution.started"
    )

    assert EventType.EXECUTION_COMPLETED.value == (
        "runtime.execution.completed"
    )

    assert EventType.EXECUTION_FAILED.value == (
        "runtime.execution.failed"
    )


def test_step_lifecycle_events_exist():

    assert EventType.STEP_STARTED.value == (
        "runtime.step.started"
    )

    assert EventType.STEP_COMPLETED.value == (
        "runtime.step.completed"
    )

    assert EventType.STEP_FAILED.value == (
        "runtime.step.failed"
    )