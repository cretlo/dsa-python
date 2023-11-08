from typing import List

def binary_search_iterative(arr: List[int], item: int) -> bool:
    lo, hi = 0, len(arr)

    while lo < hi:
        m = (lo + hi) // 2

        if arr[m] == item:
            return True
        elif arr[m] > item:
            hi = m
        else:
            lo = m + 1

    return False

    
def binary_search_recursive(arr: List[int], item: int) -> bool:

    def search(arr: List[int], lo: int, hi: int, item: int) -> bool:
        if lo >= hi:
            return False

        m = (lo + hi) // 2

        if arr[m] == item:
            return True
        elif arr[m] > item:
            return search(arr, lo, m, item)
        else:
            return search(arr, m + 1, hi, item)


    return search(arr, 0, len(arr), item)

