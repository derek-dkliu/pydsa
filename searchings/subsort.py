# time: O(n)
def subsort(A):
    left = -1
    for i in range(len(A) - 1):
        if A[i] > A[i + 1]:
            left = i
            break
    if left == -1:
        return None

    right = -1
    for i in range(len(A) - 1, left, -1):
        if A[i] < A[i - 1]:
            right = i
            break

    min = A[left]
    max = A[right]
    for i in range(left + 1, right):
        if A[i] < min: min = A[i]
        if A[i] > max: max = A[i]

    # use linear search to find m and n
    m = 0
    n = len(A) - 1
    for i in range(0, left + 1):
        if A[i] > min:
            m = i
            break
    for i in range(right, len(A)):
        if A[i] >= max:
            n = i - 1
            break

    # # use binary search to find m and n
    # m = binary_search(A, min, 0, left, True)
    # n = binary_search(A, max, right, len(A) - 1, False) - 1

    return m, n

def binary_search(A, t, low, high, rightmost):
    while low <= high:
        mid = (low + high) // 2
        if t == A[mid]:
            if rightmost:
                low = mid + 1
            else:
                high = mid - 1
        elif t < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low

cases = [
    [1, 4, 3, 5],
    [1, 3, 3, 7, 4, 3, 10],
    [1, 3, 7, 4, 3, 7, 7, 7, 10],
    [1, 2, 3],
    [3, 2, 1, 0, -1]
]
for A in cases:
    print(A, subsort(A))