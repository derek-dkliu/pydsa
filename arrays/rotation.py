# juggle between array index with k steps
def rotate1(A, k):
    if k == 0: return A
    n = len(A)
    if k < 0: k += n
    k %= n
    m = gcd(n, k)
    for i in range(m):
        tmp = A[i]
        j = i
        while True:
            p = j + k
            if p >= n: p -= n
            if p == i: break
            A[j] = A[p]
            j = p
        A[j] = tmp
    return A

def gcd(a, b):
    if b == 0: return a
    return gcd(b, a % b)

# swap chunks recursively
def rotate2(A, k):
    if k == 0: return A
    n = len(A)
    if k < 0: k += n
    k %= n
    rot(A, 0, n - 1, k)
    return A

def rot(A, low, high, k):
    right = low + k
    size = high - right + 1
    if k == size:
        swap(A, low, right, k)
    elif k < size:
        swap(A, low, right, k)
        rot(A, right, high, k)
    else:
        swap(A, low, right, size)
        rot(A, low + size, high, k - size)

def swap(A, i, j, size):
    for s in range(size):
        A[i + s], A[j + s] = A[j + s], A[i + s]

# reverse chunks
def rotate3(A, k):
    if k == 0: return A
    n = len(A)
    if k < 0: k += n
    k %= n
    reverse(A, 0, k - 1)
    reverse(A, k, n - 1)
    reverse(A, 0, n - 1)
    return A

def reverse(A, i, j):
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

cases = [(8, 3), (9, 3), (5, 1), (8, -3), (8, 11)]
for n, k in cases:
    A = list(range(n))
    print(k, rotate1(A, k))
    A = list(range(n))
    print(k, rotate2(A, k))
    A = list(range(n))
    print(k, rotate3(A, k))
