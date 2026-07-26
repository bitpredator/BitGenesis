from bitgenesis.runtime.runtime_manager import RuntimeManager


class Decision:

    action = "noop"



def test_runtime_manager_creates_execution_plan():

    runtime = RuntimeManager()


    result = runtime.create_plan(
        Decision()
    )


    assert result.success
    assert len(
        result.plan.steps
    ) == 1



def test_runtime_manager_executes_decision():

    runtime = RuntimeManager()


    result = runtime.execute_decision(
        Decision()
    )


    assert result is not None