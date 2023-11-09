from typing import List

def bubble_sort(arr: List[int]):
    for i in range(1, len(arr)):
        for j in range(len(arr) - i):
            if arr[j] > arr[j + 1]:
                tmp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = tmp

