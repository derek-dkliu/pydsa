def subtract(a, b):
    return a + _negate(b)

def _negate(num):
    return ~num + 1

def multiply(a, b):
    memo = {}
    if abs(a) < abs(b):
        a, b = b, a
    if b < 0:
        return _negate(_mul(a, _negate(b), memo))
    else:
        return _mul(a, b, memo)

def _mul(a, b, memo):
    if b == 0: return 0
    if b == 1: return a
    if (a, b) in memo: return memo[(a, b)]

    p = 0
    half_b = b >> 1
    if b % 2 == 0:
        p = _mul(a, half_b, memo) + _mul(a, half_b, memo)
    else:
        p = a + _mul(a, half_b, memo) + _mul(a, half_b, memo)
    memo[(a, b)] = p
    return p

def divide(a, b):
    if a < 0 and b > 0:
        return _negate(_div(_negate(a), b))
    elif a > 0 and b < 0:
        return _negate(_div(a, _negate(b)))
    else:
        return _div(abs(a), abs(b))

def _div(a, b):
    if b == 0: raise ValueError('divisor cannot be zero')
    if a < b: return 0
    return 1 + _div(a - b, b)

print(subtract(7, 3))
print(subtract(31, 28))
print(subtract(3, 0))
print(subtract(5, -2))
print(subtract(4, 6))

print(multiply(10, 7))
print(multiply(125, 16))
print(multiply(3, 0))
print(multiply(0, 11))
print(multiply(5, -3))
print(multiply(-5, 3))
print(multiply(-5, -3))

print(divide(9, 3))
print(divide(-9, 3))
print(divide(9, -3))
print(divide(-9, -3))
print(divide(0, 3))
print(divide(1000, 8))

