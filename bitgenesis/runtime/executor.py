from __future__ import annotations

from datetime import datetime

from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.action_context import ActionContext
from bitgenesis.runtime.execution_result import ExecutionResult
from bitgenesis.runtime.result import ActionResult
from bitgenesis.events.event_bus import EventBus

from bitgenesis.runtime.actions.bootstrap import (
    register_default_actions,
)


class Executor:
    """
    Executes runtime plans.

    The executor consumes an ActionRegistry.
    If no registry is provided, it creates
    an isolated registry with default actions.

    Shared registries should be injected by RuntimeManager.

    The EventBus is optional and allows the executor
    to participate in the runtime event flow.
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

            self.registry = ActionRegistry()

            register_default_actions(
                self.registry
            )

        else:

            self.registry = registry



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


        finished_at = datetime.now()


        duration_ms = (
            finished_at - started_at
        ).total_seconds() * 1000


        execution_result = ExecutionResult(
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


        return execution_result