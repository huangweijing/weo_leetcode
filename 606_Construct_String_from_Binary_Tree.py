from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        result = str(root.val)
        if root.left is None:
            if root.right is not None:
                result += "()"
        else:
            result += f"({self.tree2str(root.left)})"
        if root.right is not None:
            result += f"({self.tree2str(root.right)})"
        return result
