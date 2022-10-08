from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def my_remove(self, root: TreeNode, parent:):
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root is None:
            return None
        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)
        if root.val == target:
            if left is None and right is None:
                return None
        root.left = left
        root.right = right
        return root

