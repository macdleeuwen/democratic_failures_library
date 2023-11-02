# Tests for borda count function
import unittest
from election_systems.borda_count import borda_count


class TestFirstPastThePost(unittest.TestCase):
    # test function to test equality of two value
    def test_fptp_simple(self):
        simple_votes = [["A"], ["B"], ["B"]]
        simple_answer = ['B', 'A']
        multiple_candidates_listed = [["Steve", "Mary"], ["Steve", "Mary", "Sadie"], ["Frank"], ["Rose", "Felicia"]]
        multiple_candidates_listed_answer = ['Steve', 'Mary', 'Frank', 'Rose', 'Felicia', 'Sadie']
        simple_result = borda_count(simple_votes)
        multiple_candidates_result = borda_count(multiple_candidates_listed)
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(simple_answer, simple_result)
        self.assertEqual(multiple_candidates_listed_answer, multiple_candidates_result)


if __name__ == '__main__':
    unittest.main()

