def check_anagram(a, b):
    if len(a) != len(b):
        return False
    counter = {}
    for s in a:
        counter[s] = counter.get(s, 0) + 1
    for s in b:
        counter[s] -= 1
        if counter[s] < 0:
            return False
    return True

import random
def shuffle_string(s):
    t = list(s)
    random.shuffle(t)
    return ''.join(t)

a = 'helloworld'
b = shuffle_string(a)
print(check_anagram(a, b))

