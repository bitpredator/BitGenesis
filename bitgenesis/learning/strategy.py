from __future__ import annotations


from bitgenesis.learning.experience import Experience



class LearningStrategy:
    """
    Base learning strategy.

    Provides the default learning contract
    used by the LearningEngine.

    Future implementations may extend this class
    with specialized strategies:

    - reinforcement learning
    - pattern extraction
    - memory optimization
    - behavioral adaptation
    """


    def learn(
        self,
        experience: Experience,
    ):
        """
        Processes one experience.

        Default implementation returns the
        unchanged experience metadata.

        Specialized strategies should override
        this method.
        """


        return {
            "strategy": self.__class__.__name__,
            "experience_id": experience.id,
            "reward": experience.reward(),
            "processed": True,
        }