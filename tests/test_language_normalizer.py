from bitgenesis.language.normalizer import TextNormalizer



def test_normalizer_lowercase():

    normalizer = TextNormalizer()

    result = normalizer.normalize(
        "CIAO BITGENESIS"
    )

    assert result == "ciao bitgenesis"



def test_normalizer_spaces():

    normalizer = TextNormalizer()

    result = normalizer.normalize(
        "  chi   ha   creato   bitgenesis  "
    )

    assert result == (
        "chi ha creato bitgenesis"
    )



def test_normalizer_punctuation():

    normalizer = TextNormalizer()

    result = normalizer.normalize(
        "Chi ha creato BitGenesis???"
    )

    assert result == (
        "chi ha creato bitgenesis?"
    )