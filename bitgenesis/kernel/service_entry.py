from __future__ import annotations

from dataclasses import dataclass, field


from bitgenesis.kernel.service import KernelService
from bitgenesis.kernel.descriptor import ServiceDescriptor
from bitgenesis.kernel.service_state import ServiceState



@dataclass(slots=True)
class ServiceEntry:
    """
    Represents a registered Kernel service.

    Holds:
    - service instance
    - immutable descriptor
    - runtime lifecycle state
    """


    service: KernelService

    descriptor: ServiceDescriptor


    state: ServiceState = field(
        default=ServiceState.CREATED
    )



    # --------------------------------------------------
    # Metadata
    # --------------------------------------------------

    @property
    def service_type(
        self,
    ) -> type[KernelService]:

        return type(
            self.service
        )



    @property
    def name(
        self,
    ) -> str:

        return self.descriptor.name



    @property
    def priority(
        self,
    ) -> int:

        return self.descriptor.priority



    @property
    def auto_start(
        self,
    ) -> bool:

        return self.descriptor.auto_start



    # --------------------------------------------------
    # Lifecycle
    # --------------------------------------------------

    def start(
        self,
    ):

        self.state = ServiceState.STARTING


        try:

            self.service.start()


            self.state = ServiceState.RUNNING


        except Exception:

            self.state = ServiceState.FAILED

            raise



    def stop(
        self,
    ):

        self.state = ServiceState.STOPPING


        try:

            self.service.stop()


            self.state = ServiceState.STOPPED


        except Exception:

            self.state = ServiceState.FAILED

            raise



    def tick(
        self,
    ):

        if self.state != ServiceState.RUNNING:

            return


        try:

            self.service.tick()


        except Exception:

            self.state = ServiceState.FAILED

            raise