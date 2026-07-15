from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.executor import Executor


class RuntimeManager:
    """
    Coordinates runtime execution.

    Responsibilities:
    - own action registry
    - own executor
    - manage execution lifecycle events
    - expose lifecycle state
    """


    def __init__(
        self,
        registry: ActionRegistry | None = None,
        memory_store=None,
        graph=None,
        event_bus: EventBus | None = None,
    ):

        self.memory_store = memory_store
        self.graph = graph
        self.event_bus = event_bus


        self.registry = (
            registry
            or ActionRegistry(
                event_bus=self.event_bus
            )
        )


        self.executor = Executor(
            registry=self.registry,
            memory_store=self.memory_store,
            graph=self.graph,
            event_bus=self.event_bus,
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


        if self.event_bus:

            self.event_bus.emit(
                Event(
                    category=EventCategory.RUNTIME,
                    type=EventType.EXECUTION_STARTED,
                    source="runtime_manager",
                    payload={
                        "plan": str(plan),
                    },
                )
            )


        try:

            result = self.executor.execute(
                plan,
                decision,
                event,
            )


        except Exception as exc:

            if self.event_bus:

                self.event_bus.emit(
                    Event(
                        category=EventCategory.RUNTIME,
                        type=EventType.EXECUTION_FAILED,
                        source="runtime_manager",
                        payload={
                            "error": str(exc),
                        },
                    )
                )

            raise



        if self.event_bus:

            self.event_bus.emit(
                Event(
                    category=EventCategory.RUNTIME,
                    type=(
                        EventType.EXECUTION_COMPLETED
                        if result.success
                        else EventType.EXECUTION_FAILED
                    ),
                    source="runtime_manager",
                    payload={
                        "success": result.success,
                        "actions_executed": (
                            result.actions_executed
                        ),
                    },
                )
            )


        return result



    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------

    def tick(self):

        if not self.running:
            return