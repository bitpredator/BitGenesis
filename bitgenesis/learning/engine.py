from __future__ import annotations


from bitgenesis.learning.experience import Experience
from bitgenesis.learning.strategy import LearningStrategy



class LearningEngine:
    """
    Coordinates learning operations.

    Current responsibilities:

    - store experiences
    - execute learning strategies
    - expose learning statistics

    Future responsibilities:

    - model adaptation
    - knowledge consolidation
    - autonomous improvement
    """


    def __init__(
        self,
        strategies: list[LearningStrategy] | None = None,
    ):


        self.strategies = (
            strategies
            or []
        )


        self.experiences: list[Experience] = []



    # --------------------------------------------------
    # Experience management
    # --------------------------------------------------


    def remember(
        self,
        experience: Experience,
    ) -> None:
        """
        Stores a new experience.
        """


        self.experiences.append(
            experience
        )



    def learn(
        self,
        experience: Experience,
    ):
        """
        Processes an experience
        through registered strategies.
        """


        self.remember(
            experience
        )


        results = []


        for strategy in self.strategies:

            results.append(
                strategy.learn(
                    experience
                )
            )


        return results



    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------


    @property
    def experience_count(
        self,
    ) -> int:

        return len(
            self.experiences
        )


    def clear(
        self,
    ) -> None:

        self.experiences.clear()