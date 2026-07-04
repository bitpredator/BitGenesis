from bitgenesis.identity.profile import IdentityProfile


def test_identity_profile_creation():

    profile = IdentityProfile(
        name="BitGenesis",
        creator="Bitpredator",
        project="BitGenesis",
        version="0.1.0",
        description="AI Framework",
    )

    assert profile.name == "BitGenesis"
    assert profile.creator == "Bitpredator"
    assert profile.project == "BitGenesis"
    assert profile.version == "0.1.0"
    assert profile.description == "AI Framework"