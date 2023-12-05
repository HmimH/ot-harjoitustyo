"""Specialised classes: Viewstate class, for non dialogue screens, 
Check for skill-checks"""

from dialogue import Dialogue
from screenstate import Screenstate
from random import randint
from player import Player


class Viewstate:
    """Calls an individual scene in the game. Offers no options."""

    def __init__(self, background, icons=[], message="", next=quit, choice1=""):  # pylint: disable = dangerous-default-value
        """Creates an effectstate"""
        self.background = background
        self.icons = icons
        self.message = message
        self.next = next
        self.choice1 = choice1
        # self.effect = effect #this is likely a callable for 
        # printing whatever is specific to the state
        # but also including sleep() and such. May be changed later

    def __str__(self):
        """Turns the state into a string. Mainly for testing."""
        return f"{self.background}\n{self.icons}\n{self.message}" + \
            f"\n 1. {self.choice1}"

    def ask(self):
        """Creates the choice function, calls the next state"""
        choice = 0
        while choice not in ["i", "m", "1", ""]:
            choice = input("Choose: ")
        if choice == "i" or choice == "m":
            self.menu()
        if choice == "1" or choice == "":
            self.next()

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


class Check:
    """Calls an individual scene in the game. Offers no options."""

    def __init__(self, background, icons=[], message="", nextsuccess=quit, nextfail=quit, choicesuccess="", choicesfail=""):  # pylint: disable = dangerous-default-value
        """Creates an effectstate"""
        self.background = background
        self.icons = icons
        self.message = message
        self.next = nextsuccess
        self.choice = choicesuccess
        self.nextf = nextfail
        self.choicef = choicesfail
        # succeeds bby default
        # self.effect = effect #this is likely a callable for printing whatever is specific to the state
        # but also including sleep() and such. May be changed later

    def __str__(self):
        """Turns the state into a string. Mainly for testing."""
        return f"{self.background}\n{self.icons}\n{self.message}"

    def check(self, stat, dc=10, player=Player()):
        """Creates the choice function, calls the next state"""
        print("Fortune favours the bold?")
        if stat == "intelligence":
            checkresult = player.intelligencehcheck(dc)
        elif stat == "stealth":
            checkresult = player.stealthcheck(dc)
        elif stat == "speech":
            checkresult = player.speechcheck(dc)
        elif stat == "dexterity":
            checkresult = player.dexteritythcheck(dc)
        elif stat == "strength":
            checkresult = player.strengthcheck(dc)
        if checkresult[2]:
            print("Passed check")
        else:
            print("Failed check")
            self.next = self.nextf
            self.choice = self.choicef
        print(f"Required: {dc}")
        print(f"Your roll: {checkresult[0]}")
        print(f"Your stat: {checkresult[1]}")
        print(f"Your total: {checkresult[0] + checkresult[1]}")

        print(f"1. {self.choice}")
        choice = 0
        while choice not in ["i", "m", "1", ""]:
            choice = input("Choose: ")
        if choice == "i" or choice == "m":
            self.menu()
        if choice == "1" or choice == "":
            self.next()

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
