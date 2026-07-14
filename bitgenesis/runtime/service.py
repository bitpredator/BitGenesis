from __future__ import annotations

from bitgenesis.kernel.service import KernelService

from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event
from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)

from bitgenesis.runtime.action_registry import ActionRegistry
from bitgenesis.runtime.runtime_manager import RuntimeManager

from bitgenesis.runtime.actions.bootstrap import (
    register_default_actions,
)


class RuntimeService(KernelService):
    """
    Kernel service responsible for runtime execution.

    Responsibilities:
    - own ActionRegistry
    - own RuntimeManager
    - manage runtime lifecycle
    - expose execution layer to Kernel
    """


    def __init__(
        self,
        event_bus: EventBus,
        registry: ActionRegistry | None = None,
        manager: RuntimeManager | None = None,
        memory_store=None,
        graph=None,
    ):

        self.event_bus = event_bus


        # --------------------------------------------------
        # Action Registry
        # --------------------------------------------------

        self.registry = (
            registry
            or ActionRegistry()
        )


        if registry is None:

            register_default_actions(
                self.registry
            )


        # --------------------------------------------------
        # Runtime Manager
        # --------------------------------------------------

        self.manager = (
            manager
            or RuntimeManager(
                registry=self.registry,
                memory_store=memory_store,
                graph=graph,
            )
        )


        self.running = False



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(self) -> None:

        if self.running:
            return


        self.running = True


        self.event_bus.publish(
            Event(
                category=EventCategory.RUNTIME,
                type=EventType.RUNTIME_STARTED,
                source="runtime",
                payload={
                    "status": "running",
                },
            )
        )



    def stop(self) -> None:

        if not self.running:
            return


        self.running = False


        self.event_bus.publish(
            Event(
                category=EventCategory.RUNTIME,
                type=EventType.RUNTIME_STOPPED,
                source="runtime",
                payload={
                    "status": "stopped",
                },
            )
        )



    def tick(self) -> None:
        """
        Runtime maintenance cycle.

        Future:
        - scheduled actions
        - queued execution
        - background workers
        """

        if not self.running:
            return


        self.manager.tick()



    # --------------------------------------------------
    # Execution
    # --------------------------------------------------

    def execute(
        self,
        plan,
        decision=None,
        event=None,
    ):

        if not self.running:

            raise RuntimeError(
                "Runtime service is not running"
            )


        return self.manager.execute(
            plan,
            decision,
            event,
        )