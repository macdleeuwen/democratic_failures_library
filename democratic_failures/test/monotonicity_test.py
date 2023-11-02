# Tests for borda count function
import unittest
from monotonicity import monotonicity


class TestMonotonicity(unittest.TestCase):
    # test function to test equality of two value
    def test_monotonicity_simple(self):
        monotonic_votes_two = [["A", "C", "B"], ["A", "C", "B"], ["A", "B", "C"], ["A", "B", "C"],
                               ["A", "B", "C"], ["A", "B", "C"],  ["B", "C", "A"],  ["B", "C", "A"],
                               ["B", "C", "A"], ["B", "A", "C"], ["B", "A", "C"], ["C", "A", "B"],
                               ["C", "A", "B"], ["C", "A", "B"], ["C", "A", "B"], ["C", "A", "B"],
                               ["C", "A", "B"]]
        non_monotonic_votes = [["C", "B", "A"], ["C", "B", "A"], ["C", "B", "A"], ["C", "B", "A"],
                               ["C", "B", "A"], ["A", "C", "B"], ["A", "C", "B"], ["A", "C", "B"],
                               ["A", "C", "B"], ["B", "A", "C"], ["B", "A", "C"], ["B", "A", "C"],
                               ["B", "A", "C"], ["B", "A", "C"], ["B", "A", "C"], ["B", "A", "C"],
                               ["B", "A", "C"]]
        monotonic_votes = [["B", "A", "C"], ["C", "B", "A"], ["A", "C", "B"],
                           ["B", "A", "C"], ["C", "B", "A"]]
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertTrue(monotonicity(monotonic_votes))
        self.assertFalse(monotonicity(non_monotonic_votes))
        self.assertTrue(monotonicity(monotonic_votes_two))


if __name__ == '__main__':
    unittest.main()