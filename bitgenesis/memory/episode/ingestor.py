from __future__ import annotations


class EpisodeIngestor:
    """
    Ingests memories into the episodic memory system.

    Responsibilities:
    - receive memory objects
    - forward them to the episode manager

    Future versions may implement:
    - temporal segmentation
    - execution boundaries
    - semantic grouping
    - episode lifecycle management
    """

    def __init__(
        self,
        episode_manager,
    ):

        self.episode_manager = episode_manager

    def ingest(
        self,
        memory,
    ) -> None:
        """
        Ingest a memory object.
        """

        if memory is None:
            return

        append = getattr(
            self.episode_manager,
            "append",
            None,
        )

        if callable(append):
            append(memory)