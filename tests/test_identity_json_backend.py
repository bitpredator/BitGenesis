from pathlib import Path

from bitgenesis.identity.profile import IdentityProfile
from bitgenesis.identity.storage.json_backend import JsonIdentityBackend


def create_profile() -> IdentityProfile:
    return IdentityProfile(
        name="BitGenesis",
        creator="Bitpredator",
        project="BitGenesis",
        version="0.2.0",
        description="Artificial Cognitive Architecture from Scratch",
    )


def test_json_identity_backend_creation(tmp_path):

    path = tmp_path / "identity.json"

    backend = JsonIdentityBackend(
        path
    )

    assert backend is not None
    assert path.exists()



def test_save_and_load_identity(tmp_path):

    path = tmp_path / "identity.json"

    backend = JsonIdentityBackend(
        path
    )

    profile = create_profile()

    backend.save(
        profile
    )

    loaded = backend.load()

    assert loaded is not None

    assert loaded.name == profile.name
    assert loaded.creator == profile.creator
    assert loaded.project == profile.project
    assert loaded.version == profile.version
    assert loaded.description == profile.description



def test_identity_exists(tmp_path):

    path = tmp_path / "identity.json"

    backend = JsonIdentityBackend(
        path
    )

    assert backend.exists() is False


    backend.save(
        create_profile()
    )

    assert backend.exists() is True



def test_clear_identity(tmp_path):

    path = tmp_path / "identity.json"

    backend = JsonIdentityBackend(
        path
    )

    backend.save(
        create_profile()
    )

    assert backend.exists() is True


    backend.clear()


    assert backend.exists() is False
    assert backend.load() is None