def dec2binstr(n):
    if n == 0: return '0'
    sign = ''
    if n < 0:
        sign = '-'
        n = -n
    whole = int(n)
    frac = n - whole
    return sign + int2binstr(whole) + frac2binstr(frac)

from collections import deque
def int2binstr(n):
    bins = deque()
    while n > 0:
        bins.appendleft(str(n & 1))
        n >>= 1
    return ''.join(bins)

def frac2binstr(n):
    if n < 0 or n >= 1:
        raise Exception('Not a fraction number')
    bins = []
    while n > 0:
        n *= 2
        if n >= 1:
            bins.append('1')
            n -= 1
        else:
            bins.append('0')
    str = ''.join(bins)
    return '.' + str if str != '' else ''

for case in [1/2+1/8+1/16, .72, 11.5, 11.2, -12.34, 0]:
    print(case, "=", dec2binstr(case))
