from __future__ import annotations

import json
from pathlib import Path

from bitgenesis.identity.profile import IdentityProfile

from .backend import IdentityBackend
from .version import CURRENT_IDENTITY_SCHEMA


class JsonIdentityBackend(IdentityBackend):
    """
    JSON persistence backend for IdentityProfile.

    Stores the static identity of BitGenesis
    inside a JSON document.
    """

    def __init__(
        self,
        path: str | Path = "data/identity.json",
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
            "schema_version": CURRENT_IDENTITY_SCHEMA,
            "identity": None,
        }

        self._write(data)


    def _read(self) -> dict:

        return json.loads(
            self._path.read_text(
                encoding="utf-8",
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
    # Persistence
    # ---------------------------------------------------------

    def save(
        self,
        profile: IdentityProfile,
    ) -> None:

        data = {
            "schema_version": CURRENT_IDENTITY_SCHEMA,
            "identity": profile.to_dict(),
        }

        self._write(data)


    def load(self) -> IdentityProfile | None:

        data = self._read()

        identity = data.get(
            "identity"
        )

        if identity is None:
            return None


        return IdentityProfile.from_dict(
            identity
        )


    def exists(self) -> bool:

        data = self._read()

        return data.get(
            "identity"
        ) is not None


    def clear(self) -> None:

        self._write(
            {
                "schema_version": CURRENT_IDENTITY_SCHEMA,
                "identity": None,
            }
        )