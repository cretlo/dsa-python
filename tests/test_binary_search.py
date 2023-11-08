import unittest
from searches.binary_search import binary_search_iterative as bsi
from searches.binary_search import binary_search_recursive as bsr


class TestBinarySearch(unittest.TestCase):

    def test_binary_search_iterative(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(bsi(arr, 1))
        self.assertTrue(bsi(arr, 4))
        self.assertTrue(bsi(arr, 5))
        self.assertTrue(bsi(arr, 7))
        self.assertTrue(bsi(arr, 10))

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(bsi(arr, 1))
        self.assertTrue(bsi(arr, 4))
        self.assertTrue(bsi(arr, 5))
        self.assertTrue(bsi(arr, 7))
        self.assertTrue(bsi(arr, 9))

    def test_binary_search_recursive(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertTrue(bsr(arr, 1))
        self.assertTrue(bsr(arr, 4))
        self.assertTrue(bsr(arr, 5))
        self.assertTrue(bsr(arr, 7))
        self.assertTrue(bsr(arr, 10))

        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertTrue(bsr(arr, 1))
        self.assertTrue(bsr(arr, 4))
        self.assertTrue(bsr(arr, 5))
        self.assertTrue(bsr(arr, 7))
        self.assertTrue(bsr(arr, 9))

if __name__ == "__main__":
    unittest.main()
