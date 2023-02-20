def closest_sum(A, B, k):
    A.sort()
    B.sort(reverse=True)

    min_diff = float('inf')
    ans = None
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        sum = A[i] + B[j]
        if sum == k:
            return (A[i], B[j])
        
        diff = abs(sum - k)
        if diff < min_diff:
            min_diff = diff
            ans = (A[i], B[j])

        if sum < k:
            i += 1
        else:
            j += 1
    return ans