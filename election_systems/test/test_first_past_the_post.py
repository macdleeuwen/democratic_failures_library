# Tests for first past the post function
import unittest
from election_systems.first_past_the_post import first_past_the_post


class TestFirstPastThePost(unittest.TestCase):
    # test function to test equality of two value
    def test_fptp_simple(self):
        simple_votes = [["A"], ["B"], ["B"]]
        simple_answer = ['B', 'A']
        more_candidates = [["Steve"], ["Steve"], ["Mary"], ["Frank"], ["Mary"], ["Sadie"], ["Sadie"],
                           ["Rose"], ['Sadie']]
        more_candidates_answer = ['Sadie', 'Steve', 'Mary', 'Frank', 'Rose']
        multiple_candidates_listed = [["Steve", "Mary"], ["Steve", "Mary", "Sadie"], ["Frank"], ["Rose", "Felicia"]]
        multiple_candidates_listed_answer = ['Steve', 'Frank', 'Rose']
        simple_result = first_past_the_post(simple_votes)
        more_candidates_result = first_past_the_post(more_candidates)
        multiple_candidates_result = first_past_the_post(multiple_candidates_listed)
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(simple_answer, simple_result)
        self.assertEqual(more_candidates_answer, more_candidates_result)
        self.assertEqual(multiple_candidates_listed_answer, multiple_candidates_result)


if __name__ == '__main__':
    unittest.main()
