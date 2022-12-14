from linked_list import Node

"""digits are stored in reverse order in lists"""
# iterative
def sum_lists1(head1, head2):
    dummy = Node(0)
    tail = dummy
    n1 = head1
    n2 = head2
    carry = 0
    while n1 or n2 or carry:
        d1 = n1.val if n1 else 0
        d2 = n2.val if n2 else 0
        sum = d1 + d2 + carry
        carry = sum >= 10
        node = Node(sum % 10)
        tail.next = node
        tail = node
        n1 = n1.next if n1 else None
        n2 = n2.next if n2 else None
    return dummy.next

# recursive
def sum_lists2(head1, head2):
    if head1 is None: return head2
    if head2 is None: return head1
    sum = head1.val + head2.val
    head = Node(sum % 10)
    carry = Node(sum // 10) if sum // 10 > 0 else None
    node = sum_lists2(head1.next, head2.next)
    node = sum_lists2(carry, node)
    head.next = node
    return head

# recursion with carry as an addtional input
def sum_lists3(head1, head2, carry = 0):
    if head1 is None and head2 is None and carry == 0:
        return None
    node = Node(0)
    sum = carry
    if head1 is not None:
        sum += head1.val
    if head2 is not None:
        sum += head2.val
    node.val = sum % 10
    node.next = sum_lists3(
        head1.next if head1 else None,
        head2.next if head2 else None,
        1 if sum >= 10 else 0
    )
    return node


"""digit are stored in ordinary order in lists"""
# reverse the lists and resuse one of the above methods
def sum_lists_forward1(head1, head2):
    head1 = reverse(head1)
    head2 = reverse(head2)
    return reverse(sum_lists1(head1, head2))

# pad the shorter list with zeros and do recursion
def sum_lists_forward2(head1, head2):
    len1 = _get_length(head1)
    len2 = _get_length(head2)
    if len1 < len2:
        head1 = _pad_list(head1, len2 - len1)
    elif len1 > len2:
        head2 = _pad_list(head2, len1 - len2)
    carry, head = _sum_lists_forward2(head1, head2)
    if carry > 0:
        node = Node(carry)
        node.next = head
        head = node
    return head
    
def _sum_lists_forward2(head1, head2):
    if head1 is None or head2 is None:
        return (0, None)
    carry, head = _sum_lists_forward2(head1.next, head2.next)
    sum = carry + head1.val + head2.val
    carry = 1 if sum >= 10 else 0
    node = Node(sum % 10)
    node.next = head
    head = node
    return (carry, head)
    
def _pad_list(head, length):
    while length:
        node = Node(0)
        node.next = head
        head = node
        length -= 1
    return head

def _get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length


# reverse linked list in place
def reverse(head):
    node = head.next
    head.next = None
    while node:
        next = node.next
        node.next = head
        head = node
        node = next
    return head

cases = [
    [[1, 2, 3], [3, 2, 1]],
    [[2], [9]],
    [[9, 9], [1]],
    [[2,7,3], [1,7,6,8]]
]
for i, [L1, L2] in enumerate(cases):
    print(f"case {i+1}:")
    head1 = Node.create(L1)
    head2 = Node.create(L2)
    Node.print(head1)
    Node.print(head2)
    Node.print(sum_lists1(head1, head2))
    Node.print(sum_lists2(head1, head2))
    Node.print(sum_lists3(head1, head2))
    Node.print(sum_lists_forward1(head1, head2))
    head1 = Node.create(L1)
    head2 = Node.create(L2)
    Node.print(sum_lists_forward2(head1, head2))
