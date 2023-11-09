import unittest

from sorts.bubble_sort import bubble_sort


class TestBubbleSort(unittest.TestCase):

    def test_bubble_sort(self):
        arr = [3, 16, 12, 5, 4, 3, 2, 1, 2, 10]
        sorted_arr = sorted(arr)

        print(arr)
        print(sorted_arr)

        self.assertFalse(arr == sorted_arr)
        bubble_sort(arr)
        self.assertTrue(arr == sorted_arr)



if __name__ == '__main__':
    unittest.main()
