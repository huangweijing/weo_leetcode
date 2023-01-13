import math
from typing import Optional
from functools import cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = -math.inf

    @cache
    def max_path(self, root: Optional[TreeNode]) -> int:
        ans = root.val
        if root.left is not None:
            val = self.max_path(root.left)
            ans = max(ans, val + root.val)
        if root.right is not None:
            val = self.max_path(root.right)
            ans = max(ans, val + root.val)
        return ans

    def my_path_sum(self, root: Optional[TreeNode]):
        path = root.val
        if root.left is not None:
            val = self.max_path(root.left)
            path = max(path, val + path)
            self.my_path_sum(root.left)
        if root.right is not None:
            val = self.max_path(root.right)
            self.my_path_sum(root.right)
            path = max(path, val + path)
        self.ans = max(self.ans, path)
        print(root.val, path)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.my_path_sum(root)
        return int(self.ans)


