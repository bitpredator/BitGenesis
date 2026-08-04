from bitgenesis.learning.strategy import LearningStrategy


class TestStrategy(LearningStrategy):
    """
    Concrete implementation for testing.
    """

    def learn(
        self,
        experience,
    ):

        return {
            "learned": True,
            "experience": experience,
        }



def test_strategy_creation():

    strategy = TestStrategy()

    assert strategy is not None



def test_strategy_can_learn():

    strategy = TestStrategy()


    result = strategy.learn(
        {
            "success": True
        }
    )


    assert result is not None

    assert result["learned"] is True