from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.action_context import ActionContext

from bitgenesis.runtime.actions.bootstrap import (
    register_default_actions,
)


class ExecutionResult:

    def __init__(self, success=True, results=None):

        self.success = success
        self.results = results or []


class Executor:

    def __init__(
        self,
        memory_store=None,
        graph=None,
        registry: ActionRegistry | None = None,
    ):

        self.memory_store = memory_store
        self.graph = graph

        self.registry = registry or ActionRegistry()

        if registry is None:
            register_default_actions(
                self.registry
            )


    def execute(self, plan, decision=None, event=None):

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

            result = self.registry.execute(
                step.action,
                context,
            )

            results.append(result)

        return ExecutionResult(
            success=True,
            results=results,
        )