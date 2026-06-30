"""
Serialization helpers.
"""

from __future__ import annotations

from dataclasses import asdict


class Serializable:
    """
    Base serialization mixin.
    """

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)