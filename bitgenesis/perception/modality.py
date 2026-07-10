from enum import Enum


class PerceptionModality(str, Enum):
    """
    Supported perception modalities.
    """

    TEXT = "text"

    IMAGE = "image"

    AUDIO = "audio"

    VIDEO = "video"

    EVENT = "event"

    SENSOR = "sensor"

    TOOL = "tool"

    UNKNOWN = "unknown"