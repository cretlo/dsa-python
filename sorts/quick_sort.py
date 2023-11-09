
from typing import List

def partition(arr: List[int], lo: int, hi: int) -> int:
    pivot = arr[hi]

    i = lo - 1

    for j in range(lo, hi):
        if arr[j] <= pivot:
            i += 1
            tmp = arr[j]
            arr[j] = arr[i]
            arr[i] = tmp

    i += 1
    arr[hi] = arr[i]
    arr[i] = pivot
    return i


def qs(arr: List[int], lo: int, hi: int):
    if (hi - lo) < 1:
        return

    pivotIdx = partition(arr, lo, hi)
    qs(arr, lo, pivotIdx - 1)
    qs(arr, pivotIdx + 1, hi)


def quick_sort(arr: List[int]):
    qs(arr, 0, len(arr) - 1)


arr = [5, 6, 5, 3, 2]
print("sorted:", sorted(arr))
quick_sort(arr)
print(arr)
