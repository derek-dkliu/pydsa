from collections import Counter

# O(n): use counter
def palindrome_perm1(string):
    counter = Counter()
    for s in filter(str.isalpha, string.lower()):
        counter[s] += 1
    odd = False
    for count in counter.values():
        if count % 2 == 1:
            if odd: return False
            odd = True
    return True

# O(n): use bitmap
def palindrome_perm2(string):
    bitmap = 0
    for s in filter(str.isalpha, string.lower()):
        p = ord(s) - ord('a')
        bitmap ^= (1 << p)
    # to check if a bitmap has exactly one bit set to 1:
    # subtract one from the integer, then AND it with the integer
    return bitmap == 0 or bitmap & (bitmap - 1) == 0

cases = ['Tact Coa', '', 'abc']
for i, case in enumerate(cases):
    print(f"case {i+1}: {case}")
    print(palindrome_perm1(case))
    print(palindrome_perm2(case))
