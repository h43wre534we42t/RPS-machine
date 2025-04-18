from AI import AI
import unittest
from trie import Trie
import random

class TestAI(unittest.TestCase):
    def setUp(self):
        self.memory = Trie()
        self.ai1 = AI(1, self.memory)

    def test_decide_move_returns_counter_move(self):
        self.memory.add_node("RPS")  #adds "RPS" and "PS"

        result = self.ai1.decide_move("XXRP")
        self.assertEqual(result, 'R')

        result = self.ai1.decide_move("XXXP")
        self.assertEqual(result, 'R')

        self.assertEqual(self.memory.frequency("RP"), 0)
        result = self.ai1.decide_move("XXXR")
        self.assertIsNone(result)


    def test_decide_move_returns_none_if_no_pattern(self):
        result = self.ai1.decide_move("RPS")
        self.assertIsNone(result)

    def test_random_move_returns_random_move(self):
        for _ in range(1000):
            move = self.ai1.random_move()
            self.assertIn(move, ["R", "P", "S"])

    def test_decide_move_respects_lookback(self):
        self.memory.add_node("RPS")
        result = self.ai1.decide_move("PPPPRP")
        self.assertEqual(result, "R")

    def test_decide_move_with_short_input(self):
        self.memory.add_node("RPS")
        result = self.ai1.decide_move("S")
        self.assertIsNone(result)

    def test_random_move_with_seed(self):
        random.seed(42)
        move1 = self.ai1.random_move()
        random.seed(42) 
        self.assertEqual(move1, self.ai1.random_move())

    def test_credit_attribute_exists(self):
        self.assertEqual(self.ai1.credit, 0)
        self.ai1.credit = 10
        self.assertEqual(self.ai1.credit, 10)


