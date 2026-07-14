from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from bitgenesis.identity.profile import IdentityProfile


class IdentityBackend(ABC):
    """
    Persistence backend for the IdentityProfile.
    """

    @abstractmethod
    def save(
        self,
        profile: IdentityProfile,
    ) -> None:
        ...

    @abstractmethod
    def load(self) -> IdentityProfile | None:
        ...

    @abstractmethod
    def exists(self) -> bool:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...