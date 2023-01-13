import math
from functools import cache
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.node_sum_dict = dict[TreeNode, int]()
        self.total_sum = 0
        self.ans = 0
        self.min_diff = math.inf

    @cache
    def calc_sum(self, root: Optional[TreeNode]) -> int:
        sum_val = root.val
        if root.left is not None:
            sum_val += self.calc_sum(root.left)
        if root.right is not None:
            sum_val += self.calc_sum(root.right)
        self.node_sum_dict[root] = sum_val
        return sum_val

    def my_ans(self, root: Optional[TreeNode]):
        root_sum = self.node_sum_dict[root]
        diff = abs((self.total_sum - root_sum) - root_sum)
        if diff < self.min_diff:
            self.min_diff = diff
            self.ans = root_sum * (self.total_sum - root_sum)
            self.ans = self.ans % (10 ** 9 + 7)

        if root.left is not None:
            self.my_ans(root.left)
        if root.right is not None:
            self.my_ans(root.right)

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.total_sum = self.calc_sum(root)
        if root.left is not None:
            self.my_ans(root.left)
        if root.right is not None:
            self.my_ans(root.right)
        return self.ans
