import unittest
from unittest.mock import Mock
from main_AI import Main_AI

class test_main_AI(unittest.TestCase):
    def setUp(self):
        self.ai = Main_AI()

    def test_move_is_played(self):
        self.ai.play("PPPPP", "P")
        self.assertEqual(self.ai.play("PPPPP", "R"), "S")

    def test_playing_counter_move(self):
        self.ai.play("RP", "S")
        self.ai.play("RP", "S")
        self.ai.play("RP", "R")
        self.assertEqual(self.ai.play("RP", "P"), "R")

    def test_add_credits(self):
        moves = ["R", "R", "R", "R", "P"]
        self.ai.add_credits(moves, "S")
        self.assertEqual(self.ai.display_credits(), [1, 1, 1, 1, -1])