import random

class BinaryTreeBST:
    def __init__(self):
        self.root = None

    def size(self):
        return self._size(self.root)

    def _size(self, node):
        return 0 if node is None else node.size

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None: return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None: return TreeNode(key)
        if key <= node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None: return None
        if key == node.key:
            if node.left is None: return node.right
            if node.right is None: return node.left
            x = self.min(node.right)
            x.right = self._delete_min(node.right)
            x.left = node.left
            node = x
        elif key < node.key:
            self.left = self._delete(self.left, key)
        else:
            self.right = self._delete(self.right, key)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def delete_min(self):
        if self.root is None: return
        self.root = self._delete_min(self.root)

    def _delete_min(self, node):
        if node.left is None: return node.right
        node.left = self._delete_min(self.left)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def min(self):
        node = self.root
        if node is None: return None
        while node.left:
            node = node.left
        return node

    # time: O(log n)
    def random(self):
        rank = random.randint(0, self.size() - 1)
        return self.select(rank), rank

    def select(self, rank):
        return self._select(self.root, rank)

    def _select(self, node, rank):
        if node is None: return None

        leftsize = self._size(node.left)
        if rank == leftsize:
            return node
        elif rank < leftsize:
            return self._select(node.left, rank)
        else:
            return self._select(node.right, rank - leftsize - 1)
    
    # time: O(n)
    def random2(self):
        n = random.randint(0, self.size() - 1)
        counter = [n, None]
        self._inorder(self.root, counter)
        return counter[1], n

    def _inorder(self, node, counter):
        if node is None: return
        self._inorder(node.left, counter)
        counter[0] -= 1
        if counter[0] < 0:
            if not counter[1]:
                counter[1] = node
            return 
        self._inorder(node.right, counter)


class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

    def __str__(self):
        return str(self.key)

from binary_tree import BinaryTree
tree = BinaryTreeBST()
for key in [5, 7, 4, 2, 6, 8, 1, 10, 3, 9, 4, 5, 6, 9]:
    tree.insert(key)
BinaryTree.print(tree.root, format=True)

print(*tree.random())
print(*tree.random2())