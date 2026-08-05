from bitgenesis.language.detector import (
    LanguageDetector,
    Language,
)



def test_detect_italian():

    detector = LanguageDetector()


    result = detector.detect(
        "Chi ha creato BitGenesis?"
    )


    assert result == Language.ITALIAN




def test_detect_english():

    detector = LanguageDetector()


    result = detector.detect(
        "Who created BitGenesis?"
    )


    assert result == Language.ENGLISH




def test_detect_unknown():

    detector = LanguageDetector()


    result = detector.detect(
        "12345 xyz"
    )


    assert result == Language.UNKNOWN