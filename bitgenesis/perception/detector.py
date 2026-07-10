from bitgenesis.perception.modality import PerceptionModality


class ModalityDetector:
    """
    Detects the modality of an incoming stimulus.

    This initial implementation always assumes text.
    """

    def detect(self, input_data) -> PerceptionModality:

        if isinstance(input_data, str):

            return PerceptionModality.TEXT

        return PerceptionModality.UNKNOWN