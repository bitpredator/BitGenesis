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
    ):

        self.event_bus = event_bus

        self.registry = registry or ActionRegistry()

        self.manager = manager or RuntimeManager(
            self.registry
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
        action: str,
        context,
    ):

        if not self.running:
            raise RuntimeError(
                "Runtime service is not running"
            )


        return self.manager.execute(
            action,
            context,
        )