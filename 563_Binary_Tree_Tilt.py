from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sum_tilt = 0
        # = dict[TreeNode, int]()

    def sum_tree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        sum_left = self.sum_tree(root.left)
        sum_right = self.sum_tree(root.right)
        self.sum_tilt += abs(sum_left - sum_right)
        return sum_left + sum_right + root.val

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.sum_tree(root)
        return self.sum_tilt
