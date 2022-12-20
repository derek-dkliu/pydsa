"""
if the each node has link to its parent, this question is essentially
finding the intersection of two singly linked lists. The linked list is
the path from each node up to the root.
"""
def common_ancestor(root, p, q):
    node, ancestor = dfs(root, p, q)
    return node if ancestor else None

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

from binary_tree import BinaryTree
if __name__ == '__main__':
    root = BinaryTree.create(10, prob=.9)
    BinaryTree.print(root, format = True)
    p = BinaryTree.search(root, 7)
    q = BinaryTree.search(root, 9)
    print(f"common ancestor of {p} and {q}:", common_ancestor(root, p, q))
