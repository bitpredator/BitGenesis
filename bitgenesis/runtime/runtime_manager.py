from __future__ import annotations


from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.event import Event

from bitgenesis.events.enums import (
    EventCategory,
    EventType,
)


from bitgenesis.runtime.action_registry import (
    ActionRegistry,
)

from bitgenesis.runtime.executor import (
    Executor,
)

from bitgenesis.runtime.planner import (
    CognitiveExecutionPlanner,
)

from bitgenesis.runtime.service_context import (
    ServiceContext,
)

from bitgenesis.runtime.service_orchestrator import (
    ServiceOrchestrator,
)



class RuntimeManager:
    """
    Coordinates runtime execution.

    Responsibilities:

    - own action registry
    - own executor
    - own execution planner
    - own service orchestrator
    - register runtime services
    - discover runtime services
    - execute runtime services
    - manage runtime lifecycle
    """



    def __init__(
        self,
        registry: ActionRegistry | None = None,
        memory_store=None,
        graph=None,
        event_bus: EventBus | None = None,
        planner: CognitiveExecutionPlanner | None = None,
        services: list[object] | None = None,
        orchestrator: ServiceOrchestrator | None = None,
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


        self.planner = (
            planner
            or CognitiveExecutionPlanner()
        )



        self.executor = Executor(
            registry=self.registry,
            memory_store=self.memory_store,
            graph=self.graph,
            event_bus=self.event_bus,
        )



        self.service_orchestrator = (
            orchestrator
            or ServiceOrchestrator(
                services=services,
            )
        )



        self.context = ServiceContext(
            event_bus=self.event_bus,
            memory_store=self.memory_store,
            graph=self.graph,
            runtime_state=self,
        )


        self.running = False



    # ==================================================
    # Lifecycle
    # ==================================================

    def start(
        self,
    ):

        if self.running:

            return


        self.running = True


        self.service_orchestrator.start_services(
            self.context
        )


        if self.event_bus:

            self.event_bus.emit(
                Event(
                    category=EventCategory.RUNTIME,
                    type=EventType.RUNTIME_STARTED,
                    source="runtime_manager",
                    payload={},
                )
            )



    def stop(
        self,
    ):

        if not self.running:

            return


        self.service_orchestrator.stop_services(
            self.context
        )


        self.running = False



        if self.event_bus:

            self.event_bus.emit(
                Event(
                    category=EventCategory.RUNTIME,
                    type=EventType.RUNTIME_STOPPED,
                    source="runtime_manager",
                    payload={},
                )
            )



    # ==================================================
    # Planning
    # ==================================================

    def create_plan(
        self,
        decision,
    ):


        result = self.planner.create_plan(
            decision
        )


        if self.event_bus:

            self.event_bus.emit(
                Event(
                    category=EventCategory.PLANNING,
                    type=(
                        EventType.PLAN_CREATED
                        if result.success
                        else EventType.PLAN_FAILED
                    ),
                    source="runtime_manager",
                    payload={
                        "success": result.success,
                        "reason": result.reason,
                    },
                )
            )


        return result



    # ==================================================
    # Execution
    # ==================================================

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



    # ==================================================
    # Cognitive execution
    # ==================================================

    def execute_decision(
        self,
        decision,
        event=None,
    ):


        planning_result = self.create_plan(
            decision
        )


        if not planning_result.success:

            return None



        return self.execute(
            planning_result.plan,
            decision=decision,
            event=event,
        )



    # ==================================================
    # Service management
    # ==================================================

    def register_service(
        self,
        service,
        name: str | None = None,
        metadata: dict | None = None,
    ):
        """
        Register runtime service.
        """


        if name is None:

            name = type(service).__name__



        # Compatibility attributes

        if not hasattr(
            service,
            "service",
        ):

            try:

                service.service = service

            except Exception:

                pass



        if not hasattr(
            service,
            "name",
        ):

            try:

                service.name = name

            except Exception:

                pass



        return self.service_orchestrator.register(
            service,
            name=name,
            metadata=metadata,
        )



    def unregister_service(
        self,
        service,
    ):

        return self.service_orchestrator.unregister(
            service
        )



    def discover_service(
        self,
        name: str,
    ):

        return self.service_orchestrator.discover(
            name
        )



    def discover_services(
        self,
    ):

        return self.service_orchestrator.all()



    def list_services(
        self,
    ):

        return self.discover_services()



    # ==================================================
    # Service orchestration
    # ==================================================

    def orchestrate_services(
        self,
    ):


        result = self.service_orchestrator.execute(
            self.context
        )


        if self.event_bus:

            self.event_bus.emit(
                Event(
                    category=EventCategory.RUNTIME,
                    type=(
                        EventType.SERVICE_FAILED
                        if not result.success
                        else EventType.SERVICE_TICKED
                    ),
                    source="runtime_manager",
                    payload={
                        "services_executed": (
                            result.services_executed
                        ),
                        "failed_services": (
                            result.failed_services
                        ),
                    },
                )
            )



        return result



    # ==================================================
    # Runtime loop
    # ==================================================

    def tick(
        self,
    ):


        if not self.running:

            return None



        return self.orchestrate_services()