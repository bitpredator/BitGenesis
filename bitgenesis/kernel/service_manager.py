from __future__ import annotations


from bitgenesis.kernel.registry import ServiceRegistry
from bitgenesis.kernel.service import KernelService


class ServiceManager:
    """
    Manages Kernel service lifecycle.

    Responsible for:
    - registration
    - unregistration
    - startup
    - shutdown
    - runtime ticking
    """


    def __init__(
        self,
        registry: ServiceRegistry | None = None,
    ):

        self.registry = registry or ServiceRegistry()



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------


    def register(
        self,
        service: KernelService,
    ):

        self.registry.register(
            service
        )



    def unregister(
        self,
        service: KernelService,
    ):

        self.registry.unregister(
            service
        )



    def get(
        self,
        service_type,
    ):

        return self.registry.get(
            service_type
        )



    def get_by_name(
        self,
        name: str,
    ):

        return self.registry.get_by_name(
            name
        )



    def all(self):

        return self.registry.all()



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------


    def start_all(self):

        for service in self.registry.all():

            service.start()



    def stop_all(self):

        for service in reversed(
            self.registry.all()
        ):

            service.stop()



    def tick_all(self):

        for service in self.registry.all():

            service.tick()