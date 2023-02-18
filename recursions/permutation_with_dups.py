"""Recursion tree"""
def permutation(string):
    result = []
    permutate(string, [], result)
    return result

def permutate(string, curr, result):
    if len(string) == 0:
        result.append(''.join(curr))
        return
    chosen = set()
    for i in range(len(string)):
        if string[i] in chosen: continue
        chosen.add(string[i])
        remainder = string[0:i] + string[i + 1:]
        curr.append(string[i])
        permutate(remainder, curr, result)
        curr.pop()

print(permutation(''))
print(permutation('aaaaaa'))
print(permutation('abb'))
print(permutation('abbc'))