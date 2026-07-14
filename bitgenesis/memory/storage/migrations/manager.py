from __future__ import annotations

from bitgenesis.memory.storage.version import (
    CURRENT_MEMORY_SCHEMA,
)


class MemoryMigrationManager:
    """
    Coordinates memory storage schema migrations.
    """

    def migrate(
        self,
        data: dict,
    ) -> dict:
        """
        Upgrade storage data to the current schema.
        """

        version = data.get(
            "schema_version",
            CURRENT_MEMORY_SCHEMA,
        )

        if version == CURRENT_MEMORY_SCHEMA:
            return data

        return self._upgrade(
            data,
            version,
        )

    def _upgrade(
        self,
        data: dict,
        version: str,
    ) -> dict:
        """
        Apply schema upgrades.

        Placeholder for future migrations.
        """

        data["schema_version"] = CURRENT_MEMORY_SCHEMA

        return data