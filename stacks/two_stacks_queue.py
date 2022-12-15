from stack import Stack

class Queue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def empty(self):
        return self.s1.empty() and self.s2.empty()

    def __len__(self):
        return len(self.s1) + len(self.s2)

    def add(self, item):
        self.s1.push(item)

    def remove(self):
        if self.empty():
            raise Exception("Empty queue")
        if self.s2.empty():
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if self.empty(): return None
        if self.s2.empty():
            while self.s1:
                self.s2.push(self.s1.pop())
        return self.s2.peek()

    def __iter__(self):
        self._temp = list(self.s2) + list(reversed(list(self.s1)))
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._temp):
            item = self._temp[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration 

queue = Queue()
for i in range(10):
    queue.add(i)
print(*queue)
while queue:
    print(queue.peek(), queue.remove())

