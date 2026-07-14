from bitgenesis.events.event_bus import EventBus
from bitgenesis.events.enums import EventCategory, EventType
from bitgenesis.events.event import Event

from bitgenesis.kernel.kernel import Kernel

from bitgenesis.memory.service import MemoryService
from bitgenesis.identity.service import IdentityService
from bitgenesis.runtime.service import RuntimeService


def bootstrap(
    bus: EventBus | None = None,
):

    if bus is None:
        bus = EventBus()

    kernel = Kernel(
        bus
    )


    # --------------------------------------------------
    # Runtime Services
    # --------------------------------------------------

    memory_service = MemoryService(
        bus
    )

    identity_service = IdentityService(
        bus
    )

    runtime_service = RuntimeService(
        bus
    )


    kernel.register(
        memory_service
    )

    kernel.register(
        identity_service
    )

    kernel.register(
        runtime_service
    )


    # --------------------------------------------------
    # Start Kernel
    # --------------------------------------------------

    kernel.start()


    # --------------------------------------------------
    # System Birth Event
    # --------------------------------------------------

    bus.publish(
        Event(
            category=EventCategory.MEMORY,
            type=EventType.MEMORY_BOOTSTRAP,
            source="bootstrap",
            payload={
                "message": "BitGenesis system initialized",
                "phase": "birth",
            },
        )
    )


    return (
        bus,
        kernel,
        memory_service.store,
    )