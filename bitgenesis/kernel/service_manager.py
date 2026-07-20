from __future__ import annotations


from bitgenesis.kernel.registry import ServiceRegistry
from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor



class ServiceManager:
    """
    Manages Kernel service lifecycle.

    Responsibilities:
    - registration
    - metadata management
    - startup ordering
    - shutdown ordering
    - runtime ticking
    """


    def __init__(
        self,
        registry: ServiceRegistry | None = None,
    ):

        self.registry = (
            registry
            or ServiceRegistry()
        )


        self._descriptors: dict[
            int,
            ServiceDescriptor,
        ] = {}



    # --------------------------------------------------
    # Registration
    # --------------------------------------------------


    def register(
        self,
        service: KernelService,
        descriptor: ServiceDescriptor | None = None,
    ):


        if descriptor is None:

            descriptor = ServiceDescriptor(
                name=(
                    getattr(
                        service,
                        "name",
                        None,
                    )
                    or type(service).__name__
                ),
                version="1.0.0",
            )


        self.registry.register(
            service
        )


        self._descriptors[
            id(service)
        ] = descriptor



    def unregister(
        self,
        service: KernelService,
    ):


        self.registry.unregister(
            service
        )


        self._descriptors.pop(
            id(service),
            None,
        )



    # --------------------------------------------------
    # Lookup
    # --------------------------------------------------


    def get(
        self,
        service_type,
    ):

        return self.registry.get(
            service_type
        )



    def get_by_name(
        self,
        name,
    ):

        return self.registry.get_by_name(
            name
        )



    def all(self):

        return self.registry.all()



    def descriptor(
        self,
        service,
    ):


        if isinstance(
            service,
            type,
        ):

            for instance in self.registry.all():

                if type(instance) is service:

                    return self._descriptors.get(
                        id(instance)
                    )

            return None


        return self._descriptors.get(
            id(service)
        )



    # --------------------------------------------------
    # Ordering
    # --------------------------------------------------


    def _ordered_services(self):

        return sorted(
            self.registry.all(),
            key=lambda service:
                self._descriptors[
                    id(service)
                ].priority,
        )



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------


    def start_all(self):


        for service in self._ordered_services():

            descriptor = self._descriptors[
                id(service)
            ]


            if not descriptor.auto_start:

                continue


            service.start()



    def stop_all(self):


        for service in reversed(
            self._ordered_services()
        ):

            service.stop()



    def tick_all(self):


        for service in self.registry.all():

            service.tick()