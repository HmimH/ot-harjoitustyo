"""Defines the functions used to call states."""
from screenstate import Screenstate
from dialogue import Dialogue




def startmenu():
    """Call startmenu"""
    menudia = Dialogue("Can you hear the call?", "Start Game",
                       "Load Game", "Quit", state1, state2, quit)
    menustate = Screenstate(
        ":) :) :) :) This is a test background", [], menudia)
    print(menustate)
    menustate.ask()


def state1():
    """Call state 1"""
    s1dia = Dialogue(
        "You are standing in the entrance hall of Exactum. What would you like to do?",
        "Go to Gurula",
        "Go to Komero",
        "Listen to the voice.",
        quit,
        quit,
        quit)
    s1 = Screenstate(":) This is the background showing Exactum. :)", [
                     "__o/\\__", "That is an example of a student"], s1dia)

    print("")
    print("You can hear a strange song from the hills.")
    print("Where is it coming from?")
    print("You must follow it.")
    print("You step into Exactum.")
    print("There isn't much time.")

    print(s1)
    s1.ask()


def state2():
    """Call state 2. Incomplete"""
    print("Hello 2")


def menu(prevstate: Screenstate):
    """Call game menu. Incomplete."""
    menudia = Dialogue("Menu", "Continue Game", "Load Game",
                       "Quit", state1, state2, quit)
    menustate = Screenstate(":) :) :) :) This is a test background", [
    ], menudia)
    print(menustate)
    menustate.ask()
