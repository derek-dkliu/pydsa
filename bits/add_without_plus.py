def add(n, m):
    i = 1
    c = 0
    sum = 0
    while n != 0 or m != 0 or c != 0:
        a = n & 1
        b = m & 1
        d = a ^ b ^ c  # odd(a, b, c)
        sum |= lshift(d, i)
        c = major(a, b, c)
        i <<= 1 
        n >>= 1
        m >>= 1
    return sum

def lshift(n, i):
    i >>= 1
    while i != 0:
        n <<= 1
        i >>= 1
    return n

def major(a, b, c):
    return (~a & b & c) | (a & ~b & c) | (a & b & ~c) | (a & b & c)

def odd(a, b, c):
    return (a & ~b & ~c) | (~a & b & ~c) | (~a & ~b & c) | (a & b & c)

def add1(a, b):
    if b == 0: return a
    sum = a ^ b
    carry = (a & b) << 1
    return add1(sum, carry)

def add2(a, b):
    while b != 0:
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    return a

cases = [
    [2, 3],
    [11, 9],
    [11, 99],
    [10, 0]
]
for n, m in cases:
    print(add1(n, m), add2(n, m))
