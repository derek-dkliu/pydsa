"""
Find the pivot node whose val >= val
Prepend all smaller nodes to pivot node
"""
def partition1(head, val):
    # find the pivot node
    node = head
    while node:
        if node.val >= val:
            break
        node = node.next
    if node is None:
        return head
    n = node
    while n.next:
        next = n.next
        if next.val < val:
            # break link to 'next' node, and prepend to head
            n.next = next.next
            next.next = head
            head = next
        else:
            n = next
    return head

"""
Use a dummy node to append either smaller nodes or bigger nodes
Leave bigger node or smaller nodes on the original list
Merge these two lists
(relative order is kept)
"""
def partition2(head, val):
    if head is None: return None
    dummy = Node(0)
    tail = dummy
    node = head
    while node.next:
        next = node.next
        if (head.val < val and next.val < val) or (head.val >= val and next.val >= val):
            node = next
        else:
            node.next = next.next
            tail.next = next
            tail = next
            tail.next = None
    if head.val < val:
        node.next = dummy.next
        return head
    else:
        tail.next = head
        return dummy.next

"""
One new list to store before elements
Another new list to store after elements
Merge these two new lists
(relative order is kept)
"""
def partition3(head, val):
    head1 = None
    head2 = None
    tail1 = None
    tail2 = None
    node = head
    while node:
        # remember next before cutting off the node
        next = node.next
        node.next = None
        if node.val < val:
            if head1 is None:
                head1 = node
                tail1 = head1
            else:
                tail1.next = node
                tail1 = node
        else:
            if head2 is None:
                head2 = node
                tail2 = head2
            else:
                tail2.next = node
                tail2 = node
        node = next
    if head1 is None:
        return head2
    else:
        tail1.next = head2
        return head1

"""
Prepend all smaller nodes to head node
Apppend all bigger nodes to tail node
Nullify the tail next
"""
def partition4(node, val):
    head = node
    tail = node
    while node:
        # remember next before cutting off the node
        next = node.next
        node.next = None
        if node.val < val:
            # prepend to head
            node.next = head
            head = node
        else:
            # append to next
            tail.next = node
            tail = node
        node = next
    # nullify tail next to break the self loop in case of
    # no bigger nodes or the first node is the only bigger node
    tail.next = None
    return head

"""Use flag to indicate if any node smaller than target needs to be prepend to head"""
def partition5(head, t):
    node = head
    swapped = node.val >= t
    while node.next:
        if node.next.val >= t:
            swapped = True
            node = node.next
        elif swapped:
            n = node.next
            node.next = node.next.next
            n.next = head
            head = n
        else:
            node = node.next
    return head

from linked_list import Node
head = Node.create([3, 5, 8, 5, 10, 2, 1])
Node.print(head)
Node.print(partition1(head, 5))

head = Node.create([3, 5, 8, 5, 10, 2, 1])
Node.print(partition2(head, 5))

head = Node.create([3, 5, 8, 5, 10, 2, 1])
Node.print(partition3(head, 5))

head = Node.create([3, 5, 8, 5, 10, 2, 1])
Node.print(partition4(head, 5))

head = Node.create([1, 2, 3, 4, 5])
Node.print(partition4(head, 5))

head = Node.create([3, 5, 8, 5, 10, 2, 1])
Node.print(partition5(head, 5))

head = Node.create([1, 2, 3, 4, 5])
Node.print(partition5(head, 5))

head = Node.create([5, 4, 3, 2, 1])
Node.print(partition5(head, 5))