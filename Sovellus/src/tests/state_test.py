import unittest
from unittest.mock import patch
from screenstate import Screenstate
from dialogue import Dialogue


class TestScreenstates(unittest.TestCase):
    """Tests for testing the screenstate-class"""    

    def test_init_state_creates_the_right_state_str(self):
        """Tests if the created state matches the intended."""
        s = Screenstate("Background", ["a", "b", "c"], Dialogue(
            "message", "1", "2", "3", quit, quit, quit))
        h = str(s)
        self.assertEqual(
            h, f"Background\n{['a', 'b', 'c']}\nmessage\n 1. 1\n 2. 2\n 3. 3")
