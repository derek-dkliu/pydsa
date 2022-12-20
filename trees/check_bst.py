# time:  O(N)
# space: O(log N) on a balanced tree
def check_bst(root):
    return is_bst(root, None, None)

def is_bst(root, min, max):
    if root is None: return True
    if min is not None and root.val <= min: # root.val < min if duplicate is on right side
        return False    
    if max is not None and root.val >= max: # root.val > max if duplicate is on left side
        return False
    return is_bst(root.left, min, root.val) and is_bst(root.right, root.val, max)

from minimal_tree import minimal_tree
from binary_tree import BinaryTree
root = minimal_tree(range(10))
BinaryTree.print(root, format=True)
print(check_bst(root))

arr = list([0,1,2,3,4,9,5,6,7,8,10,11])
root = minimal_tree(arr)
BinaryTree.print(root, format=True)
print(check_bst(root))