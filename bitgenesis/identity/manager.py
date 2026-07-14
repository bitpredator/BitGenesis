from __future__ import annotations

from bitgenesis.identity.profile import IdentityProfile
from bitgenesis.identity.storage.backend import IdentityBackend


class IdentityManager:
    """
    Manages BitGenesis static identity.

    Handles identity lifecycle and optional persistence.
    """

    def __init__(
        self,
        backend: IdentityBackend | None = None,
    ):

        self._backend = backend

        self._profile = None


        if self._backend is not None:

            self._profile = self._backend.load()


        if self._profile is None:

            self._profile = IdentityProfile(
                name="BitGenesis",
                creator="Bitpredator",
                project="BitGenesis",
                version="0.2.0",
                description=(
                    "A modular cognitive AI framework focused on memory, "
                    "reasoning, planning and autonomous execution."
                ),
            )


            if self._backend is not None:

                self._backend.save(
                    self._profile
                )


    # ---------------------------------------------------------
    # Access
    # ---------------------------------------------------------

    @property
    def profile(self):

        return self._profile


    def get(self):

        return self._profile


    def as_dict(self):

        return self._profile.to_dict()