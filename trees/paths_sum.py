# time:  O(n logn)
# space: O(log n) in a balanced tree
def paths_sum(root, sum):
    return dfs(root, sum, True)

def dfs(node, sum, empty):
    if node is None: return 0
    sum -= node.val
    count = 0
    if sum == 0: count += 1
    count += dfs(node.left, sum, False)
    count += dfs(node.right, sum, False)
    if empty:
        sum += node.val
        count += dfs(node.left, sum, True)
        count += dfs(node.right, sum, True)
    return count

# time:  O(n logn)
# space: O(log n) in a balanced tree
def paths_sum1(root, sum):
    if root is None: return 0
    count = dfs1(root, sum)
    count += paths_sum1(root.left, sum)
    count += paths_sum1(root.right, sum)
    return count

def dfs1(node, sum):
    if node is None: return 0
    sum -= node.val
    count = 0
    if sum == 0: count += 1
    count += dfs1(node.left, sum)
    count += dfs1(node.right, sum)
    return count

# time:  O(n)
# space: O(log n) in a balanced tree
from collections import Counter
def paths_sum2(root, sum):
    return dfs2(root, sum, 0, Counter())

def dfs2(node, sum, curr, counter):
    if node is None: return 0
    curr += node.val
    # get number of paths ending at current node but not started at root
    count = counter[curr - sum]
    # include the path ending at current node and started at root
    if curr == sum: count += 1
    # increase the count with current cumulative sum
    counter[curr] += 1
    count += dfs2(node.left, sum, curr, counter)
    count += dfs2(node.right, sum, curr, counter)
    # reverse the count with current cumulative sum so other nodes don't use it
    # since the current node should not be considered part of other nodes' paths 
    # when nodes are visited in DFS manner.
    counter[curr] -= 1
    return count

from binary_tree import BinaryTree

# seq = 
# seq = 
# seq = 

cases = [
    [[1,2,4,2,1,-1], 4],
    [[1,2,3,4,3,3,1,-1,1,1,0], 5],
    [[1,2,1,-2,3,-1], 0]
]
for i, (seq, sum) in enumerate(cases):
    print(f"case {i+1}:")
    root = BinaryTree.create(seq)
    # BinaryTree.print(root, format=True)
    print(paths_sum(root, sum))
    print(paths_sum1(root, sum))
    print(paths_sum2(root, sum))