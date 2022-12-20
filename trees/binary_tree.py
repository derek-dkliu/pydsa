from collections import deque
import random
from enum import Enum

class Traversal(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

class BinaryTree:
    @staticmethod
    def create(seq, **kwarg):
        if isinstance(seq, int):
            seq = range(seq)
        prob = kwarg.get('prob', 1)
        seq = deque(seq)
        root = TreeNode(seq.popleft())
        queue = deque()
        queue.append(root)
        while seq:
            node = queue[0]
            if random.random() < prob:
                node.left = TreeNode(seq.popleft())
                queue.append(node.left)
            if seq and random.random() < prob:
                node.right = TreeNode(seq.popleft())
                queue.append(node.right)
            if node.left or node.right:
                queue.popleft()
        return root

    def _createnode(seq, prob):
        if not seq: return None
        node = TreeNode(seq.popleft())
        hit = False
        while not hit:
            if random.random() < prob:
                node.left = BinaryTree._createnode(seq, prob)
                hit = True
            if random.random() < prob:
                node.right = BinaryTree._createnode(seq, prob)
                hit = True
        return node

    @staticmethod
    def search(node, val):
        if node is None: return None
        if node.val == val: return node
        return BinaryTree.search(node.left, val) or BinaryTree.search(node.right, val)


    @staticmethod
    def sequence(node, **kwarg):
        sep = kwarg.get('seq', ' ')
        end = kwarg.get('end', 'x')
        result = []
        BinaryTree._sequence(node, result, end)
        return sep.join(map(str, result))

    @staticmethod
    def _sequence(node, result, end = 'x'):
        if node is None:
            result.append(end)
            return
        result.append(node.val)
        BinaryTree._sequence(node.left, result, end)
        BinaryTree._sequence(node.right, result, end)

    @staticmethod
    def desequence(seq, **kwarg):
        sep = kwarg.get('seq', ' ')
        end = kwarg.get('end', 'x')
        if isinstance(seq, str):
            seq = deque(seq.split(sep))
        else:
            seq = deque(seq)
        return BinaryTree._desequence(seq, end)

    def _desequence(seq, end = 'x'):
        if not seq: return None
        c = seq.popleft()
        if c == end: return None
        node = TreeNode(c)
        node.left = BinaryTree._desequence(seq)
        node.right = BinaryTree._desequence(seq)
        return node

    @staticmethod
    def preorder(node, result, level = 0, left = None):
        if node is None: return
        result.append((node, level, left))
        BinaryTree.preorder(node.left, result, level + 1, True)
        BinaryTree.preorder(node.right, result, level + 1, False)

    @staticmethod
    def inorder(node, result, level = 0, left = None):
        if node is None: return
        BinaryTree.inorder(node.left, result, level + 1, True)
        result.append((node, level, left))
        BinaryTree.inorder(node.right, result, level + 1, True)

    @staticmethod
    def postorder(node, result, level = 0, left = None):
        if node is None: return
        BinaryTree.postorder(node.left, result, level + 1, True)
        BinaryTree.postorder(node.right, result, level + 1, False)
        result.append((node, level, left))

    @staticmethod
    def print(node, **kwarg):
        format = kwarg.get('format', None)
        order = kwarg.get('order', Traversal.PREORDER)
        result = []
        if order is Traversal.INORDER:
            BinaryTree.inorder(node, result)
        elif order is Traversal.POSTORDER:
            BinaryTree.postorder(node, result)
        else:
            BinaryTree.preorder(node, result)
        if format:
            print("\n".join(BinaryTree.format(*item) for item in result))
        else:
            print(" ".join(str(item[0]) for item in result))

    @staticmethod
    def format(node, level, left):
        prefix = '   ' * (level - 1) + '|--' if level > 0 else ''
        suffix = ('L' if left else 'R') if level > 0 else ''
        return prefix + str(node) + suffix

class TreeNode:
    def __init__(self, val = None):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.val)

# iterative preorder
def preorder(root):
    result = []
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    print(" ".join(map(str, result)))

# iterative postorder
def postorder(root):
    result = deque()
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.appendleft(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    print(" ".join(map(str, result)))

# iterative inorder
def inorder(root):
    result = []
    stack = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr)
        curr = curr.right
    print(" ".join(map(str, result)))


"""
Inorder traversal visits the left subtree, current node, then right subtree. 
In order to be able to go back to current node after traversing left subtree,
Before actually move ot the left child, we first need to find the rightmost node of left subtree
and make it to link back to current node. At the time when we are back to the current node,
we will have to find this rightmost node again and remove the link.
"""
# iterative inorder with O(1) space
def inorder_constant(root):
    result = deque()
    curr = root
    while curr:
        if curr.left:
            # find the rightmost node of current node's left subtree
            pre = curr.left
            while pre.right and pre.right is not curr:
                pre = pre.right
            # set right pointer of rightmost node to current node, or
            if pre.right is None:
                pre.right = curr
                curr = curr.left
            # unset right pointer if we are back to current node
            # print current node, and visit right subtree of current node
            # since we are done with left subtree
            else:
                pre.right = None
                result.append(curr)
                curr = curr.right
        # print current node, and visit right subtree when there's no left subtree
        else:
            result.append(curr)
            curr = curr.right
    print(" ".join(map(str, result)))
        
        
if __name__ == '__main__':
    root = BinaryTree.create(10)
    preorder(root)
    BinaryTree.print(root)
    # BinaryTree.print(root, format=True)
    inorder(root)
    inorder_constant(root)
    BinaryTree.print(root, order=Traversal.INORDER)
    # BinaryTree.print(root, order=Traversal.INORDER, format=True)
    postorder(root)
    BinaryTree.print(root, order=Traversal.POSTORDER)
    # BinaryTree.print(root, order=Traversal.POSTORDER, format=True)
