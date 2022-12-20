def successor(root, val):
    node = search(root, val)
    if node is None:
        raise Exception(f"No node with value {val}")
    # return leftmost node of node's right subtree if any
    if node.right:
        return min(node.right)
    else:
        # return node's parent if node is a left child, otherwise
        # go up until the node is a left child
        while node.parent and node.parent.right is node:
            node = node.parent
        return node.parent

def search(node, val, parent = None):
    if node is None: return None
    node.parent = parent
    if val == node.val:
        return node
    elif val < node.val:
        return search(node.left, val, node)
    else:
        return search(node.right, val, node)

def min(node):
    if node.left is None:
        return node
    return min(node.left)

def min1(node):
    while node.left:
        node = node.left
    return node

def search1(node, val):
    while node:
        if val == node.val:
            return node
        elif val < node.val:
            node = node.left
        else:
            node = node.right
    return None


from minimal_tree import minimal_tree
from binary_tree import BinaryTree
root = minimal_tree(range(10))
BinaryTree.print(root, format=True)
print(successor(root, 0))
print(successor(root, 1))
print(successor(root, 2))
print(successor(root, 3))
print(successor(root, 4))
print(successor(root, 5))
print(successor(root, 9))

