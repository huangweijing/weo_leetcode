from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.left is not None:
            root.left = self.pruneTree(root.left)

        if root.right is not None:
            root.right = self.pruneTree(root.right)

        if root.left is None and root.right is None and root.val == 0:
            return None
        else:
            return root
