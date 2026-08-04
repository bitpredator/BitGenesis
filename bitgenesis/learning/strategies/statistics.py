from __future__ import annotations


from collections import Counter

from bitgenesis.learning.experience import Experience
from bitgenesis.learning.strategy import LearningStrategy



class StatisticsLearningStrategy(LearningStrategy):
    """
    Learning strategy based on experience statistics.

    Current responsibilities:

    - count experiences
    - track success rate
    - track failure rate
    - collect metadata statistics

    Future extensions:

    - pattern detection
    - behavioral analysis
    - adaptation signals
    """


    def __init__(self):

        self.total_experiences = 0

        self.successful_experiences = 0

        self.failed_experiences = 0

        self.states = Counter()

        self.metadata = Counter()



    def learn(
        self,
        experience: Experience,
    ) -> dict:
        """
        Processes one experience.
        """


        self.total_experiences += 1


        if experience.success:

            self.successful_experiences += 1

        else:

            self.failed_experiences += 1



        state = experience.metadata.get(
            "state"
        )


        if state:

            self.states[state] += 1



        for key, value in experience.metadata.items():

            self.metadata[
                key
            ] += 1



        return self.statistics()



    @property
    def success_rate(self) -> float:

        if self.total_experiences == 0:

            return 0.0


        return (
            self.successful_experiences
            /
            self.total_experiences
        )



    @property
    def failure_rate(self) -> float:

        if self.total_experiences == 0:

            return 0.0


        return (
            self.failed_experiences
            /
            self.total_experiences
        )



    def statistics(
        self,
    ) -> dict:
        """
        Returns current learning statistics.
        """


        return {

            "total": self.total_experiences,

            "successful": (
                self.successful_experiences
            ),

            "failed": (
                self.failed_experiences
            ),

            "success_rate": (
                self.success_rate
            ),

            "failure_rate": (
                self.failure_rate
            ),

            "states": dict(
                self.states
            ),

            "metadata": dict(
                self.metadata
            ),
        }