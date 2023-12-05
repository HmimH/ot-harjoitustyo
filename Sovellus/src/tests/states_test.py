import unittest
from screenstate import Screenstate
from dialogue import Dialogue


class TestClasses(unittest.TestCase):
    """Tests for various classes"""

    def test_init_dialogue_creates_the_right_dialogue_str(self):
        """Tests if the created dialogue matches the intended"""
        h = str(Dialogue("message", "1", "2", "3", quit, quit, quit))
        self.assertEqual(
            h,
            "Message: 'message'\\ln1'1'  2'2" +
            f"' 3'3'\\ln1.e'{str(quit)} 2.e'{str(quit)} 3.e'{str(quit)}")

    def test_init_state_creates_the_right_state_str(self):
        """Tests if the created state matches the intended."""
        s = Screenstate("Background", ["a", "b", "c"], Dialogue(
            "message", "1", "2", "3", quit, quit, quit))
        h = str(s)
        self.assertEqual(
            h, f"Background\n{['a', 'b', 'c']}\nmessage" +
            "\n 1. 1 \n 2. 2\n 3. 3")
