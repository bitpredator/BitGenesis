from __future__ import annotations

from datetime import datetime

from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.action_context import ActionContext
from bitgenesis.runtime.execution_result import ExecutionResult
from bitgenesis.runtime.result import ActionResult

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.runtime.actions.bootstrap import (
    register_default_actions,
)



class Executor:
    """
    Executes runtime plans.

    Executor responsibility:
    - execute plan steps
    - emit step lifecycle events

    Action lifecycle belongs to ActionRegistry.
    Execution lifecycle belongs to RuntimeManager.
    """


    def __init__(
        self,
        memory_store=None,
        graph=None,
        registry: ActionRegistry | None = None,
        event_bus: EventBus | None = None,
    ):

        self.memory_store = memory_store
        self.graph = graph
        self.event_bus = event_bus


        if registry is None:

            self.registry = ActionRegistry(
                event_bus=self.event_bus
            )

            register_default_actions(
                self.registry
            )

        else:

            self.registry = registry



    # --------------------------------------------------
    # Events
    # --------------------------------------------------

    def _emit(
        self,
        event_type,
        payload,
    ):

        if not self.event_bus:
            return


        self.event_bus.emit(
            Event(
                category=EventCategory.RUNTIME,
                type=event_type,
                source="executor",
                payload=payload,
            )
        )



    # --------------------------------------------------
    # Execution
    # --------------------------------------------------

    def execute(
        self,
        plan,
        decision=None,
        event=None,
    ):


        started_at = datetime.now()


        results = []


        for step in plan.steps:


            self._emit(
                EventType.STEP_STARTED,
                {
                    "action": step.action,
                },
            )


            context = ActionContext(
                step=step,
                decision=decision,
                plan=plan,
                event=event,
                memory_store=self.memory_store,
                graph=self.graph,
            )


            try:

                result = self.registry.execute(
                    step.action,
                    context,
                )


            except Exception as exc:

                result = ActionResult.fail(
                    action=step.action,
                    error=str(exc),
                )


            results.append(
                result
            )


            self._emit(
                (
                    EventType.STEP_COMPLETED
                    if result.success
                    else EventType.STEP_FAILED
                ),
                {
                    "action": step.action,
                    "success": result.success,
                },
            )



        finished_at = datetime.now()


        duration_ms = (
            finished_at - started_at
        ).total_seconds() * 1000



        return ExecutionResult(
            success=all(
                result.success
                for result in results
            ),

            results=results,

            actions_executed=len(results),

            started_at=started_at,

            finished_at=finished_at,

            duration_ms=duration_ms,
        )