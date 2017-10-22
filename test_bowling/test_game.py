import unittest

class GameTest(unittest.TestCase):
    def test_new_game_returns_zero(self):
        from bowling.game import new_game
        new_game_value = new_game()
        self.assertEqual(new_game_value, 0)
