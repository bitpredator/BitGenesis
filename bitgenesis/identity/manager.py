from bitgenesis.identity.profile import IdentityProfile


class IdentityManager:

    def __init__(self):

        self._profile = IdentityProfile(
            name="BitGenesis",
            creator="Bitpredator",
            project="BitGenesis",
            version="0.1.0",
            description=(
                "A modular cognitive AI framework focused on memory, "
                "reasoning, planning and autonomous execution."
            ),
        )

    @property
    def profile(self):

        return self._profile

    def get(self):

        return self._profile

    def as_dict(self):

        return {
            "name": self._profile.name,
            "creator": self._profile.creator,
            "project": self._profile.project,
            "version": self._profile.version,
            "description": self._profile.description,
        }