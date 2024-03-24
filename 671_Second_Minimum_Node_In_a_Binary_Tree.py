from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.min_val = []

    def my_sol(self, root: TreeNode):
        if root is None:
            return
        if root.val not in self.min_val:
            self.min_val.append(root.val)
            self.min_val.sort()
            if len(self.min_val) > 2:
                self.min_val.pop()
        if root.left is not None:
            self.my_sol(root.left)
        if root.right is not None:
            self.my_sol(root.right)

    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.my_sol(root)
        if len(self.min_val) < 2:
            return -1
        return self.min_val[1]



