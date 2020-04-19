"""
This module implements quick sort algorithm
"""

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


if __name__ == "__main__":
    arr = [59, 2, 8, 1, 3, 90, 23]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)