def boolean_evaluation(exp, result):
    count = evaluate(exp, result, 0, len(exp) - 1, {})
    return count

def evaluate(exp, result, low, high, memo):
    if low == high:
        return 1 if str2bool(exp[low]) == result else 0

    substr = exp[low: high+1]
    if (result, substr) in memo: return memo[(result, substr)]

    count = 0
    for i in range(low + 1, high):
        op = exp[i]
        ltotal = catalan_number((i - low) // 2)
        rtotal = catalan_number((high - i) // 2)
        ltrue = evaluate(exp, True, low, i - 1, memo)
        rtrue = evaluate(exp, True, i + 1, high, memo)
        lfalse = ltotal - ltrue
        rfalse = rtotal - rtrue
        if op == '|':
            if result:
                count += ltrue * rtrue
                count += ltrue * rfalse
                count += lfalse * rtrue
            else:
                count += lfalse * rfalse
        elif op == '&':
            if result:
                count += ltrue * rtrue
            else:
                count += ltrue * rfalse
                count += lfalse * rtrue
                count += lfalse * rfalse
        elif op == '^':
            if result:
                count += ltrue * rfalse
                count += lfalse * rtrue
            else:
                count += ltrue * rtrue
                count += lfalse * rfalse
    memo[(result, substr)] = count
    return count
        
def str2bool(string):
    return string == '1'

import math
def catalan_number(n):
    return int(math.factorial(2 * n) / (math.factorial(n+1) * math.factorial(n)))

cases = [
    ("1^0|0|1", False),
    ("0&0&0&1", False),
    ("0&0&0&1^1|0", True)
]

for expression, result in cases:
    count = boolean_evaluation(expression, result)
    print(expression, result, count)
