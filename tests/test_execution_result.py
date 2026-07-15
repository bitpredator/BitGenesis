from datetime import datetime

from bitgenesis.runtime.execution_result import (
    ExecutionResult,
)

from bitgenesis.runtime.result import (
    ActionResult,
)


def test_execution_result_success():

    action_result = ActionResult.ok(
        action="store_memory",
        data={
            "id": "123"
        },
    )


    result = ExecutionResult(
        success=True,
        results=[
            action_result
        ],
        actions_executed=1,
        started_at=datetime.now(),
        finished_at=datetime.now(),
        duration_ms=1.5,
    )


    assert result.success is True

    assert result.actions_executed == 1

    assert result.duration_ms >= 0

    assert result.started_at is not None

    assert result.finished_at is not None

    assert len(result.results) == 1

    assert result.results[0].action == "store_memory"

    assert result.successful_actions == 1

    assert result.failed_actions == 0



def test_execution_result_failed_actions():

    failed_action = ActionResult.fail(
        action="query_knowledge",
        error="Knowledge graph unavailable",
    )


    result = ExecutionResult(
        success=False,
        results=[
            failed_action
        ],
        actions_executed=1,
    )


    assert result.success is False

    assert result.actions_executed == 1

    assert result.failed_actions == 1

    assert result.successful_actions == 0

    assert result.results[0].error == (
        "Knowledge graph unavailable"
    )