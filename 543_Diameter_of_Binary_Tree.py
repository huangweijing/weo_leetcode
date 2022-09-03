from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0

    def max_path(self, root: TreeNode) -> int:
        if root is None:
            return None
        left_max, right_max = 0, 0
        if root.left is not None:
            left_max = self.max_path(root.left) + 1
        if root.right is not None:
            right_max = self.max_path(root.right) + 1
        self.diameter = max(self.diameter, left_max + right_max)
        return max(left_max, right_max)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_path(root)
        return self.diameter
