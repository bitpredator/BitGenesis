from bitgenesis.identity.manager import IdentityManager


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