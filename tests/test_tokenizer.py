from bitgenesis.language.tokenizer import Tokenizer



def test_basic_tokenization():

    tokenizer = Tokenizer()


    result = tokenizer.tokenize(
        "Chi ha creato BitGenesis?"
    )


    assert result == [
        "chi",
        "ha",
        "creato",
        "bitgenesis",
    ]




def test_lowercase_conversion():

    tokenizer = Tokenizer()


    result = tokenizer.tokenize(
        "BITGENESIS Cognitive System"
    )


    assert result == [
        "bitgenesis",
        "cognitive",
        "system",
    ]




def test_punctuation_removal():

    tokenizer = Tokenizer()


    result = tokenizer.tokenize(
        "Ciao, mondo!"
    )


    assert result == [
        "ciao",
        "mondo",
    ]




def test_accent_support():

    tokenizer = Tokenizer()


    result = tokenizer.tokenize(
        "Perché sei qui?"
    )


    assert result == [
        "perché",
        "sei",
        "qui",
    ]




def test_empty_input():

    tokenizer = Tokenizer()


    assert tokenizer.tokenize("") == []