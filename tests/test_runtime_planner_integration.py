from bitgenesis.runtime.runtime_loop import RuntimeLoop



class FakeDecision:

    def __init__(
        self,
        action,
    ):
        self.action = action



def test_runtime_loop_has_planner():

    loop = RuntimeLoop(
        runtime_manager=None
    )


    assert loop.planner is not None



def test_runtime_loop_creates_execution_plan():

    loop = RuntimeLoop(
        runtime_manager=None
    )


    result = loop.plan(
        FakeDecision(
            "store_memory"
        )
    )


    assert result.success

    assert loop.last_plan is not None


    assert (
        loop.last_plan.steps[0].action
        == "store_memory"
    )