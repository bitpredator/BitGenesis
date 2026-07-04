from bitgenesis.runtime.action_registry import ActionRegistry

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

        # Memory
        self.registry.register(
            "store_memory",
            store_memory,
        )

        self.registry.register(
            "retrieve_memory_items",
            retrieve_memory_items,
        )

        # Knowledge
        self.registry.register(
            "query_knowledge_graph",
            query_knowledge_graph,
        )

    def execute(self, plan):

        results = []

        for step in plan.steps:

            result = self.registry.execute(
                step.action,
                step,
                self,
            )

            results.append(result)

        return ExecutionResult(
            success=True,
            results=results,
        )