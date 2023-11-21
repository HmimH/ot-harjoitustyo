from time import sleep
from screenstate import Screenstate
from dialogue import Dialogue

#menu dialogue


def startmenu():
    menudia = Dialogue("Can you hear the call?", "Start Game", "Load Game", "Quit", state1, state2, quit)
    menustate = Screenstate(":) :) :) :) This is a test background", [], menudia, menu)
    print (menustate)
    menustate.ask()



def state1():
    s1dia = Dialogue("You are standing in the entrance hall of Exactum. What would you like to do?", "Go to Gurula", "Go to Komero", "Listen to the voice.", quit, quit, quit)
    s1 = Screenstate(":) This is the background showing Exactum. :)", ["__o/\__", "That is an example of a student"], s1dia, menu)

    print ("")
    sleep(2)
    print("You can hear a strange song from the hills.")
    sleep(2.5)
    print("Where is it coming from?")
    sleep(2)
    print("You must follow it.")
    sleep (4)
    print ("You step into Exactum.")
    sleep (1.7)
    print ("There isn't much time.")

    print (s1)
    s1.ask()



def state2():
    print ("Hello 2")

def menu(prevstate: Screenstate):
    menudia = Dialogue("Menu", "Continue Game", "Load Game", "Quit", state1, state2, quit)
    menustate = Screenstate(":) :) :) :) This is a test background", [], menudia, prevstate)
    print(menustate)
    menustate.ask()





