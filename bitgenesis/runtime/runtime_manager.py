from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.executor import Executor


class RuntimeManager:
    """
    Coordinates runtime execution.

    Responsibilities:
    - own action registry
    - own executor
    - expose lifecycle state
    """


    def __init__(
        self,
        registry: ActionRegistry | None = None,
        memory_store=None,
        graph=None,
    ):

        self.memory_store = memory_store

        self.graph = graph


        self.registry = (
            registry
            or ActionRegistry()
        )


        self.executor = Executor(
            registry=self.registry,
            memory_store=self.memory_store,
            graph=self.graph,
        )


        self.running = False



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self):

        if self.running:
            return

        self.running = True


    def stop(self):

        if not self.running:
            return

        self.running = False



    # --------------------------------------------------
    # Execution
    # --------------------------------------------------

    def execute(
        self,
        plan,
        decision=None,
        event=None,
    ):

        return self.executor.execute(
            plan,
            decision,
            event,
        )


    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------

    def tick(self):

        if not self.running:
            return