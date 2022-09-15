from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.last_num = -1
        self.min_diff = math.inf

    def inorder(self, root: TreeNode):
        if root is None:
            return
        if root.left is not None:
            self.inorder(root.left)
        if self.last_num != -1:
            self.min_diff = min(self.min_diff, abs(root.val - self.last_num))
        self.last_num = root.val
        if root.right is not None:
            self.inorder(root.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        return self.min_diff
