"""Defines the functions used to call states."""
from random import randint
from screenstate import Screenstate
from dialogue import Dialogue
from effectstate import Check
from effectstate import Viewstate
from player import Player
import initialize_database

#"""Menu states"""

def startmenu():
    """Call startmenu INCOMPLETE"""
    menudia = Dialogue("Can you hear the call?", "Start Game",
                       "Load Game", "Quit", createplayer, quit, quit)
    menustate = Screenstate(
        ":) :) :) :) This is a test background", [], menudia)
    print(menustate)
    menustate.ask()


def menu(prevstate: Screenstate):
    """Call game menu. Incomplete."""
    menudia = Dialogue("Menu", "Continue Game", "Load Game",
                       "Quit", quit, quit, quit)
    menustate = Screenstate(":) :) :) :) This is a test background", [
    ], menudia)
    print(menustate)
    menustate.ask()


def createplayer():
    question = "0"
    while question != "2":
        print("Randomised stats:")
        speech = randint(1, 6)
        intelligence = randint(1, 6)
        strength = randint(1, 6)
        dexterity = randint(1, 6)
        stealth = randint(1, 6)
        print(f"Speech {speech}")
        print(f"Intelligence {intelligence}")
        print(f"Strength {strength}")
        print(f"Dexterity {dexterity}")
        print(f"Stealth {stealth}")
        print("1. Reroll stats")
        print("2. Start game")
        question = input("Roll again? ")
    newplayer = Player([stealth, speech, intelligence, strength, dexterity])
    initialize_database.delete_database(newplayer.db)
    initialize_database.initialize_database(newplayer.db)
    initialize_database.add_to_database(newplayer.db, (f"Speech {speech}"))
    initialize_database.add_to_database(
        newplayer.db, (f"Intelligence {intelligence}"))
    initialize_database.add_to_database(newplayer.db, (f"Strength {strength}"))
    initialize_database.add_to_database(
        newplayer.db, (f"Dexterity {dexterity}"))
    initialize_database.add_to_database(newplayer.db, (f"Stealth {stealth}"))

    state1()


#"""Standard game states"""

def state1():
    """Call state 1"""
    dia = Dialogue(
        "You are standing in the entrance hall of Exactum. What would you like to do?",
        "Go to Gurula",
        "Go to Komero",
        "Listen to the voice.",
        state2gurula,
        state3komero,
        state4listen)
    bg = Screenstate(":) This is the background showing Exactum. :)", [
                     "__o/\\__", "That is an example of a student"], dia)

    print("")
    print("You can hear a strange song from the hills.")
    print("Where is it coming from?")
    print("You must follow it.")
    print("You step into Exactum.")
    print("There isn't much time.")

    print(bg)
    bg.ask()


def state2gurula():
    """Call state 2, Gurula"""
    dia = Dialogue(
        "You arrive in Gurula. It is relatively empty. You see snacks and drinks. " + \
        "There is a jäärä completely immersed in whatever he is doing. " + \
        "There also an unattended laptop opposit to the jäärä.",
        "Observe the foods",
        "Observe the Jäärä",
        "Observe the laptop",
        state5food,
        quit,
        quit)
    bg = Screenstate(":) This is the background showing Gurula. :)", [
                     "__o/\\__", "That is an exampl(e of a student"], dia)

    print(bg)
    bg.ask()


def state3komero():
    """Call state 2, Komero (Intercepted)"""
    dia = Dialogue(
        "You walk up the stairs and arrive in front of Komero. " + \
        "But the Mathematician blocks the way! You can't get past the Mathematician.",
        "Talk about 'Introduction to Logic'[int]",
        "Pump that pummpauslemma [str]",
        "Try to sneak past the mathematician [ste]",
        quit,
        quit,
        quit)
    bg = Screenstate(":) This is the background showing the Mathematician :)", [
                     "__o/\\__", "That is an example of a student"], dia)

    print(bg)
    bg.ask()


def state4listen():
    """Call state 2, Gurula"""
    dia = Dialogue(
        "You listen to the voice. A nournful song that you can just barely hear calls to you. " + \
        "Time passes. How long has it been? You see a lost physicist carrying chess boards. " + \
        "You also know the Vaksi is probably working just a few meters away." + \
        "Or better even, you could check out the big lecture hall just beyond that?",
        "Talk to the Physicist",
        "Talk to the Vaksi",
        "Go to the Lecture Hall",
        quit,
        quit,
        quit)
    bg = Screenstate(":) This is the background showing Gurula. :)", [
                     "__o/\\__", "That is an example of a student"], dia)

    print(bg)
    bg.ask()


def state5food():
    """Call state 5, food"""
    dia = Dialogue(
        "You see snacks and drinks. You think you might have just enough money to buy something.",
        "Buy the noodles",
        "Buy the energy drink",
        "Take both and run [stealth]",
        quit,
        quit,
        e1_steal_ed_noodle_gurula)
    bg = Screenstate(":) This is the background showing Gurula. :)", [
                     "__o/\\__", "That is an exampl(e of a student"], dia)

    print(bg)
    bg.ask()


#"""Effect states"""

def e1_steal_ed_noodle_gurula():
    """Check stealth, steal noodle and energy drink"""
    player = Player()
    # will need input player system later

    if player.stealthcheck(18)[2]:
        print("Passed check")
    else:
        print("Failed check")

    e1 = Check(
        "This is effect-test-background",
        [],
        "You attempt to steal the noodles",
        END_1_Police,
        END_1_Police,
        "There ain't no grave can hold your noodles",
        "That could have gone better")
    print(e1)
    e1.check("stealth")


#"""ENDINGS"""

def END_1_Police():
    """Ending 1: You have been arrested."""
    dia = Dialogue(
        "The police comes for you. You wait seemingly forever, but finally " + \
        "Kumpula disappears from view and you no longer hear the song. " + \
        "Finally you drift off in a cell somewhere. You are unwaware as the END comes. " + \
        "END 1: Police",
        "It probably wasn't a good idea",
        "You dream dreamless dreams",
        "And We Come To The End",
        quit,
        quit,
        quit)
    bg = Screenstate(":) This is the background showing Gurula. :)", [
                     "__o/\\__", "That is an example of a student"], dia)

    print(bg)
    bg.ask()
