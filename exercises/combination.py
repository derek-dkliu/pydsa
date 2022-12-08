"""backtracking: for each element, choose one or not"""
def combinate1(str):
    if len(str) == 0: return ['']
    ans = []
    comb1(str, 0, '', ans)
    return ans

def comb1(str, i, curr, ans):
    if i == len(str):
        ans.append(curr)
        return
    comb1(str, i+1, curr + str[i], ans)
    comb1(str, i+1, curr, ans)

"""DFS: lexical order"""
def combinate2(str):
    if len(str) == 0: return ['']
    ans = []
    comb2(str, 0, '', ans)
    return ans

def comb2(str, i, curr, ans):
    ans.append(curr)
    for j in range(i, len(str)):
        comb2(str, j+1, curr + str[j], ans)

"""BFS: length first then lexical order"""
from collections import deque
def combinate3(str):
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