from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_max_idx(self, nums: list[int]):
        max_data = -1
        result = -1
        for i, num in enumerate(nums):
            if num > max_data:
                max_data = num
                result = i
        return result


    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0], left=None, right=None)
        idx = self.get_max_idx(nums)
        return TreeNode(nums[idx]
                        , left=self.constructMaximumBinaryTree(nums[:idx])
                        , right=self.constructMaximumBinaryTree(nums[idx + 1:]))
