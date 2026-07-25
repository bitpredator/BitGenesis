from bitgenesis.runtime.execution_plan import ExecutionPlan
from bitgenesis.runtime.execution_step import ExecutionStep



def test_execution_plan_starts_empty():

    plan = ExecutionPlan()

    assert plan.empty()

    assert plan.steps == []



def test_execution_plan_add_step():

    plan = ExecutionPlan()


    step = ExecutionStep(
        action="remember",
    )


    plan.add(
        step
    )


    assert not plan.empty()

    assert len(
        plan.steps
    ) == 1


    assert (
        plan.steps[0].action
        == "remember"
    )



def test_execution_plan_orders_steps_by_priority():

    plan = ExecutionPlan()


    first = ExecutionStep(
        action="low",
        priority=100,
    )


    second = ExecutionStep(
        action="high",
        priority=10,
    )


    plan.add(first)
    plan.add(second)


    ordered = plan.ordered_steps()


    assert ordered == [
        second,
        first,
    ]



def test_execution_plan_has_identifier():

    plan = ExecutionPlan()


    assert plan.id is not None

    assert isinstance(
        plan.id,
        str,
    )