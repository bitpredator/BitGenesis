from __future__ import annotations


from bitgenesis.runtime.runtime_manager import (
    RuntimeManager,
)

from bitgenesis.runtime.action_registry import (
    ActionRegistry,
)

from bitgenesis.runtime.result import (
    ActionResult,
)

from bitgenesis.events.event_bus import (
    EventBus,
)



print("=== Runtime Manager Functional Test ===")



# --------------------------------------------------
# Event capture
# --------------------------------------------------

events = []


def event_listener(event):

    events.append(event)



bus = EventBus()



# --------------------------------------------------
# Runtime Manager
# --------------------------------------------------

registry = ActionRegistry(
    event_bus=bus,
)


runtime = RuntimeManager(
    registry=registry,
    event_bus=bus,
)



# --------------------------------------------------
# Register test action
# --------------------------------------------------

executed = {
    "value": False,
}



def cognitive_action(
    context,
):

    executed["value"] = True


    return ActionResult.ok(
        action="cognitive_action",
        data={
            "status": "ok",
            "source": "runtime_manager_test",
        },
    )



registry.register(
    "cognitive_action",
    cognitive_action,
)



print(
    "Action registered:",
    registry.all(),
)



# --------------------------------------------------
# Create decision
# --------------------------------------------------

class Decision:

    def __init__(
        self,
        action,
    ):

        self.action = action



decision = Decision(
    "cognitive_action"
)



# --------------------------------------------------
# Planning
# --------------------------------------------------

plan_result = runtime.create_plan(
    decision
)



print(
    "Plan created:",
    plan_result.success,
)



assert plan_result.success is True


assert len(
    plan_result.plan.steps
) == 1



# --------------------------------------------------
# Execution
# --------------------------------------------------

execution_result = runtime.execute(
    plan_result.plan,
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



# --------------------------------------------------
# Decision shortcut
# --------------------------------------------------

shortcut_result = runtime.execute_decision(
    decision
)



assert shortcut_result.success is True



print(
    "execute_decision OK"
)



# --------------------------------------------------
# Final validation
# --------------------------------------------------

print(
    "Events captured:",
    len(events),
)



print(
    "=== Runtime Manager Test OK ==="
)