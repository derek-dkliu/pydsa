"""
time:  O(A+B)
space: O(1)
"""
def intersect(head1, head2):
    len1, tail1 = _get_length_tail(head1)
    len2, tail2 = _get_length_tail(head2)
    if tail1 is not tail2:
        return None

    step = abs(len1 - len2)
    if len1 > len2:
        head1 = _move_forward(head1, step)
    elif len1 < len2:
        head2 = _move_forward(head2, step)

    while head1 is not head2:
        head1 = head1.next
        head2 = head2.next
    return head1

def _get_length_tail(node):
    if node is None: return (0, None)
    length = 1
    while node.next:
        length += 1
        node = node.next
    return (length, node)

def _move_forward(head, step):
    while step:
        head = head.next
        step -= 1
    return head

from linked_list import Node

cases = [
    [3, 3, 1],
    [3, 4, 2],
    [0, 0, 2],
    [2, 0, 2],
    [3, 3, 0]
]
for len1, len2, common in cases:
    head1, head2 = Node.create_intersection(len1, len2, common)
    Node.print(head1)
    Node.print(head2)
    print(intersect(head1, head2))
