class TreeNode:
    def __init__(self):
        self.left_cnt = 0
        self.right_cnt = 0
        self.cnt = 0
        self.val = 0
        self.left = None
        self.right = None

def add_value(root: TreeNode, insert_val: int) -> int:
    if root.val == insert_val:
        root.cnt += 1


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
