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

    - own RuntimeManager
    - own ActionRegistry
    - manage runtime lifecycle
    - expose execution layer
    - integrate services
    - propagate runtime events
    """


    def __init__(
        self,
        event_bus: EventBus,
        registry: ActionRegistry | None = None,
        manager: RuntimeManager | None = None,
        memory_store=None,
        graph=None,
        services=None,
    ):

        self.event_bus = event_bus


        # --------------------------------------------------
        # Action registry
        # --------------------------------------------------

        self.registry = (
            registry
            or ActionRegistry(
                event_bus=self.event_bus
            )
        )


        if registry is None:

            register_default_actions(
                self.registry
            )


        # --------------------------------------------------
        # Runtime manager
        # --------------------------------------------------

        self.manager = (
            manager
            or RuntimeManager(
                registry=self.registry,
                memory_store=memory_store,
                graph=graph,
                event_bus=self.event_bus,
                services=services,
            )
        )


        self.running = False



    # ==================================================
    # Lifecycle
    # ==================================================

    def start(
        self,
    ) -> None:

        if self.running:

            return


        self.running = True


        # Start internal runtime

        self.manager.start()


        self.event_bus.emit(
            Event(
                category=EventCategory.RUNTIME,
                type=EventType.RUNTIME_STARTED,
                source="runtime_service",
                payload={
                    "status": "running",
                },
            )
        )



    def stop(
        self,
    ) -> None:

        if not self.running:

            return


        # Stop internal runtime

        self.manager.stop()


        self.running = False


        self.event_bus.emit(
            Event(
                category=EventCategory.RUNTIME,
                type=EventType.RUNTIME_STOPPED,
                source="runtime_service",
                payload={
                    "status": "stopped",
                },
            )
        )



    def tick(
        self,
    ):
        """
        Executes one runtime maintenance cycle.
        """


        if not self.running:

            return None


        return self.manager.tick()



    # ==================================================
    # Execution
    # ==================================================

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



    def execute_decision(
        self,
        decision,
        event=None,
    ):


        if not self.running:

            raise RuntimeError(
                "Runtime service is not running"
            )


        return self.manager.execute_decision(
            decision,
            event,
        )



    # ==================================================
    # Services
    # ==================================================

    def register_service(
        self,
        service,
        name=None,
        metadata=None,
    ):

        return self.manager.register_service(
            service,
            name=name,
            metadata=metadata,
        )



    def unregister_service(
        self,
        service,
    ):

        return self.manager.unregister_service(
            service
        )



    def discover_service(
        self,
        name,
    ):

        return self.manager.discover_service(
            name
        )



    def discover_services(
        self,
    ):

        return self.manager.discover_services()



    # ==================================================
    # Runtime information
    # ==================================================

    @property
    def metrics(self):

        return self.manager.metrics


    @property
    def statistics(self):

        return self.manager.statistics


    def snapshot(self):

        return self.manager.snapshot()