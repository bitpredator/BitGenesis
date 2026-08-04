from __future__ import annotations

from bitgenesis.core.brain import Brain

from bitgenesis.cli.commands import CLICommand
from bitgenesis.cli.formatter import ConsoleFormatter



class ConsoleInterface:
    """
    Interactive console interface for BitGenesis.

    Responsibilities:

    - interact with users
    - route commands
    - expose runtime controls
    - display cognitive responses
    """


    def __init__(
        self,
        brain: Brain | None = None,
    ):

        self.brain = brain or Brain()

        self.formatter = ConsoleFormatter()

        self.running = False



    # ==================================================
    # Lifecycle
    # ==================================================

    def start(
        self,
    ):

        self.running = True


        print(
            self.formatter.banner(
                self.brain.version
            )
        )


        while self.running:

            try:

                user_input = input(
                    "> "
                ).strip()


                if not user_input:

                    continue


                if user_input.startswith("/"):

                    self.handle_command(
                        user_input
                    )

                    continue


                response = self.brain.ask(
                    user_input
                )


                if response is None:

                    print(
                        "No cognitive response generated."
                    )

                else:

                    print(
                        response
                    )



            except KeyboardInterrupt:

                print()

                self.shutdown()



            except Exception as exc:

                print(
                    self.formatter.error(
                        str(exc)
                    )
                )



    # ==================================================
    # Command Router
    # ==================================================

    def handle_command(
        self,
        command: CLICommand | str,
    ):

        # Compatibility with old tests/API
        if isinstance(
            command,
            str,
        ):

            command = CLICommand(
                command
            )



        if command.name == "/exit":

            self.shutdown()

            return



        if command.name == "/help":

            self.help()

            return



        if command.name == "/stats":

            print(
                self.brain.stats()
            )

            return



        if command.name == "/memory":

            memories = self.brain.remember()


            if not memories:

                print(
                    memories
                )

            else:

                print(
                    self.formatter.memory(
                        memories
                    )
                )

            return



        if command.name == "/runtime":

            self.runtime_command(
                command
            )

            return



        if command.name == "/events":

            self.events_command()

            return



        if command.name == "/learning":

            self.learning_command(
                command
            )

            return



        print(
            self.formatter.unknown_command(
                command.raw
            )
        )



    # ==================================================
    # Runtime Commands
    # ==================================================

    def runtime_command(
        self,
        command: CLICommand,
    ):

        runtime = getattr(
            self.brain,
            "runtime",
            None,
        )


        if runtime is None:

            print(
                "Runtime unavailable."
            )

            return



        action = command.argument(
            0
        )



        if action == "start":

            runtime.start()

            print(
                "Runtime started."
            )

            return



        if action == "stop":

            runtime.stop()

            print(
                "Runtime stopped."
            )

            return



        if action == "tick":

            result = runtime.tick()

            print(
                self.formatter.runtime(
                    "tick",
                    result
                )
            )

            return



        if action == "snapshot":

            snapshot = runtime.snapshot()

            print(
                snapshot
            )

            return



        if action == "status":

            print(
                self.formatter.status(
                    {
                        "running":
                            runtime.running,

                        "services":
                            len(
                                runtime.list_services()
                            ),
                    }
                )
            )

            return



        print(
            "Usage: /runtime <status|start|stop|tick|snapshot>"
        )



    # ==================================================
    # Events
    # ==================================================

    def events_command(
        self,
    ):

        bus = getattr(
            self.brain,
            "event_bus",
            None,
        )


        if bus is None:

            print(
                "EventBus unavailable."
            )

            return



        print(
            self.formatter.events(
                bus.subscriber_count()
            )
        )



    # ==================================================
    # Learning
    # ==================================================

    def learning_command(
        self,
        command: CLICommand,
    ):

        engine = getattr(
            self.brain,
            "learning_engine",
            None,
        )


        if engine is None:

            print(
                "LearningEngine unavailable."
            )

            return



        action = command.argument(
            0
        )


        if action == "stats":

            print(
                engine.statistics()
            )

            return



        print(
            "Usage: /learning stats"
        )



    # ==================================================
    # Help
    # ==================================================

    def help(
        self,
    ):

        print(
            """
Available commands:

/help                   Show commands

/stats                  Brain statistics

/memory                 Stored memories


/runtime status         Runtime status
/runtime start          Start runtime
/runtime stop           Stop runtime
/runtime tick           Execute runtime tick
/runtime snapshot       Runtime snapshot


/events                 EventBus information


/learning stats         Learning statistics


/exit                   Shutdown BitGenesis


Anything else is interpreted as a cognitive request.
"""
        )



    # ==================================================
    # Shutdown
    # ==================================================

    def shutdown(
        self,
    ):

        self.running = False


        print(
            "BitGenesis shutdown."
        )