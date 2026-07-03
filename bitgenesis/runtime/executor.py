class ExecutionResult:

    def __init__(self, success=True, results=None):

        self.success = success
        self.results = results or []


class Executor:

    def __init__(self, memory_store=None, graph=None):

        self.memory_store = memory_store
        self.graph = graph

    def execute(self, plan):

        results = []

        for step in plan.steps:

            result = self._execute_step(step)
            results.append(result)

        return ExecutionResult(
            success=True,
            results=results
        )

    def _execute_step(self, step):

        action = step.action

        # ------------------------
        # MEMORY OPERATIONS
        # ------------------------
        if action == "store_memory":

            if self.memory_store:
                self.memory_store.add(step.target)

            return {
                "action": action,
                "status": "stored"
            }

        if action == "retrieve_memory_items":

            return {
                "action": action,
                "status": "retrieved",
                "data": step.target
            }

        # ------------------------
        # KNOWLEDGE OPERATIONS
        # ------------------------
        if action == "query_knowledge_graph":

            if self.graph:
                return {
                    "action": action,
                    "status": "queried",
                    "data": step.target
                }

        # ------------------------
        # FALLBACK
        # ------------------------
        return {
            "action": action,
            "status": "noop"
        }