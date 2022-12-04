from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def count_operation(self):

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        
        q = deque()
        q.append(root)
        while len(q) > 0:
            new_q = deque()

            while len(q) > 0:
                node = q.popleft()
                if node.left is not None:
                    new_q.append(node.left)
                if node.right is not None:
                    new_q.append(node.right)
            q = new_q
