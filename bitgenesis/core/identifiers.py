"""
BitGenesis Foundation Layer

Identifier utilities shared across the entire architecture.
"""

from __future__ import annotations

from uuid import UUID, uuid4

CoreID = UUID


def generate_id() -> CoreID:
    """
    Generate a new unique identifier.

    Returns
    -------
    UUID
        Random UUID v4.
    """
    return uuid4()