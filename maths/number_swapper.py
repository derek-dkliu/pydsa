# sum may cause number overflow
def swap(a, b):
    a += b
    b = a - b
    a = a - b
    print(a, b)

# diff is preferred
def swap2(a, b):
    a -= b
    b += a
    a = b - a
    print(a, b)

# use xor
def swap3(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a, b)

cases =[
    [3, 5],
    [2, 2],
    [0, 5]
]
for a, b in cases:
    print(a, b)
    swap3(a, b)
