"""
To sort an array, first divide it into two halves and then sort its subarrays,
repeat this process until the subarray is of size one, then merge subarrays
back to form a sorted array.
"""

# time: O(n logn)
# space O(n)
def merge_sort(arr):
    aux = [None] * len(arr)
    sort(arr, aux, 0, len(arr) - 1)

def sort(arr, aux, low, high):
    if low >= high: return

    mid = (low + high) // 2
    sort(arr, aux, low, mid)
    sort(arr, aux, mid + 1, high)
    # return if already sorted
    if arr[mid] <= arr[mid + 1]:
        return
    merge(arr, aux, low, mid, high)

def merge(arr, aux, low, mid, high):
    for i in range(low, high + 1):
        aux[i] = arr[i]

    left = low
    right = mid + 1
    for i in range(low, high + 1):
        if left > mid:
            break
        elif right > high:
            arr[i] = aux[left]
            left += 1
        elif aux[left] <= aux[right]:
            arr[i] = aux[left]
            left += 1
        else:
            arr[i] = aux[right]
            right += 1

import random
arr = list(range(15))
arr.extend([-1, -3, -5])
random.shuffle(arr)
print(arr)
merge_sort(arr)
print(arr)
