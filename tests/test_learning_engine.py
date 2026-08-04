from bitgenesis.learning.engine import LearningEngine

from bitgenesis.learning.experience import Experience



def test_learning_engine_creation():

    engine = LearningEngine()

    assert engine is not None



def test_learning_engine_observes_experience():

    engine = LearningEngine()


    experience = Experience(
        input_data="question",
        output_data="answer",
        success=True,
    )


    result = engine.learn(
        experience
    )


    assert result is not None



def test_learning_engine_stores_experience():

    engine = LearningEngine()


    experience = Experience(
        input_data="hello",
        output_data="response",
        success=True,
    )


    engine.learn(
        experience
    )


    assert len(
        engine.experiences
    ) == 1