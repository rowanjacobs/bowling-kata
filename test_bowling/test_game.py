import unittest
from bowling.game import Game

class GameTest(unittest.TestCase):
    def test_new_game_returns_zero(self):
        new_game = Game()
        self.assertEqual(new_game.score, 0)

    def test_roll_first_roll_returns_pins(self):
        game = Game()
        pins = 7
        game.roll(pins)
        self.assertEqual(game.score, pins)

    def test_roll_adds_pins_to_roll(self):
        game = Game()
        score = 5
        game.roll(score)
        pins = 7
        game.roll(pins)
        self.assertEqual(game.score, score+pins)

    # spare
    def test_roll_spare(self):
        pass

    # strike
    def test_roll_strike(self):
        pass
