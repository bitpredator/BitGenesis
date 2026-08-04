from __future__ import annotations


from abc import ABC, abstractmethod


from bitgenesis.learning.experience import Experience



class LearningStrategy(ABC):
    """
    Base interface for learning strategies.

    Future implementations may include:

    - reinforcement learning
    - pattern extraction
    - memory optimization
    - behavioral adaptation
    """


    @abstractmethod
    def learn(
        self,
        experience: Experience,
    ):
        """
        Processes one experience.
        """

        raise NotImplementedError