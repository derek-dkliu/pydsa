# time:  O(n + m)   where n, m are size of tree1 and tree2 respectively
# space: O(n + m)
def check_subtree1(root1, root2):
    # preorder traversal of tree with null node considered
    seq1 = []
    preorder(root1, seq1)
    seq1 = ''.join(seq1)
    seq2 = []
    preorder(root2, seq2)
    seq2 = ''.join(seq2)
    # root2 is subtree of root1 is seq2 is substring of seq1
    return seq1.find(seq2) != -1

def preorder(root, result):
    if root is None:
        result.append('x')
        return
    result.append(str(root.val))
    preorder(root.left, result)
    preorder(root.right, result)


# time:  O(n + km)
# space: O(log n + log m)
def check_subtree2(root1, root2):
    if root2 is None: return True   # empty tree is always a subtree
    return is_subtree(root1, root2)

def is_subtree(root, node):
    if root is None: return False   # while big tree is empty, return not found
    elif root.val == node.val and match(root, node): return True
    else: return is_subtree(root.left, node) or is_subtree(root.right, node)

def match(n1, n2):
    if n1 is None and n2 is None: return True
    elif n1 is None or n2 is None: return False
    elif n1.val != n2.val: return False
    else: return match(n1.left, n2.left) and match(n1.right, n2.right)


from binary_tree import BinaryTree
seq1 = "1 1 2 x x 1 2 3 x x x 3 x x 1 3 x 1 2 x x x 2 1 2 x x 3 x x 3 x x"
root1 = BinaryTree.desequence(seq1)
BinaryTree.print(root1, format=True)
seq2 = "1 2 x x 3 x x"
root2 = BinaryTree.desequence(seq2)
BinaryTree.print(root2, format=True)
print(check_subtree1(root1, root2), check_subtree2(root1, root2))
