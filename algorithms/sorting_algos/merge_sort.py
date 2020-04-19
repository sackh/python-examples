"""
This module has implementation of merge sort algorithm
"""


def merge(left, right, arr):
    i, j, k = 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr):
    arr_len = len(arr)
    if arr_len < 2:
        return
    mid = arr_len // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    merge_sort(left_arr)
    merge_sort(right_arr)
    merge(left_arr, right_arr, arr)


if __name__ == "__main__":
    arr = [5, 2, 8, 1, 3]
    merge_sort(arr)
    print(arr)