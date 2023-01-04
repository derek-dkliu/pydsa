def multiply(a, b):
    if a < b:
        a, b = b, a
    return mul(a, b)

def mul(a, b):
    if b == 1: return a

    c = b >> 1
    h = mul(a, c)
    p = h + h
    if b % 2 == 1:
        p += a
    return p

cases = [
    (5, 7),
    (3, 10000)
]
for a, b in cases:
    print(a, b, multiply(a, b))