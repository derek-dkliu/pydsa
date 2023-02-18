"""
if the each node has link to its parent, this question is essentially
finding the intersection of two singly linked lists. The linked list is
the path from each node up to the root.
"""
def common_ancestor1(root, p, q):
    ancestor, valid = dfs(root, p, q)
    return ancestor if valid else None

def dfs(node, p, q):
    if node is None:
        return (None, False)
    if node is p and node is q:
        return (node, True)

    n1, a1 = dfs(node.left, p, q)
    if a1: return (n1, a1)

    n2, a2 = dfs(node.right, p, q)
    if a2: return (n2, a2)

    # current node is first common ancestor if
    # p found from left subtree and q foudn from right subtree
    if n1 and n2:
        return (node, True)

    # current node is p or q, and the other is found from one subtree
    if node is p or node is q:
        return (node, n1 is not None or n2 is not None)

    return (n1 or n2, False)

"""Top down method"""
def common_ancestor2(root, p, q):
    if root is None:
        return None
    elif root is p and root is q:
        return root
    elif root is p:
        if cover(root.left, q) or cover(root.right, q):
            return root
        else:
            return None
    elif root is q:
        if cover(root.left, p) or cover(root.right, p):
            return root
        else:
            return None
    else:
        pleft = cover(root.left, p)
        qright = cover(root.right, q)
        if pleft and qright: return root
        qleft = cover(root.left, q)
        pright = cover(root.right, p)
        if qleft and pright: return root
        if pleft and qleft: return common_ancestor2(root.left, p, q)
        elif pright and qright: return common_ancestor2(root.right, p, q)
        else: return None

def cover(root, node):
    if root is None: return False
    elif root is node: return True
    else: return cover(root.left, node) or cover(root.right, node)

"""Bottom up method"""
def common_ancestor3(root, p, q):
    ancestor, _ = _common_ancestor3(root, p, q)
    return ancestor

def _common_ancestor3(root, p, q):
    if root is None:
        return None, False
    elif root is p and root is q:
        return root, True

    # return (ancestor, found either p or q)
    n1, b1 = _common_ancestor3(root.left, p, q)
    if n1: return n1, b1

    n2, b2 = _common_ancestor3(root.right, p, q)
    if n2: return n2, b2

    if root is p or root is q:
        if b1 or b2: return root, True
        else: return None, True
    else:
        if b1 and b2: return root, True
        else: return None, b1 or b2


from binary_tree import BinaryTree
if __name__ == '__main__':
    root = BinaryTree.create(10, prob=.9)
    BinaryTree.print(root, format = True)
    p = BinaryTree.search(root, 7)
    q = BinaryTree.search(root, 9)
    print(f"common ancestor of {p} and {q}:", 
            common_ancestor1(root, p, q),
            common_ancestor2(root, p, q),
            common_ancestor3(root, p, q))
