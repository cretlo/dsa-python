import unittest
from searches.linear_search import linear_search

class TestLinearSearch(unittest.TestCase):

    def test_linear_search(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        self.assertTrue(linear_search(arr, 5))
        self.assertFalse(linear_search(arr, 105))
        self.assertTrue(linear_search(arr, 10))
        self.assertFalse(linear_search(arr, 1000))
        self.assertTrue(linear_search(arr, 1))


if __name__ == "__main__":
    unittest.main()
