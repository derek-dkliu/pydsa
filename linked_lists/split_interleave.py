def split_interleave1(head):
    # start both pointers from head
    # stop when the fast pointer hits None
    # slow pointer ends up at the first node of second half
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    p1 = head
    p2 = slow
    # handle the last node of second half outside the loop
    while p2.next:      # look one node ahead
        n1 = p1.next
        n2 = p2.next
        p1.next = p2
        p2.next = n1
        p1 = n1
        p2 = n2
    # append last node to the last node of the first half
    p1.next = p2
    return head

def split_interleave2(head):
    # start slow pointer from head
    # start fast pointer from head.next
    # stop when the fast pionter hits None
    # slow pointer ends up at the last node of first half
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    p1 = head
    p2 = slow.next
    # split the list into two halves
    slow.next = None
    while p2:
        n1 = p1.next
        n2 = p2.next
        p1.next = p2
        p2.next = n1
        p1 = n1
        p2 = n2
    return head

from linked_list import Node
head = Node.create(range(10))
Node.print(head)
head = split_interleave1(head)
Node.print(head)

head = Node.create(range(10))
head = split_interleave2(head)
Node.print(head)