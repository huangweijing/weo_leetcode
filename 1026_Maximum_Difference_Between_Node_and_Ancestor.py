# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sol = 0

    def my_diff(self, root: Optional[TreeNode], max_val, min_val):
        self.sol = max(abs(max_val - root.val), abs(root.val - min_val), self.sol)
        if root.left is not None:
            self.my_diff(root.left, max(max_val, root.val), min(min_val, root.val))
        if root.right is not None:
            self.my_diff(root.right, max(max_val, root.val), min(min_val, root.val))

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.my_diff(root, root.val, root.val)
        return self.sol



