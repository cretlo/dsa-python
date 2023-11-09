from typing import List


def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j - 1] > arr[j]:
                tmp = arr[j - 1] 
                arr[j - 1] = arr[j]
                arr[j] = tmp
                continue

            break

