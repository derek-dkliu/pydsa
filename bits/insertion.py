import math
def insertion(n, m, i, j):
    len = math.floor(math.log2(m)) + 1
    for k in range(j - i + 1):
        p = len - 1 - k
        q = j - k
        val = 1 if p >= 0 and m & (1 << p) != 0 else 0
        n = (n & ~(1 << q)) | (val << q)
    return bin(n)

def insertion2(n, m, i, j):
    # clear bits through i to j
    # create a mask with 0s in the middle through i to j
    mask = (-1 << j + 1) + (1 << i) - 1
    n &= mask
    # align m to bit j
    k = j - math.floor(math.log2(m))
    m <<= k
    return bin(n + m)

cases = [
    [0b1000001, 0b1011, 0, 4],
    [0b10000, 0b1011, 2, 5],
]    
for c, [n, m, i, j] in enumerate(cases):
    print(f"case {c+1}: n={n:b},m={m:b},i={i},j={j}")
    print(insertion(n, m, i, j))
    print(insertion2(n, m, i, j))
