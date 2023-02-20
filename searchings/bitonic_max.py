def search_max(A):
    low = 0
    high = len(A) - 1
    while low != high:
        mid = (low + high) // 2
        if A[mid] < A[mid+1]:
            low = mid + 1
        elif A[mid] > A[mid+1]:
            high = mid
        else:
            return A[mid]
    return A[low]

inc = list(range(1, 20))
dec = list(range(18, 0, -2))
bitone = inc + dec
print(bitone, search_max(bitone))
