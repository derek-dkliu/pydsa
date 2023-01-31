def factorial_zeros(n):
    if n < 0: return -1
    map = dict()
    i = 1
    while i * 5 <= n:
        map[i * 5] = 1 + map.get(i, 0)
        i += 1
    count = sum(map.values())
    return count

def factorial_zeros2(n):
    if n < 0: return -1
    count = 0
    i = 5
    while n // i > 0:
        count += n // i
        i *= 5
    return count

for n in [1, 5, 10, 13, 99, 100]:
    print(n, factorial_zeros(n), factorial_zeros2(n))