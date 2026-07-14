from bitgenesis.runtime.result import ActionResult


def test_action_result_success():

    result = ActionResult.ok(
        action="store_memory",
        data={
            "id": "123"
        },
    )

    assert result.success is True
    assert result.action == "store_memory"
    assert result.data["id"] == "123"


def test_action_result_failure():

    result = ActionResult.fail(
        action="store_memory",
        error="memory unavailable",
    )

    assert result.success is False
    assert result.action == "store_memory"
    assert result.error == "memory unavailable"