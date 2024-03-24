from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while len(q) > 0:
            new_q = deque()
            if level & 1 == 0:
                last = 0
                while len(q) > 0:
                    n = q.popleft()
                    if n.val <= last:
                        return False
                    if n.val & 1 == 0:
                        return False
                    if n.left is not None:
                        new_q.append(n.left)
                    if n.right is not None:
                        new_q.append(n.right)
                    last = n.val
            elif level & 1 == 1:
                last = 0
                while len(q) > 0:
                    n = q.pop()
                    if n.val <= last:
                        return False
                    if n.val & 1 == 1:
                        return False
                    if n.right is not None:
                        new_q.appendleft(n.right)
                    if n.left is not None:
                        new_q.appendleft(n.left)
                    last = n.val
            level += 1
            q = new_q
        return True

