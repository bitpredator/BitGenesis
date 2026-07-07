from bitgenesis.core.version import Version, VERSION


def test_default_version():

    version = Version()

    assert version.major == 0
    assert version.minor == 1
    assert version.patch == 0


def test_version_string():

    version = Version(
        major=1,
        minor=2,
        patch=3,
    )

    assert version.string == "1.2.3"


def test_version_str():

    version = Version(
        major=0,
        minor=1,
        patch=0,
    )

    assert str(version) == "0.1.0"


def test_global_version():

    assert VERSION.major == 0
    assert VERSION.minor == 1
    assert VERSION.patch == 0


def test_global_version_string():

    assert str(VERSION) == "0.1.0"