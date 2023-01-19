class StreamBST:
    def __init__(self):
        self.root = None

    def _size(self, node):
        return 0 if node is None else node.size

    def track(self, key):
        self.root = self.insert(self.root, key)
        
    def insert(self, node, key):
        if node is None:
            return Node(key)
        if key <= node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)
        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def rank(self, key):
        return self._rank(self.root, key)

    def _rank(self, node, key):
        if node is None: return -1
        if key == node.key:
            return self._size(node.left)
        elif key < node.key:
            return self._rank(node.left, key)
        else:
            right_rank = self._rank(node.right, key)
            if right_rank == -1:
                return -1
            return 1 + self._size(node.left) + right_rank

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.size = 1

stream = [5, 1, 4, 4, 5, 9, 7, 13, 3]
bst = StreamBST()
for num in stream:
    bst.track(num)
print(bst.rank(1))
print(bst.rank(3))
print(bst.rank(4))
print(bst.rank(6))