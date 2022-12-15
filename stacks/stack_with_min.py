from stack import Stack

"""
time:  O(1)
space: O(N)
"""
class StackWithMin(Stack):
    def push(self, val):
        currmin = self.min() if self else float('inf')
        item = self.Item(val, min(currmin, val))
        super().push(item)

    def pop(self):
        item = super().pop()
        return item.val

    def min(self):
        if self.empty():
            raise Exception("Empty stack")
        return self.peek().min

    class Item:
        def __init__(self, val, min):
            self.val = val
            self.min = min

"""
time:  O(1)
space: O(N)
"""
class StackWithMin2(Stack):
    def __init__(self):
        self.minstack = Stack()
        super().__init__()

    def push(self, val):
        if self.empty() or val <= self.minstack.peek():
            self.minstack.push(val)
        super().push(val)

    def pop(self):
        val = super().pop()
        if val == self.minstack.peek():
            self.minstack.pop()
        return val

    def min(self):
        if self.minstack:
            return self.minstack.peek()
        else:
            raise Exception("Empty stack")

"""
assume all values to be handled are integers
time:  O(1)
space: O(1)
"""
class StackWithMin3(Stack):
    def __init__(self):
        self._min = None
        super().__init__()

    def push(self, val):
        if self.empty():
            self._min = val
            super().push(val)
        else:
            if val >= self._min:
                super().push(val)
            else:
                x = val * 2 - self._min
                super().push(x)
                self._min = val

    def pop(self):
        x = super().pop()
        if x >= self._min:
            return x
        else:
            val = self._min
            self._min = val * 2 - x
            return val
    
    def min(self):
        if self.empty():
            raise Exception("Empty stack")
        else:
            return self._min

stack = StackWithMin()
for val in [5,7,3,4,2]:
    stack.push(val)
print([item.val for item in stack])
print([item.min for item in stack])
while stack:
    print(stack.min(), stack.pop())

print("----" * 4)
stack = StackWithMin2()
for val in [5,7,3,4,2]:
    stack.push(val)
print(*stack)
print(*stack.minstack)
while stack:
    print(stack.min(), stack.pop())

print("----" * 4)
stack = StackWithMin3()
for val in [5,7,3,4,2]:
    stack.push(val)
while stack:
    print(stack.min(), stack.pop())