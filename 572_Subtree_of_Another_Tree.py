from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def is_equal(self, r1: TreeNode, r2: TreeNode):
        if r1 is None and r2 is None:
            return True
        if r1 is not None and r2 is not None \
            and r1.val == r2.val and self.is_equal(r1.left, r2.left) and self.is_equal(r1.right, r2.right):
             return True
        else:
            return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is None:
            return True
        if (root is None and subRoot is not None) or (root is not None and subRoot is None):
            return False

        if root.val == subRoot.val:
            left_result = self.is_equal(root.left, subRoot.left)
            right_result = self.is_equal(root.right, subRoot.right)
            if left_result and right_result:
                return True

        left_result = self.isSubtree(root.left, subRoot)
        right_result = self.isSubtree(root.right, subRoot)
        return left_result or right_result




