# Tests the condorcet_criterion function.

import unittest
from democratic_failures.condorcet_criterion import condorcet


class TestCondorcet(unittest.TestCase):
    # test function to test equality of two value
    def test_condorcet(self):
        simple_votes = [["A"], ["B"], ["B"]]
        condorcet_votes = [["A", "B", "C"], ["A", "B", "C"], ["A", "B", "C"],
                           ["B", "C", "A"], ["B", "C", "A"]]
        paradox_votes = [["A", "B", "C"], ["B", "C", "A"], ["C", "A", "B"]]
        simple_result = condorcet(simple_votes, "B")
        # B is the Borda count winner
        condorcet_violated_result = condorcet(condorcet_votes, "B")
        # A is preferred by 3 voters to all alternatives, making it the condorcet winner
        condorcet_satisfied_result = condorcet(condorcet_votes, "A")
        paradox_result = condorcet(paradox_votes, "C")
        # assertEqual() to check equality of first & second value
        self.assertEqual(simple_result, True)
        self.assertEqual(condorcet_violated_result, False)
        self.assertEqual(condorcet_satisfied_result, True)
        self.assertEqual(paradox_result, False)


if __name__ == '__main__':
    unittest.main()