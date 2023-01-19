# time:  O(logn) for unique element arr, O(n) for many duplicate elments
# space: O(logn) for unique element arr, O(n) for many duplicate elments
def search_rotated(arr, t):
    return search(arr, t, 0, len(arr) - 1)

def search(arr, t, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if arr[mid] == t:
        return mid
    
    if arr[low] < arr[mid]:
        if t >= arr[low] and t < arr[mid]:
            return search(arr, t, low, mid - 1)
        else:
            return search(arr, t, mid + 1, high)
    elif arr[low] > arr[mid]:
        if t <= arr[high] and t > arr[mid]:
            return  search(arr, t, mid + 1, high)
        else:
            return search(arr, t, low, mid - 1)
    else:
        if arr[high] != arr[mid]:
            return search(arr, t, mid + 1, high)
        else:
            ans = search(arr, t, mid + 1, high)
            if ans != -1:
                return ans
            ans = search(arr, t, low, mid - 1)
            return ans

arr = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
print(search_rotated(arr, 5))

arr = [2, 2, 2, 3, 4, 2]
print(search_rotated(arr, 3))