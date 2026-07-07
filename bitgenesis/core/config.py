from dataclasses import dataclass


@dataclass(slots=True)
class BrainConfig:

    name: str = "BitGenesis"

    version: str = "0.1.0"

    auto_reflection: bool = False

    auto_inference: bool = False

    auto_consolidation: bool = False