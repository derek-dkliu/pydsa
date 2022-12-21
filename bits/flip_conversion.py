def flip_convert1(n, m):
    flip = 0
    while n != 0 or m != 0:
        if n & 1 != m & 1:
            flip += 1
        n = rshift(n, 1)
        m = rshift(m, 1)
    return flip

def rshift(a, b):
    return (a % 0x100000000) >> b

def flip_convert2(n, m):
    flip = 0
    c = n ^ m
    while c != 0:
        flip += (c & 1)
        c = rshift(c, 1)
    return flip

def flip_convert3(n, m):
    flip = 0
    c = n ^ m
    while c != 0 and flip < 32:
        flip += 1
        c &= c - 1
    return flip

cases = [
    [0b11101, 0b1111],
    [0, -1]
]
for i, [n, m] in enumerate(cases):
    print(f"case {i+1}: {n:b}, {m:b}")
    print(flip_convert1(n, m))
    print(flip_convert2(n, m))
    print(flip_convert3(n, m))