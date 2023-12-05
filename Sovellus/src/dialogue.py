"""

First etc. depict the choices that can be made. Type not defined because it may be empty
or something other than a state which it usually is.
Message shows the prompt
The effects are the dialogue options' consequences

"""


class Dialogue:
    """Offers the dialogue options. Mainly for use within the screenstate-class."""

    def __init__(self, message="", first="", second="", third="",
                 firsteffect=quit, secondeffect=quit, thirdeffect=quit):
        """Creates the Dialogue"""
        self.first = first
        self.second = second
        self.third = third
        self.e_1 = firsteffect
        self.e_2 = secondeffect
        self.e_3 = thirdeffect
        self.message = message

    def __str__(self):
        """Creates a string. Mainly for testing."""
        return (
            f"Message: '{self.message}'\\ln1'{self.first}'  2'{self.second}" +
            f"' 3'{self.third}'\\ln1.e'{str(self.e_1)} 2.e'{str(self.e_2)} 3.e'{str(self.e_3)}")
