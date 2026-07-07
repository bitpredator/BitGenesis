from dataclasses import dataclass


@dataclass(slots=True)
class BrainStats:

    memories: int = 0
    episodes: int = 0
    knowledge: int = 0

    state: str = "idle"

    version: str = "0.1.0"

    def as_dict(self) -> dict:

        return {
            "memories": self.memories,
            "episodes": self.episodes,
            "knowledge": self.knowledge,
            "state": self.state,
            "version": self.version,
        }