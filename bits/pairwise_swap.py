def pairwise_swap1(n):
    mask = 0b11
    count = 0
    c = n
    while c != 0:
        if c & mask == 1 or c & mask == 2:
            n ^= mask << count
        c = rshift(c, 2)
        count += 2
    return n

def rshift(a, b):
    return (a % 0x100000000) >> b

# 5 instructions only
# assume 32-bit integer
def pairwise_swap2(n):
    odd_mask = 0xaaaaaaaa
    even_mask = 0x55555555
    return rshift(n & odd_mask, 1) | (n & even_mask) << 1

cases = [0b1001101, 0, 1, 0b111, 0b1111, 0b110]
for i, case in enumerate(cases):
    print(f"case {i+1}: {case:b}")
    print(f"{pairwise_swap1(case):b}")
    print(f"{pairwise_swap2(case):b}")