from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if depth == 1:
            return TreeNode(val=val, left=root)
        elif depth == 2:
            if root.left is not None:
                root.left = TreeNode(val=val, left=root.left)
            else:
                root.left = TreeNode(val=val)
            if root.right is not None:
                root.right = TreeNode(val=val, right=root.right)
            else:
                root.right = TreeNode(val=val)
        else:
            self.addOneRow(root.left, val, depth=depth - 1)
            self.addOneRow(root.right, val, depth=depth - 1)
        return root