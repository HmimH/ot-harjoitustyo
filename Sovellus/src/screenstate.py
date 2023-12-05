"""
background is likely to be string but is not defined at this time
because of potential changes with text vs. graphic interface etc.

icons is a list of sprites. it will be largely empty until graphic ui is implemented
menu us always

dialogue provides the options for proceeding
"""

from dialogue import Dialogue


class Screenstate:
    """Calls an individual scene in the game. Offers options through a Dialogue."""

    def __init__(self, background, icons=[], choices=Dialogue()):  # pylint: disable = dangerous-default-value
        # hope that's okay, icons must be able to be empty
        """Creates a screenstate"""
        self.background = background
        self.icons = icons
        self.choices = choices

    def __str__(self):
        """Turns the state into a string. Mainly for testing."""
        return f"{self.background}\n{self.icons}\n{self.choices.message}" + \
            f"\n 1. {self.choices.first} \n 2. {self.choices.second}\n 3. {self.choices.third}"

    def ask(self):
        """Creates the choice function, calls the next state"""
        choice = 0
        while choice not in ["i", "m", "1", "2", "3"]:
            choice = input("Choose: ")
        if choice == "i" or choice == "m":
            self.menu()
        if choice == "1":
            self.choices.e_1()
        if choice == "2":
            self.choices.e_2()
        if choice == "3":
            self.choices.e_3()

    def menu():
        """A menu function for saving, continuing etc. Incomplete."""
        state1 = quit  # temporary
        state2 = quit  # temporary
        menudia = Dialogue("Can you hear the call?", "Start Game",
                           "Load Game", "Quit", state1, state2, quit)
        menustate = Screenstate(
            ":) :) :) :) This is a test background", [], menudia)
        print(menustate)
        menustate.ask()
