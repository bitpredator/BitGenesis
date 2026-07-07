from dataclasses import dataclass


@dataclass(frozen=True)
class Version:

    major: int = 0
    minor: int = 1
    patch: int = 0

    @property
    def string(self) -> str:

        return f"{self.major}.{self.minor}.{self.patch}"

    def __str__(self) -> str:

        return self.string


VERSION = Version()