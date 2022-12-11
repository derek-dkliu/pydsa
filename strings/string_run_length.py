def string_run_length(s):
    comp = []
    count = 1
    for i in range(len(s)):
        if i == len(s) - 1 or s[i] != s[i+1]:
            comp.append(s[i] + str(count))
            count = 1
        else:
            count += 1
    comp = ''.join(comp)
    return comp if len(comp) < len(s) else s

cases = [
    "aabcccccaaa",
    "abc",
    ""
]
for i, s in enumerate(cases):
    print(f"Case {i+1}:", s, string_run_length(s))


