# time:  O(n*n*n!)
# space: O(n!)
def permutation(string):
    result = []
    permutate(string, [], result)
    return result

def permutate(string, curr, result):
    if len(string) == 0:
        result.append(''.join(curr))
        return
    for i in range(len(string)):
        remainder = string[0:i] + string[i + 1:]
        curr.append(string[i])
        permutate(remainder, curr, result)
        curr.pop()

print(permutation(''))
print(permutation('a'))
print(permutation('ab'))
print(permutation('abc'))