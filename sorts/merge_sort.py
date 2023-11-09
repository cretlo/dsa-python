from typing import List

def merge_sort(arr: List[int]):

    def merge(arr: List[int], lo: int, m: int, hi: int):
        arrL, arrR = arr[lo:m], arr[m:hi]

        i = j = 0
        k = lo

        while(i < len(arrL) and j < len(arrR)):
            if arrL[i] <= arrR[j]:
                arr[k] = arrL[i]
                i += 1
            else:
                arr[k] = arrR[j]
                j += 1

            k += 1

        while (i < len(arrL)):
            arr[k] = arrL[i]
            i += 1
            k += 1

        while (j < len(arrR)):
            arr[k] = arrR[j]
            j += 1
            k += 1

        return


    def ms(arr: List[int], lo: int, hi: int):
        if (hi - lo) <= 1:
            return

        m = (lo + hi) // 2
        ms(arr, lo, m)
        ms(arr, m, hi)
        merge(arr, lo, m, hi)
        return

    ms(arr, 0, len(arr))

arr = [5, 6, 3, 4]
print(arr)
merge_sort(arr)
print(arr)

