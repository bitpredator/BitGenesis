from __future__ import annotations

from bitgenesis.core.brain import Brain
from bitgenesis.cli.formatter import CLIFormatter


class ConsoleInterface:
    """
    Interactive console interface for BitGenesis.
    """


    def __init__(
        self,
        brain: Brain | None = None,
    ):

        self.brain = brain or Brain()

        self.running = False



    def start(self):

        self.running = True


        print()

        print(
            f"BitGenesis Cognitive System v{self.brain.version}"
        )

        print(
            "Type '/help' for commands."
        )

        print(
            "Type '/exit' to shutdown."
        )

        print()



        while self.running:

            try:

                user_input = input("> ").strip()


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
                    f"[ERROR] {exc}"
                )




    def handle_command(
        self,
        command: str,
    ):

        command = command.lower()



        if command == "/exit":

            self.shutdown()

            return



        if command == "/help":

            self.help()

            return



        if command == "/stats":

            print(
                self.brain.stats()
            )

            return



        if command == "/memory":

            memories = self.brain.remember()

            print(
                memories
            )

            return



        if command == "/learning":

            print(
                CLIFormatter.learning(
                    self.brain.learning_stats()
                )
            )

            return



        print(
            f"Unknown command: {command}"
        )




    def help(self):

        print(
            """
Available commands:

/help       Show commands
/stats      Show brain statistics
/memory     Show memories
/learning   Show learning statistics
/exit       Shutdown BitGenesis

Anything else is interpreted as a cognitive request.
"""
        )




    def shutdown(self):

        self.running = False


        print(
            "BitGenesis shutdown."
        )