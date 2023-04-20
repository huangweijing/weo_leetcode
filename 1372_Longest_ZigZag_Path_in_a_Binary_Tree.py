from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.ans = 0

    def my_sol(self, root: TreeNode, direct: int) -> int:
        # :param direct: 1: left, 2: right
        if root is None:
            return 0
        my_sol1 = self.my_sol(root.right, 2)
        my_sol2 = self.my_sol(root.left, 1)

        height = max(my_sol1, my_sol2)
        self.ans = max(self.ans, height)
        if direct == 1:
            height = my_sol1 + 1
            self.ans = max(self.ans, height)
            return height
        elif direct == 2:
            height = my_sol2 + 1
            self.ans = max(self.ans, height)
            return height

    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.my_sol(root, 0)
        return self.ans
