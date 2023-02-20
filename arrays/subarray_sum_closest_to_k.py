def subarray_sum(A, k):
    bst = BST()
    sum = 0
    min_diff = float('inf')
    ans = None
    for i, num in enumerate(A):
        sum += num
        if sum == k:
            return (sum, 0, i)
        
        low = bst.floor(sum - k)
        if low is not None:
            diff = sum - k - low
            if diff < min_diff:
                min_diff = diff
                ans = (sum - low, bst.get(low) + 1, i)
        high = bst.ceil(sum - k)
        if high is not None:
            diff = high - (sum - k)
            if diff < min_diff:
                min_diff = diff
                ans = (sum - high, bst.get(high) + 1, i)
        bst.put(sum, i)
    return ans

# A = [2, 3, 5, -2, 1, -3, 2]
# k = 7
# subarray_sum(A, k)