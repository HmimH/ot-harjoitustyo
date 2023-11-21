import unittest
#from ..screenstate import Screenstate
#from ..dialogue import Dialogue
#saan kahdelta ylläolevalta pelkkiä import erroreita. Korjaan vielä, mutta en tänään. 
# Alla siis 21.11. kopioidut luokat Screenstate ja Dialogue





class Dialogue:
    def __init__(self, message: str, first, second, third, firsteffect: callable, secondeffect: callable, thirdeffect: callable):
        #first etc. depict the choices that can be made. Type is not defined because it may be empty
        #or something other than a state which it usually is.
        #Message shows the prompt
        #The effects are the dialogue options' consequences
        self.first = first
        self.second = second
        self.third = third
        self.e_1 = firsteffect
        self.e_2 = secondeffect
        self.e_3 = thirdeffect
        self.message = message

        #a possibility for a def check(resulta, resultb, DC, stat)




class Screenstate:
    def __init__(self, background, icons: list, choices: Dialogue, menu: callable):
        #background is likely to be string but is not defined at this time 
        #because of potential changes with text vs. graphic interface etc.

        #icons is a list of sprites. it will be largely empty until graphic ui is implemented
        #menu us always

        #dialogue provides the options for proceeding

        self.background = background
        self.icons = icons
        self.choices = choices
        self.menu = menu

    def __str__(self):
        return (f"{self.background}\n{self.icons}\n{self.choices.message}\n 1. {self.choices.first}\n 2. {self.choices.second}\n 3. {self.choices.third}")

    def ask(self):
        choice = 0
        while choice not in ["i","m","1","2","3"]:
            choice = input("Choose: ")
        if choice == "i" or choice == "m":
            self.menu(self)
        if choice == "1":
            self.choices.e_1()
        if choice == "2":
            self.choices.e_2()
        if choice == "3":
            self.choices.e_3()







class TestScreenstates(unittest.TestCase):
    def test_init_state_creates_the_right_state_str(self):
        s = Screenstate("Background", ["a","b","c"],Dialogue("message", "1", "2", "3", quit, quit, quit), quit)
        h = str(s)
        self.assertEqual(h, f"Background\n{['a', 'b', 'c']}\nmessage\n 1. 1\n 2. 2\n 3. 3")
