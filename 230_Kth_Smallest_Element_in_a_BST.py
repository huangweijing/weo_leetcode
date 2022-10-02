from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.arr = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1
        result = self.kthSmallest(root.left, k)
        if result != -1:
            return result
        self.arr.append(root.val)
        if len(self.arr) == k:
            return root.val
        result = self.kthSmallest(root.right, k)
        if result != -1:
            return result
        return -1
