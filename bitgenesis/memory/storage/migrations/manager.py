from __future__ import annotations

from bitgenesis.memory.storage.version import (
    CURRENT_MEMORY_SCHEMA,
)


class MemoryMigrationManager:
    """
    Coordinates memory storage schema migrations.

    Future responsibilities:

    - detect storage schema
    - execute migrations
    - upgrade persisted memories
    """

    def migrate(
        self,
        data: dict,
    ) -> dict:
        """
        Upgrade storage data to the current schema.

        Currently no migrations are required.
        """

        data["schema_version"] = CURRENT_MEMORY_SCHEMA

        return data