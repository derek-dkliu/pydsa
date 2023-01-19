# time: O(logn) on average, O(n) for worst case
def sparse_search(arr, t):
    if t is None or t == "": return -1
    return search(arr, t, 0, len(arr) - 1)

def search(arr, t, low, high):
    if low > high: return -1

    mid = (low + high) // 2
    # find closest non-empty string if middle is empty
    if arr[mid] == "":
        left = mid - 1
        right = mid + 1
        while True:
            if left < low and right > high:
                return -1
            elif left >= low and arr[left] != "":
                mid = left
                break
            elif right <= high and arr[right] != "":
                mid = right
                break
            left -= 1
            right += 1
    if arr[mid] == t:
        return mid
    elif arr[mid] < t:
        return search(arr, t, mid + 1, high)
    else:
        return search(arr, t, low, mid - 1)


arr = ["at", "", "", "", "ball", "", "", "car", "", "", "", "", "dad", ""]
print(sparse_search(arr, "ball"))

arr = ["", "ball"]
print(sparse_search(arr, "ball"))
