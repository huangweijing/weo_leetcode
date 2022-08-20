from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.sol:int = 0

    def my_sum_numbers(self, root: TreeNode, num: str):
        num = num + str(root.val)
        if root.left is None and root.right is None:
            self.sol += int(num)
            return
        if root.left is not None:
            self.my_sum_numbers(root.left, num)
        if root.right is not None:
            self.my_sum_numbers(root.right, num)


    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.my_sum_numbers(root, "")
        return self.sol

