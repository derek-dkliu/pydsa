# time:  O(n)
def peaks_valleys1(arr):
    for i in range(1, len(arr), 2):
        j = max_index(arr, i - 1, i, i + 1)
        if j != i:
            swap(arr, i, j)

def max_index(arr, i, j, k):
    index = i if arr[i] > arr[j] else j
    if k < len(arr) and arr[index] < arr[k]:
        index = k
    return index

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# time:  O(n)
def peaks_valleys2(arr):
    peak = False
    for i in range(1, len(arr)):
        if peak:
            if arr[i] < arr[i - 1]:
                swap(arr, i, i -1)
        else:
            if arr[i] > arr[i - 1]:
                swap(arr, i, i - 1)
        peak = not peak

arr = [4, 1, 0, 8, 7, 9]
peaks_valleys1(arr)
print(arr)

arr = [4, 1, 0, 8, 7, 9]
peaks_valleys2(arr)
print(arr)