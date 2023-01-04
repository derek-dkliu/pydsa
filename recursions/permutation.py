"""Simple recursion: Think about base case and build up"""
def permutate1(str):
    if len(str) == 0: return ['']
    return perm1(str, 0)

def perm1(str, i):
    if i == len(str) - 1: return [str[i]]

    result = []
    c = str[i]
    for s in perm1(str, i + 1):
        for j in range(len(s) + 1):
            result.append(s[0:j] + c + s[j:])
    return result

"""Backtracking: Draw a tree with available optoins as branches"""
def permutate2(str):
    if len(str) == 0: return ['']
    ans = []
    perm2(str, '', ans)
    return ans

def perm2(opt, curr, ans):
    if len(opt) == 1:
        ans.append(curr + opt)
        return
    for i in range(len(opt)):
        perm2(opt[0:i] + opt[i+1:], curr + opt[i], ans)

"""Backtracking + In-place swap"""
def permutate3(str):
    if len(str) == 0: return ['']
    ans = []
    perm3(list(str), 0, ans)
    return ans

def perm3(arr, i, ans):
    if i == len(arr): 
        ans.append(''.join(arr))
        return
    for j in range(i, len(arr)):
        swap(arr, i, j)
        perm3(arr, i + 1, ans)
        swap(arr, i, j)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == '__main__':
    cases = [
        'abc',                  # general
        'abcd',                 # even size
        '',                     # empty
        'a'                     # one
    ]
    for i, case in enumerate(cases):
        print(f"{'case'.upper()} {i+1}: {case}")
        print(permutate1(case))
        print(permutate2(case))
        print(permutate3(case))