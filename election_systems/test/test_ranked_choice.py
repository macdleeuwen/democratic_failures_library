# Tests the ranked choice function.

import unittest
from election_systems.ranked_choice import ranked_choice


class TestRankedChoice(unittest.TestCase):
    # test function to test equality of two value
    def test_irv_simple(self):
        ranked_votes_two = [["A", "C", "B"], ["A", "C", "B"], ["A", "B", "C"], ["A", "B", "C"],
                               ["A", "B", "C"], ["A", "B", "C"],  ["B", "C", "A"],  ["B", "C", "A"],
                               ["B", "C", "A"], ["B", "A", "C"], ["B", "A", "C"], ["C", "A", "B"],
                               ["C", "A", "B"], ["C", "A", "B"], ["C", "A", "B"], ["C", "A", "B"],
                               ["C", "A", "B"]]
        ranked_vote_result_two = ["C", "A", "B"]
        ranked_votes = [["C", "B", "A"], ["C", "B", "A"], ["C", "B", "A"], ["C", "B", "A"],
                               ["C", "B", "A"], ["A", "C", "B"], ["A", "C", "B"], ["A", "C", "B"],
                               ["A", "C", "B"], ["B", "A", "C"], ["B", "A", "C"], ["B", "A", "C"],
                               ["B", "A", "C"], ["B", "A", "C"], ["B", "A", "C"], ["B", "A", "C"],
                               ["B", "A", "C"]]
        ranked_vote_result = ["C", "B", "A"]
        simple_votes = [["B", "A", "C"], ["C", "B", "A"], ["A", "C", "B"],
                           ["B", "A", "C"], ["C", "B", "A"]]
        simple_vote_result = ["C", "B", "A"]
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(ranked_choice(ranked_votes_two), ranked_vote_result_two)
        self.assertEqual(ranked_choice(ranked_votes), ranked_vote_result)
        self.assertEqual(ranked_choice(simple_votes), simple_vote_result)


if __name__ == '__main__':
    unittest.main()