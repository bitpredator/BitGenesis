from bitgenesis.identity.manager import IdentityManager
from bitgenesis.identity.storage.json_backend import JsonIdentityBackend


def test_identity_manager_returns_profile():

    manager = IdentityManager()

    profile = manager.get()

    assert profile.name == "BitGenesis"
    assert profile.creator == "Bitpredator"
    assert profile.project == "BitGenesis"


def test_identity_manager_profile_property():

    manager = IdentityManager()

    assert manager.profile.name == "BitGenesis"


def test_identity_manager_as_dict():

    manager = IdentityManager()

    data = manager.as_dict()

    assert data["name"] == "BitGenesis"
    assert data["creator"] == "Bitpredator"
    assert data["project"] == "BitGenesis"
    assert "version" in data
    assert "description" in data

def test_identity_manager_persists_profile(tmp_path):

    path = tmp_path / "identity.json"

    backend = JsonIdentityBackend(
        path
    )


    manager = IdentityManager(
        backend=backend
    )

    profile = manager.get()


    assert profile.name == "BitGenesis"
    assert backend.exists() is True


    second_manager = IdentityManager(
        backend=backend
    )

    restored = second_manager.get()


    assert restored.name == profile.name
    assert restored.creator == profile.creator
    assert restored.project == profile.project
    assert restored.version == profile.version
    assert restored.description == profile.description