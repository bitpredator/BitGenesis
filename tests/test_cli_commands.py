from bitgenesis.cli.console import ConsoleInterface


class DummyBrain:
    """
    Minimal fake brain for CLI testing.
    """

    version = "0.3.0-dev"

    def __init__(self):
        self.shutdown_called = False

    def stats(self):
        return {
            "state": "idle",
            "memories": 0,
            "knowledge": 0,
        }

    def remember(self):
        return []

    def ask(self, text):
        return f"echo: {text}"



def test_console_creation():

    console = ConsoleInterface(
        brain=DummyBrain()
    )

    assert console.brain is not None
    assert console.running is False



def test_help_command(capsys):

    console = ConsoleInterface(
        brain=DummyBrain()
    )

    console.handle_command(
        "/help"
    )

    captured = capsys.readouterr()

    assert "/help" in captured.out
    assert "/exit" in captured.out



def test_stats_command(capsys):

    console = ConsoleInterface(
        brain=DummyBrain()
    )

    console.handle_command(
        "/stats"
    )

    captured = capsys.readouterr()

    assert "idle" in captured.out



def test_memory_command(capsys):

    console = ConsoleInterface(
        brain=DummyBrain()
    )

    console.handle_command(
        "/memory"
    )

    captured = capsys.readouterr()

    assert "[]" in captured.out



def test_unknown_command(capsys):

    console = ConsoleInterface(
        brain=DummyBrain()
    )

    console.handle_command(
        "/unknown"
    )

    captured = capsys.readouterr()

    assert "Unknown command" in captured.out



def test_exit_command():

    console = ConsoleInterface(
        brain=DummyBrain()
    )

    console.running = True

    console.handle_command(
        "/exit"
    )

    assert console.running is False



def test_console_brain_request():

    console = ConsoleInterface(
        brain=DummyBrain()
    )

    response = console.brain.ask(
        "hello"
    )

    assert response == "echo: hello"