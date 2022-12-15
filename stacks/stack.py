class Stack:
    def __init__(self, capacity = 1):
        self.data = [None] * capacity
        self.n = 0

    def peek(self):
        if self.empty(): return None
        return self.data[self.n - 1]

    def push(self, item):
        if self.n == len(self.data):
            self._resize(self.n * 2)

        self.data[self.n] = item
        self.n += 1

    def pop(self):
        if self.empty():
            raise Exception("Empty stack")
        item = self.data[self.n - 1]
        self.data[self.n - 1] = None
        self.n -= 1
        if self.n > 0 and self.n <= len(self.data) / 4:
            self._resize(len(self.data) // 2)
        return item

    def _resize(self, capacity):
        temp = [None] * capacity
        for i in range(self.n):
            temp[i] = self.data[i]
        self.data = temp

    def empty(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def __iter__(self):
        self.count = self.n
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            return self.data[self.count]
        else:
            raise StopIteration

class StackList:
    def __init__(self):
        self.head = None
        self.n = 0

    def peek(self):
        if self.empty(): return None
        return self.head.val

    def push(self, item):
        self.head = Node(item, self.head)
        self.n += 1

    def pop(self):
        if self.empty():
            raise Exception("Empty stack")
        item = self.head.val
        self.head = self.head.next
        self.n -= 1
        return item

    def empty(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def __iter__(self):
        self._curr = self.head
        return self

    def __next__(self):
        if self._curr:
            item = self._curr.val
            self._curr = self._curr.next
            return item
        else:
            raise StopIteration

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

if __name__ == '__main__':
    stack = Stack()
    s = 'hello_world'
    print(s)
    for c in s:
        stack.push(c)
    for c in stack:
        print(c, end="")
    print()
    while stack:
        print(stack.pop(), end="")
    print()
    print(len(stack))

    stacklist = StackList()
    s = 'dog is god'
    print(s)
    for c in s:
        stacklist.push(c)
    for c in stacklist:
        print(c, end="")
    print()
    while stacklist:
        print(stacklist.pop(), end="")
    print()
    print(len(stacklist))