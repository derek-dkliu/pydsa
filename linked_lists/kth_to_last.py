# time:  O(n)
# space: O(1)
# find length - k
def kth_to_last(head, k):
    # determine length
    length = 0
    node = head
    while node:
        node = node.next
        length += 1

    # find length - k
    t = length - k
    if t < 0:
        return None 
        # raise Exception("invalid k")
    index = 0
    node = head
    while node:
        if index == t:
            return node
        index += 1
        node = node.next
    return None

# time:  O(n)
# space: O(n)
# recursive
def kth_to_last2(head, k):
    node, _ = _kth_to_last2(head, k)
    return node

def _kth_to_last2(node, k):
    if node is None:
        return (None, 0)
    n, i = _kth_to_last2(node.next, k)
    if i + 1 == k:
        n = node
    return (n, i + 1)

# time:  O(n)
# space: O(1)
# iterative
def kth_to_last3(head, k):
    p1 = head
    p2 = head
    # move p2 k nodes forward
    i = 0
    while i < k:
        if p2 is None:
            return None
            # raise Exception("invalid k")
        p2 = p2.next
        i += 1
    # move p1 and p2 at the same pace,
    # when p2 hits the end, p1 will be at the right place
    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1

from linked_list import Node
for n in [0, 1, 2, 3, 4]:
    head = Node.create(range(n))
    Node.print(head)
    for k in range(1, n + 1):
        if k == 4: k = 5
        print(f"{k}th to last:", kth_to_last(head, k), kth_to_last2(head, k), kth_to_last3(head, k))