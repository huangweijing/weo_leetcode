from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        result = 0
        if root.left is not None and root.left.left is None and root.left.right is None:
            result += root.left.val
        else:
            result += self.sumOfLeftLeaves(root.left)
        result += self.sumOfLeftLeaves(root.right)
        return result


