class Cache1:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None        # point to oldest node
        self.tail = None        # point to newest node
        self.map = dict()       # map from query to node
        self.size = 0

    def upsert(self, query, results):
        if query in self.map:
            node = self.map[query]
            node.val = results
            self.move_to_tail(node)
            return
        
        self.append_to_tail(query, results)
        if self.size > self.capacity:
            self.remove_from_head()

    def get(self, query):
        if query not in self.map:
            return None
        node = self.map[query]
        self.move_to_tail(node)
        return node.val

    def remove_from_head(self):
        del self.map[self.head.key]
        self.head = self.head.next
        self.size -= 1

    def append_to_tail(self, query, results):
        node = Node1(query, results)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.map[query] = node
        self.size += 1

    def move_to_tail(self, node):
        if node == self.tail:
            return
        else:
            # swap content of node with node.next
            self.map[node.key] = node.next
            self.map[node.next.key] = node
            node.key, node.next.key = node.next.key, node.key
            node.val, node.next.val = node.next.val, node.val
            # move node.next to tail
            if node.next != self.tail:
                next = node.next
                node.next = node.next.next
                next.next = None
                self.tail.next = next
                self.tail = next

    def __str__(self):
        sb = []
        node = self.head
        while node:
            sb.append(str(node))
            node = node.next
        return " -> ".join(sb)

class Node1:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

    def __str__(self):
        return f"{self.key}|{self.val}"
    
class Cache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None    # point to newest node
        self.tail = None    # point to oldest node
        self.map = dict()   # map from query to node
        self.size = 0

    def upsert(self, query, results):
        if query in self.map:
            node = self.map[query]
            node.val = results
            self.move_to_front(node)
            return

        # add new node to head
        node = Node2(query, results)
        self.move_to_front(node)
        self.map[query] = node
        self.size += 1

        # remove oldest node if full 
        if self.size > self.capacity:
            del self.map[self.tail.key]
            self.remove_from_list(self.tail)
            self.size -= 1

    def get(self, query):
        if query not in self.map:
            return None
        node = self.map[query]
        self.move_to_front(node)
        return node.val

    def move_to_front(self, node):
        if node == self.head:
            return
        self.remove_from_list(node)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = node

    def remove_from_list(self, node):
        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            node.prev = prev
        if node == self.head:
            self.head = next
        if node == self.tail:
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

class Node2:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
    def __str__(self):
        return f"{self.key}|{self.val}"


cache1 = Cache1(5)
cache2 = Cache2(5)
for key in 'abcdaefee':
    cache1.upsert(key, ord(key))
    cache2.upsert(key, ord(key))
    print(cache1)
    print(cache2)