"""
For each round i, maintain the invariant that items (<=i) are sorted.
To do so, inserting item i to a proper place by comparing and 
swaping it with item from i-1 to 0
"""

# time:  O(n^2) on average and worst case, O(n) in best case
# space: O(1)
def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                swap(arr, j, j - 1)
            else:
                break

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

import random
arr = list(range(15))
random.shuffle(arr)
print(arr)
insertion_sort(arr)
print(arr)