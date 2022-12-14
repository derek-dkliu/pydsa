"""
1. find the middle node and break the list into two halves
   in way that second half is no longer than the first half
2. reverse the second half and compare if every node in two halves
   is equal to another up to the end of second half
"""
# time:  O(N)
# space: O(1)
def check_palindrome1(head):
    if head is None:
        return False
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # break the list
    p1 = head
    p2 = slow.next
    slow.next = None
    p2 = reverse(p2)
    while p2:
        if p2.val != p1.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True

def reverse(head):
    if head is None: return None
    node = head.next
    head.next = None
    while node:
        next = node.next
        node.next = head
        head = node
        node = next
    return head


# time:  O(N)
# space: O(N)
def check_palindrome2(head):
    if head is None: return False
    p1 = head
    p2 = reverse_new(head)
    while p1:
        if p1.val != p2.val:
            return False
        p1 = p1.next
        p2 = p2.next
    return True

def reverse_new(head):
    if head is None: return None
    new_head = None
    node = head
    while node:
        new_node = Node(node.val)
        new_node.next = new_head
        new_head = new_node
        node = node.next
    return new_head

from collections import deque

# time:  O(N)
# space: O(N)
def check_palindrome3(head):
    if head is None: return False
    stack = deque()
    node = head
    while node:
        stack.append(node.val)
        node = node.next
    while stack:
        if head.val != stack.pop():
            return False
        head = head.next
    return True

# time:  O(N)
# space: O(N)
def check_palindrome4(head):
    if head is None: return False
    stack = deque()
    slow = head
    fast = head.next
    stack.append(slow.val)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # in case of odd lenght, don't add the middle node's value
        if fast:
            stack.append(slow.val)
    node = slow.next
    while node:
        if node.val != stack.pop():
            return False
        node = node.next
    return True

# time:  O(N)
# space: O(N)
def check_palindrome5(head):
    if head is None: return False
    stack = deque()
    # start both pointers from head and stop when fast hits end
    # can push less than half nodes onto stack
    # check fast pointer is not null then the second half start from slow.next
    slow = head
    fast = head
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if slow.val != stack.pop():
            return False
        slow = slow.next
    return True

# recursion
# time:  O(N)
# space: O(N)
def check_palindrome6(head):
    if head is None: return False
    length = _get_length(head)
    ans, _ = _check_palindrome6(head, length)
    return ans

def _check_palindrome6(node, length):
    if length <= 1:
        return (True, node.next if length == 1 else node)
    ans, next = _check_palindrome6(node.next, length - 2)
    if ans:
        ans = node.val == next.val
    return (ans, next.next)

def _get_length(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length

from linked_list import Node
cases = [
    [1],
    [2,2],
    [1,2,1],
    [1,2,2,1],
    [1,2,2,2],
    [1,2,3],
    [2,1]
]
for case in cases:
    head = Node.create(case)
    Node.print(head)
    print(check_palindrome1(head))
    head = Node.create(case)
    print(check_palindrome2(head))
    head = Node.create(case)
    print(check_palindrome3(head))
    head = Node.create(case)
    print(check_palindrome4(head))
    head = Node.create(case)
    print(check_palindrome5(head))
    head = Node.create(case)
    print(check_palindrome6(head))