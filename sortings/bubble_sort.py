"""
For each round, move the largest element to the right end by
comparing and swaping with neighbour element.
Stop when no swap is needed in a certain round.
"""

# time:  O(n^2) on average and worst case, O(n) in best case
# space: O(1)

def bubble_sort(arr):
    sorted = False
    sort_num = 0
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1 - sort_num):
            if arr[i] > arr[i + 1]:
                swap(arr, i, i + 1)
                sorted = False
        sort_num += 1

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

import random
arr = list(range(15))
random.shuffle(arr)
print(arr)
bubble_sort(arr)
print(arr)