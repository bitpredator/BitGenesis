from bitgenesis.learning.experience import Experience


def test_experience_creation():

    experience = Experience(
        input_data="hello",
        output_data="world",
        success=True,
    )

    assert experience is not None

    assert experience.input_data == "hello"

    assert experience.output_data == "world"

    assert experience.success is True



def test_experience_default_values():

    experience = Experience(
        input_data="test",
        output_data=None,
    )

    assert experience.success is False