def one_edit_away1(s1, s2):
    if len(s1) == len(s2):
        return one_replace(s1, s2)
    elif len(s1) + 1 == len(s2):
        return one_insert(s1, s2)
    elif len(s2) + 1 == len(s1):
        return one_insert(s1, s1)
    else:
        return False

def one_replace(s1, s2):
    diff = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if diff: return False
            diff = True
    return True

def one_insert(s1, s2):
    i = 0
    j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if i != j: return False
            j += 1
        else:
            i += 1
            j += 1
    return True

def one_edit_away2(s1, s2):
    if abs(len(s1) - len(s2)) > 1: return False

    if len(s1) > len(s2):
        s1, s2 = s2, s1
    i = 0
    j = 0
    diff = False
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if diff: return False
            diff = True
            if len(s1) == len(s2):
                i += 1
            j += 1
        else:
            i += 1
            j += 1

    return True

cases = [
    ('pat','pad'),      # len(s1) == len(s2)
    ('pale', 'ple'),    # len(s1) - 1 == len(s2)
    ('tee', 'teer'),    # len(s1) + 1 == len(s2)
    ('tee', 'rtee'),    # len(s1) + 1 == len(s2)
    ('tee', 'tree'),    # len(s1) + 1 == len(s2)
    ('tap', 'pat')      # permutation
]
for i, (s1, s2) in enumerate(cases):
    print(f"Case {i+1}:", s1, s2)
    print(one_edit_away1(s1, s2))
    print(one_edit_away2(s1, s2))