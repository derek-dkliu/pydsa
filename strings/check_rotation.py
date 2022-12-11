def check_rotation(s1, s2):
    return len(s1) == len(s2) and s1 in s2 + s2

cases = [
    ['bottlewater', 'erbottlewat'],
    ['abc', 'cabcab']
]
for i, (s1, s2) in enumerate(cases):
    print(f"Case {i+1}:", s1, s2)
    print(check_rotation(s1, s2))