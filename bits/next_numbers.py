def next_smallest(n):
    if n == 0: return -1
    c = n
    c0 = 0
    c1 = 0
    while c & 1 == 0:
        c0 += 1
        c >>= 1
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    p = c0 + c1
    # flip rightmost non-trailing zero
    n |= (1 << p)
    # clear all bits to the right of p
    n &= (-1 << p)
    # insert (c1 - 1) ones on the right
    n |= (1 << c1 - 1) - 1
    return n

def prev_largest(n):
    if n == 0: return -1
    c = n
    c0 = 0
    c1 = 0
    while c & 1 == 1:
        c1 += 1
        c >>= 1
    while c & 1 == 0:
        c0 += 1
        c >>= 1
    p = c0 + c1
    # flip rightmost non-trailing one
    n &= ~(1 << p)
    # clear all bits to the right of p
    n &= (-1 << p)
    # insert (c1 + 1) ones on the left
    n |= ((1 << c1 + 1) - 1) << (c0 - 1)
    return n

for i, n in enumerate([0b10001100, 0]):
    print(f"case {i+1}: {n:b}")
    next = next_smallest(n)
    prev = prev_largest(n)
    print(f"{next:b} {prev:b}")
