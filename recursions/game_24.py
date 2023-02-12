"""Brute force solution"""
def gen24():
    results = []
    candidates = []
    _gen24(4, [], candidates)
    for expr in candidates:
        vals = calculate(expr)
        if any(map(lambda x: round(x, 10) == 24, vals)):
            results.append(expr)
    return results

def _gen24(n, curr, results):
    for i in range(1, 11):
        curr.append(i)
        if n == 1:
            results.append(curr[:])
        else:
            for op in "+-*/":
                curr.append(op)
                _gen24(n - 1, curr, results)
                curr.pop()
        curr.pop()

def calculate(expr):
    return calc(expr, 0, len(expr) - 1)

def calc(expr, low, high):
    if low == high:
        return [expr[low]]

    results = []
    for i in range(low + 1, high, 2):
        lefts = calc(expr, low, i - 1)
        rights = calc(expr, i + 1, high)
        for v1 in lefts:
            for v2 in rights:
                val = compute(v1, v2, expr[i])
                if val is not None:
                    results.append(val)
    return results

def compute(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    else:
        return v1 / v2 if v2 != 0 else None

# results = gen24()
# combinations = {}
# for expr in results:
#     key = tuple(sorted([v for v in expr if isinstance(v, int)]))
#     solutions = combinations.get(key, [])
#     solutions.append(expr)
#     combinations[key] = solutions

# singles = []
# for key, solutions in combinations.items():
#     if len(solutions) == 1:
#         singles.append([key, *solutions])
# singles.sort(key=lambda x: x[0])

# print(len(results), len(combinations), len(singles))
# print('\n'.join(map(lambda x: f"{x[0]}\t: {x[1]}", singles)))

# cases = [(1,5,5,5),(3,3,8,8),(5,6,6,9)]
# for key in cases:
#     print(combinations.get(key, None))

"""First generate unique combinations, then solve each of them"""
def combination(n, k):
    results = []
    nums = list(range(1, n + 1))
    combinate(nums, k, 0, [], results)
    return results

def combinate(nums, k, index, curr, results):
    if index == len(nums):
        return
    if len(curr) == k:
        results.append(curr[:])
        return

    curr.append(nums[index])
    combinate(nums, k, index, curr, results)
    curr.pop()
    combinate(nums, k, index + 1, curr, results)

def solve(arr):
    results = set()
    _solve(arr, list(map(str, arr)), results)
    return results

def _solve(arr, opt, results):
    if len(arr) == 1:
        if abs(arr[0] - 24) <= 1e-10:
            results.add(opt[0])
        return

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            new_arr = [v for k, v in enumerate(arr) if k != i and k != j]
            new_opt = [v for k, v in enumerate(opt) if k != i and k != j]
            a, b = compute_possibles(arr[i], arr[j], opt[i], opt[j])
            for v, e in zip(a, b):
                new_arr.append(v)
                new_opt.append(e)
                _solve(new_arr, new_opt, results)
                new_opt.pop()
                new_arr.pop()

def compute_possibles(a, b, e, f):
    res = [a+b, a-b, b-a, a*b]
    expr = [f"({e}+{f})", f"({e}-{f})", f"({f}-{e})", f"({e}*{f})"]
    if a:
        res.append(b / a)
        expr.append(f"({f}/{e})")
    if b:
        res.append(a / b)
        expr.append(f"({e}/{f})")
    return res, expr

# def _solve(arr):
#     if len(arr) == 1:
#         return abs(arr[0] - 24) <= 1e-10
#     for i in range(len(arr)):
#         for j in range(i + 1, len(arr)):
#             rest = [v for k, v in enumerate(arr) if k != i and k != j]
#             for v in compute_possibles(arr[i], arr[j]):
#                 rest.append(v)
#                 if _solve(rest):
#                     return True
#                 rest.pop()
#     return False

# def compute_possibles(a, b):
#     res = [a+b, a-b, b-a, a*b]
#     if a:
#         res.append(b / a)
#     if b:
#         res.append(a / b)
#     return res

def evaluate(expr):
    rater = Rater()
    nums = []
    ops = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c == '(':
            i += 1
        elif c.isnumeric():
            j = fetch_number(expr, i)
            nums.append(int(expr[i:j]))
            i = j
        elif c == ')':
            v2 = nums.pop()
            v1 = nums.pop()
            op = ops.pop()
            val = 0
            if op == '+':
                val = v1 + v2
            elif op == '-':
                val = v1 - v2
            elif op == '*':
                val = v1 * v2
            else:
                val = v1 / v2
            nums.append(val)
            rater.check(v1, v2, op)
            i += 1
        else:
            ops.append(expr[i])
            i += 1
    # return nums.pop()
    return rater.score()

def fetch_number(expr, start):
    index = start
    while index < len(expr) and expr[index].isnumeric():
        index += 1
    return index

class Rater:
    def __init__(self):
        self.frac = 0
        self.bigs = 0
        self.prod = 0
        self.divs = 0
        self.muls = 0
        self.subs = 0
        self.adds = 0
        self.misc = 0

    def score(self):
        return self.frac * 9 + self.bigs * 8 + self.divs * 7 + self.prod * 4 + \
            self.muls * 3 + self.subs * 2 + self.adds + self.misc

    def check(self, v1, v2, op):
        if int(v1) != v1 or int(v2) != v2:
            self.frac += 1
        if op == '+':
            self.adds += 1
        elif op == '-':
            if v1 > 25 and self.subs == 0:
                self.bigs += 1
            self.subs += 1
        elif op == '*':
            if v1 > 10 or v2 > 10:
                self.prod += 1
            if v1 != 1 and v2 != 1:
                self.muls += 1
        else:
            if v1 > 24:
                self.bigs += 1
            elif v1 > 10:
                self.misc += 3
            if v1 != v2 and v2 != 1:
                self.divs += 1

results = combination(10, 4)
print('combinations:', len(results))

solvables = {}
solutions = []
for arr in results:
    sols = solve(arr)
    if sols:
        solvables[tuple(arr)] = sols
    for sol in sols:
        solutions.append(sol)
print('solvables:', len(solvables))
print('solutions:', len(solutions))

# cases = [(1,5,5,5),(3,3,8,8),(5,6,6,9),(1,4,5,6),(2,5,5,10)]
# for key in cases:
#     print(solvables.get(key, None))

def score_and_sort(arr):
    min = float('inf')
    scores = {}
    for expr in arr:
        score = evaluate(expr)
        if score <= min:
            min = score
        scores[expr] = score
    sorted_sols = sorted(arr, key=lambda x:scores[x])
    return round(min, 3), sorted_sols

puzzles = []
for puzzle, sols in solvables.items():
    score, sorted_sols = score_and_sort(sols)
    puzzles.append([puzzle, score, sorted_sols])
puzzles.sort(key=lambda x: x[1], reverse=True)

for i in range(60):
    puzzle, score, sols = puzzles[i]
    sols = ', '.join(sols[:5]) + ('...' if len(sols) > 5 else '')
    print(f"{puzzle}\t{score}\t{sols}")
