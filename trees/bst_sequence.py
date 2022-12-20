from collections import deque

def bst_sequence(root):
    if root is None: return [deque()]

    lseq = bst_sequence(root.left)
    rseq = bst_sequence(root.right)

    result = []
    prefix = deque()
    prefix.append(root.val)
    if lseq and rseq:
        for left in lseq:
            for right in rseq:
                combine_seqs(left, right, prefix, result)
    return result

def combine_seqs(left, right, prefix, result):
    if not left:
        result.append(prefix + right)
        return
    if not right:
        result.append(prefix + left)
        return
    
    # backtracking
    prefix.append(left.popleft())
    combine_seqs(left, right, prefix, result)
    left.appendleft(prefix.pop())

    prefix.append(right.popleft())
    combine_seqs(left, right, prefix, result)
    right.appendleft(prefix.pop())


from minimal_tree import minimal_tree
from binary_tree import BinaryTree
root = minimal_tree(range(4))
BinaryTree.print(root, format=True)
print(bst_sequence(root))
