def detect_loop(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    if slow is not fast:
        return None
    
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow

from linked_list import Node

cases = [
    [2, 2],
    [5, 4],
    [6, 4],
    [7, 3],
    [5, 0]
]
for len, loop_len in cases:
    head = Node.create_loop(len, loop_len)
    Node.print(head)
    print(detect_loop(head))
