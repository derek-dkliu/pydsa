def two_sum_index(A, target):
    map = {}
    pairs = []
    for i in range(len(A)):
        rem = target - A[i]
        if rem in map:
            for j in map[rem]:
                pairs.append((j, i))
        indices = map.get(A[i], [])
        indices.append(i)
        map[A[i]] = indices
    return pairs

# time:  O(n)
# space: O(n)
def two_sum(A, target):
    visited = {}
    pairs = []
    for i in range(len(A)):
        rem = target - A[i]
        if rem in visited:
            if not visited[rem]:
                pairs.append((rem, A[i]))
                visited[rem] = True
            if A[i] in visited:
                visited[A[i]] = True
        else:
            visited[A[i]] = False
    return pairs

def two_sum1(A, target):
    visited = set()
    pairs = set()
    for i in range(len(A)):
        rem = target - A[i]
        if rem in visited:
            pair = (rem, A[i]) if rem < A[i] else (A[i], rem)
            pairs.add(pair)
        visited.add(A[i])
    return pairs

# time:  O(n logn)
# space: O(1)
def two_sum2(A, target):
    A.sort()
    i = 0
    j = len(A) - 1
    pairs = []
    while i < j:
        sum = A[i] + A[j]
        if sum == target:
            pairs.append((A[i], A[j]))
            i += 1
            j -= 1
            # avoid duplicates
            while A[i] == A[i-1]:
                i += 1
            while A[j] == A[j+1]:
                j -= 1
        elif sum < target:
            i += 1
        else:
            j -= 1
    return pairs

cases = [
    ([1, 5, -1, 2, 4, 3, 6, 3, 2], 5)
]
for A, t in cases:
    print(two_sum_index(A, t))
    print(two_sum(A, t))
    print(two_sum1(A, t))
    print(two_sum2(A, t))