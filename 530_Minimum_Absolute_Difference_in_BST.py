import math
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.min_diff = math.inf

    def update_min_diff(self, num1, num2):
        if num1 is None or num2 is None:
            return
        self.min_diff = min(self.min_diff, abs(num2 - num1))

    def getMinMax(self, root: TreeNode) -> (int, int):
        if root is None:
            return None, None, None
        min_val, max_val = root.val, root.val
        if root.left is not None:
            left_min, left_max = self.getMinMax(root.left)
            self.update_min_diff(left_max, root.val)
            min_val = left_min

        if root.right is not None:
            right_min, right_max = self.getMinMax(root.right)
            self.update_min_diff(root.val, right_min)
            max_val = right_max

        return min_val, max_val

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.getMinMax(root)
        return self.min_diff