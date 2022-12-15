from stack import Stack

class MultipleStacks(Stack):
    def __init__(self, threshold):
        self.threshold = threshold
        self.stacks = []
        self.n = 0

    def push(self, val):
        if self.empty() or len(self.stacks[-1]) == self.threshold:
            self.stacks.append(Stack())
        stack = self.stacks[-1]
        stack.push(val)
        self.n += 1

    def pop(self):
        if self.empty():
            raise Exception("Empty stack")
        stack = self.stacks[-1]
        item = stack.pop()
        self.n -= 1
        if stack.empty():
            self.stacks.pop()
        return item

    def popat(self, index):
        if self.empty():
            raise Exception("Empty stack")
        if index < 0 or index >= len(self.stacks):
            raise Exception("Stack index out of range")
        stack = self.stacks[index]
        if stack.empty():
            raise Exception(f"Empty stack {index}")
        item = stack.pop()
        if stack.empty():
            del self.stacks[index]
        self.n -= 1
        return item

    def empty(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def __str__(self):
        res = []
        for i, stack in enumerate(self.stacks):
            res.append(f"{i}: {' '.join(map(str, stack))}")
        return '\n'.join(res)

import random
stacks = MultipleStacks(5)
for val in range(17):
    stacks.push(val)
    print(stacks)
    print('----' * 4)
while stacks:
    index = random.randint(0, len(stacks.stacks) - 1)
    print(index, stacks.popat(index))
