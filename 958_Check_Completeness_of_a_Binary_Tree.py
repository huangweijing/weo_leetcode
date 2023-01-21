from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # is_complete, is_perfect, height
    def my_sol(self, root: Optional[TreeNode]) -> (bool, bool, int):
        left_is_complete, left_is_perfect, left_height = True, True, 0
        right_is_complete, right_is_perfect, right_height = True, True, 0
        if root.left is not None:
            left_is_complete, left_is_perfect, left_height = self.my_sol(root.left)
        if root.right is not None:
            right_is_complete, right_is_perfect, right_height = self.my_sol(root.right)

        height = max(left_height, right_height) + 1
        if left_is_perfect and right_is_perfect and left_height == right_height:
            return True, True, height
        if left_is_perfect and right_is_perfect and left_height == right_height + 1:
            return True, False, height
        if left_is_perfect and right_is_complete and left_height == right_height:
            return True, False, height
        if left_is_complete and right_is_perfect and left_height == right_height + 1:
            return True, False, height
        return False, False, height

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        ans, _, __ = self.my_sol(root)
        return ans