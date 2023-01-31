# time:  O(A logA + B logA)
def smallest_diff(A, B):
    swapped = False
    if len(B) < len(A):
        swapped = True
        A, B = B, A
    A.sort()
    min_diff = float('inf')
    min_pair = None
    for i, t in enumerate(B):
        j = binary_search(A, t)
        if j == len(A):
            j -= 1
        if j - 1 >= 0 and abs(A[j - 1] - B[i]) < abs(A[j] - B[i]):
            j = j - 1
        if abs(A[j] - B[i]) < min_diff:
            min_diff = abs(A[j] - B[i])
            min_pair = (A[j], B[i]) 
    return (min_pair[1], min_pair[0]) if swapped else min_pair

def binary_search(A, t):
    low = 0
    high = len(A) - 1
    while low <= high:
        mid = (low + high) // 2
        if t == A[mid]:
            return mid
        elif t < A[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return low

# time: O(A logA + B logB)
def smallest_diff2(A, B):
    A.sort()
    B.sort()
    i = 0
    j = 0
    min_diff = float('inf')
    min_pair = None
    while i < len(A) and j < len(B):
        diff = abs(A[i] - B[j])
        if diff < min_diff:
            min_diff = diff
            min_pair = (A[i], B[j])
        if A[i] < B[j]:
            i += 1
        else:
            j += 1
    return min_pair

cases = [
    ([1, 3, 15, 11, 2], [23, 127, 235, 19, 8]),
    ([1, 3, 15, 11, 2, 99], [23, 127, 235, 19, 8]),
]
for A, B in cases:
    print(smallest_diff(A, B), smallest_diff2(A, B))
