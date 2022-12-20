import math
from binary_tree import TreeNode, BinaryTree, Traversal

def minimal_tree(arr):
    return create(arr, 0, len(arr) - 1)

def create(arr, low, high):
    if low > high:
        return None
    mid = math.ceil((low + high) / 2)
    node = TreeNode(arr[mid])
    node.left = create(arr, low, mid - 1)
    node.right = create(arr, mid + 1, high)
    return node

if __name__ == '__main__':
    for i, size in enumerate([1,2,3,4,5]):
        print(f"case {i + 1}:")
        arr = list(range(size))
        root = minimal_tree(arr)
        BinaryTree.print(root, order=Traversal.INORDER)
        BinaryTree.print(root, format=True)
