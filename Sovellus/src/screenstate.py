from dialogue import Dialogue

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
