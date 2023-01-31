class LRU:
    def __init__(self, max):
        self.max = max
        self.map = {}
        self.head = None
        self.tail = None

    def retrieve(self, key):
        if key not in self.map:
            return None
        node = self.map[key]
        self.move_to_head(node)
        return node.val

    def insert(self, key, val):
        # update value if key exists
        if key in self.map:
            node = self.map[key]
            node.val = val
            self.move_to_head(node)
        else:
            node = Node(key, val)
            self.add_to_head(node)
            self.map[key] = node
            if len(self.map) > self.max:
                self.delete(self.tail)

    def delete(self, key):
        if key not in self.map:
            return
        node = self.map[key]
        del self.map[key]
        self.remove_from_list(node)

    def move_to_head(self, node):
        if node is self.head:
            return
        self.remove_from_list(node)
        self.add_to_head(node)
        
    def add_to_head(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

    def remove_from_list(self, node):
        if node is None:
            return
        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev
        if node is self.head:
            self.head = next
        if node is self.tail:
            self.tail = prev
        node.prev = None
        node.next = None

    def __str__(self):
        sb = []
        node = self.head
        while node:
            sb.append(str(node))
            node = node.next
        return " -> ".join(sb)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

    def __str__(self):
        return f"{self.key}|{self.val}"


cache = LRU(5)
for key in 'abcdaefee':
    cache.insert(key, ord(key))
    print(cache)