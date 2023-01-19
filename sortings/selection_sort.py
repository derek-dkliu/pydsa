"""
From round i to length - 1, find the min element of the array starting from i + 1,
swap the min with i
"""

# time:  O(n^2)
# space: O(1)
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        swap(arr, i, min)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


import random
arr = list(range(15))
random.shuffle(arr)
print(arr)
selection_sort(arr)
print(arr)