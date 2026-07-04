from bitgenesis.identity.manager import IdentityManager
from bitgenesis.identity.query import IdentityQuery


def test_identity_query_returns_profile():

    manager = IdentityManager()

    query = IdentityQuery(manager)

    profile = query.profile()

    assert profile.name == "BitGenesis"
    assert profile.creator == "Bitpredator"
    assert profile.project == "BitGenesis"


def test_identity_query_returns_field():

    manager = IdentityManager()

    query = IdentityQuery(manager)

    assert query.field("name") == "BitGenesis"
    assert query.field("creator") == "Bitpredator"
    assert query.field("project") == "BitGenesis"


def test_identity_query_returns_none_for_unknown_field():

    manager = IdentityManager()

    query = IdentityQuery(manager)

    assert query.field("does_not_exist") is None


def test_identity_query_returns_dictionary():

    manager = IdentityManager()

    query = IdentityQuery(manager)

    data = query.as_dict()

    assert isinstance(data, dict)
    assert data["name"] == "BitGenesis"
    assert data["creator"] == "Bitpredator"
    assert data["project"] == "BitGenesis"
    assert "version" in data
    assert "description" in data


def test_identity_query_uses_default_manager():

    query = IdentityQuery()

    assert query.field("name") == "BitGenesis"