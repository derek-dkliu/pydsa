"""
pros:
1. easier to implement delete
2. preformance degrades gracefully.
cons:
1. not cache friendly
"""
class SeparateChaining:
    init_capacity = 10

    def __init__(self, m = 0):
        self.m = m or SeparateChaining.init_capacity
        self.n = 0
        self.data = [None] * self.m

    def contains(self, key):
        return self.get(key) != None

    def get(self, key):
        if key == None: raise Exception("None key")
        i = self._hash(key)
        node = self.data[i]
        while node:
            if node.key == key:
                return node.val
            node = node.next
        return None

    def put(self, key, val):
        if key == None: raise Exception("None key")
        if val is None:
            self.delete(key)
            return

        # # double table size if average lenght of list >= 10
        # if self.n >= self.m * 10:
        #     self._resize(self.m * 2)

        i = self._hash(key)
        node = self.data[i]
        while node:
            if node.key == key:
                node.val = val
                return
            node = node.next
        self.data[i] = Node(key, val, self.data[i])
        self.n += 1

    def delete(self, key):
        if key == None: raise Exception("None key")
        i = self._hash(key)
        self.data[i] = self._delete(self.data[i], key)

        # # halve table size if average length of list <= 2
        # if self.m > SeparateChaining.init_capacity and self.n <= self.m * 2:
        #     self._resize(self.m // 2)

    def _delete(self, node, key):
        if node is None: return None
        if node.key == key:
            self.n -= 1
            return node.next
        node.next = self._delete(node.next, key)
        return node

    def _resize(self, capacity):
        temp = SeparateChaining(capacity)
        for node in self.data:
            while node:
                temp.put(node.key, node.val)
                node = node.next
        self.data = temp.data
        self.m = temp.m
        self.n = temp.n

    def _hash(self, key):
        return hash(key) % self.m

    def __len__(self):
        return self.n

    def __str__(self):
        out = ''
        for i, node in enumerate(self.data):
            out += f"{i}: "
            while node:
                out += f"{node.key}|{node.val}"
                node = node.next
                if node:
                    out += " -> "
            out += '\n'
        return out

class Node:
    def __init__(self, key, val, next):
        self.key = key
        self.val = val
        self.next = next

if __name__ == '__main__':
    hashmap = SeparateChaining()
    for i in range(65, 80):
        hashmap.put(chr(i), i)
    print(hashmap)
    print(len(hashmap))

