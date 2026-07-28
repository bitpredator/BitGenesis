from __future__ import annotations


from bitgenesis.runtime.planner import (
    CognitiveExecutionPlanner,
)

from bitgenesis.runtime.action_registry import (
    ActionRegistry,
)

from bitgenesis.runtime.executor import (
    Executor,
)

from bitgenesis.runtime.result import (
    ActionResult,
)



print("=== Cognitive Planner Functional Test ===")



# --------------------------------------------------
# Fake decision
# --------------------------------------------------

class TestDecision:

    def __init__(
        self,
        action: str,
    ):

        self.action = action



# --------------------------------------------------
# Planner
# --------------------------------------------------

planner = CognitiveExecutionPlanner()


decision = TestDecision(
    "test_action"
)


planner_result = planner.create_plan(
    decision
)



print(
    "Planner success:",
    planner_result.success,
)


print(
    "Generated steps:",
    len(
        planner_result.plan.steps
    ),
)



assert planner_result.success is True


assert len(
    planner_result.plan.steps
) == 1



assert (
    planner_result.plan.steps[0].action
    == "test_action"
)



# --------------------------------------------------
# Runtime execution
# --------------------------------------------------

executed = {
    "value": False
}



def test_action(context):

    executed["value"] = True


    return ActionResult.ok(
        action="test_action",
        data={
            "message": "planner execution ok",
        },
    )



registry = ActionRegistry()


registry.register(
    "test_action",
    test_action,
)



executor = Executor(
    registry=registry,
)



execution_result = executor.execute(
    planner_result.plan,
    decision=decision,
)



print(
    "Execution success:",
    execution_result.success,
)


print(
    "Actions executed:",
    execution_result.actions_executed,
)



assert execution_result.success is True


assert execution_result.actions_executed == 1


assert executed["value"] is True



print(
    "=== Cognitive Planner Test OK ==="
)