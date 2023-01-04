"""Simple recursion: Think about base case and build up"""
def combinate1(str):
    if len(str) == 0: return ['']
    return comb1(str, 0)

def comb1(str, index):
    if index == len(str): return ['']

    result = []
    for substr in comb1(str, index + 1):
        result.append(substr)
        result.append(str[index] + substr)
    return result

"""backtracking: for each element, choose one or not"""
def combinate2(str):
    if len(str) == 0: return ['']
    ans = []
    comb2(str, 0, '', ans)
    return ans

def comb2(str, i, curr, ans):
    if i == len(str):
        ans.append(curr)
        return
    comb2(str, i+1, curr + str[i], ans)
    comb2(str, i+1, curr, ans)

"""DFS: lexical order"""
def combinate3(str):
    if len(str) == 0: return ['']
    ans = []
    comb3(str, 0, '', ans)
    return ans

def comb3(str, i, curr, ans):
    ans.append(curr)
    for j in range(i, len(str)):
        comb3(str, j+1, curr + str[j], ans)

"""BFS: length first then lexical order"""
from collections import deque
def combinate4(str):
    if len(str) == 0: return ['']
    ans = []
    q = deque()
    q.append(("", 0))   # push curr string and option index
    while q:
        (s, i) = q.popleft()
        ans.append(s)
        for j in range(i, len(str)):
            q.append((s + str[j], j+1))
    return ans

if __name__ == '__main__':
    cases = [
        'abc',                  # general
        'abcd',                 # even size
        '',                     # empty
        'a'                     # one
    ]
    for i, case in enumerate(cases):
        print(f"{'case'.upper()} {i+1}: {case}")
        print(combinate1(case))
        print(combinate2(case))
        print(combinate3(case))
        print(combinate4(case))