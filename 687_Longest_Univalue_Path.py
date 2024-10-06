from typing import Optional
from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def root_len(self, root: TreeNode, val: int) -> int:
        if root is None:
            return 0
        if root.val != val:
            return 0
        left_len, right_len = 0, 0
        if root.left is not None:
            left_len = self.root_len(root.left, val)
        if root.right is not None:
            right_len = self.root_len(root.right, val)
        return max(left_len, right_len) + 1

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_lp, right_lp = 0, 0
        val = root.val
        root_path = self.root_len(root.left, val) + self.root_len(root.right, val)
        if root.left is not None:
            left_lp = self.longestUnivaluePath(root.left)
        if root.right is not None:
            right_lp = self.longestUnivaluePath(root.right)
        return max(left_lp, right_lp, root_path)
