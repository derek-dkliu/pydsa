def dec2binstr(n):
    if n <= 0 or n >= 1:
        return 'ERROR'
    bins = []
    while n > 0:
        n *= 2
        if n >= 1:
            bins.append('1')
            n -= 1
        else:
            bins.append('0')
        if len(bins) > 32:
            return 'ERROR'
    return ''.join(bins)

for case in [1/2+1/8+1/16, .72]:
    print(case, "=", dec2binstr(case))
    