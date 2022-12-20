# time:  O(N)   where N is the number of nodes of the tree
# space: O(H)   where H is the height of the tree
def check_balanced(root):
    return is_balanced(root)[0]

def is_balanced(root):
    if root is None:
        return (True, -1)
    lb, lh = is_balanced(root.left)
    rb, rh = is_balanced(root.right)
    balanced = lb and rb and abs(lh - rh) <= 1
    return (balanced, 1 + max(lh, rh))

from binary_tree import BinaryTree
import random
for i, seed in enumerate([1, 5]):
    print(f"case {i+1}:")
    random.seed(seed)
    root = BinaryTree.create(10, prob=.9)
    BinaryTree.print(root, format=True)
    print(check_balanced(root))