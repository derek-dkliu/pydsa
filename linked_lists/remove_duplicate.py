# chekc node.next
def remove_dup1(head):
    if head is None:
        return None
    visited = set()
    visited.add(head.val)
    node = head
    while node.next:
        if node.next.val in visited:
            node.next = node.next.next
        else:
            visited.add(node.next.val)
            node = node.next
    return head

# remember prev
def remove_dup2(head):
    visited = set()
    node = head
    prev = None
    while node:
        if node.val in visited:
            prev.next = node.next
        else:
            visited.add(node.val)
            prev = node
        node = node.next
    return head

# time:  O(n^2)
# space: O(1)
# check node.next
def remove_dup3(head):
    p1 = head
    while p1:
        p2 = p1
        while p2.next:
            if p2.next.val == p1.val:
                p2.next = p2.next.next
            else:
                p2 = p2.next
        p1 = p1.next
    return head

# time:  O(n^2)
# space: O(1)
# remember prev
def remove_dup4(head):
    p1 = head
    while p1:
        p2 = p1.next
        prev = p1
        while p2:
            if p2.val == p1.val:
                prev.next = p2.next
            else:
                prev = p2
            p2 = p2.next
        p1 = p1.next
    return head

"""This will modify linked list structure"""
# time:  O(n logn)
# space: O(logn)
def remove_dup5(head):
    head = sort(head)
    node = head
    while node.next:
        if node.next.val == node.val:
            node.next = node.next.next
        else:
            node = node.next
    return head

def sort(head):
    if not head.next:
        return head
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    left = head
    right = slow.next
    slow.next = None

    left = sort(left)
    right = sort(right)
    return merge(left, right)

def merge(left, right):
    head = left if left.val <= right.val else right
    curr = None
    while left and right:
        if left.val <= right.val:
            if curr:
                curr.next = left
            curr = left
            left = left.next
        else:
            if curr:
                curr.next = right
            curr = right
            right = right.next
    if left:
        curr.next = left
    elif right:
        curr.next = right
    return head


from linked_list import Node
head = Node.create([6,3,2,6,2,1])
Node.print(head)
head = remove_dup1(head)
Node.print(head)

head = Node.create([6,3,2,6,2,1])
head = remove_dup2(head)
Node.print(head)

head = Node.create([6,3,2,6,2,1])
head = remove_dup3(head)
Node.print(head)

head = Node.create([6,3,2,6,2,1])
head = remove_dup4(head)
Node.print(head)

head = Node.create([6,3,2,6,2,1])
head = remove_dup5(head)
Node.print(head)