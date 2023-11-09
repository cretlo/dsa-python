import unittest
import random
from sorts.merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):

    def test_merge_sort(self):
        arr = []
        merge_sort(arr)
        self.assertTrue(arr == [])

        arr = [random.randrange(0, 100) for _ in range(0, 100)]
        sorted_arr = sorted(arr)

        self.assertFalse(arr is sorted_arr)
        self.assertFalse(arr == sorted_arr)

        merge_sort(arr)
        self.assertFalse(arr is sorted_arr)
        self.assertTrue(arr == sorted_arr)


        arr = [random.randrange(0, 99) for _ in range(0, 99)]
        sorted_arr = sorted(arr)

        merge_sort(arr)
        self.assertFalse(arr is sorted_arr)
        self.assertTrue(arr == sorted_arr)

if __name__ == '__main__':
    unittest.main()
