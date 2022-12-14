def delete_middle(middle):
    if middle is None or middle.next is None:
        return False
    middle.val = middle.next.val
    middle.next = middle.next.next
    return True

def find_middle_floor(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def find_middle_ceil(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

from linked_list import Node
for i, n in enumerate([3, 4, 5]):
    print(f"case {i+1}:", end=" ")
    head = Node.create(range(n))
    Node.print(head)
    middle = find_middle_floor(head)
    print(f"middle: {middle}")
    delete_middle(middle)
    Node.print(head)

print('--- middle ceiling ---')
for i, n in enumerate([3, 4, 5]):
    print(f"case {i+1}:", end=" ")
    head = Node.create(range(n))
    Node.print(head)
    middle = find_middle_ceil(head)
    print(f"middle: {middle}")
    delete_middle(middle)
    Node.print(head)