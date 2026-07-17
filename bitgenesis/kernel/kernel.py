from __future__ import annotations


from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import (
    EventType,
    EventCategory,
)

from bitgenesis.events.event import Event


from bitgenesis.core.brain_builder import BrainBuilder
from bitgenesis.core.config import BrainConfig


from bitgenesis.kernel.registry import ServiceRegistry
from bitgenesis.kernel.state import KernelState



class Kernel:


    def __init__(
        self,
        bus: EventBus | None = None,
        config: BrainConfig | None = None,
    ):


        self.bus = bus or EventBus()

        self.config = config or BrainConfig()


        self.registry = ServiceRegistry()


        # legacy compatibility

        self.services = ()


        self.state = KernelState.CREATED


        self.running = False


        self.brain = None



    # --------------------------------------------------
    # Services
    # --------------------------------------------------


    def _refresh_services(self):

        self.services = self.registry.all()



    def register(
        self,
        service,
    ):


        self.registry.register(
            service
        )


        self._refresh_services()



        self.bus.emit(
            Event(
                category=EventCategory.KERNEL,
                type=EventType.SERVICE_REGISTERED,
                source="kernel",
                payload={
                    "service": type(service).__name__,
                    **self._service_metadata(service),
                },
            )
        )



    def unregister(
        self,
        service,
    ):


        self.registry.unregister(
            service
        )


        self._refresh_services()



        self.bus.emit(
            Event(
                category=EventCategory.KERNEL,
                type=EventType.SERVICE_UNREGISTERED,
                source="kernel",
                payload={
                    "service": type(service).__name__,
                },
            )
        )



    def get_service(
        self,
        service_type,
    ):

        return self.registry.get(
            service_type
        )



    def get_service_by_name(
        self,
        name,
    ):

        return self.registry.get_by_name(
            name
        )



    def get_brain(self):

        return self.brain



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------


    def bootstrap(self):


        builder = BrainBuilder(
            self.config
        )


        self.brain = builder.build()


        return self.brain




    def start(self):


        if self.running:

            return



        self.bootstrap()



        for service in self.registry.all():


            service.start()



            self.bus.emit(
                Event(
                    category=EventCategory.KERNEL,
                    type=EventType.SERVICE_STARTED,
                    source="kernel",
                    payload={
                        "service": type(service).__name__,
                        **self._service_metadata(service),
                    },
                )
            )



        self.state = KernelState.RUNNING


        self.running = True



        # ----------------------------------------------
        # Legacy events
        # ----------------------------------------------

        self.bus.emit(
            Event(
                category=EventCategory.KERNEL,
                type=EventType.KERNEL_INITIALIZED,
                source="kernel",
                payload={
                    "brain": self.brain,
                },
            )
        )


        self.bus.emit(
            Event(
                category=EventCategory.SYSTEM,
                type=EventType.SYSTEM_STARTED,
                source="kernel",
                payload={
                    "status": "running",
                },
            )
        )



        # ----------------------------------------------
        # New architecture event
        # ----------------------------------------------

        self.bus.emit(
            Event(
                category=EventCategory.KERNEL,
                type=EventType.KERNEL_READY,
                source="kernel",
                payload={
                    "services": len(
                        self.registry.all()
                    ),
                },
            )
        )



    def stop(self):


        if not self.running:

            return



        for service in reversed(
            self.registry.all()
        ):


            service.stop()



            self.bus.emit(
                Event(
                    category=EventCategory.KERNEL,
                    type=EventType.SERVICE_STOPPED,
                    source="kernel",
                    payload={
                        "service": type(service).__name__,
                        **self._service_metadata(service),
                    },
                )
            )



        self.state = KernelState.STOPPED


        self.running = False



        self.bus.emit(
            Event(
                category=EventCategory.KERNEL,
                type=EventType.KERNEL_SHUTDOWN,
                source="kernel",
                payload={
                    "status": "stopped",
                },
            )
        )



    # --------------------------------------------------
    # Runtime
    # --------------------------------------------------


    def tick(self):


        for service in self.registry.all():


            service.tick()



            self.bus.emit(
                Event(
                    category=EventCategory.KERNEL,
                    type=EventType.SERVICE_TICKED,
                    source="kernel",
                    payload={
                        "service": type(service).__name__,
                        **self._service_metadata(service),
                    },
                )
            )

    def _service_metadata(
        self,
        service,
    ) -> dict:
        """
        Returns service metadata.

        Supports both modern KernelService
        and legacy plain service objects.
        """

        if hasattr(service, "metadata"):
            return service.metadata()

        return {
            "name": getattr(
                service,
                "name",
                type(service).__name__,
            ),
            "version": getattr(
                service,
                "version",
                "0.0.0",
            ),
            "type": type(service).__name__,
        }        