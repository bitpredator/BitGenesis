from __future__ import annotations

from enum import Enum


class Intent(Enum):
    """
    High-level user intention.

    Intents represent what the user is trying
    to achieve rather than the exact wording.

    Future versions may introduce:
    - confidence scores
    - hierarchical intents
    - intent composition
    """

    UNKNOWN = "unknown"

    QUESTION = "question"

    STATEMENT = "statement"

    COMMAND = "command"

    GREETING = "greeting"

    FAREWELL = "farewell"

    CONFIRMATION = "confirmation"

    NEGATION = "negation"

    HELP = "help"

    INFORMATION_REQUEST = "information_request"

    CREATOR_QUERY = "creator_query"

    IDENTITY_QUERY = "identity_query"