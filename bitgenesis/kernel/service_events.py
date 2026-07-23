from enum import Enum, auto


class EventType(Enum):

    SERVICE_REGISTERED = auto()

    SERVICE_UNREGISTERED = auto()

    SERVICE_STARTED = auto()

    SERVICE_STOPPED = auto()

    SERVICE_TICK = auto()



class ServiceEvent:

    def __init__(
        self,
        type,
        service
    ):
        self.type = type
        self.service = service