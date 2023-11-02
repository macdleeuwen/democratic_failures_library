# Tests for first past the post function
import unittest
from democratic_failures.majority_criterion import majority


class TestMajority(unittest.TestCase):
    # test function to test equality of two value
    def test_majority_simple(self):
        simple_votes = [["A"], ["B"], ["B"]]
        more_candidates = [["Steve"], ["Steve"], ["Mary"], ["Frank"], ["Mary"], ["Sadie"], ["Sadie"],
                           ["Sadie"], ['Sadie']]
        multiple_candidates_listed = [["Steve", "Mary"], ["Steve", "Mary", "Sadie"], ["Steve"], ["Rose", "Felicia"]]
        simple_result = majority(simple_votes, 'B')
        more_candidates_result = majority(more_candidates, 'Sadie')
        multiple_candidates_result = majority(multiple_candidates_listed, 'Mary')
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertTrue(simple_result)
        self.assertTrue(more_candidates_result)
        self.assertFalse(multiple_candidates_result)


if __name__ == '__main__':
    unittest.main()