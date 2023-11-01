# Tests for copeland method function
import unittest
from copeland import copeland


class TestCopeland(unittest.TestCase):
    # test function to test equality of two value
    def test_copeland_simple(self):
        multiple_candidates_listed = [["Steve", "Mary"], ["Steve", "Mary", "Sadie"], ["Frank"], ["Rose", "Felicia"]]
        multiple_candidates_listed_answer = ['Steve', 'Mary', 'Rose', 'Sadie', 'Frank', 'Felicia']
        multiple_candidates_result = copeland(multiple_candidates_listed)
        # error message in case if test case got failed
        message = "First value and second value are not equal !"
        # assertEqual() to check equality of first & second value
        self.assertEqual(multiple_candidates_listed_answer, multiple_candidates_result)


if __name__ == '__main__':
    unittest.main()