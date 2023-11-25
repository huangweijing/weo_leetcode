from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.low, self.high = 0, 0

    def my_trim(self, node: TreeNode) -> Optional[TreeNode]:
        if node is None:
            return None
        if node.val < self.low:
            return self.my_trim(node.right)
        if node.val > self.high:
            return self.my_trim(node.left)
        node.left = self.my_trim(node.left)
        node.right = self.my_trim(node.right)
        return node

    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.low, self.high = low, high
        return self.my_trim(root)

