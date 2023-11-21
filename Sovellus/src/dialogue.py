

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
