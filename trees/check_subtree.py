# time:  O(n + m)   where n, m are size of tree1 and tree2 respectively
# space: O(n + m)
def check_subtree1(root1, root2):
    # preorder traversal of tree with null node considered
    seq1 = BinaryTree.sequence(root1)
    seq2 = BinaryTree.sequence(root2)
    # root2 is subtree of root1 is seq2 is substring of seq1
    return seq1.find(seq2) != -1


# time:  O(n + km)
# space: O(log n + log m)
def check_subtree2(root1, root2):
    if root2 is None: return True
    return is_subtree(root1, root2)

def is_subtree(root, node):
    if root is None: return None
    if root.val == node.val and match(root, node):
        return True
    return is_subtree(root.left, node) or is_subtree(root.right, node)

def match(n1, n2):
    if n1 is None and n2 is None: return True
    if n1 is None or n2 is None: return False
    if n1.val != n2.val: return False
    return match(n1.left, n2.left) and match(n1.right, n2.right)


from binary_tree import BinaryTree
seq1 = "1 1 2 x x 1 2 3 x x x 3 x x 1 3 x 1 2 x x x 2 1 2 x x 3 x x 3 x x"
root1 = BinaryTree.desequence(seq1)
BinaryTree.print(root1, format=True)
seq2 = "1 2 x x 3 x x"
root2 = BinaryTree.desequence(seq2)
BinaryTree.print(root2, format=True)
print(check_subtree1(root1, root2), check_subtree2(root1, root2))
