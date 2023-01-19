"""
For an array, find a pivot, move all items smaller than the pivot to the left,
move all items larger than the pivot to the right, repeat this process for both
left part and right part until they are of size one.
"""

# time:  O(n logn) on average, O(n^2) in worst case
# space: O(logn) for the recursion stack

import random
def quick_sort(arr):
    # shuffling is needed for performance guarantee
    random.shuffle(arr)
    sort(arr, 0, len(arr) - 1)

def sort(arr, low, high):
    if low >= high: return

    p = partition(arr, low, high)
    sort(arr, low, p - 1)
    sort(arr, p + 1, high)

def partition(arr, low, high):
    pivot = arr[low]
    left = low + 1
    right = high
    while left <= right:
        # check if left pointer out of bound, and stop at item equal to pivot
        while left <= right and arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        # swap only if left and right pointers have not yet crossed each other
        if left <= right:
            swap(arr, left, right)
            left += 1
            right -= 1
    # swap pivot item to the proper place
    swap(arr, low, right)
    return right
    
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


arr = list(range(15))
random.shuffle(arr)
print(arr)
quick_sort(arr)
print(arr)
