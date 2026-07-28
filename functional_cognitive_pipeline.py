from __future__ import annotations


from bitgenesis.runtime.action_registry import (
    ActionRegistry,
)

from bitgenesis.runtime.executor import (
    Executor,
)

from bitgenesis.runtime.execution_plan import (
    ExecutionPlan,
)

from bitgenesis.runtime.execution_step import (
    ExecutionStep,
)

from bitgenesis.runtime.action_context import (
    ActionContext,
)

from bitgenesis.runtime.result import (
    ActionResult,
)



print("=== Cognitive Pipeline Functional Test ===")



# --------------------------------------------------
# Test action
# --------------------------------------------------

executed = {
    "value": False,
}



def test_action(
    context: ActionContext,
):

    executed["value"] = True


    return ActionResult.ok(
        action="test_action",
        data={
            "status": "ok",
            "message": "action executed",
        },
    )



# --------------------------------------------------
# Action Registry
# --------------------------------------------------

registry = ActionRegistry()


registry.register(
    "test_action",
    test_action,
)



print(
    "Registered actions:",
    registry.all(),
)


assert registry.contains(
    "test_action"
)



# --------------------------------------------------
# Execution Plan
# --------------------------------------------------

plan = ExecutionPlan()


plan.add(
    ExecutionStep(
        action="test_action",
        payload={
            "value": 123,
        },
        priority=1,
    )
)



print(
    "Plan steps:",
    len(plan.steps),
)


assert plan.empty() is False



# --------------------------------------------------
# Executor
# --------------------------------------------------

executor = Executor(
    registry=registry,
)



result = executor.execute(
    plan,
)



print(
    "Execution success:",
    result.success,
)


print(
    "Actions executed:",
    result.actions_executed,
)



assert result.success is True


assert result.actions_executed == 1


assert executed["value"] is True



action_result = result.results[0]


print(
    "Action result:",
    action_result,
)



assert isinstance(
    action_result,
    ActionResult,
)


assert action_result.action == "test_action"


assert action_result.success is True


assert action_result.data["status"] == "ok"



print(
    "=== Cognitive Pipeline Test OK ==="
)