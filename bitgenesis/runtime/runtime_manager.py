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
        memory_store=None,
        graph=None,
    ):

        self.memory_store = memory_store

        self.graph = graph

        self.registry = ActionRegistry()


        self.executor = Executor(
            memory_store=self.memory_store,
            graph=self.graph,
            registry=self.registry,
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