import unittest
from trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_add_node_single_sequence(self):
        self.trie.add_node("RPS")

        self.assertEqual(self.trie.frequency("RPS"), 1)
        self.assertEqual(self.trie.frequency("PS"), 1)

        self.assertEqual(self.trie.frequency("RP"), 0)
        self.assertEqual(self.trie.frequency("R"), 0)

    def test_add_node_multiple_sequences(self):
        self.trie.add_node("RPS")
        self.trie.add_node("RPR")

        self.assertEqual(self.trie.frequency("RPS"), 1)
        self.assertEqual(self.trie.frequency("RPR"), 1)
        self.assertEqual(self.trie.frequency("RP"), 0)
        self.assertEqual(self.trie.frequency("PR"), 1) 

    def test_frequency_list(self):
        self.trie.add_node("RPS")
        self.trie.add_node("RPR")
        self.trie.add_node("RPS")

        freq_list = self.trie.frequency_list("RP")
        self.assertIn(('S', 2), freq_list)
        self.assertIn(('R', 1), freq_list)

        self.assertEqual(self.trie.frequency_list("XYZ"), [])

    def test_next_move(self):
        self.trie.add_node("RPS")
        self.trie.add_node("RPR")
        self.trie.add_node("RPS")

        self.assertEqual(self.trie.next_move("RP"), 'S')

        self.assertIsNone(self.trie.next_move("XYZ"))

