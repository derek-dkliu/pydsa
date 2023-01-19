import random

def quick_sort(arr):
    random.shuffle(arr)
    sort(arr, 0, len(arr) - 1)

def sort(arr, low, high):
    if low >= high: return

    p, q = partition(arr, low, high)
    sort(arr, low, p - 1)
    sort(arr, q + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    lt = low        # left bound of pivot
    gt = high       # right bound of pivot
    i = low + 1     # current pointer
    while i <= gt:
        if arr[i] < pivot:
            swap(arr, i, lt)
            lt += 1
            i += 1
        elif arr[i] > pivot:
            swap(arr, i, gt)
            gt -= 1
        else:
            i += 1
    return lt, gt

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


arr = list(range(15))
random.shuffle(arr)
print(arr)
quick_sort(arr)
print(arr)