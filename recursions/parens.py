"""
1. build the solution of n parens from solution of n-1 parens
2. insert a pair of parens to every existing parens identified by left paren
3. insert a pair of parens at the beginning
4. any other places wound reduce to the earlier cases.
"""
def parens(n):
    result = set()
    if n == 0:
        result.add('')
        return result
    if n == 1:
        result.add('()')
        return result

    for item in parens(n - 1):
        for i in range(len(item)):
            if item[i] == '(':
                result.add(item[0:i+1] + '()' + item[i+1:])
        result.add('()' + item)
    return result

"""
1. generate each string of the solution from scratch
2. add either left or right paren at each step, decrease the remaining count of left or right paren
3. once we are run out of left paren or the remaining right paren are less than left paren, stop as it is invalid
4. when both left and right parens are used up, add the current string to the result list
"""
# def parens2(n):
#     result = []
#     curr = [None] * (n * 2)
#     gen_parens(n, n, 0, curr, result)
#     return result

# def gen_parens(left_rem, right_rem, index, curr, result):
#     if left_rem < 0 or right_rem < left_rem:
#         return
#     if left_rem == 0 and right_rem == 0:
#         result.append(''.join(curr))
#         return
#     curr[index] = '('
#     gen_parens(left_rem - 1, right_rem, index + 1, curr, result)
#     curr[index] = ')'
#     gen_parens(left_rem, right_rem - 1, index + 1, curr, result)

def parens2(n):
    result = []
    gen_parens(n, n, [], result)
    return result

def gen_parens(left_rem, right_rem, curr, result):
    if left_rem < 0 or right_rem < left_rem:
        return
    if left_rem == 0 and right_rem == 0:
        result.append(''.join(curr))
        return
    curr.append('(')
    gen_parens(left_rem - 1, right_rem, curr, result)
    curr.pop()
    curr.append(')')
    gen_parens(left_rem, right_rem - 1, curr, result)
    curr.pop()

import math
def catalan(n):
    return math.factorial(2 * n) / math.factorial(n + 1) / math.factorial(n)

print(parens(0))
print(parens2(0))
print(parens(1))
print(parens2(1))
print(parens(2))
print(parens2(2))
print(parens(3))
print(parens2(3))
print(parens(4), catalan(4))
print(parens2(4), catalan(4))
print(len(parens(5)), catalan(5))
print(len(parens2(5)), catalan(5))
print(len(parens(6)), catalan(6))
print(len(parens2(6)), catalan(6))
print(len(parens(7)), catalan(7))
print(len(parens2(7)), catalan(7))