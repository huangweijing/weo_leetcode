from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.result = 0

    def sum_and_cnt_of_st(self, root: TreeNode) -> (int, int):
        if root is None:
            return 0, 0
        sum_val = root.val
        cnt_val = 1
        if root.left is not None:
            sub_sum_val, sub_cnt_val = self.sum_and_cnt_of_st(root.left)
            sum_val += sub_sum_val
            cnt_val += sub_cnt_val
        if root.right is not None:
            sub_sum_val, sub_cnt_val = self.sum_and_cnt_of_st(root.right)
            sum_val += sub_sum_val
            cnt_val += sub_cnt_val
        if int(sum_val / cnt_val) == root.val:
            self.result += 1
        return sum_val, cnt_val

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.sum_and_cnt_of_st(root)
        return self.result

