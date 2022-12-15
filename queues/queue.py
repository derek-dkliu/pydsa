class Queue:
    def __init__(self, capacity = 1):
        self.first = 0      # position to remove item
        self.last = 0       # position to add item
        self.n = 0          # number of items
        self.data = [None] * capacity

    def peek(self):
        if self.empty(): return None
        return self.data[self.first]

    def add(self, item):
        if self.n == len(self.data):
            self._resize(self.n * 2)

        self.data[self.last] = item
        self.last += 1
        if self.last == len(self.data):
            self.last = 0
        self.n += 1
        
    def remove(self):
        if self.empty():
            raise Exception("Empty queue")
        item = self.data[self.first]
        self.data[self.first] = None
        self.first += 1
        if self.first == len(self.data):
            self.first = 0
        self.n -= 1

        if self.n > 0 and self.n <= len(self.data) / 4:
            self._resize(len(self.data) // 2)
        return item

    def _resize(self, capacity):
        temp = [None] * capacity
        for i in range(self.n):
            temp[i] = self.data[(self.first + i) % len(self.data)]
        self.data = temp
        self.first = 0
        self.last = self.n
    
    def empty(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def __iter__(self):
        self.count = -1
        return self

    def __next__(self):
        if self.count < self.n - 1:
            self.count += 1
            return self.data[(self.first + self.count) % len(self.data)]
        else:
            raise StopIteration

class QueueList:
    def __init__(self):
        self.first = None       # first item to remove
        self.last = None        # append to last item to add
        self.n = 0

    def peek(self):
        if self.empty(): return None
        return self.first.val

    def add(self, item):
        node = Node(item)
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.n += 1

    def remove(self):
        if self.empty():
            raise Exception("Empty queue")
        item = self.first.val
        self.first = self.first.next
        if self.first is None:
            self.last = None
        self.n -= 1
        return item

    def empty(self):
        return self.n == 0

    def __len__(self):
        return self.n

    def __iter__(self):
        self._curr = self.first
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
    queue = Queue()
    s = 'hello_world'
    print(s)
    for c in s:
        queue.add(c)
    for c in queue:
        print(c, end="")
    print()
    while queue:
        print(queue.remove(), end="")
    print()
    print(len(queue))

    queuelist = Queue()
    s = 'hello_world'
    print(s)
    for c in s:
        queuelist.add(c)
    for c in queuelist:
        print(c, end="")
    print()
    while queuelist:
        print(queuelist.remove(), end="")
    print()
    print(len(queuelist))