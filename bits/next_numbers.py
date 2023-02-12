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

    # for 32-bit integer
    # if n = 11..100..0, no next smallest number with same number of 1s
    if c0 + c1 == 31:
        return -1

    p = c0 + c1
    # flip rightmost non-trailing zero
    n |= (1 << p)
    # clear all bits to the right of p
    n &= (-1 << p)
    # insert (c1 - 1) ones on the right
    n |= (1 << c1 - 1) - 1
    return n

def prev_largest(n):
    c = n
    c0 = 0
    c1 = 0
    while c & 1 == 1:
        c1 += 1
        c >>= 1

    # if n = 00..011..1, no prev largest number with same number of 1s
    if c == 0:
        return -1

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

for i, n in enumerate([0b101, 0b110, 0b11, 0b10001, 0b10010, 0b10011, 0b10110, 0b10001100, 0, 1]):
    print(f"case {i+1}: {n:b}")
    prev = prev_largest(n)
    next = next_smallest(n)
    print(f"{prev:b} {next:b}")
