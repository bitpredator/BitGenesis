from __future__ import annotations

import json
from datetime import datetime
from enum import Enum
from pathlib import Path
from uuid import UUID

from bitgenesis.memory.object import MemoryObject

from .backend import MemoryBackend
from .version import CURRENT_MEMORY_SCHEMA


class BitGenesisJSONEncoder(json.JSONEncoder):
    """
    JSON encoder for BitGenesis cognitive objects.

    Handles UUIDs, datetime objects,
    enums and domain objects.
    """

    def default(self, obj):

        if isinstance(obj, UUID):
            return str(obj)

        if isinstance(obj, datetime):
            return obj.isoformat()

        if isinstance(obj, Enum):
            return obj.value

        if hasattr(obj, "to_dict"):
            return obj.to_dict()

        return super().default(obj)


class JsonMemoryBackend(MemoryBackend):
    """
    Persistent JSON backend for MemoryStore.

    Stores MemoryObject instances inside a JSON file.
    """


    def __init__(
        self,
        path: str | Path = "data/memories.json",
    ) -> None:

        self._path = Path(path)

        self._path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        if not self._path.exists():
            self._initialize_file()


    # ---------------------------------------------------------
    # File handling
    # ---------------------------------------------------------

    def _initialize_file(self) -> None:

        data = {
            "schema_version": CURRENT_MEMORY_SCHEMA,
            "memories": [],
        }

        self._write(data)



    def _read(self) -> dict:

        data = json.loads(
            self._path.read_text(
                encoding="utf-8"
            )
        )

        return self._normalize_schema(
            data
        )



    def _normalize_schema(
        self,
        data: dict,
    ) -> dict:
        """
        Normalize legacy storage formats.

        Older versions used:
            "version": "1.0"

        New format uses:
            "schema_version": "1.0"
        """

        if "schema_version" not in data:

            if "version" in data:

                data["schema_version"] = data["version"]

            else:

                data["schema_version"] = CURRENT_MEMORY_SCHEMA


        return data



    def _write(
        self,
        data: dict,
    ) -> None:

        self._path.write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
                cls=BitGenesisJSONEncoder,
            ),
            encoding="utf-8",
        )


    # ---------------------------------------------------------
    # CRUD
    # ---------------------------------------------------------

    def save(
        self,
        memory: MemoryObject,
    ) -> None:

        data = self._read()

        memories = data["memories"]

        serialized = memory.to_dict()

        for index, item in enumerate(memories):

            if item["id"] == serialized["id"]:

                memories[index] = serialized

                self._write(data)

                return


        memories.append(serialized)

        self._write(data)



    def get(
        self,
        memory_id: str,
    ) -> MemoryObject | None:

        data = self._read()

        for item in data["memories"]:

            if item["id"] == memory_id:

                return MemoryObject.from_dict(
                    item
                )

        return None



    def remove(
        self,
        memory_id: str,
    ) -> None:

        data = self._read()

        data["memories"] = [
            memory
            for memory in data["memories"]
            if memory["id"] != memory_id
        ]

        self._write(data)



    def exists(
        self,
        memory_id: str,
    ) -> bool:

        return self.get(memory_id) is not None



    # ---------------------------------------------------------
    # Bulk
    # ---------------------------------------------------------

    def load(self) -> list[MemoryObject]:

        data = self._read()

        return [
            MemoryObject.from_dict(memory)
            for memory in data["memories"]
        ]



    def clear(self) -> None:

        self._write(
            {
                "schema_version": CURRENT_MEMORY_SCHEMA,
                "memories": [],
            }
        )