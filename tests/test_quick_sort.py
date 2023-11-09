import unittest
import random
from sorts.quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):

    def test_quick_sort(self):
        arr = []
        quick_sort(arr)
        self.assertTrue(arr == [])

        arr = [random.randrange(0, 100) for _ in range(0, 100)]
        arr_sorted = sorted(arr)
        self.assertTrue(arr is not arr_sorted)
        quick_sort(arr)
        self.assertTrue(arr == arr_sorted)

if __name__ == "__main__":
    unittest.main()
