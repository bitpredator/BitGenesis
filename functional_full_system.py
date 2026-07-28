from __future__ import annotations

import time


from bitgenesis.kernel.kernel import Kernel
from bitgenesis.kernel.service import KernelService


from bitgenesis.runtime.runtime_manager import RuntimeManager
from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.result import ActionResult


from bitgenesis.events.event_bus import EventBus



print("=== BitGenesis Full System Functional Test ===")



# ==================================================
# Event capture
# ==================================================

captured_events = []


def capture_event(event):

    captured_events.append(
        event
    )



# ==================================================
# Test Service
# ==================================================

class FullSystemService(KernelService):

    def __init__(self):

        super().__init__(
            "full_system_service"
        )

        self.ticks = 0



    def tick(self):

        self.ticks += 1



# ==================================================
# Kernel boot
# ==================================================

bus = EventBus()


bus.subscribe(
    object,
    capture_event,
)


kernel = Kernel(
    bus=bus,
)


service = FullSystemService()



kernel.register(
    service
)



print(
    "Kernel service registered"
)



kernel.start()



assert kernel.running is True


assert kernel.brain is not None


print(
    "Kernel started"
)



# ==================================================
# RuntimeLoop validation
# ==================================================

time.sleep(
    0.3
)



assert kernel.runtime_loop.tick_count > 0


assert service.ticks > 0



print(
    "RuntimeLoop ticks:",
    kernel.runtime_loop.tick_count,
)



print(
    "Service ticks:",
    service.ticks,
)



# ==================================================
# RuntimeManager
# ==================================================

registry = ActionRegistry(
    event_bus=bus,
)



runtime = RuntimeManager(
    registry=registry,
    event_bus=bus,
)



executed = {
    "value": False,
}



def full_action(context):

    executed["value"] = True


    return ActionResult.ok(
        action="full_action",
        data={
            "status": "complete",
        },
    )



registry.register(
    "full_action",
    full_action,
)



print(
    "Runtime action registered"
)



# ==================================================
# Cognitive decision
# ==================================================

class Decision:

    def __init__(
        self,
        action,
    ):

        self.action = action



decision = Decision(
    "full_action"
)



plan_result = runtime.create_plan(
    decision
)



assert plan_result.success is True


print(
    "Plan generated"
)



execution = runtime.execute_decision(
    decision
)



assert execution.success is True


assert execution.actions_executed == 1


assert executed["value"] is True



print(
    "Cognitive execution completed"
)



# ==================================================
# Shutdown
# ==================================================

kernel.stop()



assert kernel.running is False



print(
    "Kernel stopped"
)



print(
    "Events captured:",
    len(captured_events),
)



print(
    "=== BitGenesis Full System Test OK ==="
)