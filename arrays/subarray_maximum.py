# time:  O(n^2)
def max_subarray(A):
    max_sum = -float('inf')
    for i in range(len(A)):
        sum = 0
        for j in range(i, len(A)):
            sum += A[j]
            if sum > max_sum:
                max_sum = sum
    return max_sum

# time:  O(n)
def max_subarray2(A):
    max_sum = -float('inf')
    sum = 0
    for i in range(len(A)):
        sum += A[i]
        if sum > max_sum:
            max_sum = sum
        if sum < 0:
            sum = 0
    return max_sum

cases = [
    [2, 3, -4, 5, 1, -2, -4, 1],
    [1, 1, 1, 1, 1],
    [1, 1, -1, 1, 1],
    [-1, 1, 1, 1, 1],
    [1, 1, 1, 1, -1],
    [-3, -2, -1, -5, -6],
]
for A in cases:
    print(max_subarray(A), max_subarray2(A))