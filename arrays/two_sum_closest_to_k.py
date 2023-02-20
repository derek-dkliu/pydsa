def two_sum(A, k):
    A = A[:]
    A.sort()
    min_diff = float('inf')
    ans = None
    i = 0
    j = len(A) - 1
    while i < j:
        sum = A[i] + A[j]
        if sum == k:
            return (A[i], A[j])
        
        diff = abs(sum - k)
        if diff < min_diff:
            min_diff = diff
            ans = (A[i], A[j])

        if sum < k:
            i += 1
        else:
            j -= 1
    return ans

cases = [
    ([2, 5, 2, 4, 8, 2], 8)
]
for A, t in cases:
    print(two_sum(A, t))