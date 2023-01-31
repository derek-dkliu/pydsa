#time: O(n)
def calculator(expr):
    nums = []
    ops = []
    index = 0
    while index < len(expr):
        c = expr[index]
        if c.isdecimal():
            num, index = fetch_num(expr, index)
            nums.append(num)
        else:
            while ops and priority(c) <= priority(ops[-1]):
                compute(nums, ops)
            ops.append(c)
            index += 1
    while ops:
        compute(nums, ops)
    return nums.pop()

def fetch_num(expr, start):
    index = start
    while index < len(expr) and expr[index].isdecimal():
        index += 1
    return int(expr[start: index]), index

def compute(nums, ops):
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
    elif op == '/':
        val = v1 / v2
    else:
        raise Exception('invalid operation')
    nums.append(val)
    
def priority(op):
    if op == '+' or op == '-':
        return 1
    else:
        return 2


class Term:
    def __init__(self, op, num):
        self.op = op
        self.num = num

    def apply_result(self, val):
        return Term.compute(val, self.op, self.num)

    def apply_term(self, term):
        self.num = Term.compute(self.num, term.op, term.num)

    @staticmethod
    def compute(v1, op, v2):
        val = 0
        if op == '+':
            val = v1 + v2
        elif op == '-':
            val = v1 - v2
        elif op == '*':
            val = v1 * v2
        elif op == '/':
            val = v1 / v2
        else:
            raise Exception('invalid operation')
        return val

    @staticmethod
    def parse_num(expr, start):
        index = start
        while index < len(expr) and expr[index].isdecimal():
            index += 1
        return int(expr[start: index]), index

def parse_terms(expr):
    terms = []
    op = '+'
    index = 0
    while index < len(expr):
        if index > 0:
            op = expr[index]
            index += 1
        num, index = Term.parse_num(expr, index)
        terms.append(Term(op, num))
    return terms

def calculatorByTerm(expr):
    result = 0
    buffer = None
    terms = parse_terms(expr)
    for i in range(len(terms)):
        curr = terms[i]
        if buffer is None:
            buffer = curr
        else:
            buffer.apply_term(curr)
        next = terms[i + 1] if i < len(terms) - 1 else None
        if next is None or next.op == '+' or next.op == '-':
            result = buffer.apply_result(result)
            buffer = None
    return result


print(calculator("11+2*3-4"))
print(calculator("1+2*3-4+5"))
print(calculator("1+2*3-4/2"))
print(calculator("1+2*3-4/5-6+7"))
print(calculator("0"))
print('-' * 5)
print(calculatorByTerm("11+2*3-4"))
print(calculatorByTerm("1+2*3-4+5"))
print(calculatorByTerm("1+2*3-4/2"))
print(calculatorByTerm("1+2*3-4/5-6+7"))
print(calculatorByTerm("0"))

