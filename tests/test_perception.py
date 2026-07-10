from bitgenesis.perception import (
    Perception,
    PerceptionBuilder,
    PerceptionModality,
    ModalityDetector,
)


def test_perception_creation():

    perception = Perception(
        raw_input="hello",
    )

    assert perception.raw_input == "hello"

    assert perception.modality == "text"

    assert perception.language is None

    assert perception.source is None

    assert perception.metadata == {}


def test_perception_builder_text_input():

    builder = PerceptionBuilder()

    perception = builder.build("hello world")

    assert isinstance(perception, Perception)

    assert perception.raw_input == "hello world"

    assert perception.modality == "text"


def test_modality_detector_text():

    detector = ModalityDetector()

    result = detector.detect(
        "hello"
    )

    assert result == PerceptionModality.TEXT


def test_modality_detector_unknown():

    detector = ModalityDetector()

    result = detector.detect(
        12345
    )

    assert result == PerceptionModality.UNKNOWN


def test_perception_metadata():

    perception = Perception(
        raw_input="data",
        metadata={
            "source": "test",
        },
    )

    assert perception.metadata["source"] == "test"