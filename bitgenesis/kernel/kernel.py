from __future__ import annotations


from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import (
    EventType,
    EventCategory,
)
from bitgenesis.events.event import Event


from bitgenesis.core.brain_builder import BrainBuilder
from bitgenesis.core.config import BrainConfig


from bitgenesis.kernel.service_manager import ServiceManager
from bitgenesis.kernel.runtime_loop import RuntimeLoop
from bitgenesis.kernel.state import KernelState



class Kernel:


    def __init__(
        self,
        bus: EventBus | None = None,
        config: BrainConfig | None = None,
    ):


        self.bus = bus or EventBus()

        self.config = config or BrainConfig()


        self.service_manager = ServiceManager(
            event_bus=self.bus,
        )


        self.runtime_loop = RuntimeLoop(
            service_manager=self.service_manager,
        )


        # compatibility layer
        self.services = ()


        self.state = KernelState.CREATED

        self.running = False

        self.brain = None



    # --------------------------------------------------
    # Services
    # --------------------------------------------------


    def _refresh_services(self):

        self.services = self.service_manager.all()



    def register(
        self,
        service,
        descriptor=None,
    ):


        self.service_manager.register(
            service,
            descriptor,
        )


        self._refresh_services()



    def unregister(
        self,
        service,
    ):


        self.service_manager.unregister(
            service
        )


        self._refresh_services()



    def get_service(
        self,
        service_type,
    ):


        return self.service_manager.get(
            service_type
        )



    def get_service_by_name(
        self,
        name,
    ):


        return self.service_manager.get_by_name(
            name
        )



    def get_brain(self):

        return self.brain



    # --------------------------------------------------
    # Bootstrap
    # --------------------------------------------------


    def bootstrap(self):


        builder = BrainBuilder(
            self.config
        )


        self.brain = builder.build()


        return self.brain



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------


    def start(self):


        if self.running:
            return



        self.bootstrap()



        self.service_manager.start_all()



        self.runtime_loop.start()



        self.state = KernelState.RUNNING

        self.running = True



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



    def stop(self):


        if not self.running:
            return



        self.runtime_loop.stop()



        self.service_manager.stop_all()



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

        self.runtime_loop.step()