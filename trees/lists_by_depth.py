import sys, os
sys.path.insert(0, os.getcwd())
from linked_lists.linked_list import Node, LinkedList
from collections import deque

def lists_by_depth1(root):
    lists = []
    linkedlist = LinkedList()
    linkedlist.add(root)
    while linkedlist:
        lists.append(linkedlist)
        parents = linkedlist
        linkedlist = LinkedList()
        for parent in parents:
            if parent.left:
                linkedlist.add(parent.left)
            if parent.right:
                linkedlist.add(parent.right)
    return lists

def lists_by_depth2(root):
    lists = []
    queue = deque()
    queue.append((root, 0))
    while queue:
        node, level = queue.popleft()
        listnode = Node(node)
        if level == len(lists):
            lists.append(listnode)
        else:
            listnode.next = lists[-1]
            lists[-1] = listnode
        if node.left:
            queue.append((node.left, level + 1))
        if node.right:
            queue.append((node.right, level + 1))
    return lists

def lists_by_depth3(root):
    lists = []
    dfs(root, 0, lists)
    return lists

def dfs(node, level, lists):
    listnode = Node(node)
    if level == len(lists):
        lists.append(listnode)
    else:
        listnode.next = lists[level]
        lists[level] = listnode
    if node.left:
        dfs(node.left, level + 1, lists)
    if node.right:
        dfs(node.right, level + 1, lists)

from binary_tree import BinaryTree
root = BinaryTree.create(10, prob=.9)
BinaryTree.print(root, format=True)
l1 = lists_by_depth1(root)
for list in l1:
    print(list)
l2 = lists_by_depth2(root)
for head in l2:
    Node.print(head)
l3 = lists_by_depth3(root)
for head in l3:
    Node.print(head)