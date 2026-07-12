from dataclasses import dataclass

from .state import KernelState


@dataclass(slots=True)
class KernelLifecycle:

    state: KernelState = KernelState.STOPPED

    cycles: int = 0

    started: bool = False