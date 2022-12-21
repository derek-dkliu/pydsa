def longest_ones(n):
    if n == 0: return 1
    prev = 0
    curr = 0
    ans = 0
    haszero = 0
    while n != 0:
        if n & 1 > 0:
            curr += 1
        else:
            prev = curr
            curr = 0
            haszero = 1
        ans = max(prev + curr + haszero, ans)
        n = rshift(n, 1)
    return ans

def rshift(n, m):
    return (n % 0x100000000) >> m

cases = [
    0b11110111011,
    0b1100111,      # two consecutive 0s
    0b1111,         # all ones
    0b101,
    0b100,
    0b10,
    1,              # one
    0,              # zero        
    -1,             # all ones
    -5,             # negative
    -6,             # negative ending with 0
]
for i, case in enumerate(cases):
    print(f"case {i+1}: {case:b}")
    print(longest_ones(case))