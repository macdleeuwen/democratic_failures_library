# Tests for the IIA method.

# Case for Borda count violating IIA taken from:
# https://en.wikipedia.org/wiki/Independence_of_irrelevant_alternatives

import unittest
from democratic_failures.independence_of_irrelevant_alternatives import iia


class IIA_Test(unittest.TestCase):
    # test function to test equality of two value
    def test_iia_simple(self):
        simple_votes = [["A"], ["B"], ["B"]]
        fptp_ranking = [('B', 2), ('A', 1)]
        iia_violated_votes = [["A", "B", "C", "D", "E"], ["A", "B", "C", "D", "E"],
                              ["A", "B", "C", "D", "E"], ["C", "D", "E", "B", "A"],
                              ["E", "C", "D", "B", "A"]]
        borda_ranking = [('C', 13), ('A', 12), ('B', 11), ('D', 8), ('E', 6)]
        simple_result = iia(simple_votes, fptp_ranking, "FPTP")
        violated_result = iia(iia_violated_votes, borda_ranking, "Borda")

        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertTrue(simple_result)
        self.assertFalse(violated_result)


if __name__ == '__main__':
    unittest.main()