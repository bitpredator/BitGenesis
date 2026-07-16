"""
BitGenesis Core Builder Compatibility Layer.

This module exists for backward compatibility.

The real implementation lives in:
bitgenesis.core.brain_builder
"""

from bitgenesis.core.brain_builder import BrainBuilder

__all__ = [
    "BrainBuilder",
]