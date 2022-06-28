from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        if root.left is None and root.right is None:
            return root.val == targetSum

        r1 = False
        r2 = False
        if root.left is not None:
            r1 = self.hasPathSum(root.left, targetSum - root.val)
        if root.right is not None:
            r2 = self.hasPathSum(root.right, targetSum - root.val)
        return r1 or r2
