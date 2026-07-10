from __future__ import annotations

import json
from pathlib import Path

from bitgenesis.memory.object import MemoryObject

from .backend import MemoryBackend


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
            "version": "1.0",
            "memories": [],
        }

        self._write(data)


    def _read(self) -> dict:

        return json.loads(
            self._path.read_text(
                encoding="utf-8"
            )
        )


    def _write(
        self,
        data: dict,
    ) -> None:

        self._path.write_text(
            json.dumps(
                data,
                indent=4,
                ensure_ascii=False,
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
                "version": "1.0",
                "memories": [],
            }
        )