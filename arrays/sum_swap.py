# time:  O(A logA + B logB)
def sum_swap(A, B):
    A.sort()
    B.sort()
    sum1 = sum(A)
    sum2 = sum(B)
    target = (sum1 - sum2) / 2

    min = float('inf')
    pair = None
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        diff = A[i] - B[j]
        if diff == target:
            return (A[i], B[j])
        if abs(diff - target) < min:
            min = abs(diff - target)
            pair = (A[i], B[j])
        if diff < target:
            i += 1
        else:
            j += 1
    return pair

cases = [
    ([4,1,2,3], [3,5,2,6]),
    ([4,1,2,3], [-1,9,2,6]),
    ([4,0,2,3], [3,5,2,6]),
]
for A, B in cases:
    print(sum_swap(A, B))