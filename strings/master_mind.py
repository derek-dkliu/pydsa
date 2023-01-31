# time:  O(n)
# space: O(n)
def master_mind(solution, guess):
    indexset = {}
    for i, s in enumerate(solution):
        if s not in indexset:
            indexset[s] = set()
        indexset[s].add(i)

    hit = 0
    pseudo_count = {}
    for i, s in enumerate(guess):
        if s in indexset:
            if i in indexset[s]:
                hit += 1
                indexset[s].remove(i)
            else:
                if s not in pseudo_count:
                    pseudo_count[s] = 0
                pseudo_count[s] += 1
    pseudo_hit = 0
    for s, c in pseudo_count.items():
        if s in indexset:
            pseudo_hit += min(c, len(indexset[s]))
    return hit, pseudo_hit
    
# time:  O(n)
# space: O(n)
from collections import Counter
def master_mind2(solution, guess):
    hit = 0
    counter = Counter()     # freq of each non-hit char
    for i, s in enumerate(solution):
        if s == guess[i]:
            hit += 1
        else:
            counter[s] += 1
    pseudo_hit = 0
    for i, s in enumerate(guess):
        if s != solution[i] and counter[s] > 0:
            pseudo_hit += 1
            counter[s] -= 1
    return hit, pseudo_hit


cases = [
    ('RGBY', 'BGRY'),
    ('RGBY', 'YYYY'),
    ('RGBY', 'YBGR'),
]
for (solution, guess) in cases:
    print(master_mind(solution, guess), master_mind2(solution, guess))