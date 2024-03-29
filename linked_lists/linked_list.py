class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

    # append to node whose next is None
    def append(self, item):
        if item is None: return
        node = self
        while node.next:
            node = node.next
        node.next = item if isinstance(item, Node) else Node(item)

    def __str__(self):
        return str(self.val)

    @staticmethod
    def create(vals):
        dummy = Node(0)
        node = dummy
        for val in vals:
            node.next = Node(val)
            node = node.next
        return dummy.next

    @staticmethod
    def create_intersection(len1, len2, common_len):
        head1 = Node.create(range(len1))
        head2 = Node.create(range(len2))
        common = Node.create(["*" + str(i) for i in range(common_len)])
        if head1 is None:
            head1 = common
        else:
            head1.append(common)
        if head2 is None:
            head2 = common
        else:
            head2.append(common)
        return (head1, head2)

    @staticmethod
    def create_loop(len, loop_len):
        if loop_len > len:
            raise Exception("loop length is large than the total length")
        head = Node.create(range(len))
        node = head
        step = len - loop_len
        while step:
            node = node.next
            step -= 1
        head.append(node)
        return head

    # check node.next
    @staticmethod
    def delete1(head, val):
        if head is None:
            return None
        if head.val == val:
            return head.next
        node = head
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
                return head
            node = node.next
        return head

    # remember prev
    @staticmethod
    def delete2(head, val):
        if head is None:
            return None
        if head.val == val:
            return head.next
        prev = head
        node = head.next
        while node:
            if node.val == val:
                prev.next = node.next
                return head
            prev = node
            node = node.next
        return head

    # recursive
    @staticmethod
    def delete3(node, val):
        if node is None:
            return None
        if node.val == val:
            return node.next
        node.next = Node.delete3(node.next, val)
        return node

    @staticmethod
    def print(node):
        visited = set()
        result = []
        while node:
            result.append(node.val)
            if node in visited:
                break
            visited.add(node)
            node = node.next
        print(' -> '.join(map(str, result)))

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def add(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
        self.n += 1

    def remove(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        self.n -= 1
        return node

    @staticmethod
    def create(items):
        head = None
        tail = None
        for item in items:
            if head is None:
                head = item
                tail = head
            else:
                tail.next = item
                tail = item
        return

    @staticmethod
    def reversed(head):
        new_head = None
        while head:
            node = Node(head.val)
            node.next = new_head
            new_head = node
            head = head.next
        return new_head

    @staticmethod
    def reverse(head):
        new_head = None
        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next
        return new_head

    @staticmethod
    def reverse2(head):
        node = head
        while node.next:
            next = node.next
            node.next = next.next
            next.next = head
            head = next
        return head

    def __len__(self):
        return self.n

    def __iter__(self):
        self._tail = self.head
        return self
    
    def __next__(self):
        if self._tail:
            item = self._tail.val
            self._tail = self._tail.next
            return item
        else:
            raise StopIteration

    def __str__(self):
        chain = []
        node = self.head
        while node:
            chain.append(node.val)
            node = node.next
        return ' -> '.join(map(str, chain))

if __name__ == '__main__':
    linked_list = LinkedList()
    for i in range(10):
        linked_list.add(i)
    print(*linked_list)
    print(linked_list)

    # create nodes with range vals
    head = Node.create(range(10))
    Node.print(head)

    # delete node by vals
    for val in [4, 0, 9]:
        print(f"delete {val}")
        head = Node.delete1(head, val)
        Node.print(head)

    print("Reverse a linked list")
    head = Node.create(list(range(10)))
    Node.print(head)
    Node.print(LinkedList.reversed(head))
    head = LinkedList.reverse(head)
    Node.print(head)
