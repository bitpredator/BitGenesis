from bitgenesis.perception.detector import ModalityDetector
from bitgenesis.perception.perception import Perception


class PerceptionBuilder:
    """
    Builds Perception objects from external inputs.
    """

    def __init__(self):

        self._detector = ModalityDetector()

    def build(self, input_data) -> Perception:

        modality = self._detector.detect(input_data)

        return Perception(
            raw_input=input_data,
            modality=modality.value,
        )