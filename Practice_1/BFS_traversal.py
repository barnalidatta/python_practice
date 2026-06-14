# Binary Tree Level Order Traversal
# Data Structure : Dqueue - Double ended queue
# adding and removing elements from both ends with O(1) constant time complexity
# Traverse : BFS
# Space complexity : O(n)
# deque holding list of node object
# 1. Put the head or root into a queue
# 2. Take a node out
# 3. Process it
# 4. Put its neighbors/children into the queue
# 5. Repeat
# pyright: reportAttributeAccessIssue=false

from collections import deque
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
def bfs(root):
    if not root:
        return
    
    results = []
    q = deque([root])

    while q:
        level_size = len(q)
        level = []
        for _ in range(level_size):
            node = q.popleft() 
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        results.append(level)
    return results

#root = [3,9,20,None,None,15,7]
# Build tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(bfs(root))
