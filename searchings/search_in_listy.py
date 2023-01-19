# time:  O(logn)
# space: O(1)
def search(arr, t):
    index = 1
    while arr[index] != -1 and arr[index] < t:
        index += index
    return binary_search(arr, t, index // 2, index)

def binary_search(arr, t, low, high):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == t:
            return mid
        elif arr[mid] > t or arr[mid] == -1:
            high = mid - 1
        else:
            low = mid + 1
    return -1

class Listy:
    def __init__(self, size):
        self.arr = list(range(size))

    def __getitem__(self, index):
        if index < 0 or index >= len(self.arr):
            return -1
        return self.arr[index]

    def __str__(self):
        return str(self.arr)

arr = Listy(16)
print(arr)
print(search(arr, 8))
