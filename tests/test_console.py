from bitgenesis.cli.console import ConsoleInterface


class FakeBrain:
    """
    Minimal fake brain for CLI tests.
    """

    version = "0.3.0-dev"


    def __init__(self):

        self.questions = []


    def ask(
        self,
        question,
    ):

        self.questions.append(
            question
        )

        return "Fake cognitive response."


    def stats(self):

        return {
            "state": "idle",
            "cycles": 1,
        }


    def remember(self):

        return [
            "memory one",
            "memory two",
        ]



def test_console_initialization():

    brain = FakeBrain()

    console = ConsoleInterface(
        brain=brain
    )


    assert console.brain is brain

    assert console.running is False



def test_console_processes_question(
    monkeypatch,
    capsys,
):

    brain = FakeBrain()

    console = ConsoleInterface(
        brain=brain
    )


    inputs = iter(
        [
            "Hello BitGenesis",
            "/exit",
        ]
    )


    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )


    console.start()


    assert (
        "Hello BitGenesis"
        in brain.questions
    )


    output = capsys.readouterr().out


    assert (
        "Fake cognitive response."
        in output
    )



def test_console_help_command(
    monkeypatch,
    capsys,
):

    brain = FakeBrain()

    console = ConsoleInterface(
        brain=brain
    )


    inputs = iter(
        [
            "/help",
            "/exit",
        ]
    )


    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )


    console.start()


    output = capsys.readouterr().out


    assert (
        "Available commands"
        in output
    )



def test_console_stats_command(
    monkeypatch,
    capsys,
):

    brain = FakeBrain()

    console = ConsoleInterface(
        brain=brain
    )


    inputs = iter(
        [
            "/stats",
            "/exit",
        ]
    )


    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )


    console.start()


    output = capsys.readouterr().out


    assert (
        "idle"
        in output
    )



def test_console_memory_command(
    monkeypatch,
    capsys,
):

    brain = FakeBrain()

    console = ConsoleInterface(
        brain=brain
    )


    inputs = iter(
        [
            "/memory",
            "/exit",
        ]
    )


    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )


    console.start()


    output = capsys.readouterr().out


    assert (
        "memory one"
        in output
    )



def test_console_exit_command(
    monkeypatch,
):

    brain = FakeBrain()

    console = ConsoleInterface(
        brain=brain
    )


    inputs = iter(
        [
            "/exit",
        ]
    )


    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )


    console.start()


    assert console.running is False