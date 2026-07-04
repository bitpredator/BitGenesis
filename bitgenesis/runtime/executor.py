from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.action_context import ActionContext

from bitgenesis.runtime.actions.memory import (
    store_memory,
    retrieve_memory_items,
)

from bitgenesis.runtime.actions.knowledge import (
    query_knowledge_graph,
)


class ExecutionResult:

    def __init__(self, success=True, results=None):

        self.success = success
        self.results = results or []


class Executor:

    def __init__(self, memory_store=None, graph=None):

        self.memory_store = memory_store
        self.graph = graph

        self.registry = ActionRegistry()

        # Memory actions
        self.registry.register(
            "store_memory",
            store_memory,
        )

        self.registry.register(
            "retrieve_memory_items",
            retrieve_memory_items,
        )

        # Knowledge actions
        self.registry.register(
            "query_knowledge_graph",
            query_knowledge_graph,
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