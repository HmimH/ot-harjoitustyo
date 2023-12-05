"""Player class, including the stats and methods for accessing them"""

from random import randint
import sqlite3


class Player:
    """Player class"""

    def __init__(self, stats=[5, 5, 5, 5, 5]):
        """Create a player class"""
        self.stealth = stats[0]
        self.speech = stats[1]
        self.intelligence = stats[2]
        self.strength = stats[3]
        self.dexterity = stats[4]
        self.db = sqlite3.connect("eventlog.db")

    def stealthcheck(self, dc):
        """Stealth stat check"""
        # animation maybe?
        roll = randint(1, 6) + randint(1, 6)
        if self.stealth + roll >= dc:
            return (roll, self.stealth, True)
        else:
            return (roll, self.stealth, False)

    def intelligencehcheck(self, dc):
        """Intelligence stat check"""
        # animation maybe?
        roll = randint(1, 6) + randint(1, 6)
        if self.intelligence + roll >= dc:
            return (roll, self.intelligence, True)
        return (roll, self.intelligence, False)

    def speechcheck(self, dc):
        """Speech stat check"""
        # animation maybe?
        roll = randint(1, 6) + randint(1, 6)
        if self.speech + roll >= dc:
            return (roll, self.speech, True)
        return (roll, self.speech, False)

    def strengthcheck(self, dc):
        """Strength stat check"""
        # animation maybe?
        roll = randint(1, 6) + randint(1, 6)
        if self.strength + roll >= dc:
            return (roll, self.strength, True)
        return (roll, self.strength, False)

    def dexteritythcheck(self, dc):
        """Dexterity stat check"""
        # animation maybe?
        roll = randint(1, 6) + randint(1, 6)
        if self.dexterity + roll >= dc:
            return (roll, self.dexterity, True)
        return (roll, self.dexterity, False)

        # connections to the database
        # database will be applied through the player class
        # will have to include: stats, inventory, time left,
        # visited lockable states true or false, most recent state
