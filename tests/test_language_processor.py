from bitgenesis.language.processor import (
    LanguageProcessor,
)


from bitgenesis.language.detector import (
    Language,
)



def test_processor_returns_context():

    processor = LanguageProcessor()


    context = processor.process(
        "Chi ha creato BitGenesis?"
    )


    assert context.raw_text == (
        "Chi ha creato BitGenesis?"
    )


    assert context.language == (
        Language.ITALIAN
    )


    assert context.tokens == [
        "chi",
        "ha",
        "creato",
        "bitgenesis",
    ]



def test_processor_normalizes_text():

    processor = LanguageProcessor()


    context = processor.process(
        "HELLO WORLD!"
    )


    assert context.normalized_text == (
        "hello world"
    )



def test_context_serialization():

    processor = LanguageProcessor()


    context = processor.process(
        "Who created BitGenesis?"
    )


    data = context.to_dict()


    assert data["language"] == "en"

    assert "tokens" in data



def test_token_count():

    processor = LanguageProcessor()


    context = processor.process(
        "BitGenesis understands language"
    )


    assert context.token_count == 3