import unittest
import random
from sorts.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [random.randrange(0, 100) for i in range(100)]
        sorted_arr = sorted(arr)

        self.assertFalse(arr == sorted_arr)

        insertion_sort(arr) 
        self.assertFalse(arr is sorted_arr)
        self.assertTrue(arr == sorted_arr)


if __name__ == "__main__":
    unittest.main()
