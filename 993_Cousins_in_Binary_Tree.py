from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        parent = dict[int, int]()
        level = dict[int, int]()
        q = [root]
        l = 0
        while len(q) > 0:
            new_q = []
            while len(q) > 0:
                node = q.pop()
                if node.left is not None:
                    parent[node.left.val] = node
                    level[node.left.val] = l
                    new_q.append(node.left)
                if node.right is not None:
                    parent[node.right.val] = node
                    level[node.right.val] = l
                    new_q.append(node.right)
            if x in parent:
                break
            q = new_q
            l += 1
            
        if x not in parent or y not in parent:
            return False
        return level[x] == level[y] and parent[x] != parent[y]

