from bitgenesis.cli.console import ConsoleInterface
from bitgenesis.core.brain import Brain



def test_learning_command(capsys):

    console = ConsoleInterface(
        Brain()
    )


    console.handle_command(
        "/learning"
    )


    output = capsys.readouterr().out


    assert "Learning Statistics" in output

    assert "Experiences:" in output




def test_learning_after_question(capsys):

    brain = Brain()


    brain.ask(
        "Who created you?"
    )


    console = ConsoleInterface(
        brain
    )


    console.handle_command(
        "/learning"
    )


    output = capsys.readouterr().out


    assert "Learning Statistics" in output

    assert "Experiences:" in output

    assert "Successful:" in output

    assert "Failed:" in output