from typing import Optional
from functools import cache


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @cache
    def my_sol(self, root: Optional[TreeNode], last_robbed: bool) -> int:
        if root is None:
            return 0
        score1 = self.my_sol(root.left, False) + self.my_sol(root.right, False)
        score2 = self.my_sol(root.left, True) + self.my_sol(root.right, True) + root.val
        if last_robbed:
            score = score1
        else:
            score = max(score1, score2)
        return score


    def rob(self, root: Optional[TreeNode]) -> int:
        return self.my_sol(root, False)
